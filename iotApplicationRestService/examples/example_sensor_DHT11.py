import RPi.GPIO as GPIO
import time
import datetime
import Adafruit_DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
gpio=17
temp = 0
hum = 0
sensor=Adafruit_DHT.DHT11
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

if temperature:
  print('Temperature')
  temp = temperature
  print ('{0:0.1f} ℃'.format(temperature))
  print('Humidity')
  hum = humidity
  print('{0:0.1f} %'.format(humidity))
else:
  print('Error')


