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
        'type': 'location', 
        'location': {
            'longitude': 6.075501230687077,
            'latitude': 43.08811078662267,
            'name': 'SMSBOX',
            'address': '20 Av. Élie Gautier, 83320 Carqueiranne'
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
