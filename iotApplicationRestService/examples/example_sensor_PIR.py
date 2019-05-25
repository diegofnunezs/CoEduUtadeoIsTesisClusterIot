import RPi.GPIO as GPIO
import time

node_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(node_pin, GPIO.IN)

def do_read_movement():
	for x in range(0, 5):
		if GPIO.input(node_pin):
			return 1
		else:
                        time.sleep(1)
	return 0

if __name__ == '__main__':
	x=do_read_movement()
	print(x)
