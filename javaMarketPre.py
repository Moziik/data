import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic data for years 2017 to 2022
years = np.arange(2017, 2023)
job_counts = np.array([100, 120, 150, 180, 200, 220])  # Example data

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(years.reshape(-1, 1), job_counts, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict job counts for 2024
predicted_jobs_2024 = model.predict([[2024]])[0]

# Predict percentage change
percentage_change = ((predicted_jobs_2024 - job_counts[-1]) / job_counts[-1]) * 100

# Print prediction
print("Predicted Java job market in 2024:")
print(f"Based on generated data and linear regression model, predicted Java job listings in 2024: {predicted_jobs_2024}")
print(f"Predicted percentage change: {percentage_change:.2f}%")

# Calculate model performance
y_pred_train = model.predict(X_train)
print("\nModel Performance:")
print(f"Mean Squared Error: {mean_squared_error(y_train, y_pred_train):.2f}")
print(f"R2 Score: {r2_score(y_train, y_pred_train):.2f}")
