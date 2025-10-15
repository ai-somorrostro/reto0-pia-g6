-- MEDIA MÓVIL 30 DÍAS + COMPARACIÓN PRECIO ACTUAL VS MEDIA (JOIN con metales)
WITH datos AS (
    SELECT 
        p.id_metal,
        p.fecha_hora,
        p.precio_venta,
        AVG(p.precio_venta) OVER (
            PARTITION BY p.id_metal 
            ORDER BY p.fecha_hora 
            ROWS BETWEEN 30 PRECEDING AND CURRENT ROW
        ) AS media_movil_30d
    FROM precios p
    WHERE p.divisa = 'USD' AND p.id_metal = 1  
)
SELECT 
    m.nombre AS nombre_metal,
    d.fecha_hora,
    ROUND(d.precio_venta, 2) AS precio_actual,
    ROUND(d.media_movil_30d, 2) AS media_movil_30d,
    CASE 
        WHEN d.precio_venta > d.media_movil_30d THEN 'Por encima (tendencia alcista)'
        WHEN d.precio_venta < d.media_movil_30d THEN 'Por debajo (tendencia bajista)'
        ELSE 'En la media'
    END AS situacion_precio
FROM datos d
INNER JOIN metales m ON m.id = d.id_metal  çç
ORDER BY d.fecha_hora;
