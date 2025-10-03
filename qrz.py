import json

import requests

with open("qrz.token", "r") as f:
    token = f.read().strip()

url = "http://logbook.qrz.com/api"
body = {"KEY": token, "ACTION": "FETCH", "OPTION": "TYPE:ADIF"}

response = requests.post(url, data=body)

if response.status_code == 200:
    print(response.text)
