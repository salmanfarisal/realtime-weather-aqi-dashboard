import pandas as pd
from sqlalchemy import create_engine

# 1. DATABASE CONNECTION
DB_URI = 'postgresql://username:`"YOUR_PASSWORD"`@localhost:5432/portfolio_automation_db'
engine = create_engine(DB_URI)

# 2. FETCH THE JOINED DATA FROM SQL
# Kita gunakan query JOIN yang sama seperti sebelumnya
query = """
SELECT 
    w.city, 
    w.temperature_c, 
    a.us_aqi, 
    a.pm2_5,
    w.data_timestamp
FROM jakarta_weather_history w
JOIN jakarta_air_quality_logs a 
ON w.city = a.city 
AND DATE_TRUNC('hour', w.data_timestamp) = DATE_TRUNC('hour', a.recorded_at)
ORDER BY w.data_timestamp DESC;
"""

try:
    print("Fetching unified data from portfolio_automation_db...")
    df_unified = pd.read_sql(query, engine)

    if not df_unified.empty:
        # 3. DEFINE THE HEALTH LOGIC
        def get_health_advice(aqi):
            if aqi <= 50:
                return "Good - Air quality is satisfactory."
            elif aqi <= 100:
                return "Moderate - Sensitive groups should limit outdoor activity."
            elif aqi <= 150:
                return "Unhealthy for Sensitive Groups - Wear a mask outdoors."
            else:
                return "Unhealthy - Avoid outdoor activities and use air purifiers."

        # 4. APPLY THE LOGIC
        print("Applying health advisory logic...")
        df_unified['health_recommendation'] = df_unified['us_aqi'].apply(get_health_advice)

        # 5. EXPORT FINAL REPORT
        df_unified.to_excel('jakarta_final_health_report.xlsx', index=False)
        
        print("\n✅ Success: 'jakarta_final_health_report.xlsx' has been generated!")
        print(df_unified[['temperature_c', 'us_aqi', 'health_recommendation']].head())
    else:
        print("⚠️ No data found to analyze. Please run the fetcher scripts first.")

except Exception as e:
    print(f"❌ Error: {e}")