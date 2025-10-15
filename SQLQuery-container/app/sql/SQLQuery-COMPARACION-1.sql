-- COMPARACIÓN ENTRE ORO Y PLATA POR AÑO (DIFERENCIA EN USD, %, Y RATIO ORO/PLATA)
WITH precios_filtrados AS (
    SELECT 
        id_metal,
        YEAR(fecha_hora) AS año,
        AVG(precio_venta) AS precio_medio
    FROM precios
    WHERE id_metal IN (1, 2) AND divisa = 'USD'
    GROUP BY id_metal, YEAR(fecha_hora)
),
comparacion AS (
    SELECT 
        oro.año,
        oro.precio_medio AS precio_oro,
        plata.precio_medio AS precio_plata,
        ROUND(oro.precio_medio - plata.precio_medio, 2) AS diferencia_dolares,
        CAST(ROUND(((oro.precio_medio - plata.precio_medio) / plata.precio_medio * 100), 2) AS VARCHAR) + '%' AS diferencia_porcentaje,
        ROUND(oro.precio_medio / plata.precio_medio, 2) AS ratio_oro_plata
    FROM precios_filtrados oro
    INNER JOIN precios_filtrados plata 
        ON oro.año = plata.año
    WHERE oro.id_metal = 1 AND plata.id_metal = 2
)
SELECT 
    año,
    ROUND(precio_oro, 2) AS precio_oro,
    ROUND(precio_plata, 2) AS precio_plata,
    diferencia_dolares,
    diferencia_porcentaje,
    ratio_oro_plata
FROM comparacion
ORDER BY año;
