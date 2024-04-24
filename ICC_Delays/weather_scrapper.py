import requests
from bs4 import BeautifulSoup
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class WeatherScrapper:
    def __init__(self):
        self.API_KEY = config['API']['key']
        self.weather_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'

    def convert_to_json(self, params):
        response = requests.get(self.weather_url, params=params)
        return response.json()

    def get_data(self, location, time, date1, date2=None):

        params = {
            'location': location,
            'date1': f'{date1}T{time}',
            'date2': date2,
            'key': self.API_KEY
        }

        response = self.convert_to_json(params=params)
        days = response['days'][0]      # don't care about others days
        print(days['temp'], days['snow'], days['windspeed'])
        return days['temp'], days['snow'], days['windspeed']
