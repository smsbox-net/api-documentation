<?php

$url = 'https://api.wababox.net/waba/1.1/json/<WABAID>/message/<PHONEID>';
$headers = [
    'Authorization: App <APIKEY>',
    'Content-Type: application/json'
];

$data = [
    "recipients" => ["+336XXXXXXXX"],
    "contentMessage" => [
        "type" => "template",
        "template" => [
            "name" => "otp",
            "language" => [
                "code" => "fr"
            ],
            "components" => [
                [
                    "type" => "body",
                    "parameters" => [
                        [
                            "type" => "text",
                            "text" => "123456"
                        ]
                    ]
                ],
                [
                    "type" => "button",
                    "sub_type" => "url",
                    "index" => "0",
                    "parameters" => [
                        [
                            "type" => "text",
                            "text" => "123456"
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
