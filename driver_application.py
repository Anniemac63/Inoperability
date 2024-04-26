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

openweatherapi = 'd9804b583cc153c803b42a66f07690f2'
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

BASE = " http://127.0.0.1:5000/"
APP_VERSION = "v1/"


# Function to retrieve weather data
def get_weather_data(latitude, longitude, api_key):
    url = f"https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        temperature_celsius = weather_data["data"][0]["temp"]
        weather_description = weather_data["data"][0]["weather"]["description"]
        return {"temperature": temperature_celsius, "description": weather_description}
    else:
        print("Error fetching weather data. Check your API key and coordinates.")
        return None

# Your latitude and longitude
latitude = 37.7749
longitude = -122.4194

# Your Weatherbit API key
weatherbit_api_key = "389b04aa3eab4670bae87dfe95be895e"

# Retrieve weather data
weather_data = get_weather_data(latitude, longitude, weatherbit_api_key)

if weather_data:
    print("Retrieved Weather Data:", weather_data)

# Define your base URL and API version
BASE_URL = "http://127.0.0.1:5000/"
API_VERSION = "v1/"

# Update weather data for each item
for i, item in enumerate(data):
    response = requests.put(BASE_URL + API_VERSION + "WeatherData/" + str(i), {"weather": weather_data})
    print(response.json())

# Retrieve data for a specific item
input()
response = requests.get(BASE_URL + API_VERSION + "WeatherData/2")
print(response.json())

for i in range(len(data)):
    response = requests.put(BASE + APP_VERSION + "WeatherData/" + str(i), data[i])
    print(response.json())
 
input()
response = requests.get(BASE + APP_VERSION + "WeatherData/2")
print(response.json())

import requests

# Function to retrieve weather data
def get_weather_data(latitude, longitude, api_key):
    url = f"https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        temperature_celsius = weather_data["data"][0]["temp"]
        weather_description = weather_data["data"][0]["weather"]["description"]
        return {"temperature": temperature_celsius, "description": weather_description}
    else:
        print("Error fetching weather data. Check your API key and coordinates.")
        return None

# Your latitude and longitude
latitude = 37.7749
longitude = -122.4194

# Your Weatherbit API key
weatherbit_api_key = "389b04aa3eab4670bae87dfe95be895e"

# Define your base URL and API version
BASE_URL = "http://127.0.0.1:5000/"
API_VERSION = "v1/"

# Define your data
data = [
    {"name": "The Frozen Ones", "views": 100},
    {"name": "The Frozen Void", "views": 1020},
    {"name": "The Mars Experiment", "views": 10}
]


# Retrieve weather data
weather_data = get_weather_data(latitude, longitude, weatherbit_api_key)

if weather_data:
    print("Retrieved Weather Data:", weather_data)

# Update weather data for each item
for i, item in enumerate(data):
    response = requests.put(BASE_URL + API_VERSION + "WeatherData/" + str(i), {"weather": weather_data})
    print(response.json())

# Retrieve data for a specific item
input()
response = requests.get(BASE_URL + API_VERSION + "WeatherData/2")
print(response.json())
