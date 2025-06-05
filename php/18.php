<?php

$n=1;
while($n<=10){
    echo " $n <br>";
    $n++;
    
}
// while loop
/**
 * Iterates over a sequence of values using a while loop.
 * 
 * The loop continues as long as the specified condition is true.
 * It is commonly used when the number of iterations is not known beforehand.
 * 
 * Example:
 * while ($condition) {
 *     // Code to execute on each iteration
 * }
 * 
 * @var int $n Loop counter variable.
 * @var bool $condition Condition that determines whether to continue the loop.
 */
//finite loop
// Note: Ensure that the condition will eventually become false to avoid an infinite loop.
//infinite loop
// while (true) {
//     // Code that will run indefinitely
//     // Be cautious with infinite loops as they can cause the program to hang.
//     // Use a break statement to exit the loop when needed.   
//     break; // Example of breaking out of the infinite loop
?>