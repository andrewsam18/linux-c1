<?php
$x = 10;

switch ($x) {
    case 1:
        echo ("to 1");
        break;
    case 4:
        echo( "to 4");
        break;
    case 10:
        echo("correct option");
        break;
    default:
        echo("final option");//always true if no other case matches
        break;
}
?>
