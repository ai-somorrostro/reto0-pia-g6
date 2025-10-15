#!/bin/bash

echo "🚀 Iniciando servicio de actualización de precios de metales..."
echo "⏰ El script se ejecutará cada 10 minutos"

# Ejecutar inmediatamente al iniciar
echo "📊 Ejecutando primera actualización..."
python -u /app/api_request.py

# Loop infinito que ejecuta cada 10 minutos
while true; do
    sleep 600  # 600 segundos = 10 minutos
    echo "📊 $(date): Ejecutando actualización de precios..."
    python -u /app/api_request.py
done
