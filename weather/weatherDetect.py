import requests, json
import pprint

api_key = "147b1134e5c0d89525cc02377dc0940f"


base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = "chennai"


complete_url = base_url + "appid=" + api_key + "&q=" + city_name
print(complete_url)
response = requests.get(complete_url)
print(response)
x = response.json()
pprint.pprint(x)




#weather("chennai")