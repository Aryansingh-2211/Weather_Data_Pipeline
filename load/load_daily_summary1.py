import pandas as pd
from db_connection import get_connection

# Read Gold CSV
df = pd.read_csv(
    "/opt/airflow/weather-data-pipeline/datasets/gold/gold_daily_summary1.csv"
)

# Connect SQL Server
conn = get_connection()
cursor = conn.cursor()

# Remove old data before loading the latest Gold data
cursor.execute("DELETE FROM gold_daily_summary1")

# Insert latest Gold data
for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO gold_daily_summary1
        (
            weather_date,
            avg_temperature,
            max_temperature,
            min_temperature,
            avg_humidity,
            avg_wind_speed
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        row["weather_date"],
        row["avg_temperature"],
        row["max_temperature"],
        row["min_temperature"],
        row["avg_humidity"],
        row["avg_wind_speed"]
    )

conn.commit()

print("✅ Gold Daily Summary Loaded Successfully")

cursor.close()
conn.close()