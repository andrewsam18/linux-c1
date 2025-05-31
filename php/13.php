<?php
$x = 10;
if($x>5){//true
    if($x>12){   //false
     echo " x is larger";

} else {
        echo "smaller";
    }
}

//nested if
// This code demonstrates the use of nested if statements in PHP.
// - The outer if checks if $x is greater than 5.
// - The inner if checks if $x is greater than 12.
// - If both conditions are true, it prints "x is larger".
// - If the outer condition is true but the inner condition is false, it prints "smaller".
// - If the outer condition is false, the inner condition is not evaluated.
// - This structure allows for more complex decision-making in the code.
// - Nested if statements can be used to create more specific conditions based on previous checks.
// if-else
// - The outer if-else structure allows for handling different scenarios based on the value of $x.      
// - The inner if-else structure allows for further refinement of the decision-making process based on additional conditions.
// - This approach helps in organizing code and making it more readable by clearly defining the flow of logic.  

?>