<?php

$template =
    $_POST['template'];

$smarty->display(
    "string:" . $template
);