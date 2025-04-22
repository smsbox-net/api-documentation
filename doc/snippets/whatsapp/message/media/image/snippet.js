const url = 'https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID>';
const headers = {
    'Authorization': 'App <APIKEY>',
    'Content-Type': 'application/json'
};
const data = {
    recipients: [
        "+336XXXXXXXX"
    ],
    contentMessage: {
        type: 'image',
        image: {
            link: 'https://www.example.com/fr/file.jpeg',
            filename: 'file.jpeg'
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
