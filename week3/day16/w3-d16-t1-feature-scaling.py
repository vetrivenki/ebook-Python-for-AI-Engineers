"""Week 3 | Day 16 | Task 1: Fit scalers only on training data.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.preprocessing import StandardScaler, MinMaxScaler

train = [[10, 100], [20, 200], [30, 300]]
future = [[40, 400]]
for scaler in [StandardScaler(), MinMaxScaler()]:
    print(type(scaler).__name__)
    print("Scaled training data:", scaler.fit_transform(train))
    print("Future data using training statistics:", scaler.transform(future))
print("MinMaxScaler can return values outside [0, 1] for new data.")
