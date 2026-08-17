import pandas as pd
from db_connection import get_connection

# Read Gold CSV
df = pd.read_csv(
    "/opt/airflow/weather-data-pipeline/datasets/gold/gold_weather_summary.csv"
)

# Connect SQL Server
conn = get_connection()
cursor = conn.cursor()

# Remove old data before loading the latest Gold data
cursor.execute("DELETE FROM gold_weather_summary")

# Insert latest Gold data
for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO gold_weather_summary
        (
            weather,
            total_records
        )
        VALUES (?, ?)
    """,
        row["weather"],
        row["total_records"]
    )

conn.commit()

print("✅ Gold Weather Summary Loaded Successfully")

cursor.close()
conn.close()