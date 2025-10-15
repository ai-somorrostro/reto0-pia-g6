from fastapi import FastAPI
from .db_utils import execute_sql_file

app = FastAPI()

# === 🔧 Función genérica para cargar datos de cualquier metal ===
def get_metal_data(nombre_metal: str):
    """Ejecuta las consultas SQL y construye la respuesta para el metal indicado."""
    metal = nombre_metal.upper()

    # Paths de las consultas (ajusta si tus archivos están en otra ruta)
    sql_anual = f"app/sql/SQLQuery-{metal}-1.sql"
    sql_decenal = f"app/sql/SQLQuery-{metal}-2.sql"

    # Ejecutar consultas SQL
    df_anual = execute_sql_file(sql_anual)
    df_decenal = execute_sql_file(sql_decenal)

    # Convertir resultados a diccionarios
    data_anual = df_anual.to_dict(orient="records")
    data_decenal = df_decenal.to_dict(orient="records")

    # Construir respuesta estructurada
    response = {
        "precio-decenal": {
            str(row["periodo_decada"]): {
                "precio-inicio-decada": row["precio_inicio_decada"],
                "precio-final-decada": row["precio_fin_decada"],
                "cambio-dolares": row["cambio_dolares"],
                "cambio-porcentual": row["cambio_porcentaje"],
            }
            for row in data_decenal
        },
        "precio-anual": {
            str(row["año"]): {
                "precio-inicio": row["precio_inicio"],
                "precio-fin": row["precio_fin"],
                "cambio-dolares": row["cambio_dolares"],
                "cambio-porcentual": row["cambio_porcentaje"],
            }
            for row in data_anual
        },
    }

    return response


# === 🟡 Oro ===
@app.get("/oro")
def get_oro():
    return get_metal_data("oro")


# === ⚪ Plata ===
@app.get("/plata")
def get_plata():
    return get_metal_data("plata")


# === 🟣 Paladio ===
@app.get("/paladio")
def get_paladio():
    return get_metal_data("paladio")


# === 🔵 Platino ===
@app.get("/platino")
def get_platino():
    return get_metal_data("platino")


# === ⚫ Rodio ===
@app.get("/rodio")
def get_rodio():
    return get_metal_data("rodio")


# === 🟠 Aluminio ===
@app.get("/aluminio")
def get_aluminio():
    return get_metal_data("aluminio")


# === 🟤 Cobre ===
@app.get("/cobre")
def get_cobre():
    return get_metal_data("cobre")


# === 🔋 Litio ===
@app.get("/litio")
def get_litio():
    return get_metal_data("litio")


# === 🧲 Níquel ===
@app.get("/niquel")
def get_niquel():
    return get_metal_data("niquel")
