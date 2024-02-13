pragma solidity >=0.8.19 <0.9.0;

/*

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

contract Searching {

    // uint, address, mapping, struct
    constructor() {}

    function linearSearch(uint[] memory a, uint x) public pure returns (uint) {
        for (uint i = 0; i < a.length; i++) {
            if (x == a[i]) return i;
        }
        return 0;
    }

    function binarySearch(uint[] memory a, uint x) public returns (uint) {
        // a.sort()
        if (a.length == 0) return 0;

        uint f = 0; uint l = a.length - 1; uint m;
        rBinarySearch(a, 7); rBinarySearch(a, 7, f, l);

        while (f < l) {
            m = (f + l) / 2;
            if (x < a[m]) l = m - 1;
            if (x > a[m]) f = m + 1;
            else return m;
        }
        return 0;
    }

    function rBinarySearch(uint[] memory a, uint x) private returns (uint) {
        if (a.length == 0) return 0;
        uint m = a.length / 2;
        if (x < a[m]) return rBinarySearch(a, x); // slice a
        if (x > a[m]) return rBinarySearch(a, x); // slice a
        else return m;
    }

    function rBinarySearch(uint[] memory a, uint x, uint f, uint l) private returns (uint) {
        if (a.length == 0) return 0;
        uint m = (f + l) / 2;
        if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
        if (x > a[m]) return rBinarySearch(a, x, m + 1, l);
        else return m;
    }

}

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

contract Sorting {

    constructor() {}

}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//





////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function main(string[] calldata args) pure returns (uint) {
    // console.log('')
    return 0;
}