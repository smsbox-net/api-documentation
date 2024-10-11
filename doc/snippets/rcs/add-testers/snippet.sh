curl --request POST \
	--url https://api.smsbox.pro/rcs/json/<AGENTID>/add-testers \
	--header 'Authorization: App <APIKEY>' \
	--header 'Content-Type: application/json' \
	--data '{ "recipients": "+336XXXXXXXX" }'
