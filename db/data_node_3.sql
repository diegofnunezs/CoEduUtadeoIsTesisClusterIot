INSERT INTO network_metadata (sense_interval) VALUES (600);

INSERT INTO node_metadata (node_id, location) VALUES (3, 'Kitchen');

INSERT INTO sensor_metadata (sensor_id, description) VALUES (1, 'Movement');
INSERT INTO sensor_metadata (sensor_id, description) VALUES (2, 'Temperature');
INSERT INTO sensor_metadata (sensor_id, description) VALUES (3, 'Humidity');
INSERT INTO sensor_metadata (sensor_id, description) VALUES (4, 'Light');

INSERT INTO node_sensor (node_id, sensor_id, node_pin, data_position) VALUES (3, 2, 17, 1);
INSERT INTO node_sensor (node_id, sensor_id, node_pin, data_position) VALUES (3, 3, 17, 0);