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
        'type': 'image',
        'image': {
            'link': 'https://www.example.com/fr/file.jpeg',
            'filename': 'file.jpeg'
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
