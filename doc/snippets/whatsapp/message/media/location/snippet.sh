curl --request POST \
    --url https://api.smsbox.pro/waba/json/<WABAID>/message/<PHONEID> \
    --header 'Authorization: App <APIKEY>' \
    --header 'Content-Type: application/json' \
    --data '{
    "recipients": [
        "+336XXXXXXXX"
    ],
    "contentMessage": {
        "type": "location",
        "location": {
            "longitude": 6.075501230687077,
            "latitude": 43.08811078662267,
            "name": "SMSBOX",
            "address": "20 Av. Élie Gautier, 83320 Carqueiranne"
        }
    }
}'
