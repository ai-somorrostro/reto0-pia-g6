import pandas as pd
import datetime
import requests
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


metales = ["plata", "oro", "paladio", "platino", "rodio", "aluminio", "cobre", "litio", "niquel"]

all_data = []

for metal in metales:
    url = f"http://10.221.70.238:8000/{metal}"  # cambiamos la parte de la URL
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {metal}: {e}")
        continue  # saltamos este metal si hay error

    # Procesar precios anuales
    for year, values in data.get("precio-anual", {}).items():
        all_data.append({
            "fecha_hora": pd.to_datetime(year + "-12-31"),
            "metal": metal,
            "precio_inicio": values.get("precio-inicio"),
            "precio_fin": values.get("precio-fin"),
            "cambio_dolares": values.get("cambio-dolares"),
            "cambio_porcentual": values.get("cambio-porcentual")
        })

df_metales = pd.DataFrame(all_data)
df_metales.set_index("fecha_hora", inplace=True)

my_token = 'zLYr4_COsINfisi3-BSY4sp1LNMMqvMEPpK4iENAFNhsq-OlN6ahC-NGV08LGVq0VZjgUyLtUSL6ek3bHoC1Bw=='
client = InfluxDBClient(url="http://172.17.0.1:8086", token=my_token, org="somorrostro")
write_client = client.write_api(write_options=SYNCHRONOUS)
write_client.write("metales-bucket", record=df_metales, data_frame_measurement_name="datos-evolucion-metales", data_frame_tag_columns=["metal"])
write_client.__del__()
client.close()