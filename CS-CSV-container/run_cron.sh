#!/bin/bash

echo "🚀 Iniciando servicio de exportación de precios de metales..."
echo "⏰ El script se ejecutará cada 12 horas"

# Ejecutar inmediatamente al iniciar
echo "📊 Ejecutando primera exportación..."
python /app/export_prices.py

# Loop infinito que ejecuta cada 12 horas
while true; do
    sleep 43200  # 43200 segundos = 12 horas
    echo "📊 $(date): Ejecutando exportación de precios..."
    python /app/export_prices.py
done