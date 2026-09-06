"""Week 3 | Day 15 | Task 1: Supervised, unsupervised, and reinforcement learning.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

# Supervised: learn from inputs paired with known target values.
hours = np.array([[1], [2], [3], [4]])
scores = np.array([40, 50, 60, 70])
predictor = LinearRegression().fit(hours, scores)
print("Predicted score for 5 hours:", predictor.predict([[5]])[0])

# Unsupervised: group inputs without supplying target labels.
points = np.array([[1, 1], [1, 2], [9, 9], [9, 10]])
groups = KMeans(n_clusters=2, random_state=42, n_init=10).fit_predict(points)
print("Cluster IDs (names are arbitrary):", groups)

# Reinforcement-learning idea: update action values from rewards.
# This tiny bandit example omits states, exploration, and delayed rewards.
action_values = {"study": 0.0, "skip": 0.0}
for action, reward in [("study", 1), ("skip", 0), ("study", 1)]:
    action_values[action] += 0.5 * (reward - action_values[action])
print("Learned action values:", action_values)
