drop view security_view;
create view security_view as
select movement_view.Node as Node, movement_view.Time as Time, movement_view.Location as Location, movement_view.Movement as Movement, light_view.Light as Light
from movement_view, light_view
where movement_view.Node = movement_view.Node
group by movement_view.Time;
