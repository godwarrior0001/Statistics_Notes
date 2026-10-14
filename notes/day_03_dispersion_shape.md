# Day 3: Dispersion, Outliers, and Shape

## 1. Range and Inter-Quartile Range (IQR)
* **Range**: $x_{max} - x_{min}$ (sensitive to outliers)[span_35](start_span)[span_35](end_span).
* **IQR**: $Q_3 - Q_1$, covering the middle 50% of data[span_36](start_span)[span_36](end_span).
* **Tukey Fences (Outlier Rule)**: Lower fence = $Q_1 - 1.5 \times IQR$, Upper fence = $Q_3 + 1.5 \times IQR$[span_37](start_span)[span_37](end_span).

## 2. Variance, Standard Deviation, and CV
* **Sample Variance ($s^2$)**: $s^2 = \frac{1}{n-1}\sum(x_i - \overline{x})^2$[span_38](start_span)[span_38](end_span). Division by $n-1$ (Bessel's correction) removes downward bias[span_39](start_span)[span_39](end_span).
* **Standard Deviation ($s$)**: $\sqrt{s^2}$[span_40](start_span)[span_40](end_span).
* **Coefficient of Variation (CV)**: $CV = \frac{s}{\overline{x}} \times 100\%$ (unit-free relative spread)[span_41](start_span)[span_41](end_span).

## AI / Data Science Connection
* **Standardisation (Z-score)**: $z = \frac{x - \overline{x}}{s}$ rescales features to mean 0 and standard deviation 1, which is mandatory for distance-based models like SVM, KNN, and Neural Networks[span_42](start_span)[span_42](end_span)[span_43](start_span)[span_43](end_span).
