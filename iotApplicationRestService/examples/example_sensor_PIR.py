import RPi.GPIO as GPIO
import time

PIR = 23
ismoving = False
mov = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

for x in range(0, 25):
        ismoving = False
        print ("We're on time" + str(x))
        if GPIO.input(PIR):
                ismoving = True
                print("Motion detected "+str(ismoving))
                time.sleep(1)
                mov = mov + 1
                break ##Rompe el for 
        else:
                print("No motion detected "+str(ismoving))
                time.sleep(1)

print ("Veces que se marca en "+ str(x) + "iteraciones" + str(mov))


