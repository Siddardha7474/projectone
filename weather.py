import requests

city = input("Enter city name: ").strip()

api_key = "YOUR_API_KEY"

url = f"https://www.weatherapi.com/weather/"
response = requests.get(url)

data = response.json()

if response.status_code == 200:

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n===== WEATHER REPORT =====")
    print("City:", city_name)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Pressure:", pressure)
    print("Weather:", weather)
    print("Wind Speed:", wind_speed, "m/s")

else:
    print("Error:", data["message"])