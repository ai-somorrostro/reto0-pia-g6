# Imagen base oficial de Node-RED
FROM nodered/node-red:3.1.1

# Establecer el directorio de trabajo
WORKDIR /data

# Copiar el flujo personalizado dentro del contenedor
# Asegúrate de tener el archivo flows.json en el mismo directorio que este Dockerfile
COPY flows.json /data/flows.json

# (Opcional) Copiar un archivo de configuración de Node-RED settings.js si lo tienes
# COPY settings.js /data/settings.js

# Exponer el puerto por defecto de Node-RED
EXPOSE 1880

# Comando por defecto para iniciar Node-RED
CMD ["npm", "start", "--", "--userDir", "/data"]
