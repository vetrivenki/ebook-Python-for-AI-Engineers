"""Shared project functions. Start with the numbered Day 21 task files.

Educational CPU pipeline using synthetic customer records, not real customers.
The final test partition is never used to select models, parameters, or thresholds.
"""

from pathlib import Path
import json
import platform
import importlib.metadata

import joblib
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, average_precision_score, classification_report,
    confusion_matrix, f1_score, precision_score, recall_score,
    roc_auc_score, RocCurveDisplay,
)
from sklearn.model_selection import (
    StratifiedKFold, RandomizedSearchCV, cross_val_score, train_test_split,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "data" / "sample-churn.csv"
OUTPUT = BASE / "output"
NUMERIC = ["tenure_months", "monthly_charge", "support_calls"]
CATEGORICAL = ["contract", "payment_method"]
FEATURES = NUMERIC + CATEGORICAL
SEED = 42


def make_sample_data():
    """Create realistic-looking but explicitly synthetic practice records."""
    rng = np.random.default_rng(SEED)
    count = 900
    frame = pd.DataFrame({
        "customer_id": [f"DEMO-{i:04d}" for i in range(count)],
        "tenure_months": rng.integers(1, 73, count).astype(float),
        "monthly_charge": rng.uniform(20, 120, count).round(2),
        "support_calls": rng.poisson(2, count).astype(float),
        "contract": rng.choice(["monthly", "annual"], count),
        "payment_method": rng.choice(["card", "bank_transfer", "manual"], count),
    })
    # Labels depend on several features plus randomness; no perfect rule exists.
    log_odds = (
        -2.4 + 1.5 * (frame["contract"] == "monthly")
        + 0.025 * frame["monthly_charge"] - 0.035 * frame["tenure_months"]
        + 0.3 * frame["support_calls"]
        + 0.4 * (frame["payment_method"] == "manual")
    )
    frame["churn"] = (rng.random(count) < 1 / (1 + np.exp(-log_odds))).astype(int)
    frame.loc[rng.choice(count, 25, replace=False), "monthly_charge"] = np.nan
    frame.loc[rng.choice(count, 15, replace=False), "payment_method"] = np.nan
    return frame


def validate_features(frame):
    """Reject an invalid schema; allow missing values for the imputer."""
    missing = set(FEATURES) - set(frame.columns)
    if missing:
        raise ValueError(f"Missing feature columns: {sorted(missing)}")
    if frame.empty:
        raise ValueError("At least one customer row is required.")
    result = frame[FEATURES].copy()
    for column in NUMERIC:
        result[column] = pd.to_numeric(result[column], errors="raise")
        present = result[column].dropna()
        if not np.isfinite(present).all() or (present < 0).any():
            raise ValueError(f"{column} must contain finite nonnegative numbers.")
    for column in CATEGORICAL:
        present = result[column].dropna()
        if not present.map(lambda value: isinstance(value, str) and bool(value.strip())).all():
            raise ValueError(f"{column} must contain nonblank text or missing values.")
    # Normalize Python None to the missing marker expected by SimpleImputer.
    for column in CATEGORICAL:
        result[column] = result[column].where(result[column].notna(), np.nan)
    return result


def validate_training_data(frame):
    """Keep unique customer rows and both classes available for stratification."""
    validate_features(frame)
    if not {"customer_id", "churn"}.issubset(frame.columns):
        raise ValueError("Training data needs customer_id and churn columns.")
    if frame["customer_id"].isna().any() or frame["customer_id"].duplicated().any():
        raise ValueError("Each training customer_id must be present and unique.")
    if frame["churn"].isna().any() or set(frame["churn"].unique()) != {0, 1}:
        raise ValueError("churn must contain both 0 and 1, without missing labels.")
    if frame["churn"].value_counts().min() < 20:
        raise ValueError("Use at least 20 rows per class for this small CV example.")
    if frame[FEATURES].isna().all().any():
        raise ValueError("A training feature cannot be entirely missing.")


def load_data(path=DATA_FILE):
    """Generate the default CSV only if absent; never overwrite an existing CSV."""
    path = Path(path)
    if not path.exists():
        if path != DATA_FILE:
            raise FileNotFoundError(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        make_sample_data().to_csv(path, index=False)
    frame = pd.read_csv(path)
    validate_training_data(frame)
    return frame


def split_data(frame):
    """60% training, 20% validation, 20% untouched final test, by row index."""
    validate_training_data(frame)
    ids = np.arange(len(frame))
    train, temporary = train_test_split(
        ids, test_size=0.4, stratify=frame["churn"], random_state=SEED,
    )
    valid, test = train_test_split(
        temporary, test_size=0.5,
        stratify=frame.iloc[temporary]["churn"], random_state=SEED,
    )
    assert not set(train) & set(valid) and not set(train) & set(test)
    assert not set(valid) & set(test)
    parts = {}
    for name, indices in [("train", train), ("valid", valid), ("test", test)]:
        parts["X_" + name] = validate_features(frame.iloc[indices])
        parts["y_" + name] = frame.iloc[indices]["churn"].astype(int)
    return parts


def make_preprocessor():
    numeric = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
    ])
    categorical = Pipeline([
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("encode", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    return ColumnTransformer([
        ("numeric", numeric, NUMERIC), ("categorical", categorical, CATEGORICAL),
    ])


def candidates(include_xgboost=True):
    models = {
        "Dummy baseline": DummyClassifier(strategy="prior"),
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(
            n_estimators=60, max_depth=5, random_state=SEED, n_jobs=1,
        ),
    }
    if include_xgboost:
        # Import only when requested. No silent fallback hides missing XGBoost.
        from xgboost import XGBClassifier
        models["XGBoost"] = XGBClassifier(
            n_estimators=80, max_depth=3, learning_rate=0.08,
            eval_metric="logloss", tree_method="hist", random_state=SEED, n_jobs=1,
        )
    return {
        name: Pipeline([("prepare", make_preprocessor()), ("model", model)])
        for name, model in models.items()
    }


def compare_models(parts, include_xgboost=True):
    """Select by training-only CV ROC-AUC, not final-test performance."""
    rows = []
    folds = StratifiedKFold(n_splits=3, shuffle=True, random_state=SEED)
    for name, model in candidates(include_xgboost).items():
        scores = cross_val_score(
            model, parts["X_train"], parts["y_train"],
            scoring="roc_auc", cv=folds, n_jobs=1, error_score="raise",
        )
        rows.append({"model": name, "cv_auc": scores.mean(), "cv_std": scores.std()})
    return pd.DataFrame(rows).sort_values("cv_auc", ascending=False).reset_index(drop=True)


def tune_model(parts, comparison, include_xgboost=True):
    eligible = comparison[comparison["model"] != "Dummy baseline"]
    name = eligible.iloc[0]["model"]
    spaces = {
        "Logistic Regression": {"model__C": [0.01, 0.1, 1.0, 10.0]},
        "Random Forest": {"model__max_depth": [3, 5, None], "model__min_samples_leaf": [1, 3, 6]},
        "XGBoost": {"model__max_depth": [2, 3, 5], "model__learning_rate": [0.03, 0.08],
                    "model__n_estimators": [40, 80]},
    }
    search = RandomizedSearchCV(
        candidates(include_xgboost)[name], spaces[name], n_iter=4,
        cv=StratifiedKFold(3, shuffle=True, random_state=SEED), scoring="roc_auc",
        random_state=SEED, n_jobs=1, error_score="raise",
    )
    search.fit(parts["X_train"], parts["y_train"])
    return name, search


def choose_threshold(model, parts):
    probability = model.predict_proba(parts["X_valid"])[:, 1]
    rows = []
    for threshold in np.arange(0.1, 0.91, 0.05):
        labels = (probability >= threshold).astype(int)
        rows.append({"threshold": float(threshold), "validation_f1":
                     f1_score(parts["y_valid"], labels, zero_division=0)})
    best = max(rows, key=lambda row: (row["validation_f1"], -abs(row["threshold"] - 0.5)))
    return best["threshold"], pd.DataFrame(rows)


def fit_solution(include_xgboost=True):
    parts = split_data(load_data())
    comparison = compare_models(parts, include_xgboost)
    name, search = tune_model(parts, comparison, include_xgboost)
    model = search.best_estimator_
    threshold, threshold_table = choose_threshold(model, parts)
    # Keep this exact fitted model: refitting on validation changes its scores.
    return {
        "parts": parts, "model": model, "model_name": name, "threshold": threshold,
        "comparison": comparison, "threshold_table": threshold_table,
        "best_params": search.best_params_, "best_cv_auc": float(search.best_score_),
        "include_xgboost": include_xgboost,
    }


def evaluate_solution(solution):
    """Evaluate the frozen pipeline and threshold; do not change them afterward."""
    parts = solution["parts"]
    probability = solution["model"].predict_proba(parts["X_test"])[:, 1]
    labels = (probability >= solution["threshold"]).astype(int)
    actual = parts["y_test"]
    metrics = {
        "accuracy": accuracy_score(actual, labels),
        "precision": precision_score(actual, labels, zero_division=0),
        "recall": recall_score(actual, labels, zero_division=0),
        "f1": f1_score(actual, labels, zero_division=0),
        "roc_auc": roc_auc_score(actual, probability),
        "average_precision": average_precision_score(actual, probability),
    }
    OUTPUT.mkdir(exist_ok=True)
    report = classification_report(actual, labels, target_names=["stay", "churn"], zero_division=0)
    (OUTPUT / "classification-report.txt").write_text(report, encoding="utf-8")
    (OUTPUT / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    fig, ax = plt.subplots()
    RocCurveDisplay.from_predictions(actual, probability, ax=ax, name=solution["model_name"])
    ax.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random ranking")
    ax.set_title("Synthetic churn: untouched test partition")
    ax.legend()
    fig.savefig(OUTPUT / "roc-curve.png", bbox_inches="tight", dpi=140)
    plt.close(fig)
    print(report)
    print("Confusion matrix [stay, churn]:\n", confusion_matrix(actual, labels, labels=[0, 1]))
    return metrics


def save_solution(solution):
    """Save preprocessing AND model, plus threshold and environment metadata."""
    OUTPUT.mkdir(exist_ok=True)
    packages = ["scikit-learn", "numpy", "pandas", "joblib"]
    if solution["include_xgboost"]:
        packages.append("xgboost")
    versions = {package: importlib.metadata.version(package) for package in packages}
    bundle = {
        "pipeline": solution["model"], "threshold": solution["threshold"],
        "features": FEATURES, "model_name": solution["model_name"], "versions": versions,
        "python": platform.python_version(), "synthetic_data": True,
    }
    target = OUTPUT / "churn-pipeline.joblib"
    joblib.dump(bundle, target)
    # Safe here only because THIS process just created this local artifact.
    restored = joblib.load(target)
    example = solution["parts"]["X_valid"].iloc[:3]
    assert np.allclose(restored["pipeline"].predict_proba(example), solution["model"].predict_proba(example))
    (OUTPUT / "environment.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
    print("Saved trusted local pipeline:", target)
    return bundle


def write_summary(solution, metrics):
    OUTPUT.mkdir(exist_ok=True)
    solution["comparison"].to_csv(OUTPUT / "model-comparison.csv", index=False)
    solution["threshold_table"].to_csv(OUTPUT / "threshold-comparison.csv", index=False)
    text = (
        "# Customer Churn Prediction - Learning Report\n\n"
        "Data: 900 synthetic customers by default; not a real business dataset.\n\n"
        f"Selected model: {solution['model_name']}\n\n"
        f"XGBoost included: {solution['include_xgboost']}\n\n"
        f"Selected parameters: {solution['best_params']}\n\n"
        f"Training-CV ROC-AUC: {solution['best_cv_auc']:.3f}\n\n"
        f"Validation-selected decision threshold: {solution['threshold']:.2f}\n\n"
        f"Final test metrics: {json.dumps(metrics, indent=2)}\n\n"
        "Selection uses 3-fold CV on the 60% training partition; threshold selection "
        "uses the 20% validation partition. The remaining 20% is held out until final evaluation. "
        "Do not iterate on this test result. CV rankings have selection bias; the final test "
        "is an estimate from a small synthetic sample, not an operational guarantee.\n\n"
        "The synthetic label generator uses tenure, contract, charge, support calls, and payment "
        "method. This is by construction, not an empirical causal insight about real customers. "
        "No deployment, authentication, privacy review, or drift monitoring is implemented.\n\n"
        "Never load an untrusted joblib/pickle file. Reuse the recorded package versions.\n"
    )
    (OUTPUT / "summary.md").write_text(text, encoding="utf-8")
    print(text)


def parse_options():
    import argparse
    parser = argparse.ArgumentParser(description="Small synthetic customer-churn learning project.")
    parser.add_argument("--sklearn-only", action="store_true",
                        help="Explicit reduced mode: omit XGBoost; not a full three-model comparison.")
    return parser.parse_args()


def main():
    options = parse_options()
    solution = fit_solution(include_xgboost=not options.sklearn_only)
    metrics = evaluate_solution(solution)
    save_solution(solution)
    write_summary(solution, metrics)


if __name__ == "__main__":
    main()
