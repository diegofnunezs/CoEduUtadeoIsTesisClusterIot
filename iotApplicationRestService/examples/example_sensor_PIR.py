import RPi.GPIO as GPIO
import time

PIR = 23
ismoving = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

while True:
  if GPIO.input(PIR) == 1:
    ismoving = True
    print("Motion detected "+str(ismoving))
  else:
    print("No motion detected")





