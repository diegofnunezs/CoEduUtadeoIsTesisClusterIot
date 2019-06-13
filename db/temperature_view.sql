drop view temperature_view;
create view temperature_view as
select raw_sensor_data.node_id as Node, raw_sensor_data.time as Time, node_metadata.location as Location, raw_sensor_data.value as Temperature
from raw_sensor_data , node_sensor, sensor_metadata, node_metadata
where node_metadata.node_id = node_sensor.node_id and node_sensor.sensor_id = sensor_metadata.sensor_id and node_sensor.node_id = raw_sensor_data.node_id
and node_sensor.sensor_id = raw_sensor_data.sensor_id and node_sensor.sensor_id = 2;
