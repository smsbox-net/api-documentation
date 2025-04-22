import requests
import json

url = 'https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID>'
headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
}
data = {
    'recipients': [
        "+336XXXXXXXX"
    ],
    'contentMessage': {
        'type': 'video',
        'video': {
            'link': 'https://www.example.com/fr/file.mp4',
            'filename': 'file.mp4'
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
