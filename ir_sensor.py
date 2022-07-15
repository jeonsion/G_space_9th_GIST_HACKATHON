import RPi.GPIO as GPIO
#importing the library of RPi.GPIO
import time
#importing the library of time
sensor = 16
#declaring BCM pin 16 which is GPIO 23 of Raspberry Pi
GPIO.setmode(GPIO.BOARD)
#declaring the BCM mode of pins
GPIO.setup(sensor,GPIO.IN)
#set the behaviour of sensor as input
try:
    while True:
        #initiated a infinite while loop
        if GPIO.input(sensor):
        #checking input on sensor
            print("Object detected")
            while GPIO.input(sensor):
            #checking input on sensor again
              time.sleep(0.01)
        #generate time delay of 0.2 seconds
except KeyboardInterrupt:
#if any key is pressed on keyboard terminate the program
    GPIO.cleanup()
    #cleanup the GPIO pins for any other program use