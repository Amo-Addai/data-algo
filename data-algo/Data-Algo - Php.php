<?php

/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    function __construct() {}
    
}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    private $i;
    
    function __construct() {
        $this->i = -1;
    }

    function __destruct() {
        $this->i = -1;
    }

    public function linearSearch($a, $x) {
        foreach ($a as $i) if ($x === $i) return $i; // item
        foreach ($a as $i => $v) if ($x === $v) return $i; // index
        for ($i = 0; $i < count($a); $i++) if ($x === $a[$i]) return $i; // index
    }

    public function binarySearch($a, $x) {
        if (empty($a) || count($a) == 0) return null; // only 1 check required

        sort($a);

        function rBinarySearch($a, $x) {
            if (empty($a)) return null;
            $l = count($a);
            $m = floor($l / 2);
            if ($x == $a[$m]) return $a[$m];
            elseif ($x < $a[$m]) return rBinarySearch(
                array_slice($a, 0, $m - 1),
                // * so $m's previous index - 0 (1st item's index) is the accurate length for the slice-through
                $x
            );
            else return rBinarySearch(
                array_slice($a,
                    $m + 1,
                    ($l - 1) - ($m + 1) // * slice length (not endIndex)
                ), // * so last item's index - $m's next index is the accurate length for the slice-through
                $x
            ); // todo: length : - 1 exclusiveness
        }

        function rBinarySearch2p($a, $x, $f, $l) {
            if (empty($a)) return null;
            $m = floor($f + ($l - $f) / 2);
            if ($x == $a[$m]) return $m;
            elseif ($x < $a[$m]) return rBinarySearch2p($a, $x, $f, $m - 1);
            else return rBinarySearch2p($a, $x, $m + 1, $l);
        }

        $f = 0; $l = count($a) - 1;
        rBinarySearch($a, 7); rBinarySearch2p($a, 7, $f, $l);

        while ($f < $l) {
            $m = floor($f + ($l - $f) / 2);
            if ($x == $a[$m]) return $m;
            elseif ($x < $a[$m]) $l =  $m - 1;
            else $f = $m + 1;
        }

        return null;
    }

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