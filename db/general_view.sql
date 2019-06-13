drop view general_view;
create view general_view as
select climate_view.Node as Node, climate_view.Time as Time, climate_view.Location as Location,
climate_view.temperature as Temperature, climate_view.Humidity as Humidity,
security_view.Light as Light, security_view.Movement as Movement
from climate_view, security_view
where climate_view.Node = security_view.Node
group by climate_view.Time;
