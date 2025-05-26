<?php
function local(){
//$y = 10; // Local variable
static$y=10; // Local variable
    $y++; // Incrementing the local variable
    echo " local variable: ".$y."<br>";
}
local();
local();
//there is three types of variables in PHP:
// 1. Local variables: Variables defined within a function and accessible only within that function.
// 2. Global variables: Variables defined outside of any function and accessible throughout the script.
// 3. Static variables: Variables that retain their value between function calls, defined with the static keyword.
// The static keyword allows the variable to retain its value between function calls
// In this case, the variable $y will not be re-initialized to 10 on subsequent calls to local(). 
// Instead, it will keep its value from the last call, which is incremented by 1 each time.
// This means that the output will show the incremented value of $y each time the function is called.
// Output will be:
// local variable: 11   
// local variable: 12
// Note: Static variables are useful when you want to maintain state across function calls without using global variables.  



?>