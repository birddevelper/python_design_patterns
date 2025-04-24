# Singleton metaclass
from weather_drivers import WeatherDriverFactory
from config import AppConfig

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Singleton Client
class WeatherClient(metaclass=SingletonMeta):
    def __init__(self):
        provider = AppConfig.WEATHER_PROVIDER
        self.driver = WeatherDriverFactory.create_driver(provider)

    def get_weather(self):
        print(self.driver.get_weather())


