#step 1
#onem2m 리소스 생성하기 (cin)

import requests


url = "http://203.253.128.177:7579/Mobius/phone/data"

headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SluN3OkDey-',
  'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
}

data = {
    "m2m:cin": {
        "con" : "test on raspberry"
    }
}

r = requests.post(url, headers = headers, json = data)

try:
    r.raise_for_status()
    jr = r.json()
    #가장 최근에 생긴 con 값 받아오기
    print(jr['m2m:cin']['con'])
except Exception as exc:
    print('There was a problem %s' %(exc))
