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
        'type': 'interactive',
        'interactive': {
            'type': 'button',
            'header': {
                'type': 'text',
                'text': 'Bienvenue !'
            },
            'body': {
                'type': 'text',
                'text': 'Choisissez une option :'
            },
            'footer': {
                'type': 'text',
                'text': 'Merci de votre visite.'
            },
            'action': {
                'buttons': [
                    {
                        'type': 'reply',
                        'reply': {
                            'id': 'button1',
                            'title': 'Option 1'
                        }
                    },
                    {
                        'type': 'reply',
                        'reply': {
                            'id': 'button2',
                            'title': 'Option 2'
                        }
                    }
                ]
            }
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
