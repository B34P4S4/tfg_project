<?php

$id = $_GET['id'];

$user = $db->query(
    "SELECT * FROM users WHERE id = $id"
)->fetch();

echo json_encode($user);