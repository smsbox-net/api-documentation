import requests
import json

url = 'https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID>'
headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
}
data = {
    "recipients": ["+336XXXXXXXX"],
    "contentMessage": {
        "type": "template",
        "template": {
            "name": "otp",
            "language": {
                "code": "fr"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": "123456"
                        }
                    ]
                },
                {
                    "type": "button",
                    "sub_type": "url",
                    "index": "0",
                    "parameters": [
                        {
                            "type": "text",
                            "text": "123456"
                        }
                    ]
                }
            ]
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
