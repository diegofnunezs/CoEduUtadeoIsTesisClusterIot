DROP TABLE IF EXISTS raw_sensor_data;
DROP TABLE IF EXISTS node_metadata;
DROP TABLE IF EXISTS sensor_metadata;
DROP TABLE IF EXISTS node_sensor;
DROP TABLE IF EXISTS network_metadata; 


CREATE TABLE network_metadata (
        sense_interval INTEGER NOT NULL 
);

CREATE TABLE node_metadata (
        node_id INTEGER NOT NULL ,
        location VARCHAR(15) NOT NULL ,
        PRIMARY KEY(node_id)
);

CREATE TABLE sensor_metadata (
        sensor_id INTEGER NOT NULL ,
        description VARCHAR(15) NOT NULL 
);

CREATE TABLE node_sensor (
        node_id INTEGER NOT NULL ,
        sensor_id INTEGER NOT NULL ,
        node_pin INTEGER NOT NULL ,
        data_position INTEGER, 
        FOREIGN KEY (node_id) REFERENCES node_metadata(node_id)
);

CREATE TABLE raw_sensor_data (
        node_id INTEGER NOT NULL ,
        time TIME NOT NULL ,
        sensor_id INTEGER NOT NULL ,
        value INTEGER NOT NULL ,
        FOREIGN KEY (node_id) REFERENCES node_metadata(node_id)
);
