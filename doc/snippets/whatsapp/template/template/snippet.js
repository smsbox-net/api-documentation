const url = 'https://api.wababox.net/waba/1.1/json/<WABAID>/template/<PHONEID>';
const headers = {
	'Authorization': 'App <APIKEY>',
	'Content-Type': 'application/json'
};

fetch(url, {
	method: 'GET',
	headers: headers
})
	.then(response => response.json())
	.then(data => console.log(data))
	.catch(error => console.error('Error:', error));