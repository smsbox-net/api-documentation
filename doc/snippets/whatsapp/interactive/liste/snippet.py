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
        'type': 'interactive',
        'interactive': {
            'type': 'list',
            'header': {
                'type': 'text',
                'text': 'Bienvenue !'
            },
            'body': {
                'text': 'Choisissez une option :'
            },
            'footer': {
                'text': 'Merci de votre visite.'
            },
            'action': {
                'button': 'Voir les options',
                'sections': [
                    {
                        'title': 'Catégorie 1',
                        'rows': [
                            {
                                'id': 'option1',
                                'title': 'Option 1',
                                'description': 'Description de l\'option 1'
                            },
                            {
                                'id': 'option2',
                                'title': 'Option 2',
                                'description': 'Description de l\'option 2'
                            }
                        ]
                    }
                ]
            }
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
