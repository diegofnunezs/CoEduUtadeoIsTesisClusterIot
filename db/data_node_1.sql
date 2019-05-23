INSERT INTO network_metadata (sense_time) VALUES (30);

INSERT INTO node_metadata (node_id, location) VALUES (1, 'Study');

INSERT INTO sensor_metadata (sensor_id, description) VALUES (1, 'Movement');
INSERT INTO sensor_metadata (sensor_id, description) VALUES (2, 'Temperature');
INSERT INTO sensor_metadata (sensor_id, description) VALUES (3, 'Humidity');
INSERT INTO sensor_metadata (sensor_id, description) VALUES (4, 'Light');

INSERT INTO node_sensor (node_id, sensor_id, node_pin, data_position) VALUES (1, 1, 4, null);
INSERT INTO node_sensor (node_id, sensor_id, node_pin, data_position) VALUES (1, 2, 17, 1);
INSERT INTO node_sensor (node_id, sensor_id, node_pin, data_position) VALUES (1, 3, 17, 0);
INSERT INTO node_sensor (node_id, sensor_id, node_pin, data_position) VALUES (1, 4, 14, null);
