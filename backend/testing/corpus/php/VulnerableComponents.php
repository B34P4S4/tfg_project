<?php

require 'vendor/autoload.php';

use SomeOldLibrary\Parser;

$parser = new Parser();

echo $parser->parse(
    $_POST['content']
);