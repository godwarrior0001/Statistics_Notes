import pandas as pd

# Sample dataset creation
data = {
    "Marks": [45, 62, 70, 55, 88, 90, 40, 75, 82, 60],
    "Salary": [30000, 35000, 42000, 39000, 120000, 45000, 31000, 48000, 50000, 41000]
}
df = pd.DataFrame(data)

# Compute central tendency measures
print("--- Central Tendency ---")
print(f"Mean Marks: {df['Marks'].mean():.2f}")
print(f"Median Marks: {df['Marks'].median():.2f}")
print(f"Mode Marks: {df['Marks'].mode().tolist()}")

# Comparing mean vs median on skewed salary data
print("\n--- Handling Skewed Data (Salary) ---")
print(f"Salary Mean: {df['Salary'].mean():.2f}")
print(f"Salary Median: {df['Salary'].median():.2f}")
print("Insight: Median is preferred for salary due to high-income outliers.")
