import pyodbc
import csv
import datetime
import os

# === CONFIGURACIÓN ===
OUTPUT_DIR = "/app/exports"  # Directorio dentro del contenedor

# === FUNCIONES ===
def export_to_csv(conn, filename):
    """Exporta los datos de la tabla precios a un archivo CSV."""
    cursor = conn.cursor()
    
    # Consulta para obtener todos los datos con información del metal
    query = """
        SELECT 
            p.fecha_hora,
            m.nombre AS metal,
            m.simbolo,
            p.divisa,
            p.precio_general,
            p.precio_compra,
            p.precio_venta
        FROM precios p
        INNER JOIN metales m ON p.id_metal = m.id
        ORDER BY p.fecha_hora DESC, m.nombre
    """
    
    cursor.execute(query)
    
    # Obtener los nombres de las columnas
    columns = [column[0] for column in cursor.description]
    
    # Escribir el CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Escribir encabezados
        writer.writerow(columns)
        
        # Escribir filas
        row_count = 0
        for row in cursor:
            writer.writerow(row)
            row_count += 1
    
    return row_count


# === PROGRAMA PRINCIPAL ===
def main():
    # Crear directorio de exports si no existe
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
    output_file = os.path.join(OUTPUT_DIR, f"precios_metales_{timestamp}.csv")
    
    print("📊 Ejecutando exportación...")
    
    try:
        # Conectar a la base de datos
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
        
        print("✅ Conexión a la base de datos establecida")
        
        # Exportar a CSV
        row_count = export_to_csv(conn, output_file)
        
        print(f"✅ Exportación completada exitosamente")
        print(f"📁 Archivo generado: {output_file}")
        print(f"📊 Total de registros exportados: {row_count}")
        
    except Exception as e:
        print(f"❌ Error durante la exportación: {e}")
    
    finally:
        if 'conn' in locals():
            conn.close()
            print("🔌 Conexión cerrada")


if __name__ == "__main__":
    main()