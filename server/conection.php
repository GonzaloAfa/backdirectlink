<?php

  $url = "http://back.perfilparlamentario.info/emails/"

  public function contactEmail($name='', $email='', $msg=''){

    $conection = curl_init($url);
    curl_setopt($conection, CURLOPT_RETURNTRANSFER,1);
    $result =  curl_exec($conection);

    echo $result;

  }

  contactEmail('Gonzalo', 'gonzalo@afachile.cl', 'Tienen nsm2?');

?>
