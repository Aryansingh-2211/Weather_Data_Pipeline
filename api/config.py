
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

UNITS = "metric"

CITIES = [
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Lucknow",
    "Patna",
    "Bhopal",
    "Chandigarh",
    "Surat",
    "Indore",
    "Nagpur",
    "Visakhapatnam",
    "Gurugram",
    "Bhubaneswar",
    "Guwahati"
]

