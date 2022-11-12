import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
port="/dev/ttyAMA0" # srial port


ser =serial.Serial(port,baudrate=9600,timeout=0.5)

while 1:
    try:
        data=ser.readline()
        print(data)
    except:
        print("Loading")
        
    
    if data[0.6]=='SGPCGA':
        msg=pynmea2.parse(data)
        print(msg)
        time.sleep(2)


