# Day 1: Foundations of Statistics & Data Types

## 1. What is Statistics?
* **Definition**: Statistics is the science of collecting, organising, summarising, analysing, interpreting, and presenting data to support decision-making under uncertainty[span_16](start_span)[span_16](end_span). Formally, it is the branch of applied mathematics concerned with drawing reliable conclusions about a population from a sample[span_17](start_span)[span_17](end_span).
* **AI Connection**: Statistics is the grammar of data science; every machine-learning model, dashboard, A/B test, and forecast rests on a statistical idea[span_18](start_span)[span_18](end_span).

## 2. Population vs. Sample & Parameters vs. Statistics
* **Population ($N$)**: The entire collection of units of interest[span_19](start_span)[span_19](end_span).
* **Sample ($n$)**: A subset actually observed[span_20](start_span)[span_20](end_span).
* **Parameter**: A fixed numerical fact about the population (e.g., population mean $\mu$, population SD $\sigma$)[span_21](start_span)[span_21](end_span).
* **Statistic**: A number computed from the sample (e.g., sample mean $\overline{x}$, sample SD $s$) used to estimate a parameter[span_22](start_span)[span_22](end_span).

## 3. Scales of Measurement (Stevens)
* **Nominal**: Labels with no order (City, Department, Gender, Grade letter)[span_23](start_span)[span_23](end_span).
* **Ordinal**: Ordered categories with no fixed gap (Grade $A > B > C$, Satisfaction level)[span_24](start_span)[span_24](end_span).
* **Interval**: Ordered with equal gaps, but arbitrary zero (Temperature in Celsius)[span_25](start_span)[span_25](end_span).
* **Ratio**: Ordered with equal gaps and a true zero where zero means none (Salary, Age, Marks)[span_26](start_span)[span_26](end_span).

## AI / Data Science Connection
* Data type dictates pipeline preprocessing[span_27](start_span)[span_27](end_span): Nominal features require **One-Hot Encoding**, Ordinal features require **Ordinal Encoding**, and continuous features require **Scaling/Normalisation**[span_28](start_span)[span_28](end_span).
* 
