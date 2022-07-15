#휴대폰에서 서버에 값을 올리면 기기가 값을 실시간으로 받아온 다음 모터를 구동하는 로직
import requests
import time
import RPi.GPIO as GPIO
import time
 
in1 = 17
in2 = 18
in3 = 27
in4 = 22
 
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002
 
step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
 
direction = False # 시계방향일 때 True 시계반대방향일 때 False
 
# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
 
# initializing
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )
 
 
motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0 
 
def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup() 

def Motor_working():
    i = 0
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )
       
    






print("실시간으로 값 읽어오기")
print("----------------------------------")
while(True):
    url = 'http://203.253.128.177:7579/Mobius/phone/data/la'
    headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SluN3OkDey-',
    'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
    }

    r = requests.get(url, headers = headers)

    
    try:
        r.raise_for_status()
        jr = r.json()
        if(jr["m2m:cin"]["con"][-1]=="1"):
            print("motor_working")
            Motor_working()
        else:
            print(jr["m2m:cin"]["con"])
    except Exception as exc:
        print("There was a problem : %s".format(exc))