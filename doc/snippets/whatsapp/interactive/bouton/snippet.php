<?php

$url = 'https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID>';
$headers = [
    'Authorization: App <APIKEY>',
    'Content-Type: application/json'
];
$data = [
    'recipients' => [
        "+336XXXXXXXX"
    ],
    'contentMessage' => [
        'type' => 'interactive',
        'interactive' => [
            'type' => 'button',
            'header' => [
                'type' => 'text',
                'text' => 'Bienvenue !'
            ],
            'body' => [
                'type' => 'text',
                'text' => 'Choisissez une option :'
            ],
            'footer' => [
                'type' => 'text',
                'text' => 'Merci de votre visite.'
            ],
            'action' => [
                'buttons' => [
                    [
                        'type' => 'reply',
                        'reply' => [
                            'id' => 'button1',
                            'title' => 'Option 1'
                        ]
                    ],
                    [
                        'type' => 'reply',
                        'reply' => [
                            'id' => 'button2',
                            'title' => 'Option 2'
                        ]
                    ]
                ]
            ]
        ]
    ]
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
