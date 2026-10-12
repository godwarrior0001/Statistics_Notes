# Day 5: Estimation & Confidence Intervals

## 1. Estimation & Standard Error
* **Point Estimation**: Provides a single best guess for a parameter[span_37](start_span)[span_37](end_span).
* **Standard Error (SE)**: Measures sample mean variability: SE = sigma / sqrt(n)[span_38](start_span)[span_38](end_span).

## 2. Confidence Intervals (CI)
* For large samples or known sigma: CI = x_bar ± z_alpha/2 * (sigma / sqrt(n))[span_39](start_span)[span_39](end_span).
* For small samples with unknown sigma, the Student's t-distribution is used[span_40](start_span)[span_40](end_span)[span_41](start_span)[span_41](end_span).

## AI / Data Science Connection
* Model performance metrics (such as accuracy or F1-scores) should ideally be reported with confidence intervals or via bootstrapping rather than bare point estimates[span_42](start_span)[span_42](end_span).
* 
