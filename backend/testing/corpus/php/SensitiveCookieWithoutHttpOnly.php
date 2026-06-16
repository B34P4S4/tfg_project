<?php

setcookie(
    "session",
    $token,
    0,
    "/",
    "",
    true,
    false
);