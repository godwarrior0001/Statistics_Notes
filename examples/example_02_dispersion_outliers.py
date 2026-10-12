import pandas as pd

data = {
    "Salary": [30000, 35000, 42000, 39000, 120000, 45000, 31000, 48000, 50000, 41000]
}
df = pd.DataFrame(data)
salary_series = df["Salary"]

# Compute spread and Tukey Fences for outliers
Q1 = salary_series.quantile(0.25)
Q3 = salary_series.quantile(0.75)
IQR = Q3 - Q1

lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

outliers = salary_series[(salary_series < lower_fence) | (salary_series > upper_fence)]

print("--- Dispersion & Outliers ---")
print(f"Standard Deviation (Salary): {salary_series.std():.2f}")
print(f"Inter-Quartile Range (IQR): {IQR:.2f}")
print(f"Flagged Outliers: {outliers.tolist()}")
