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
    / "gold_weather_summary.csv"
)


def create_weather_summary():

    # Read Silver data
    df = pd.read_csv(SILVER_PATH)

    # Create weather-condition summary
    weather_summary = (
        df.groupby("weather")
        .size()
        .reset_index(name="total_records")
    )

    # Sort by record count
    weather_summary = weather_summary.sort_values(
        by="total_records",
        ascending=False
    )

    # Make sure Gold folder exists
    GOLD_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save Gold CSV
    weather_summary.to_csv(
        GOLD_PATH,
        index=False
    )

    print("Gold Weather Summary created successfully.")
    print(f"Records: {len(weather_summary)}")
    print(f"Output: {GOLD_PATH}")


if __name__ == "__main__":
    create_weather_summary()