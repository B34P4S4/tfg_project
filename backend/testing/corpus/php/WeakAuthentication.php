<?php

$user =
    findUser(
        $_POST['username']
    );

if(
    $user['password']
    ==
    $_POST['password']
){
    login($user);
}