import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# 1. API CONFIGURATION (Air quality for Jakarta)
# Using Open-Meteo Air Quality API
AIR_API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=-6.2088&longitude=106.8456&current=pm2_5,pm10,us_aqi"

# 2. DATABASE CONFIGURATION
# -------------------------
# Ensure 'portfolio_automation_db' is created
DB_URI = 'postgresql://username:`"YOUR_PASSWORD"`@localhost:5432/portfolio_automation_db'
engine = create_engine(DB_URI)

# 3. DATA FETCHING PROCESS
try:
    print("Connecting to Air Quality API...")
    response = requests.get(AIR_API_URL)
    response.raise_for_status()

    data = response.json()
    current_air = data['current']

    # 4. DATA ENGINEERING (Structuring the JSON)
    # ------------------------------------------
    air_quality_data = {
        'city' : ['Jakarta'],
        'pm2_5' :[current_air['pm2_5']],
        'pm10' : [current_air['pm10']],
        'us_aqi' : [current_air['us_aqi']],
        'recorded_at' : [datetime.now()]
    }

    df_air = pd.DataFrame(air_quality_data)

    # 5. DATABASE INJECTION
    df_air.to_sql('jakarta_air_quality_logs', engine, if_exists = 'append', index = False)

    print("\n✅ Success: Air Quality data saved to 'automation_db'!")
    print(df_air)

except Exception as e:
    print(f"❌ Error during API/Datanase operation: {e}")