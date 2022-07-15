#휴대폰에서 서버에 값을 올리면 기기가 값을 실시간으로 받아온 다음 모터를 구동하는 로직

import requests
import time




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

    time.sleep(2)
    try:
        r.raise_for_status()
        jr = r.json()
        if(jr["m2m:cin"]["con"][-1]=="1"):
            print("motor_working")
        else:
            print(jr["m2m:cin"]["con"])
    except Exception as exc:
        print("There was a problem : %s".format(exc))
