<?php

$path = $_GET['path'];

include(
    "/var/www/uploads/" .
    $path
);