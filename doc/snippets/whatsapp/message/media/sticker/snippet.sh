curl --request POST \
    --url https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
    "recipients": [
        "+336XXXXXXXX"
    ],
    "contentMessage": {
        "type": "sticker",
        "sticker": {
            "link": "https://www.example.com/fr/file.webp",
            "filename": "file.webp"
        }
    }
}'
