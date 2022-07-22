#ae 생성 하기 (사용자의 ae 중복 유무 검사)

import requests

url = "http://203.253.128.177:7579/Mobius"
aei = 0

headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'S',
  'Content-Type': 'application/vnd.onem2m-res+json;ty=2'
}
data_ae = {
    "m2m:ae" : {
        "rn": "jeonsion",
        "api" : "0.2.481.2.0001.001.000111",
        "lbl": ["key1", "key2"],
        "rr": True,
        "poa": ["http://203.254.173.104:9727"]
        }
    }


try :
    r_ae = requests.post(url, headers=headers, json=data_ae)
    r_ae.raise_for_status()
    jr_ae = r_ae.json()
    print(jr)
    print()
    print()
    #aei를 파싱하는 방법 jr["m2m:ae"]['aei']
    print("aei는" + jr_ae["m2m:ae"]['aei'])
    
except Exception as exc:
    print("이미 있는 사용자 입니다.")
    
    #컨테이너 만들기 기존에 있던 컨테이너에서 오른쪽 값 슬라이싱 해서 +1 (카운터 컨테이너, 데이터 컨테이너 동시적용)






