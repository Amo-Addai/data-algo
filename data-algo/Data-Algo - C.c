#include <stdio.h>
#include <math.h>

/* // TODO: To-Use

Generics
MemMan, ..
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

// helpers

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

// helpers

int length(int* a);
void slice(int* src, int start, int end, int** dest, int* length);
int compare(const void* a, const void* b);

// functions

int linearSearch(int a[], int x);
int binarySearch(int a[], int x);
int rBinarySearch(int a[], int x);
int rBinarySearch2p(int a[], int x, int f, int l);


int length(int* a) {
    return sizeof(a) / sizeof(a[0]);
}

void slice(int* src, int start, int end, int** dest, int* length) {
    if (start < 0 || end > *length || start >= end) {
        *dest = NULL;
        *length = 0;
        return;
    }

    *length = end - start;
    *dest = (int*)malloc(*length * sizeof(int));

    for (int i = 0; i < *length; ++i) {
        (*dest)[i] = src[start + i];
    }
}

int sortCompare(const void *a, const void* b) {
    return (
        *(int*) a - *(int*) b
    );
}


int linearSearch(int a[], int x) {
    for (int i = 0; i < length(a); i++) {
        if (x == a[i]) return i;
    }
}

int rBinarySearch(int a[], int x) {
    int l = length(a);
    if (l == 0) return;
    int m = floor(l / 2);
    if (x == a[m]) return a[m];
    else if (x < a[m]) return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
    else return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
}

int rBinarySearch2p(int a[], int x, int f, int l) {
    if (length(a) == 0) return;
    int m = floor(f + (l - f) / 2);
    if (x == a[m]) return m;
    else if (x < a[m]) return rBinarySearch2p(a, x, f, m - 1);
    else return rBinarySearch2p(a, x, m + 1, l);
}

int binarySearch(int a[], int x) {
    int len = length(a);
    if (len == 0) return;

    qsort(a, len, sizeof(int), sortCompare);

    int f = 0, l = len - 1, m;
    rBinarySearch(a, x); rBinarySearch2p(a, x, f, l);

    while (f < l) {
        m = floor(f + (l - f) / 2);
        if (x == a[m]) return m;
        else if (x < a[m]) l = m - 1;
        else f = m + 1;
    }

    return -1;
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