curl --request POST \
	--url https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID> \
	--header 'Authorization: App <APIKEY>' \
	--header 'Content-Type: application/json' \
	--data '{
	"recipients": [
		"+336XXXXXXXX"
	],
	"contentMessage": {
		"type": "template",
		"template": {
			"name": "otp",
			"language": {
				"code": "fr"
			},
			"components": [
				{
					"type": "body",
					"parameters": [
						{
							"type": "text",
							"text": "123456"
						}
					]
				},
				{
					"type": "button",
					"sub_type": "url",
					"index": "0",
					"parameters": [
						{
							"type": "text",
							"text": "123456"
						}
					]
				}
			]
		}
	}
}'
