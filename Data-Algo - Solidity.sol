/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

function linearSearch(int[] a, int x) {
    for (int i = 0; i < a.length; i++) {
        if (x == a[i]) return i;
    }
}

function binarySearch(int[] a, int x) {
    // a.sort()
    if (a.length == 0) return null; // fix

    function rBinarySearch(int[] a, int x) {
        if (a.length == 0) return null;
        var m = a.length / 2;
        if (x < a[m]) return rBinarySearch(a, x); // slice a
        if (x > a[m]) return rBinarySearch(a, x); // slice a
        else return m;
    }

    function rBinarySearch(int[] a, int x) {
        if (a.length == 0) return null;
        var m = (f + l) / 2;
        if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
        if (x > a[m]) return rBinarySearch(a, x, m + 1, l);
        else return m;
    }

    var f = 0, l = a.length - 1, m;
    rBinarySearch(a, 7); rBinarySearch(a, 7, f, l);

    while (f < l) {
        m = (f + l) / 2;
        if (x < a[m]) l = m - 1;
        if (x > a[m]) f = m + 1;
        else return m;
    }
    return null; // fix
}

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

//


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//
