import pandas as pd
from db_connection import get_connection

# Read Gold CSV
df = pd.read_csv(
    "/opt/airflow/weather-data-pipeline/datasets/gold/gold_city_summary.csv"
)

# Connect SQL Server
conn = get_connection()
cursor = conn.cursor()

# Remove old data before loading the latest Gold data
cursor.execute("DELETE FROM Gold_City_Summary")

# Insert latest Gold data
for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO Gold_City_Summary
        (
            City,
            Avg_Temperature,
            Avg_Humidity,
            Avg_Pressure,
            Avg_Wind_Speed
        )
        VALUES (?, ?, ?, ?, ?)
    """,
        row["city"],
        row["avg_temperature"],
        row["avg_humidity"],
        row["avg_pressure"],
        row["avg_wind_speed"]
    )

conn.commit()

print("✅ Gold City Summary Loaded Successfully")

cursor.close()
conn.close()