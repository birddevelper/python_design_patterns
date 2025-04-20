from weather_client import WeatherClient
from config import AppConfig

weather_client = WeatherClient(provider=AppConfig.WEATHER_PROVIDER)
weather_client.get_weather()
