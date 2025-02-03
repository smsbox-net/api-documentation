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
        type: 'interactive',
        interactive: {
            type: 'button',
            header: {
                type: 'text',
                text: 'Bienvenue !'
            },
            body: {
                type: 'text',
                text: 'Choisissez une option :'
            },
            footer: {
                type: 'text',
                text: 'Merci de votre visite.'
            },
            action: {
                buttons: [
                    {
                        type: 'reply',
                        reply: {
                            id: 'button1',
                            title: 'Option 1'
                        }
                    },
                    {
                        type: 'reply',
                        reply: {
                            id: 'button2',
                            title: 'Option 2'
                        }
                    }
                ]
            }
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
