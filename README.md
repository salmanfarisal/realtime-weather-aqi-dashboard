# Real-Time Weather & Air Quality Data Pipeline

An end-to-end data engineering project designed to fetch, process, and store real-time environmental data to provide automated health recommendations.

## 🚀 Project Overview
This project implements a robust data pipeline that integrates real-time Weather and Air Quality Index (AQI) data via the OpenWeatherMap API. The system automates the flow of data from ingestion to a structured database, ultimately generating actionable health advisory reports based on current atmospheric conditions.

## 🛠️ Tech Stack
- **Language:** Python (Requests, Pandas)
- **Database:** PostgreSQL (Relational Data Modeling)
- **API:** OpenWeatherMap API
- **Environment:** Visual Studio Code & Git

## 💡 Key Features
- **Automated Data Ingestion:** Handles real-time API requests for localized weather and air quality metrics.
- **Relational Storage:** Implements a PostgreSQL schema to maintain historical data for trend analysis.
- **Health Advisory Logic:** A Python-based engine that categorizes AQI levels and generates safety recommendations for outdoor activities.
- **Error Handling:** Built-in mechanisms to manage API limits and connection stability.

## 📁 Project Structure
- `scripts/1_fetch_weather_data.py`: Fetches real-time temperature and weather conditions.
- `scripts/2_fetch_air_quality.py`: Retrieves PM2.5, PM10, and AQI metrics.
- `scripts/3_generate_health_advisory.py`: Joins the data and applies logic to generate the final Excel report.
- `output/`: Contains the generated health advisory reports.

## ⚙️ How to Run
1. Ensure your **PostgreSQL** server is running.
2. Run the scripts in order:
   ```bash
   python scripts/1_fetch_weather_data.py
   python scripts/2_fetch_air_quality.py
   python scripts/3_generate_health_advisory.py
