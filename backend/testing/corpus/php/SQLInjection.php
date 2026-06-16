<?php

$username = $_GET['user'];

$sql =
    "SELECT * FROM users
     WHERE username = '$username'";

$result =
    mysqli_query($conn, $sql);