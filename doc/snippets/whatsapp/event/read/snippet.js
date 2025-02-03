const url = 'https://api.smsbox.pro/waba/json/<WABAID>/event/<PHONEID>';
const headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
};
const data = {
    message_id: 'wamid.xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    status: 'read'
};

fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
