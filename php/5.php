<?php
$z=3;// Global variable
function local(){
    $x = 10; // Local variable
    //$z=30;// This would create a new local variable $z, not affecting the global $z
   // global $z; // Accessing the global variable
    $y=$GLOBALS['z']; // Accessing the global variable using $GLOBALS array
   echo " local variable: $y";
}
local ();
?>