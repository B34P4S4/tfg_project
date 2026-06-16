<?php

$length =
    intval($_POST['length']);

$data =
    substr(
        $_POST['payload'],
        0,
        $length
    );

process($data);