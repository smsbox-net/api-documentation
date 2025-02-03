curl --request POST \
    --url https://api.smsbox.pro/waba/json/<WABAID>/message/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
  "recipients": [
    "+336XXXXXXXX"
  ],
 "contentMessage": {
        "type": "interactive",
        "interactive": {
            "type": "list",
            "header": {
                "type": "text",
                "text": "Bienvenue !"
            },
            "body": {
                "text": "Choisissez une option :"
            },
            "footer": {
                "text": "Merci de votre visite."
            },
            "action": {
                "button": "Voir les options",
                "sections": [
                    {
                        "title": "Catégorie 1",
                        "rows": [
                            {
                                "id": "option1",
                                "title": "Option 1",
                                "description": "Description de l'option 1"
                            },
                            {
                                "id": "option2",
                                "title": "Option 2",
                                "description": "Description de l'option 2"
                            }
                        ]
                    }
                ]
            }
        }
    }
}'
