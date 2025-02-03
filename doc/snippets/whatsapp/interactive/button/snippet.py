import requests
import json

url = 'https://api.smsbox.pro/waba/json/<WABAID>/interactive-buttons/<PHONEID>'
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
                'text': 'Welcome!'
            },
            'body': {
                'type': 'text',
                'text': 'Choose an option:'
            },
            'footer': {
                'type': 'text',
                'text': 'Thank you for your visit.'
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
