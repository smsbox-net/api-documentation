import requests
import json

url = 'https://api.smsbox.pro/waba/json/<WABAID>/message/<PHONEID>'
headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
}
data = {
    'recipients': [
        "+336XXXXXXXX"
    ],
    'contentMessage': {
        'type': 'audio',
        'audio': {
            'link': 'https://www.example.com/fr/file.mp3',
            'filename': 'file.mp3'
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
