<?php

$password = $_POST['password'];

$hash = md5($password);

savePassword($hash);