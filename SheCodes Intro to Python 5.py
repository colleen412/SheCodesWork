import requests
from rich import print

city = input('Please name a city. ')
api_key = '649bacd404ba629od0f5c308d505aat9'
api_url = f'https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}'

response = requests.get(api_url)

weather = response.json()

temp = round(weather['temperature']['current'])
country = weather['country']
humidity = weather['temperature']['humidity']

print(f'It is currently {temp}°C in {city}, {country}.')
