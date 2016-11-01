<?php

  $url = "http://back.perfilparlamentario.info/emails/";

  function contactEmail($name='', $email='', $msg=''){

    $conection = curl_init($url+"?name="+$name+"&email="+$email+"&msg="+$msg);
    curl_setopt($conection, CURLOPT_RETURNTRANSFER,1);
    $result =  curl_exec($conection);

    echo $result;

  }

  contactEmail('Gonzalo', 'gonzalo@afachile.cl', 'Tienen nsm2?');

?>
