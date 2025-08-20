import pandas as pd
from datetime import datetime

def transform_weather_data(raw_data):
    main = raw_data.get('main', {})
    wind = raw_data.get('wind', {})
    weather = raw_data.get('weather', [{}])[0]

    transformed = {
        'city': raw_data.get('name', 'Unknown'),
        'temperature_c': round(main.get('temp', 0) - 273.15, 2),
        'humidity': main.get('humidity', 0),
        'wind_speed': wind.get('speed', 0),
        'description': weather.get('description', ''),
        'timestamp': datetime.utcfromtimestamp(raw_data.get('dt', 0)).strftime('%Y-%m-%d %H:%M:%S')
    }

    return pd.DataFrame([transformed])