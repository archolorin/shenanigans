import requests

API_KEY = "XXXXXXXXXX"
WS_URL = "http://api.weatherstack.com/current"

city = "XXXX"

parameters = {'access_key': API_KEY, 'query': city}

response = requests.get(WS_URL, parameters)
js = response.json()
print(js)
print()

temperature = js['current']['temperature']
date = js['location']['localtime']
city = js['location']['name']
country = js['location']['country']

print(f"The temperature in {city}, {country} on {date} is {temperature} degrees Celsius")