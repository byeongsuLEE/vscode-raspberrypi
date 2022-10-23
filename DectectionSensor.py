import RPi.GPIO as GPIO
import time

pin=14

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

try:
    while True:
        if(GPIO.input(14) == True):
            print ("-----------------")
            time.sleep(0.05)
        else:
            print ("감지")
            time.sleep(0.05)
        
except KeyboardInterrupt:
    p.stop()
finally:
    GPIO.cleanup()
        
        
        
