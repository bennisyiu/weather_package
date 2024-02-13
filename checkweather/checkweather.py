import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("APIKEY")


class Weather():
    """This app is to get the weather forecast for the next 12 hours of the city or the coordinates of your choiceself.
    Package use example:

    # Usecase I: Create the Weather object using a city name:
    # weather = Weather(apikey={'your own api key'}, city='London')
    # Go get your own api key from https://openweathermap.org/

    # Usecase II: Create the Weather object using coordinates:
    # weather = Weather(apikey={'your own api key'}, lat=22.3, lon=114.1)

    # Get complete data for the next 12 hours:
    # weather.next_12h()

    # Get simplified data for the next 12 hours:
    # weather.next_12h_simplified()
    """

    def __init__(self, apikey=api_key, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError('Provide either city or lat and lon arguements')

        if self.data['cod'] != 200:
            raise ValueError(f"{self.data['message']}")

    def next_12h(self):
        """ Return 3-hour weather forecast for the next 12 hours as a dictionary
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """ Return time, temperature and sky conditions for the next 12 hours as a dictionary
        """
        simple_data = []
        for dict in self.data['list'][:4]:
            simple_data.append(
                (f"Time: {dict['dt_txt']}, Temperature: {dict['main']['temp']}°C, Weather: {dict['weather'][0]['description']}"))
        return simple_data
