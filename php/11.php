<?php

echo __FILE__ . "<br>";
echo __LINE__ . "<br>";
function magic() {
    echo __FUNCTION__;
}
magic();

// Difference between normal constant & magic constant:
// - Normal constants are defined by the user using define() or const, e.g. define('PI', 3.14);
// - Normal constants have fixed values throughout the script and do not change.
// - Magic constants are predefined by PHP and change depending on where they are used, e.g. __FILE__, __LINE__, __FUNCTION__, etc.
// - Magic constants provide information about the code itself, such as file name, line number, function name, class name, etc.
// - Examples of magic constants: __FILE__, __DIR__, __LINE__, __FUNCTION__, __CLASS__, __METHOD__, __NAMESPACE__.
//magic constant
//__magicconstant__
?>