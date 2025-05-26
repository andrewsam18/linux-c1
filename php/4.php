<?php
function local(){
    $x = 10; // Local variable
    echo "my value of local variable: $x";
}
local ();
$x=20;
echo"my local value outside fn:$x"; 
// This will cause an error because $x is not defined outside the function
// Call the function to see the local variable in action
// Note: In PHP, variables defined inside a function are local to that function and cannot be accessed outside of it.

// To access a variable outside the function, you can either return it or use the global keyword to make it accessible globally.
// Example of using the global keyword
?>