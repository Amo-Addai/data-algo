<?php

/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {
    
    function __construct() {}
    function __destruct() {}

    function linearSearch($a, $x) {
        foreach ($a as $i) if ($x === $i) return $i; // item
        foreach ($a as $i => $v) if ($x === $v) return $i; // index
        for ($i = 0; $i < count($a); $i++) if ($x === $a[$i]) return $i; // index
    }

    function binarySearch($a, $x) {
        // sort($a);
        if (empty($a) || count($a) == 0) return null; // only 1 check required

        function rBinarySearch($a, $x) {
            if (empty($a)) return null;
            $m = count($a) / 2;
            if ($x < $a[$m]) return rBinarySearch(array_slice($a, 0, $m - 1), $x);
            elseif ($x > $a[$m]) return rBinarySearch(array_slice($a, $m + 1), $x);
            else return $m;
        }

        function rBinarySearch2p($a, $x, $f, $l) {
            if (empty($a)) return null;
            $m = ($f + $l) / 2;
            if ($x < $a[$m]) return rBinarySearch2p($a, $x, $f, $m - 1);
            elseif ($x > $a[$m]) return rBinarySearch2p($a, $x, $m + 1, $l);
            else return $m;
        }

        $f = 0; $l = count($a) - 1;
        rBinarySearch($a, 7); rBinarySearch2p($a, 7, $f, $l);

        while ($f < $l) {
            $m = ($f + $l) / 2;
            if ($x < $a[$m]) $l =  $m - 1;
            elseif ($x > $a[$m]) $f = $m + 1;
            else return $m;
        }
    }

}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    function __construct() {}
    
}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// 






////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function main($args) {
    echo "Hello, World!";
}

?>