"""Week 3 | Day 16 | Task 3: Impute missing values inside a pipeline.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

train = [[10.0], [np.nan], [30.0]]
future = [[np.nan], [100.0]]
preprocessor = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
print("Transformed train:", preprocessor.fit_transform(train).ravel())
print("Transformed future:", preprocessor.transform(future).ravel())
print("Training median:", preprocessor.named_steps["simpleimputer"].statistics_)
