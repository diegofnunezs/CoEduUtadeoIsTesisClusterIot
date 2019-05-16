import controller
import datetime
from model import RawSensorData

if __name__ == '__main__':
	senseTimeRow = controller.get_sense_time()
	for senseTime in senseTimeRow:
		print(senseTime["sense_time"])
	node_id = 0

	nodeRow = controller.get_node()
	for node in nodeRow:
		node_id = node["node_id"]

	nodeSensorRow = controller.get_node_sensors(node_id)
	for nodeSensor in nodeSensorRow:
		print('NodeSensor {0} {1} {2} {3} '.format(nodeSensor["node_id"],nodeSensor["sensor_id"],nodeSensor["node_pin"],nodeSensor["data_position"]))

	rawSensorData = RawSensorData(node_id=node_id, sensor_id=1, value=20)

	controller.do_create_sensor_data(rawSensorData)
