-- MÁXIMOS Y MÍNIMOS HISTÓRICOS DE CADA METAL (JOIN con tabla metales)
WITH precios_basicos AS (
    SELECT 
        id_metal,
        precio_venta,
        fecha_hora
    FROM precios
    WHERE divisa = 'USD'
),
maximos_minimos AS (
    SELECT 
        p1.id_metal,
        MAX(p1.precio_venta) AS precio_maximo,
        MIN(p1.precio_venta) AS precio_minimo,
        (SELECT TOP 1 fecha_hora 
         FROM precios_basicos p2 
         WHERE p2.id_metal = p1.id_metal 
           AND p2.precio_venta = (SELECT MAX(precio_venta) FROM precios_basicos WHERE id_metal = p1.id_metal)
         ORDER BY fecha_hora ASC) AS fecha_maximo,
        (SELECT TOP 1 fecha_hora 
         FROM precios_basicos p3 
         WHERE p3.id_metal = p1.id_metal 
           AND p3.precio_venta = (SELECT MIN(precio_venta) FROM precios_basicos WHERE id_metal = p1.id_metal)
         ORDER BY fecha_hora ASC) AS fecha_minimo
    FROM precios_basicos p1
    GROUP BY p1.id_metal
)
SELECT 
    m.nombre AS nombre_metal,
    ROUND(mm.precio_maximo, 2) AS precio_maximo,
    CONVERT(date, mm.fecha_maximo) AS fecha_maximo,
    ROUND(mm.precio_minimo, 2) AS precio_minimo,
    CONVERT(date, mm.fecha_minimo) AS fecha_minimo
FROM maximos_minimos mm
INNER JOIN metales m ON m.id = mm.id_metal 
ORDER BY m.nombre;
