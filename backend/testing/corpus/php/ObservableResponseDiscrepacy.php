<?php

$user =
findUser(
    $_POST['username']
);

if(!$user){
    die(
        "User not found"
    );
}

if(
    $user['password']
    !=
    $_POST['password']
){
    die(
        "Wrong password"
    );
}