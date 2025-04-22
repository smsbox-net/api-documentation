curl --request POST \
    --url https://api.wababox.net/waba/1.1/json/<WABAID>/event/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
		"message_id": "wamid.xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
		"status": "read"
	}
}'
