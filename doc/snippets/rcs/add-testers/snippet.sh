curl --request POST \
	--url https://api.rcsbox.net/rcs/1.0/json/<AGENTID>/add-testers \
	--header 'Authorization: App <APIKEY>' \
	--header 'Content-Type: application/json' \
	--data '{ "recipients": "+336XXXXXXXX" }'
