curl --request POST \
    --url https://api.wababox.net/waba/1.1/json/<WABAID>/reaction/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
	"recipients": [
		"+336XXXXXXXX"
	],
	"contentMessage": {
		"type": "reaction",
		"reaction": {
			"message_id": 'wamid.xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
<<<<<<< HEAD
			"emoji": "\uD83D\uDE00"
=======
			"emoji": "😀"
>>>>>>> b193644 (Split messages types)
		}
	}
}'
