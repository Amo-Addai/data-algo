pragma solidity >=0.8.19 <0.9.0;

/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

contract Sorting {

    constructor() {}

}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

contract Searching {

    // uint, address, mapping, struct
    constructor() {}

    function linearSearch(uint[] memory a, uint x) public pure returns (int) {
        for (uint i = 0; i < a.length; i++) {
            if (x == a[i]) return i;
        }
        return -1;
    }

    function rBinarySearch(uint[] memory a, uint x) private returns (int) {
        if (a.length == 0) return -1;
        uint m = floor(a.length / 2); // todo: Math..floor
        if (x == a[m]) return a[m];
        else if (x < a[m]) return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
        else return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
    }

    function rBinarySearch(uint[] memory a, uint x, uint f, uint l) private returns (int) {
        if (a.length == 0) return -1;
        uint m = floor(f + (l - f) / 2);
        if (x == a[m]) return m;
        else if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
        else return rBinarySearch(a, x, m + 1, l);
    }

    function binarySearch(uint[] memory a, uint x) public returns (int) {
        if (a.length == 0) return -1;

        // todo: a.sort() 

        uint f = 0; uint l = a.length - 1; uint m;
        rBinarySearch(a, 7); rBinarySearch(a, 7, f, l);

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) l = m - 1;
            else f = m + 1;
        }
        
        return -1;
    }

}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//





////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function main(string[] calldata args) pure returns (uint) {
    // todo: print('Hello, World!')
    return 0; // unsigned int (NO -1)
}