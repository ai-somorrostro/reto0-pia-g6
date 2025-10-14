# Usamos una imagen base ligera de Python
FROM python:3.9-slim

# Copiamos el script de la app al contenedor
COPY app.py /app/app.py

# Copiamos el archivo de requerimientos
COPY requirements.txt /app/requirements.txt

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]
