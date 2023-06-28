<?php

/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

function linearSearch($a, $x) {
    foreach ($a as $i) if ($x === $i) return $i; // item
    foreach ($a as $i => $v) if ($x === $v) return $i; // index
    for ($i = 0; $i < count($a); $i++) if ($x === $a[$i]) return $i; // index
}

function binarySearch($a, $x) {
    if (empty($a) || count($a) == 0) return null; // only 1 check required

    function rBinarySearch($a, $x) {
        if (empty($a)) return null;
        $m = count($a) / 2;
        if ($x < $a[$m]) return rBinarySearch($a, $x); // slice a
        elseif ($x > $a[$m]) return rBinarySearch($a, $x); // slice a
        else return $m;
    }

    function rBinarySearch($a, $x, $f, $l) {
        if (empty($a)) return null;
        $m = ($f + $l) / 2;
        if ($x < $a[$m]) return rBinarySearch($a, $x, $f, $m - 1);
        elseif ($x > $a[$m]) return rBinarySearch($a, $x, $m + 1, $l);
        else return $m;
    }

    $f = 0; $l = count($a) - 1;
    rBinarySearch($a, 7); rBinarySearch($a, 7, $f, $l);

    while ($f < $l) {
        $m = ($f + $l) / 2;
        if ($x < $a[$m]) $l =  $m - 1;
        elseif ($x > $a[$m]) $f = $m + 1;
        else return $m;
    }
}

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

//



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// 

?>