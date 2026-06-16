<?php

$total =
    $_POST['price']
    *
    $_POST['qty']
    -
    $_POST['discount'];

charge($total);