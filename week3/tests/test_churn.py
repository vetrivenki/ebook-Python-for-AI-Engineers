"""Small schema, leakage, preprocessing, and persistence checks; no XGBoost required."""
from pathlib import Path
import sys
import tempfile
import unittest

import joblib
import numpy as np

PROJECT = Path(__file__).resolve().parents[1] / "day21" / "customer-churn-prediction"
sys.path.insert(0, str(PROJECT))
from churn_common import (
    make_sample_data, split_data, validate_training_data, validate_features,
    make_preprocessor, candidates, FEATURES,
)


class ChurnTests(unittest.TestCase):
    def setUp(self):
        self.frame = make_sample_data()

    def test_deterministic_data(self):
        self.assertTrue(self.frame.equals(make_sample_data()))

    def test_none_category_is_imputed(self):
        parts = split_data(self.frame)
        transformer = make_preprocessor().fit(parts["X_train"])
        example = parts["X_valid"].iloc[:2].copy()
        example["contract"] = None
        cleaned = validate_features(example)
        self.assertTrue(np.isfinite(transformer.transform(cleaned)).all())

    def test_valid_training_schema(self):
        validate_training_data(self.frame)

    def test_missing_column_rejected(self):
        with self.assertRaises(ValueError):
            validate_features(self.frame.drop(columns=["contract"]))

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            validate_features(self.frame.iloc[:0])

    def test_bad_numeric_rejected(self):
        self.frame["monthly_charge"] = "not-a-number"
        with self.assertRaises(ValueError):
            validate_features(self.frame)

    def test_negative_value_rejected(self):
        self.frame.loc[0, "support_calls"] = -1
        with self.assertRaises(ValueError):
            validate_features(self.frame)

    def test_infinity_rejected(self):
        self.frame.loc[0, "monthly_charge"] = np.inf
        with self.assertRaises(ValueError):
            validate_features(self.frame)

    def test_duplicate_customer_rejected(self):
        self.frame.loc[1, "customer_id"] = self.frame.loc[0, "customer_id"]
        with self.assertRaises(ValueError):
            validate_training_data(self.frame)

    def test_single_class_rejected(self):
        self.frame["churn"] = 0
        with self.assertRaises(ValueError):
            validate_training_data(self.frame)

    def test_all_missing_feature_rejected(self):
        self.frame["monthly_charge"] = np.nan
        with self.assertRaises(ValueError):
            validate_training_data(self.frame)

    def test_splits_are_disjoint_and_exclude_target(self):
        parts = split_data(self.frame)
        indices = [set(parts["X_" + name].index) for name in ["train", "valid", "test"]]
        self.assertFalse(indices[0] & indices[1] or indices[0] & indices[2] or indices[1] & indices[2])
        self.assertEqual([len(x) for x in indices], [540, 180, 180])
        self.assertEqual(list(parts["X_train"].columns), FEATURES)

    def test_preprocessor_uses_training_statistics(self):
        parts = split_data(self.frame)
        transformer = make_preprocessor().fit(parts["X_train"])
        expected = parts["X_train"][["tenure_months", "monthly_charge", "support_calls"]].median()
        actual = transformer.named_transformers_["numeric"].named_steps["impute"].statistics_
        np.testing.assert_allclose(actual, expected)

    def test_unseen_category_and_missing_values(self):
        parts = split_data(self.frame)
        transformer = make_preprocessor().fit(parts["X_train"])
        future = parts["X_valid"].iloc[:2].copy()
        future["contract"] = "unseen-contract"
        future["monthly_charge"] = np.nan
        self.assertTrue(np.isfinite(transformer.transform(future)).all())

    def test_trusted_save_load_predictions_match(self):
        parts = split_data(self.frame)
        model = candidates(include_xgboost=False)["Logistic Regression"]
        model.fit(parts["X_train"], parts["y_train"])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trusted-test-model.joblib"
            joblib.dump(model, path)
            restored = joblib.load(path)
            np.testing.assert_allclose(model.predict_proba(parts["X_valid"]),
                                       restored.predict_proba(parts["X_valid"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
