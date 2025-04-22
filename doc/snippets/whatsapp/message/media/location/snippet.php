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
        'type' => 'location', 
        'location' => [
            'longitude' => 6.075501230687077,
            'latitude' => 43.08811078662267,
            'name' => 'SMSBOX',
            'address' => '20 Av. Élie Gautier, 83320 Carqueiranne' 
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
