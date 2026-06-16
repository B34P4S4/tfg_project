<?php

session_start();

$email = $_POST['email'];

$db->query(
    "UPDATE users
     SET email='$email'
     WHERE id=".$_SESSION['user_id']
);