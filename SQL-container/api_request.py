import requests
import pyodbc
import datetime
import time

# === CONFIGURACIÓN ===
API_KEY = "aa6df692542d93910dbc047cb875c46d"
URL = f"https://api.metalpriceapi.com/v1/latest?api_key={API_KEY}&base=USD&currencies=XAU,XAG,XPD,XPT"
#INTERVAL = 10 * 60  # 10 minutos

# === FUNCIONES ===
def get_metal_prices():
    """Obtiene los precios de los metales desde la API."""
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    if not data.get("success"):
        raise Exception("Error en la respuesta de la API")

    ts = datetime.datetime.utcfromtimestamp(data["timestamp"])
    rates = data["rates"]

    metals = {
        "XAU": rates.get("USDXAU"),
        "XAG": rates.get("USDXAG"),
        "XPT": rates.get("USDXPT"),
        "XPD": rates.get("USDXPD"),
    }
    return ts, metals


def insert_prices(conn, ts, metals):
    """Inserta los precios en la tabla SQL."""
    cursor = conn.cursor()
    for symbol, price in metals.items():
        if price is None:
            continue
        cursor.execute("SELECT id FROM metales WHERE simbolo = ?", (symbol,))
        row = cursor.fetchone()
        if not row:
            print(f"⚠️ No se encontró el metal {symbol}")
            continue
        metal_id = row[0]

        cursor.execute("""
            INSERT INTO precios (fecha_hora, id_metal, divisa, precio_general, precio_compra, precio_venta)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (ts, metal_id, "USD", price, price, price))
    conn.commit()


# === PROGRAMA PRINCIPAL ===
def main():
    print("📊 Ejecutando actualización...")
    try:
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
        ts, metals = get_metal_prices()
        insert_prices(conn, ts, metals)
        print(f"✅ Precios insertados correctamente ({ts.isoformat()} UTC)")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()
