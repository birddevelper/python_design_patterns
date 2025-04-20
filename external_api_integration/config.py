from decouple import config

class AppConfig:
    # The config reads the value from the .env file.
    # If the value is not found in the .env file, it will use the default value.
    WEATHER_PROVIDER = config('WEATHER_PROVIDER', default='dummy')