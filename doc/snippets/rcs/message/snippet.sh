curl --request POST \
	--url https://api.smsbox.pro/rcs/json/<AGENTID>/message \
	--header 'Authorization: App <APIKEY>' \
	--header 'Content-Type: application/json' \
	--data '{
	"recipients": [
		"+336XXXXXXXX"
	],
	"contentMessage": {
	    "text": "example message"
	}
}'
