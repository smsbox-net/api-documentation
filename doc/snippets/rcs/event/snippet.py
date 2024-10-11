import requests
import json

url = 'https://api.smsbox.pro/rcs/json/<AGENTID>/event'
headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
}
data = {
    "recipients": ["+336XXXXXXXX"],
    "event": "READ"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
