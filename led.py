import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
while True:                             # RUN FOREVER
    GPIO.output(8,GPIO.HIGH)            #turn on
    sleep(1)                            #sleep for 1s
    GPIO.output(8,GPIO.LOW)             #turn off
    sleep(1)                            #sleep for 1s
