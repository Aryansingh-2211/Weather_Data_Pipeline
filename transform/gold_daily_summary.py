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
    / "gold_daily_summary1.csv"
)


def create_daily_summary():

    # Read Silver data
    df = pd.read_csv(SILVER_PATH)

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # Create weather date
    df["weather_date"] = df["timestamp"].dt.date

    # Create daily summary
    daily_summary = (
        df.groupby("weather_date")
        .agg(
            avg_temperature=("temperature", "mean"),
            max_temperature=("temperature", "max"),
            min_temperature=("temperature", "min"),
            avg_humidity=("humidity", "mean"),
            avg_wind_speed=("wind_speed", "mean")
        )
        .reset_index()
    )

    # Round numerical values
    numeric_columns = [
        "avg_temperature",
        "max_temperature",
        "min_temperature",
        "avg_humidity",
        "avg_wind_speed"
    ]

    daily_summary[numeric_columns] = (
        daily_summary[numeric_columns].round(2)
    )

    # Make sure Gold folder exists
    GOLD_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save Gold CSV
    daily_summary.to_csv(
        GOLD_PATH,
        index=False
    )

    print("Gold Daily Summary created successfully.")
    print(f"Records: {len(daily_summary)}")
    print(f"Output: {GOLD_PATH}")


if __name__ == "__main__":
    create_daily_summary()