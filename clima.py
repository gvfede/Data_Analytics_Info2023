from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json
import config

# Guardamos dentro de la variable api_key el password de nuetra API que esta en config.py
api_key = config.API_KEY

# Función para obtener los datos de clima de una ciudad, funciona agrgando dos parametros el nombre de la ciudad 
# y el password de la API que lo obtenemos de la variable api_key
def get_weather_data(city_name, api_key):

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        date_str = datetime.utcfromtimestamp(data["dt"]).strftime('%Y%m%d')
        file_path = f"data_analytics/openweather/tiempodiario_{city_name}_{date_str}.csv"
        df.to_csv(file_path, index=False)
        print(f"Datos de clima de {city_name} almacenados en {file_path}.")
    else:
        print(f"Error al obtener los datos de clima de {city_name}.")

get_weather_data('London', api_key=api_key)