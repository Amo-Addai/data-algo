pragma solidity >=0.8.19 <0.9.0;

/* // TODO: To-Use

State mutability - pure, view, ..
Generics
OpenZeppelin
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

contract Sorting {

    constructor() {}

    function bubbleSort(int[] memory a) public pure {
        uint n = a.length;
        for (uint i = 0; i < n; i++) {
            for (uint j = 0; j < n - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    (a[j], a[j + 1]) = (a[j + 1], a[j]);
                }
            }
        }
    }

}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

contract Searching {

    int private i;

    // uint, address, mapping, struct
    constructor() {
        i = -1; // * this. not required for props; only methods, structs, & 'this' contract
    }

    // TODO: implement QuickSort, Array-Slicing, Math's floor & ceil (not natively supported on Solidity)

    function sort(uint[] memory a) public pure { // * should allow generically signed int[] arrays
        uint n = a.length;
        for (uint i = 0; i < n; i++) {
            for (uint j = 0; j < n - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    (a[j], a[j + 1]) = (a[j + 1], a[j]);
                }
            }
        }
    }

    function floor(uint x) private pure returns (uint) {
        if (x >= 0) return x / 1;
        else return (x / 1) - 1;
    }

    function ceil(uint x) private pure returns (uint) {
        if (x >= 0) return (x / 1) + 1;
        else return x / 1;
    }

    function sliceArray(uint[] memory a, uint start, uint end) private pure returns (uint[] memory) {
        require(start < end && end <= a.length, "Invalid slice range");
        uint[] memory result = new uint[](end - start);
        for (uint i = start; i < end; i++) {
            result[i - start] = a[i];
        }
        return result;
    }

    function linearSearch(uint[] memory a, uint x) public pure returns (uint) {
        for (uint i = 0; i < a.length; i++) {
            if (x == a[i]) return i;
        }
        return 0; // -1 for signed ints
    }

    function rBinarySearch(uint[] memory a, uint x) private returns (uint) {
        if (a.length == 0) return 0;
        uint m = floor(a.length / 2); // todo: test floor()
        if (x == a[m]) return a[m];
        else if (x < a[m]) return rBinarySearch(a, x); // todo: slice a (test sliceArray() end index inclusiveness)
        else return rBinarySearch(a, x);
    }

    function rBinarySearch(uint[] memory a, uint x, uint f, uint l) private returns (uint) {
        if (a.length == 0) return 0;
        uint m = floor(f + (l - f) / 2);
        if (x == a[m]) return m;
        else if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
        else return rBinarySearch(a, x, m + 1, l);
    }

    function binarySearch(uint[] memory a, uint x) public returns (uint) {
        if (a.length == 0) return 0;

        sort(a); // todo: test

        uint f = 0; uint l = a.length - 1; uint m;
        rBinarySearch(a, 7); rBinarySearch(a, 7, f, l);

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) l = m - 1;
            else f = m + 1;
        }
        
        return 0;
    }

}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// TODO: library DataStructures

library DataStructures {

}




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function main(string[] calldata args) pure returns (uint) {
    // todo: print("Hello, World!")
    return 0; // unsigned int (NO -1)
}



/*

* // TODO: Solidity



*/




/*

* // TODO: WebStorm



* // TODO: WebStorm - Config



* // TODO: WebStorm - Issues



* // TODO: ETH-Web3.js - Notes



* // TODO: ETH - Config



* // TODO: ETH - Issues



* // TODO: ETH - Main



* Libraries - 

* Classes - 

* 'Language' Classes - 

* 3rd-Party Classes - 

* Special Data-Types - 

* Directives / Annotations - 

* Functions - 

* Methods - 

* Enumerations - 






* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes





* enum / switch cases for generics-validations






*/