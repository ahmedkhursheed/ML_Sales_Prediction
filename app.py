# app.py
from sklearn.metrics import mean_absolute_error, mean_squared_error
from src.models.predictive_loader import load_predictive_model
from src.models.forecasting_loader import load_forecasting_model 
import numpy as np
import joblib

predictive_model=load_predictive_model()
forecast_model = load_forecasting_model()

forecast_next_7_days_Total_Sales_revenue = forecast_model.forecast(steps=7)

print("SARIMA Forecast for the next 7 days: \n")
print(forecast_next_7_days_Total_Sales_revenue)


filepath='models/forecasting/acc.pkl'
accuracy_forecasting = joblib.load(filepath)
mae,mse,rmse=accuracy_forecasting

#Accuracy forcasting model

print(f"\nForcasting MAE: {mae:.6f}")
print(f"Forcasting MSE: {mse:.6f}")
print(f"Forcasting RMSE: {rmse:.6f}")


filepath='models/predictive/acc.pkl'
accuracy_predictive= joblib.load(filepath)
mae,mse,rmse=accuracy_predictive


#Accuracy for predictive model

print(f"\nPredictive Model Model MSE: {mse:.6f}")
print(f"Predictive Model Model RMSE: {rmse:.6f}")
print(f"Predictive Model Model MAE: {mae:.6f}")