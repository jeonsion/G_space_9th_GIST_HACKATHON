#ae 생성 하기 (사용자의 ae 중복 유무 검사)

import requests

url = "http://203.253.128.177:7579/Mobius"

#aei는 ae가 생성된 이후에 생성되기 때문에 null 값으로 선언
aei = 0


#----------ae 생성------------

#header_ae 선언 그냥 복붙하면 됨 건들어야할 부분 없음
headers_ae = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'S',                  #aei가 생성되기전 디폴트 값 : 'S', cin 또는 cin 생성시 aei 필요 
  'Content-Type': 'application/vnd.onem2m-res+json;ty=2'
}

#ae 생성시 필요한 데이터, json의 body 형태
data_ae = {
    "m2m:ae" : {
        "rn": "0003",           #생성할 ae의 이름  그 외부분 건들거 없음
        "api" : "0.2.481.2.0001.001.000111",
        "lbl": ["key1", "key2"],
        "rr": True,
        "poa": ["http://203.254.173.104:9727"]
        }
    }


#ae를 생성(post)하는 방법
r_ae = requests.post(url, headers=headers_ae, json=data_ae)         #중요한 부분은 여기임 json 형태로 서버에 post 하는 방법
r_ae.raise_for_status()
jr_ae = r_ae.json()

#정상적으로 json을 post하는지 출력해보기 없어도됨
print(jr_ae)

#aei를 파싱하는 방법 jr["m2m:ae"]['aei']는 생성된 aei 값을 가져온다. 출력해봐서 정상적으로 가져오는지 확인, 이따 컨테이너 만들 때 쓸꺼임
print("aei는" + jr_ae["m2m:ae"]['aei'])
aei = jr_ae["m2m:ae"]['aei']

#ae 이름 : ["m2m:ae"]["rn"] -> 컨테이너를 만들기 위해서는 기본 url에서 "/ae이름" 이 추가되어야한다 ex)http://203.253.128.177:7579/Mobius->http://203.253.128.177:7579/Mobius/count
#ae 가져오기
ae = jr_ae["m2m:ae"]["rn"]


#url 재 정의 된 url  =  url+/ae 이름
url = url+"/"+ ae


#컨테이너의 헤더 부분 중요한거는 'X-M2M-Origin': aei 형태인데 아까 
headers_cnt = {
'Accept': 'application/json',
'X-M2M-RI': '12345',
'X-M2M-Origin': aei,    #aei 위에서 정의한거 가져옴
'Content-Type': 'application/vnd.onem2m-res+json; ty=3'
}


#컨테이너의 데이터 생성 count
data_cnt_count = {
    "m2m:cnt": {
        "rn": "count",       #생성할 컨테이너 이름
        "lbl": ["ss"],
        "mbs": 16384
    }
}

#컨테이너의 데이터 생성 data
data_cnt_data = {
    "m2m:cnt": {
        "rn": "data",       #생성할 컨테이너 이름
        "lbl": ["ss"],
        "mbs": 16384
    }
}



r_cnt = requests.post(url, headers=headers_cnt, json=data_cnt_count)    #서버에 컨테이너 생성하기
r_cnt = requests.post(url, headers=headers_cnt, json=data_cnt_data)     #서버에 컨테이너 생성하기
r_cnt.raise_for_status()
jr_cnt = r_cnt.json()

print(jr_cnt)


