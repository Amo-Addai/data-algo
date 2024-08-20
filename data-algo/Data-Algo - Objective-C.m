#import <Foundation/Foundation.h>
#import <math.h>

/* // TODO: To-Use

Generics
ReactiveObjC
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
    -(void) slice: (int[]) a;
    -(int) sortCompare: (const void* a, const void* b);

    -(int) linearSearch: (int[]) a, arg2: (int) x;
    -(int) binarySearch: (int[]) a, arg2: (int) x;
    -(NSArray) binarySearch: (NSArray*) a, arg2: (NSInteger) x;
@end

@implementation Searching

    -(int) length: (int* a) {
        return sizeof(a) / sizeof(a[0]);
    }

    -(void) slice: (int* src, int start, int end, int** dest, int* length) {
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

    -(int) sortCompare(const void *a, const void* b) {
        return (
            *(int*) a - *(int*) b
        );
    }


    -(int) linearSearch: (int[]) a, arg2: (int) x {
        for (int i = 0; i < length(a); i++) {
            if (x == a[i]) return i;
        }
    }

    -(int) binarySearch: (int[]) a, arg2: (int) x {
        if (length(a) == 0) return;

        qsort(a, len, sizeof(int), sortCompare);

        int (^ rBinarySearch)(int, int) = ^(int a[], int x) {
            if (length(a) == 0) return;
            int m = floor(length(a) / 2);
            if (x == a[m]) return a[m];
            else if (x < a[m]) return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
            else return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
        }

        int (^ rBinarySearch)(int, int, int, int) = ^(int a[], int x, int f, int l) {
            if (length(a) == 0) return;
            int m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
            else return rBinarySearch(a, x, m + 1, l);
        }

        int f = 0, l = length(a) - 1;
        rBinarySearch(a, x); rBinarySearch(a, x, f, l);

        int m;

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) l = m - 1;
            else f = m + 1;
        }

        return -1;
    }

    // TODO: Re-work & Test
    -(NSArray*) binarySearch: (NSArray*) a, arg2: (NSInteger) x {
        if ([a length] == 0) return nil;

        a = [a sortedArrayUsingSelector: @selector(compare:)];
        // todo: a = [a sortedArrayUsingSelector: @comparator(compare:)];

        NSInteger (^ rBinarySearch)(NSInteger, NSInteger) = ^(NSArray* a, NSInteger x) {
            if ([a length] == 0) return nil;
            NSInteger m = floor([a length] / 2);
            if (x == a[m]) return a[m];
            else if (x < a[m]) return rBinarySearch(
                [a subarrayWithRange: NSMakeRange(0, m)],
                x
            ) else return rBinarySearch(
                [a subarrayWithRange: NSMakeRange(m + 1, [a length])],
                x
            )
        }

        NSInteger (^ rBinarySearch)(NSInteger, NSInteger) = ^(NSArray* a, NSInteger x, NSInteger f, NSInteger l) {
            if ([a length] == 0) return nil;
            NSInteger m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
            else return rBinarySearch(a, x, m + 1, l);
        }

        NSInteger f = 0, l = [a length] - 1;
        rBinarySearch(a, x); rBinarySearch(a, x, f, l);

        NSInteger m;

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) l = m - 1;
            else f = m + 1;
        }
        
        return  nil;
    }
    
@end



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// 




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        printf(""); NSLog(@"Hello, World!")
    }
    return 0;
}


/*

* // TODO: Obj-c




*/





/*

* // TODO: X-Code



* // TODO: X-Code - Issues



* // TODO: X-Code - Notes



* // TODO: Android - Objective-c - Issues



* // TODO: A-Obj-c - Main


* Libraries - 

* Classes - 

* Special Data-Types - 

* Functions - 

* Containers - 

* Components - 

* Shapes - 

* Props / Modifiers - 

* Animations - 

* Gestures - 

* Event Handlers - 

* Enumerations (raw) - 






* Specific Component-Prop-Enum Combos - 






* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes





* enum / switch cases with let-var validations




*/