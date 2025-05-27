<?php
define("Msg", "hello guys");
//define("Msg", "hello guys", true); // Deprecated in PHP 7.3.0, removed in PHP 8.0.0
echo Msg . "<br>";  // Correct usage
//echo MSG . "<br>";   Will not work in PHP 8+, "MSG" is undefined

//define(name, value ,-case-insensitive)false
//xX-> case sensitive


?>