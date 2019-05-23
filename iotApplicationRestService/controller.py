from config import db
import model as _model

def get_sense_time():
	networkMetadata = _model.NetworkMetadata.query.all()
	networkMetadataSchema = _model.NetworkMetadataSchema(many=True)
	data = networkMetadataSchema.dump(networkMetadata).data
	return data

def get_node():
	nodeMetadata = _model.NodeMetadata.query.all()
	nodeMetadataSchema = _model.NodeMetadataSchema(many=True)
	data = nodeMetadataSchema.dump(nodeMetadata).data
	return data

def get_node_sensors(node_id):
	nodeSensor = _model.NodeSensor.query.filter(_model.NodeSensor.node_id == node_id).all()
	nodeSensorSchema = _model.NodeSensorSchema(many=True)
	data = nodeSensorSchema.dump(nodeSensor).data
	return data

def get_node_sensor_data():
	rawSensorData = _model.RawSensorData.query.all()
	rawSensorDataSchema = _model.RawSensorDataSchema(many=True)
	data = rawSensorDataSchema.dump(rawSensorData).data
	return data

def do_create_sensor_data(rawSensorData):
	db.session.add(rawSensorData)
	db.session.commit()
