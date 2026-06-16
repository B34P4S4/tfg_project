<?php

$file = $_GET['file'];

readfile("/var/www/files/" . $file);