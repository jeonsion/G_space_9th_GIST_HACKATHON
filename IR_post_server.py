#모터가 구동되는 상태에서 IR이 Phone/count 값 만큼 약을 카운트했을 때 서버에 0을 올리는 코드

#importing the library of RPi.GPIO
#importing the library of time
from http import server
import RPi.GPIO as GPIO
import time
import requests
sensor = 16
#시작과 동시에 Object detected를 하므로 default 값을 -1로 선언
count =-1
#declaring BCM pin 16 which is GPIO 23 of Raspberry Pi
GPIO.setmode(GPIO.BOARD)
#declaring the BCM mode of pins
GPIO.setup(sensor,GPIO.IN)
#set the behaviour of sensor as input

while True:
    
    #서버에서 count 값을 Get
    url_count_get = 'http://203.253.128.177:7579/Mobius/phone/count/la'
    #IR에서 서버에 data 값을 Post
    url_count_post ='http://203.253.128.177:7579/Mobius/phone/data/la'

    headers_response_post = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'SluN3OkDey-',
        'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
    }

    headers_count_get = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'SluN3OkDey-',
        'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
    } 
    data = {
        "m2m:cin": {
            "con" : "response_success : 0"
        }
    }
    
    r_count_get = requests.get(url_count_get, headers = headers_count_get)
    r_count_get.raise_for_status()
    jr_count_get=r_count_get.json()
    server_count = (int)(jr_count_get["m2m:cin"]["con"])
    print("서버에서 읽어온 count의 값 : {}".format(server_count))

    


    
    #initiated a infinite while loop
    if GPIO.input(sensor):
    #checking input on sensor
        count+=1
        if(server_count == count ):
            print("잘 들어왔습니다, 서버카운트 값 : {}, 알약이 나온 개수 : {}".format(server_count, count))
            #r_response_post = requests.post(url_count_post, headers = headers_response_post, json = data )
            #r_response_post.raise_for_status()
            break
        print("count : {}, Object detected".format(count))
        while GPIO.input(sensor):  
        #checking input on sensor again
            time.sleep(0.01)
