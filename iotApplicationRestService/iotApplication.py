import datetime
import controller#, service
from time import sleep
from datetime import timedelta
from model import RawSensorData

#def sensor_read(sensor, node_pin):
#	switcher = {
#		1:service.do_read_movement(node_pin),
#		2:service.do_read_temperature(node_pin),
#		3:service.do_read_humidity(node_pin),
#		4:service.do_read_light(node_pin)
#	}
#	function = switcher.get(sensor, None)
#	return function

if __name__ == '__main__':
	isStart = False
	senseTime = 0
	nodeId = 0
	nowDate = None

	senseTimeRow = controller.get_sense_time()

	for senseTime in senseTimeRow:
		senseTime = senseTime["sense_time"]

	nodeRow = controller.get_node()
	for node in nodeRow:
		nodeId = node["node_id"]

	while True:
		if isStart:
			sleep(senseTime)
		else:
			isStart = True

		if nowDate is not None:
			nowDate += timedelta(seconds=senseTime)
		else:
			nowDate = datetime.datetime.now()

		nodeSensorRow = controller.get_node_sensors(nodeId)
		for nodeSensor in nodeSensorRow:
			print('NodeSensor {0} {1} {2} {3} '.format(nodeSensor["node_id"],nodeSensor["sensor_id"],nodeSensor["node_pin"],nodeSensor["data_position"]))
			sensorValue = 1#sensor_read(nodeSensor["sensor_id"], nodeSensor["node_pin"])
			rawSensorData = RawSensorData(node_id=nodeId, sensor_id=nodeSensor["sensor_id"], time=nowDate, value=sensorValue)
			controller.do_create_sensor_data(rawSensorData)
