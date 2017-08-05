from requests import get
from ipgetter import myip
import pyowm


class PyGeoIp:
    def __init__(self):
        self.owm = pyowm.OWM("05ad959a906f76cfeae2b45e132826c8")
        self.location = get("http://freegeoip.net/json/" + myip())
        self.response = self.location.json()
        self.lat = self.response["latitude"]
        self.lon = self.response["longitude"]

    def get_temp_location(self):
        weather = self.owm.weather_at_coords(self.lat, self.lon).get_weather()
        temps = weather.get_temperature("celsius")
        return str(temps["temp"]) + "°C / " + str(temps["temp_max"]) + "°C"

    def get_forecast_location(self):
        forecast = self.owm.three_hours_forecast_at_coords(self.lat, self.lon).get_forecast().get_weathers()
        for weather in forecast:
            return weather.get_status()
            break
