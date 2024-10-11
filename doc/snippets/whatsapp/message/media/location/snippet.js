const url = 'https://api.smsbox.pro/waba/json/<WABAID>/message/<PHONEID>';
const headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
};

const data = {
    recipients: [
        "+336XXXXXXXX"
    ],
    contentMessage: {
        type: 'location',
        location: {
            longitude: 6.075501230687077,
            latitude: 43.08811078662267,
            name: 'SMSBOX',
            address: '20 Av. Élie Gautier, 83320 Carqueiranne'
        }
    }
};

fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
