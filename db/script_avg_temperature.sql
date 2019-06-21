--Temperatura promedio cada dia, entre las 7 a.m. y 5 p.m.
SELECT strftime('%Y-%m-%d',time) as DATE, ROUND(avg(temperature), 2) AS AVG_TEMPERATURE
FROM general_view
WHERE strftime('%H:00:00',time) between strftime('%H:00:00', '07:00:00') and strftime('%H:00:00', '17:00:00')
GROUP BY strftime('%Y-%m-%d',time)