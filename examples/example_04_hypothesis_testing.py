import scipy.stats as stats

# Simulating salary groups from two departments
it_salaries = [75000, 82000, 90000, 68000, 85000, 92000]
hr_salaries = [45000, 48000, 52000, 49000, 46000, 51000]

# Perform independent two-sample t-test
t_stat, p_value = stats.ttest_ind(it_salaries, hr_salaries, equal_var=False)

print("--- Hypothesis Testing (IT vs HR Salaries) ---")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: Reject H0 — Significant difference in department salaries.")
else:
    print("Conclusion: Fail to reject H0 — No significant difference.")
  
