import requests


class Weather:
    """
    Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:
    #Create a weather object using a city name:
    #The api key below is not guaranteed to work.
    #Get your own apikey from https://api.openweathermap.org
    #And wait a couple of hours for the apikey to be activated

    >> weather1 = Weather(apikey="09cb4968626611f895c1f9b87d07e80e", city="Wroclaw")

    #Using latitude and longtitude coordinates
    >> weather2 = Weather(apikey="09cb4968626611f895c1f9b87d07e80e", lat=4.1, lon=4.5)

    #Get compleate weather data for the next 12 hours:
    >> weather1.next_12h()

    #Simplified data for the next 12 hours:
    >> weather1.next12h_simplified()

    Sample url to get sky condition icons:
    https://api.openweathermap.org/img/wn/10d@2x.png

    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")

        if self.data['cod'] != "200":
            raise ValueError(self.data['message'])

    def next_12h(self):
        """
        :return: Returns 3-hour data for the next 12 hours as a dict.
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
        :return: Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a tuple of tuples.
        """
        simple_data = []
        for dict in self.data['list'][:4]:
            simple_data.append(dict['dt_txt'], dict['main']['temp'], dict['weather'][0]['description'],
                               dict['weather'][0]['icon'])
        return simple_data

