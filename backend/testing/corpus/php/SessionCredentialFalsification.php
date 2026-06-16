<?php

session_id(
    $_POST['username']
    .
    time()
);

session_start();