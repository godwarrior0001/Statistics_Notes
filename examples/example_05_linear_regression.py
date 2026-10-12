import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample attendance vs marks data
attendance = np.array([60, 70, 75, 80, 90]).reshape(-1, 1)
marks_target = np.array([50, 60, 65, 75, 80])

# Fit Linear Regression Model (OLS)
model = LinearRegression()
model.fit(attendance, marks_target)

predictions = model.predict(attendance)
r2 = r2_score(marks_target, predictions)

print("--- Correlation & Regression ---")
print(f"Slope (Coefficient): {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"R-squared (R2): {r2:.4f}")

# Predict marks for 85% attendance
predicted_marks = model.predict([[85]])[0]
print(f"Predicted Marks for 85% Attendance: {predicted_marks:.2f}")
