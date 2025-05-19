import requests
import json

url = 'https://api.wababox.net/waba/1.1/json/<WABAID>/template/<PHONEID>'
headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
