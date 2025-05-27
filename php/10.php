<?php
define("Msg", "hello guys");// first method
const Msg2 = "hii";  //  second method Using const to define a constant
echo constant("Msg") . "<br>";  // Correct usage
echo Msg2 . "<br>";  // Correct usage
?>