

import json
import glob
import pandas as pd
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

BRONZE_PATH = BASE_DIR / "datasets" / "bronze" / "*.json"
SILVER_PATH = BASE_DIR / "datasets" / "silver" / "weather_cleaned.csv"


def transform_weather_data():

    # Find all Bronze JSON files
    files = glob.glob(str(BRONZE_PATH))

    if not files:
        raise FileNotFoundError("No Bronze JSON files found.")

    all_records = []

    # Read every Bronze JSON file
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            all_records.extend(data)
        else:
            all_records.append(data)

    # Convert to DataFrame
    df = pd.DataFrame(all_records)

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # Convert numeric columns
    numeric_columns = [
        "temperature",
        "feels_like",
        "humidity",
        "pressure",
        "wind_speed",
        "latitude",
        "longitude"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove records without city
    df = df.dropna(subset=["city"])

    # Remove duplicate weather records
    df = df.drop_duplicates(
        subset=["city", "timestamp"]
    )

    # Sort data
    df = df.sort_values(
        by=["timestamp", "city"]
    )

    # Create Silver directory if it doesn't exist
    SILVER_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save Silver data
    df.to_csv(
        SILVER_PATH,
        index=False
    )

    print("Silver transformation completed.")
    print(f"Records: {len(df)}")
    print(f"Output: {SILVER_PATH}")


if __name__ == "__main__":
    transform_weather_data()