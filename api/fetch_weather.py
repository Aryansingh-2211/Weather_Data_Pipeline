import json 
import requests
from pathlib import Path
from datetime import datetime

from config import API_KEY, BASE_URL, CITIES, UNITS


def fetch_weather_data():

    weather_records = []

     # Project Root
    BASE_DIR = Path(__file__).resolve().parent.parent

    # datasets/bronze
    output_folder = BASE_DIR / "datasets" / "bronze"

    output_folder.mkdir(parents=True, exist_ok=True)

    for city in CITIES:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": UNITS
        }

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            weather_records.append ({
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "weather":data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "latitude": data["coord"]["lat"],
                "longitude": data["coord"]["lon"],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            })

            print(f"Successfully fetched weather data for {city}")

        except Exception as e:
            print(f"Unsuccessfully fetched weather data {city} -> {e}")


    file_name = f"weather_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    file_path = output_folder / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(weather_records, file,  indent=4)


    print("\n.......................................")
    print("weather data fetched and stored successfully")
    print("Cities Collected: ", len(weather_records))
    print("Saved File: ", file_path)
    print("........................................")

if __name__ == "__main__":
    fetch_weather_data()