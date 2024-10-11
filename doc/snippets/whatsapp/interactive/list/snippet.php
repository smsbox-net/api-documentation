<?php

$url = 'https://api.smsbox.pro/waba/json/<WABAID>/interactive-list/<PHONEID>';
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
            'type' => 'list',
            'header' => [
                'type' => 'text',
                'text' => 'Welcome!'
            ],
            'body' => [
                'text' => 'Choose an option:'
            ],
            'footer' => [
                'text' => 'Thank you for your visit.'
            ],
            'action' => [
                'button' => 'View options',
                'sections' => [
                    [
                        'title' => 'Catégorie 1',
                        'rows' => [
                            [
                                'id' => 'option1',
                                'title' => 'Option 1',
                                'description' => 'Option description 1'
                            ],
                            [
                                'id' => 'option2',
                                'title' => 'Option 2',
                                'description' => 'Option description 2'
                            ]
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
