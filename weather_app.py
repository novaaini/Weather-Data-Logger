from dotenv import load_dotenv
import os
import requests
import csv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CSV_FILE = "weather_log.csv"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        # Save data into CSV
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([city_name, temp, weather])

        print(f"{city_name}: {temp}°C, {weather}")
    else:
        print("Error:", data.get("message", "Unknown error"))

if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            break
        get_weather(city)

    print(f"\nAll data saved to {CSV_FILE}")
    input("Press Enter to close...")
