import controller
from model import RawSensorData
import Adafruit_DHT

def do_read_temperature(node_pin):
	sensor=Adafruit_DHT.DHT11
	gpio=node_pin
	humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
	if temperature is not None:
		return '{0:0.1f}'.format(temperature)
	else:
		return None
	#return node_pin

def do_read_humidity(node_pin):
	return "humidity"

def do_read_movement(node_pin):
	return "movement"

def do_read_light(node_pin):
	return "light"

def sensor_read(sensor, node_pin):
	switcher = {
		1:do_read_temperature(node_pin),
		2:do_read_humidity(node_pin),
		3:do_read_movement(node_pin),
		4:do_read_light(node_pin)
	}
	function = switcher.get(sensor, "nothing")
	return function

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
		print(sensor_read(nodeSensor["sensor_id"], nodeSensor["node_pin"]))

	#rawSensorData = RawSensorData(node_id=node_id, sensor_id=1, value=20)

	#controller.do_create_sensor_data(rawSensorData)
