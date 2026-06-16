<?php

$data = $_POST['data'];

$buffer = str_repeat("A", 32);

$buffer .= $data;