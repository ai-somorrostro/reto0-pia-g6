import pyodbc
import pandas as pd

# === 🧠 Función para crear conexión a SQL Server ===
def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=host.docker.internal,1433;"
        "DATABASE=Reto-0;"
        "UID=docker_user;"
        "PWD=docker1234;"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=10;"
    )
    return conn


# === 📂 Función para ejecutar un archivo SQL y devolver DataFrame ===
def execute_sql_file(sql_file: str) -> pd.DataFrame:
    with open(sql_file, "r", encoding="utf-8") as f:
        sql_query = f.read()

    conn = get_connection()
    df = pd.read_sql(sql_query, conn)
    conn.close()

    return df
