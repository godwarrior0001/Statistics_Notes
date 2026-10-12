# Day 3: Dispersion, Outliers, and Shape

## 1. Spread and Quartiles
* **Range**: x_max - x_min (sensitive to outliers)[span_22](start_span)[span_22](end_span).
* **Inter-Quartile Range (IQR)**: Q3 - Q1, covering the middle 50% of data[span_23](start_span)[span_23](end_span).
* **Tukey Fences (Outlier Rule)**: Lower fence = Q1 - 1.5 * IQR; Upper fence = Q3 + 1.5 * IQR[span_24](start_span)[span_24](end_span).

## 2. Variance and Standard Deviation
* **Sample Variance**: s^2 = sum((x_i - x_bar)^2) / (n - 1)[span_25](start_span)[span_25](end_span). Division by n-1 is Bessel's correction to remove downward bias.
* **Standard Deviation**: s = sqrt(s^2)[span_26](start_span)[span_26](end_span).
* **Coefficient of Variation (CV)**: CV = (s / x_bar) * 100% (unit-free relative spread)[span_27](start_span)[span_27](end_span).

## AI / Data Science Connection
* **Standardisation (Z-score)**: z = (x - x_bar) / s rescales features to mean 0 and standard deviation 1, which is mandatory for distance-based models like SVMs, KNN, and Neural Networks[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span).
* 
