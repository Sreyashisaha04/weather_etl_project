# main.py

import schedule
import time
from etl.extract import extract_weather_data
from etl.transform import transform_weather_data
from etl.load import load_to_csv
from config.config import API_KEY, CITY_LIST

def run_pipeline():
    print("\n⏳ Starting ETL pipeline for all cities...\n")
    for city in CITY_LIST:
        print(f"🌐 Running ETL pipeline for: {city}")
        try:
            raw_data = extract_weather_data(city, API_KEY)
            df = transform_weather_data(raw_data)
            load_to_csv(df)
            print(df)
        except Exception as e:
            print(f"❌ Error for {city}: {e}")
    print("\n✅ ETL pipeline run completed.\n")

if __name__ == "__main__":
    print("⏰ Weather ETL Scheduler started. Running every hour.")
    run_pipeline()  # Run immediately on start

    # Schedule to run every 1 hour
    schedule.every(1).hours.do(run_pipeline)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute for scheduled tasks