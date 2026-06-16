<?php

$user =
    $_GET['user'];

file_put_contents(
    "app.log",
    "Login failed: $user\n",
    FILE_APPEND
);