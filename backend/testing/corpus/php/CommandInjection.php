<?php

$host = $_GET['host'];

echo shell_exec(
    "ping -c 4 $host"
);