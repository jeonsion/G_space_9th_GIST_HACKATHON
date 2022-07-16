#step 2
#importing the library of RPi.GPIO
#importing the library of time
import RPi.GPIO as GPIO
import time

sensor = 16
#시작과 동시에 Object detected를 하므로 default 값을 -1로 선언
count =-1
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
            count+=1
            print("count : {}, Object detected".format(count))
            while GPIO.input(sensor):
            #checking input on sensor again
              time.sleep(0.01)
        #generate time delay of 0.2 seconds
except KeyboardInterrupt:
#if any key is pressed on keyboard terminate the program
    GPIO.cleanup()
    #cleanup the GPIO pins for any other program use
