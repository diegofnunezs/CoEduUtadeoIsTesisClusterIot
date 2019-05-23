import Adafruit_DHT, RPi.GPIO as GPIO

def do_read_temperature(node_pin):
	sensor=Adafruit_DHT.DHT11
	gpio=node_pin
	humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
	if temperature is not None:
		return '{0:0.1f}'.format(temperature)
	else:
		return 0

def do_read_humidity(node_pin):
	sensor=Adafruit_DHT.DHT11
	gpio=node_pin
	humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
	if humidity is not None:
		return '{0:0.1f}'.format(humidity)
	else:
		return 0

def do_read_movement(node_pin):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(node_pin, GPIO.IN)
	if GPIO.input(node_pin) == 1:
		return 1
	else:
		return 0

def do_read_light(node_pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(node_pin, GPIO.IN)
	if GPIO.input(node_pin) == 1:
		return 0
	else:
		return 1
