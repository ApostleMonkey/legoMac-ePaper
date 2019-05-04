import json
import requests
from PIL import Image

api_key = ""
api_base = "http://api.apixu.com/v1/forecast.json?key="+api_key+"&q=GL50 3JR&days=1"

class GetWeather(object):

    def Codes(self):
        r = requests.get(api_base)
        if r.status_code == 200:
            data = json.loads(r.text)
            WeatherNow = data['current']['condition']['code']
            WeatherTomorrow = data['forecast']['forecastday'][0]['day']['condition']['code']
            return [WeatherNow, WeatherTomorrow]
            print [WeatherNow, WeatherTomorrow]
            
        else:
            return 0
