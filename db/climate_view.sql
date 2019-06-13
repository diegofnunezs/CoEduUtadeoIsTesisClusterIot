drop view climate_view;
create view climate_view as
select temperature_view.Node as Node, temperature_view.Time as Time, temperature_view.Location as Location, temperature_view.Temperature as temperature, humidity_view.Humidity as Humidity
from temperature_view, humidity_view
where temperature_view.Node = humidity_view.Node
group by temperature_view.Time;
