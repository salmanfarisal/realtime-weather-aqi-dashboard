import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# 1. API CONFIGURATION
# --------------------
# Target: Jakarta, Indonesia (Latitude: -6.2088, Longitude: 106.8456)
# Service: Open-Meteo Free Forecasting API
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast?latitude=-6.2088&longitude=106.8456&current_weather=true"

# 2. DATABASE CONFIGURATION
# -------------------------
# Connecting to your new dedicated database for automation projects
DB_URI = 'postgresql://username:`"YOUR_PASSWORD"`@localhost:5432/portfolio_automation_db'
engine = create_engine(DB_URI)

# 3. DATA ACQUISITION (API Request)
# ---------------------------------
try:
    print("Initiating connection to Open-Meteo API...")
    response = requests.get(WEATHER_API_URL)
    response.raise_for_status() # Ensures the request was successful
    
    # Parse JSON response
    json_data = response.json()
    current_weather = json_data['current_weather']
    
    # 4. DATA TRANSFORMATION (ETL Process)
    # ------------------------------------
    # Structuring the raw API response into a clean Python Dictionary
    weather_summary = {
        'city': ['Jakarta'],
        'temperature_c': [current_weather['temperature']],
        'wind_speed_kmh': [current_weather['windspeed']],
        'weather_condition_code': [current_weather['weathercode']],
        'data_timestamp': [datetime.now()]
    }
    
    # Convert dictionary to Pandas DataFrame
    df_weather = pd.DataFrame(weather_summary)
    
    # 5. DATABASE LOADING (Storage)
    # -----------------------------
    # 'if_exists=append' ensures we create a historical log every time we run the script
    df_weather.to_sql('jakarta_weather_history', engine, if_exists='append', index=False)
    
    print("\n✅ Data Pipeline Execution Successful!")
    print("Real-time weather data has been archived in 'automation_db'.")
    print("-" * 30)
    print(df_weather)

except Exception as error:
    print(f"❌ Pipeline Failure: {error}")