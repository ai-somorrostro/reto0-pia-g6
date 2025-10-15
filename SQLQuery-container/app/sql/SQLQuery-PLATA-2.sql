-- 2. EVOLUCIñN POR DñCADAS
WITH precios_con_decada AS (
    SELECT 
        (YEAR(fecha_hora) / 10) * 10 AS decada,
        YEAR(fecha_hora) AS año,
        fecha_hora,
        precio_venta
    FROM precios
    WHERE id_metal = 2 AND divisa = 'USD'
),
precios_por_decada AS (
    SELECT 
        decada,
        MIN(año) AS primer_año,
        MAX(año) AS ultimo_año
    FROM precios_con_decada
    GROUP BY decada
),
inicio_fin_decada AS (
    SELECT 
        pd.decada,
        pd.primer_año,
        pd.ultimo_año,
        (SELECT TOP 1 precio_venta 
         FROM precios_con_decada pcd1 
         WHERE pcd1.decada = pd.decada AND pcd1.año = pd.primer_año 
         ORDER BY pcd1.fecha_hora ASC) AS precio_inicio_decada,
        (SELECT TOP 1 precio_venta 
         FROM precios_con_decada pcd2 
         WHERE pcd2.decada = pd.decada AND pcd2.año = pd.ultimo_año 
         ORDER BY pcd2.fecha_hora DESC) AS precio_fin_decada
    FROM precios_por_decada pd
)
SELECT 
    CASE 
        WHEN decada = (YEAR(GETDATE()) / 10) * 10 
        THEN CAST(decada AS VARCHAR) + '-actual'
        ELSE CAST(decada AS VARCHAR) + '-' + CAST(decada + 9 AS VARCHAR)
    END AS periodo_decada,
    ROUND(precio_inicio_decada, 2) AS precio_inicio_decada,
    ROUND(precio_fin_decada, 2) AS precio_fin_decada,
    ROUND(precio_fin_decada - precio_inicio_decada, 2) AS cambio_dolares,
    CAST(ROUND(((precio_fin_decada - precio_inicio_decada) / precio_inicio_decada * 100), 2) AS VARCHAR) + '%' AS cambio_porcentaje
FROM inicio_fin_decada
ORDER BY decada;