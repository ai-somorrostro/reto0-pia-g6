# Dockerfile para InfluxDB
FROM influxdb:2.7

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de configuración si tienes uno personalizado
# COPY influxdb.conf .

# Exponer puerto de InfluxDB
EXPOSE 8086

# Comando para iniciar el servidor
CMD ["influxd"]
