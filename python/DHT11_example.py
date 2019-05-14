import RPi.GPIO as GPIO
import time
import datetime
import Adafruit_DHT

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
sensor=Adafruit_DHT.DHT11
gpio = 17
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
if temperature:
 print('TEM')
 print ('{0:0.1f}*C'.format(temperature))
 print('HUM')
 print('{0:0.1f}%'.format(humidity))
else:
 print('Error')

