#import <Foundation/Foundation.h>

/* // TODO: To-Use

Generics
MemMan, ..
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

@interface Sorting : NSObject

@end

@implementation Sorting

@end


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

@interface Searching : NSObject
    -(int) length: (int[]) a;
    -(int[]) slice: (int[]) a;

    -(int) linearSearch: (int[]) a, arg2: (int) x;
    -(int) binarySearch: (int[]) a, arg2: (int) x;
@end

@implementation Searching

    -(int) linearSearch: (int[]) a, arg2: (int) x {
        for (int i = 0; i < sizeof(a); i++) {
            if (x == a[i]) return i;
        }
    }

    // TODO: sort, length, floor, slice (exclusive), x == return a[m] & null

    -(int) binarySearch: (int[]) a, arg2: (int) x {
        if (sizeof(a) == 0) return;

        // * a = rsort(a);

        int (^ rBinarySearch)(int, int) = ^(int a[], int x) {
            if (sizeof(a) == 0) return;
            int m = floor(sizeof(a) / 2); // TODO: math.floor
            if (x == a[m]) return a[m];
            else if (x < a[m]) return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
            else return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
        }

        int (^ rBinarySearch)(int, int, int, int) = ^(int a[], int x, int f, int l) {
            if (sizeof(a) == 0) return;
            int m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
            else return rBinarySearch(a, x, m + 1, l);
        }

        int f = 0, l = sizeof(a) - 1, m;
        rBinarySearch(a, x); rBinarySearch(a, x, f, l);

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) l = m - 1;
            else f = m + 1;
        }
    }
    
@end



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// 




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void main(int argc, const char* argv[]) {
    printf(""); NSLog(@"Hello, World!")
}