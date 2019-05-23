DROP TABLE IF EXISTS raw_sensor_data;
DROP TABLE IF EXISTS node_metadata;
DROP TABLE IF EXISTS sensor_metadata;
DROP TABLE IF EXISTS node_sensor;
DROP TABLE IF EXISTS network_metadata;


CREATE TABLE network_metadata (
        sense_time INTEGER NOT NULL,
        PRIMARY KEY(sense_time)
);

CREATE TABLE node_metadata (
        node_id INTEGER NOT NULL ,
        location VARCHAR(15) NOT NULL ,
        PRIMARY KEY(node_id)
);

CREATE TABLE sensor_metadata (
        sensor_id INTEGER NOT NULL ,
        description VARCHAR(15) NOT NULL,
        PRIMARY KEY(sensor_id)
);

CREATE TABLE node_sensor (
        node_id INTEGER NOT NULL ,
        sensor_id INTEGER NOT NULL ,
        node_pin INTEGER NOT NULL ,
        data_position INTEGER,
        PRIMARY KEY (
                node_id,
                sensor_id
        ),
        FOREIGN KEY (node_id) REFERENCES node_metadata(node_id),
        FOREIGN KEY (sensor_id) REFERENCES sensor_metadata (sensor_id)
);

CREATE TABLE raw_sensor_data (
        node_id INTEGER NOT NULL ,
        time DATETIME NOT NULL ,
        sensor_id INTEGER NOT NULL ,
        value DOUBLE NOT NULL ,
        migrated BOOLEAN NOT NULL,
        PRIMARY KEY (
                node_id,
                time,
                sensor_id
        ),
        FOREIGN KEY (node_id, sensor_id) REFERENCES node_sensor (node_id, sensor_id)
);
