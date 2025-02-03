import requests
import json

url = 'https://api.smsbox.pro/waba/json/<WABAID>/event/<PHONEID>'
headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
}
data = {
    'message_id': 'wamid.xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'status': 'read'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
