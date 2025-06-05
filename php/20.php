<?php
$n=1;
while($n<3){
    $p=1;
    while($p<3){
        echo $n.":".$p;
        echo"<br>";
        $p++;
}
$n++;
/* This is the end of the outer while loop.
    The program uses nested while loops to print pairs of $n and $p values.
    For each $n from 1 to 2, it prints $p from 1 to 2, displaying the pairs as "n:p".
*/
}

?>