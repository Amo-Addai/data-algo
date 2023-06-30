#include <stdio.h>

/*

LEARN

MemMan, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

int linearSearch(int[] a, int x) {
    for (int i = 0; i < sizeof(a); i++) {
        if (x == a[i]) return i;
    }
}

int binarySearch(int[] a, int x) {
    // a = rsort(a);
    if (sizeof(a) == 0) return;

    int (^ rBinarySearch)(int, int) = ^(int[] a, int x) {
        if (sizeof(a) == 0) return;
        int m = sizeof(a) / 2;
        if (x < a[m]) return rBinarySearch(a, x); // slice a
        if (x > a[m]) return rBinarySearch(a, x); // slice a
        else return m;
    }

    int (^ rBinarySearch)(int, int, int, int) = ^(int[] a, int x, int f, int l) {
        if (sizeof(a) == 0) return;
        int m = (f + l) / 2;
        if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
        if (x > a[m]) return rBinarySearch(a, x, m + 1, l);
        else return m;
    }

    int f = 0, l = sizeof(a) - 1, m;
    rBinarySearch(a, x); rBinarySearch(a, x, f, l);

    while (f < l) {
        m = (f + l) / 2
        if (x < a[m]) l = m - 1
        else if (x > a[m]) f = m + 1
        else return m;
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
