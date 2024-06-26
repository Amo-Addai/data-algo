#include <stdio.h>

/* // TODO: To-Use

Generics
MemMan, ..
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

// private

int* check(int a[]);
int* swap(int a[]);
int* compare(int a[]);

// regular

int* insertion(int a[]);
int* selection(int a[]);
int* shell(int a[]);

// bad

int* bubble(int a[]);
int* slow(int a[]);

// special

int* counting(int a[]);
int* radix(int a[]);
int* topological(int a[]);

// hybrid

int* intro(int a[]);

// fast

int* heap(int a[]);
int* merge(int a[]);
int* quick(int a[]);



////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////


int linearSearch(int a[], int x);
int binarySearch(int a[], int x);
int rBinarySearch(int a[], int x);
int rBinarySearch2p(int a[], int x, int f, int l);

int linearSearch(int a[], int x) {
    for (int i = 0; i < sizeof(a); i++) {
        if (x == a[i]) return i;
    }
}

int rBinarySearch(int a[], int x) {
    if (sizeof(a) == 0) return;
    int m = sizeof(a) / 2;
    if (x < a[m]) return rBinarySearch(a, x); // todo: slice a
    else if (x > a[m]) return rBinarySearch(a, x); // todo: slice a
    else return m;
}

int rBinarySearch2p(int a[], int x, int f, int l) {
    if (sizeof(a) == 0) return;
    int m = (f + l) / 2;
    if (x < a[m]) return rBinarySearch2p(a, x, f, m - 1);
    else if (x > a[m]) return rBinarySearch2p(a, x, m + 1, l);
    else return m;
}

int binarySearch(int a[], int x) {
    // * a = rsort(a);
    if (sizeof(a) == 0) return;

    int f = 0, l = sizeof(a) - 1, m;
    rBinarySearch(a, x); rBinarySearch2p(a, x, f, l);

    while (f < l) {
        m = (f + l) / 2;
        if (x < a[m]) l = m - 1;
        else if (x > a[m]) f = m + 1;
        else return m;
    }
}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////


// TODO: class DataStructures


// Arrays & Strings

// (Array) Lists & Tuples

// Sets & Sequences

// WeakMaps & WeakSets

// HashMaps & HashTables

// Matrices

// Linked Lists

// Stacks

// Queues

// Heaps (max & min)

// Binary Heaps

// Priority Queues

// Trees

// Binary (Search) Trees

// Tries
    
// Graphs

// Bits



////////////////////////////////////////
//  Cracking Coding Interview Qs
////////////////////////////////////////


// Arrays & Strings

// ...




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void main(int argc, char* argv[]) {
    printf("Hello, World!");
}