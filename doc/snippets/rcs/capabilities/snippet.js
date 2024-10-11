const url = 'https://api.smsbox.pro/rcs/json/<AGENTID>/capabilities';
const headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
};
const data = {
    recipients: ["+336XXXXXXXX"]
};

fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));