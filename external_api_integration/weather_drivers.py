from abc import ABC, abstractmethod
from enum import StrEnum, auto

class WeatherProvider(StrEnum):
    REAL = auto()
    DUMMY = auto()


class WeatherDriver(ABC):
    @abstractmethod
    def get_weather(self):
        pass


class RealWeatherDriver(WeatherDriver):
    def get_weather(self):
        return "Real Weather from API"


class DummyWeatherDriver(WeatherDriver):
    def get_weather(self):
        return "Fake Weather Data"

# Factory
class WeatherDriverFactory:
    @staticmethod
    def create_driver(provider: str) -> WeatherDriver:
        if provider == WeatherProvider.REAL:
            return RealWeatherDriver()
        elif provider == WeatherProvider.DUMMY:
            return DummyWeatherDriver()
        else:
            raise ValueError(f"Unknown provider: {provider}")

