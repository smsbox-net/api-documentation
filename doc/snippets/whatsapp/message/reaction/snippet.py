import requests
import json

url = 'https://api.smsbox.pro/waba/json/<WABAID>/reaction/<PHONEID>'
headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
}
data = {
    "recipients": [
        "+336XXXXXXXX"
    ],
    "contentMessage": {
        "type": "reaction",
        "reaction": {
            "message_id": 'wamid.xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            "emoji": "😀"
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
