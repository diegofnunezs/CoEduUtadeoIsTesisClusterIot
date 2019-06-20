drop view security_view;
create view security_view as
select movement_view.Location as Location, strftime('%Y-%m-%d %H:00:00',movement_view.Time) as Time, 
max(movement_view.Movement) as Movement, max(light_view.Light) as Light
from movement_view left join light_view on
movement_view.Node = light_view.Node and
strftime('%Y-%m-%d %H:00:00',movement_view.Time) = strftime('%Y-%m-%d %H:00:00',light_view.Time)
group by movement_view.location, strftime('%Y-%m-%d %H:00:00',movement_view.Time)
