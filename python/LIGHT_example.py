import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

while True:
  if GPIO.input(4) == 1:
    print ('Darkness') 
  else:
   print ('Light')


