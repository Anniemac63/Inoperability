import requests

ip = requests.get('https://api.ipify.org').text

location = requests.get(f'http://ip-api.com/json/{ip}').json()

lat = location['lat']

lon = location['lon']

city = location['city']

print(ip)

print(location)

print(lat)

print(lon)

print(city)

openweatherapi = '8c2c3caba61078c53199754a8069645f'

weatherbitapi = '389b04aa3eab4670bae87dfe95be895e'
accuweatherapi ='TZGWHSw16k008x9f5HkFQ8VBHp5jtz0Y'

#weatherbit = requests.get(url1).json()

openweather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweatherapi}&units=imperial').json()

#accuweather = requests.get(url3).json()

print(openweather)

temp = openweather['main']['temp']

print(temp)

accuweather_location = requests.get(f'https://dataservice.accuweather.com/locations/v1/search?q={city}&apikey={accuweatherapi}').json()
location_key = accuweather_location[0]['Key']
accuweather_weather = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}').json()

print(accuweather_location)

print(location_key)

print(accuweather_weather)
import requests

# Replace with your actual API key
weatherbit_api_key = "389b04aa3eab4670bae87dfe95be895e"

# Define the latitude and longitude for your desired location
latitude = 37.7749
longitude = -122.4194

# Make an API request to get current weather data
url = f"https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key={weatherbit_api_key}"
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    temperature_celsius = weather_data["data"][0]["temp"]
    weather_description = weather_data["data"][0]["weather"]["description"]
    print(f"Current temperature: {temperature_celsius}°C")
    print(f"Weather description: {weather_description}")
else:
    print("Error fetching weather data. Check your API key and coordinates.")
