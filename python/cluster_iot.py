import RPi.GPIO as GPIO
import time 
import datetime
import sqlite3
import Adafruit_DHT

def read_temperature():
  gpio=17
  temp = 0
  sensor=Adafruit_DHT.DHT11
  humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
  if temperature:
    print('Temperature')
    temp = temperature
    print ('{0:0.1f} ℃'.format(temperature))
  else:
    print('Error')

def read_humidity():
  gpio=17
  hum = 0
  sensor=Adafruit_DHT.DHT11
  humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
  if humidity:
    print('Humidity')
    temp = temperature
    print('{0:0.1f} %'.format(humidity))
  else:
    print('Error')

def read_movement():
  PIR = 23
  ismoving = False

  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PIR, GPIO.IN)

  while True:
    if GPIO.input(PIR) == 1:
      ismoving = True
      print("Motion detected "+str(ismoving))
      break
    else:
      print("No motion detected")

def read_light():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(4,GPIO.IN)
  if GPIO.input(4) == 1:
    print ('Darkness')
  else:
   print ('Light')


if __name__ == '__main__':
    while True:
        temperature = read_temperature()
        time.sleep(5)
        humidity = read_humidity()
        time.sleep(5)
        light = read_light()
        time.sleep(5)
        movement = read_movement()
        time.sleep(5)
