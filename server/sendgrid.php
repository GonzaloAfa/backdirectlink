<?php
# includes/sengrid.php

  function contactEmail($name, $email, $msg){

    $url = 'http://back.perfilparlamentario.info/emails/';

    $ch = curl_init( $url );

    $payload = json_encode(array(
                  "customer" => $data,
                  "email" => $email,
                  "msg" => $msg));

    curl_setopt( $ch, CURLOPT_POSTFIELDS, $payload );
    curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
    curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );

    $result = curl_exec($ch);
    curl_close($ch);
  }

?>
