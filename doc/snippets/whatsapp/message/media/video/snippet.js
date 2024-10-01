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
        type: 'video',
        video: {
            link: 'https://www.example.com/fr/file.mp4',
            filename: 'file.mp4'
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
