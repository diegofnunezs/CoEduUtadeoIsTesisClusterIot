--Temperatura maxima de los sitios donde se haya registrado movimiento
SELECT location as LOCATION, ROUND(MAX(temperature), 2) as TEMPERATURE
FROM general_view
WHERE movement = 1
GROUP BY location