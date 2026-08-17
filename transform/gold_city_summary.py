import pandas as pd
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Input: Silver
SILVER_PATH = (
    BASE_DIR
    / "datasets"
    / "silver"
    / "weather_cleaned.csv"
)

# Output: Gold
GOLD_PATH = (
    BASE_DIR
    / "datasets"
    / "gold"
    / "gold_city_summary.csv"
)


def create_city_summary():

    # Read Silver data
    df = pd.read_csv(SILVER_PATH)

    # Create city-level summary
    city_summary = (
        df.groupby("city")
        .agg(
            avg_temperature=("temperature", "mean"),
            avg_humidity=("humidity", "mean"),
            avg_pressure=("pressure", "mean"),
            avg_wind_speed=("wind_speed", "mean")
        )
        .reset_index()
    )

    # Round numerical values
    numeric_columns = [
        "avg_temperature",
        "avg_humidity",
        "avg_pressure",
        "avg_wind_speed"
    ]

    city_summary[numeric_columns] = (
        city_summary[numeric_columns].round(2)
    )

    # Make sure Gold folder exists
    GOLD_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save Gold CSV
    city_summary.to_csv(
        GOLD_PATH,
        index=False
    )

    print("Gold City Summary created successfully.")
    print(f"Records: {len(city_summary)}")
    print(f"Output: {GOLD_PATH}")


if __name__ == "__main__":
    create_city_summary()