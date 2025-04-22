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
        type: 'interactive',
        interactive: {
            type: 'list',
            header: {
                type: 'text',
                text: 'Bienvenue !'
            },
            body: {
                text: 'Choisissez une option :'
            },
            footer: {
                text: 'Merci de votre visite.'
            },
            action: {
                button: 'Voir les options',
                sections: [
                    {
                        title: 'Catégorie 1',
                        rows: [
                            {
                                id: 'option1',
                                title: 'Option 1',
                                description: 'Description de l\'option 1'
                            },
                            {
                                id: 'option2',
                                title: 'Option 2',
                                description: 'Description de l\'option 2'
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
