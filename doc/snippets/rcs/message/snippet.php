<?php

$url = 'https://api.smsbox.pro/rcs/json/<AGENTID>/message';
$headers = [
    'Authorization: App <APIKEY>',
    'Content-Type: application/json'
];

$data = [
    "recipients" => ["+336XXXXXXXX"],
    "contentMessage" => [
        "text" => "example message"
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
