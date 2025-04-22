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
        "text": "Welcome!"
      },
      "body": {
        "type": "text",
        "text": "Choose an option:"
      },
      "footer": {
        "type": "text",
        "text": "Thank you for your visit."
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
