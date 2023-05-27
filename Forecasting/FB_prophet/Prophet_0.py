import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go


# Read the data into a Pandas DataFrame
file_path = r"C:\Users\jit24\OneDrive\Desktop\Major_project\Major__project\Forecasting\Average\4.csv" 

data = pd.read_csv(file_path)

# Prepare the data for Prophet
df = pd.DataFrame()
df['ds'] = pd.to_datetime(data['date'])
df['y'] = data['data']

# Create a Prophet model
model = Prophet()

# Fit the model to the data
model.fit(df)

# Generate future dates for prediction
future_dates = model.make_future_dataframe(periods=365)  # Add 365 days for future predictions

# Make predictions
predictions = model.predict(future_dates)

# Plot the forecast
model.plot(predictions)
