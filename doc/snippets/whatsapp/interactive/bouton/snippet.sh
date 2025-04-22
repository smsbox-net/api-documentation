curl --request POST \
    --url https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
  "recipients": [
    "+336XXXXXXXX"
  ],
  "contentMessage": {
    "type": "interactive",
    "interactive": {
      "type": "button",
      "header": {
        "type": "text",
        "text": "Bienvenue !"
      },
      "body": {
        "type": "text",
        "text": "Choisissez une option :"
      },
      "footer": {
        "type": "text",
        "text": "Merci de votre visite."
      },
      "action": {
        "buttons": [
          {
            "type": "reply",
            "reply": {
              "id": "button1",
              "title": "Option 1"
            }
          },
          {
            "type": "reply",
            "reply": {
              "id": "button2",
              "title": "Option 2"
            }
          }
        ]
      }
    }
  }
}'
