
import RPi.GPIO as GPIO
import time


PIR    = 23
ismoving = False


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)



try:
    time.sleep(1)

    while True:
        if GPIO.input(PIR) == 1:
          ismoving = True
          print("Motion detected "+str(ismoving))
          break
        else:
          print("No motion detected")
except KeyboardInterrupt:
    GPIO.cleanup()








