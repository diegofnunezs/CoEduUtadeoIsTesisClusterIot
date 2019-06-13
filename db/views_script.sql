create view temperature_view as
select raw_sensor_data.node_id as Node, raw_sensor_data.time as Time, node_metadata.location as Location, raw_sensor_data.value as Temperature
from raw_sensor_data , node_sensor, sensor_metadata, node_metadata
where node_metadata.node_id = node_sensor.node_id and node_sensor.sensor_id = sensor_metadata.sensor_id and node_sensor.node_id = raw_sensor_data.node_id
and node_sensor.sensor_id = raw_sensor_data.sensor_id and node_sensor.sensor_id = 2;

create view humidity_view as
select raw_sensor_data.node_id as Node, raw_sensor_data.time as Time, node_metadata.location as Location, raw_sensor_data.value as Humidity
from raw_sensor_data , node_sensor, sensor_metadata, node_metadata
where node_metadata.node_id = node_sensor.node_id and node_sensor.sensor_id = sensor_metadata.sensor_id and node_sensor.node_id = raw_sensor_data.node_id
and node_sensor.sensor_id = raw_sensor_data.sensor_id and node_sensor.sensor_id = 3;

create view climate_view as
select temperature_view.Node as Node, temperature_view.Time as Time, temperature_view.Location as Location, temperature_view.Temperature as temperature, humidity_view.Humidity as Humidity
from temperature_view, humidity_view
where temperature_view.Node = humidity_view.Node
group by temperature_view.Time;

create view light_view as
select raw_sensor_data.node_id as Node, raw_sensor_data.time as Time, node_metadata.location as Location, raw_sensor_data.value as Light
from raw_sensor_data , node_sensor, sensor_metadata, node_metadata
where node_metadata.node_id = node_sensor.node_id and node_sensor.sensor_id = sensor_metadata.sensor_id and node_sensor.node_id = raw_sensor_data.node_id
and node_sensor.sensor_id = raw_sensor_data.sensor_id and node_sensor.sensor_id = 4;

create view movement_view as
select raw_sensor_data.node_id as Node, raw_sensor_data.time as Time, node_metadata.location as Location, raw_sensor_data.value as Movement
from raw_sensor_data , node_sensor, sensor_metadata, node_metadata
where node_metadata.node_id = node_sensor.node_id and node_sensor.sensor_id = sensor_metadata.sensor_id and node_sensor.node_id = raw_sensor_data.node_id
and node_sensor.sensor_id = raw_sensor_data.sensor_id and node_sensor.sensor_id = 1;

create view security_view as
select movement_view.Node as Node, movement_view.Time as Time, movement_view.Location as Location, movement_view.Movement as Movement, light_view.Light as Light
from movement_view, light_view
where movement_view.Node = movement_view.Node
group by movement_view.Time;

create view general_view as
select climate_view.Node as Node, climate_view.Time as Time, climate_view.Location as Location,
climate_view.temperature as Temperature, climate_view.Humidity as Humidity,
security_view.Light as Light, security_view.Movement as Movement
from climate_view, security_view
where climate_view.Node = security_view.Node
group by climate_view.Time;
