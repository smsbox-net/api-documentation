curl --request POST \
    --url https://api.smsbox.pro/waba/json/<WABAID>/message/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
    "recipients": [
        "+336XXXXXXXX"
    ],
    "contentMessage": {
        "type": "audio",
        "audio": {
            "link": "https://www.example.com/fr/file.mp3",
            "filename": "file.mp3"
        }
    }
}'
