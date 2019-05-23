from datetime import datetime
from config import db, ma

class NetworkMetadata(db.Model):
	__tablename__ = "network_metadata"
	sense_time = db.Column(db.Integer, primary_key=True)

class NodeMetadata(db.Model):
	__tablename__ = "node_metadata"
	node_id = db.Column(db.Integer, primary_key=True)
	location = db.Column(db.String(15))

class NodeSensor(db.Model):
	__tablename__ = "node_sensor"
	node_id = db.Column(db.Integer, primary_key=True)
	sensor_id = db.Column(db.Integer, primary_key=True)
	node_pin = db.Column(db.Integer)
	data_position = db.Column(db.Integer)

class RawSensorData(db.Model):
	__tablename__ = "raw_sensor_data"
	node_id = db.Column(db.Integer, primary_key=True)
	sensor_id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow, onupdate=datetime.utcnow)
	value = db.Column(db.Integer)
	migrated = db.Column(db.Boolean)

class NetworkMetadataSchema(ma.ModelSchema):
	class Meta:
		model = NetworkMetadata
		sqla_session = db.session

class NodeMetadataSchema(ma.ModelSchema):
	class Meta:
		model = NodeMetadata
		sqla_session = db.session

class NodeSensorSchema(ma.ModelSchema):
	class Meta:
		model = NodeSensor
		sqla_session = db.session

class RawSensorDataSchema(ma.ModelSchema):
	class Meta:
		model = RawSensorData
		sqla_session = db.session
