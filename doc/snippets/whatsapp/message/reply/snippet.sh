curl --request POST \
    --url https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
<<<<<<< HEAD
	"recipients": [
		"+336XXXXXXXX"
	],
	"contentMessage": {
      "type": "text",
      "context": { "message_id": "wamid.xxxxxxxxxxxxxxxxxxxxxxxxxxxx" },
      "text": { "body": "Reply to the previous message." }
=======
    "recipients": [
      "+336XXXXXXXX"
    ],
    "contentMessage": {
      "type": "text",
      "context": {
        "message_id": "wamid.xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      },
      "text": {
        "body": "Reply to the previous message."
      }
>>>>>>> b193644 (Split messages types)
    }
  }'
