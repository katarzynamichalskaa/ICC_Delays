import requests
from bs4 import BeautifulSoup
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class WeatherScrapper:
    def __init__(self, location, date1, date2=None):
        self.location = location
        self.date1 = date1
        self.date2 = date2
        self.API_KEY = config['API']['key']
        self.weather_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
        self.params = {
            'location': self.location,
            'date1': self.date1,
            'date2': self.date2,
            'key': self.API_KEY
        }

    def convert_to_json(self):
        response = requests.get(self.weather_url, params=self.params)
        return response.json()

    def get_data(self):
        response = self.convert_to_json()
        days = response['days']
        print(days[0]['temp'], days[0]['snow'], days[0]['windspeed'])


weather_client = WeatherScrapper(location='Warsaw', date1='2024-04-23')
weather_client.get_data()