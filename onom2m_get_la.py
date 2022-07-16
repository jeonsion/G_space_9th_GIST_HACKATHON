#onem2m 가장 최신 리소스 가져오기(get la)

import requests

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

    print(jr["m2m:cin"]["con"])
except Exception as exc:
    print("There was a problem : %s".format(exc))
