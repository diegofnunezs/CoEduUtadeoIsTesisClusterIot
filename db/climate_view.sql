drop view climate_view;
create view climate_view as
select temperature_view.Location as Location, strftime('%Y-%m-%d %H:00:00',temperature_view.Time) as Time, 
avg(temperature_view.Temperature) as Temperature, avg(humidity_view.Humidity) as Humidity
from temperature_view left join humidity_view on
temperature_view.Node = humidity_view.Node and
strftime('%Y-%m-%d %H:00:00',temperature_view.Time) = strftime('%Y-%m-%d %H:00:00',humidity_view.Time)
group by temperature_view.Location, strftime('%Y-%m-%d %H:00:00',temperature_view.Time)
