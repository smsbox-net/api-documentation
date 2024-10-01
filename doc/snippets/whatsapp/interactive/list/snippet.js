const url = 'https://api.smsbox.pro/waba/json/<WABAID>/interactive-list/<PHONEID>';
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
            type: 'list',
            header: {
                type: 'text',
                text: 'Welcome!'
            },
            body: {
                text: 'Choose an option:'
            },
            footer: {
                text: 'Thank you for your visit.'
            },
            action: {
                button: 'View options',
                sections: [
                    {
                        title: 'Catégorie 1',
                        rows: [
                            {
                                id: 'option1',
                                title: 'Option 1',
                                description: 'Option description 1'
                            },
                            {
                                id: 'option2',
                                title: 'Option 2',
                                description: 'Option description 2'
                            }
                        ]
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
