<?php

ini_set("display_errors", 1);

try {

    throw new Exception(
        "Database connection failed"
    );

}
catch(Exception $e){

    echo $e->getTraceAsString();
}