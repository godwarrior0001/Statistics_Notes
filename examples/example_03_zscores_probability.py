import pandas as pd
import numpy as np

data = {
    "Marks": [45, 62, 70, 55, 88, 90, 40, 75, 82, 60]
}
df = pd.DataFrame(data)
marks = df["Marks"]

mean_m = marks.mean()
std_m = marks.std()

# Compute Z-scores
z_scores = (marks - mean_m) / std_m

# Verify empirical rule (percentage within 1 Standard Deviation)
within_1sd = ((z_scores.abs() <= 1).mean()) * 100

print("--- Z-Scores & Empirical Rule ---")
print(f"Z-scores: {np.round(z_scores.values, 2)}")
print(f"Percentage of data within ±1 SD: {within_1sd:.1f}% (Expected ~68%)")
