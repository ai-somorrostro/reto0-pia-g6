-- 1. CAMBIO PRECIO ORO AñO A AñO (INICIO VS FIN DE AñO)
WITH precios_inicio_fin AS (
    SELECT 
        YEAR(fecha_hora) AS año,
        precio_venta,
        ROW_NUMBER() OVER (PARTITION BY YEAR(fecha_hora) ORDER BY fecha_hora ASC) AS rn_inicio,
        ROW_NUMBER() OVER (PARTITION BY YEAR(fecha_hora) ORDER BY fecha_hora DESC) AS rn_fin
    FROM precios
    WHERE id_metal = 1 AND divisa = 'USD'
),
precios_agrupados AS (
    SELECT 
        año,
        MAX(CASE WHEN rn_inicio = 1 THEN precio_venta END) AS precio_inicio,
        MAX(CASE WHEN rn_fin = 1 THEN precio_venta END) AS precio_fin
    FROM precios_inicio_fin
    GROUP BY año
)
SELECT 
    año,
    ROUND(precio_inicio, 2) AS precio_inicio,
    ROUND(precio_fin, 2) AS precio_fin,
    ROUND(precio_fin - precio_inicio, 2) AS cambio_dolares,
    CAST(ROUND(((precio_fin - precio_inicio) / precio_inicio * 100), 2) AS VARCHAR) + '%' AS cambio_porcentaje
FROM precios_agrupados
ORDER BY año;

