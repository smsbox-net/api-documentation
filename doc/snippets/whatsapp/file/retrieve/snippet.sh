curl --request POST \
    --url https://api.smsbox.pro/waba/json/<WABAID>/event/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
		"file_id": "1234567890"
	}
}'
