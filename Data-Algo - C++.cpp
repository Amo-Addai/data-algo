#include <iostream>

using namespace std;

/*

LEARN

MemMan, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class SearchingAlgorithms {

    private:

        int i;

    public: 
    
        SearchingAlgorithms::SearchingAlgorithms () {}
        SearchingAlgorithms::~SearchingAlgorithms () {}

        int linearSearch(int a[], int x) {
            for (int i = 0; i < sizeof(a); i++) {
                if (x == a[i]) return i;
            }
        }

        int binarySearch(int a[], int x) {
            // a = rsort(a);
            if (sizeof(a) == 0) return;

            int rBinarySearch(int a[], int x) {
                if (sizeof(a) == 0) return;
                int m = sizeof(a) / 2;
                if (x < a[m]) return rBinarySearch(a, x); // slice a
                else if (x > a[m]) return rBinarySearch(a, x); // slice a
                else return m;
            }

            int rBinarySearch2p(int a[], int x, int f, int l) {
                if (sizeof(a) == 0) return;
                int m = sizeof(a) / 2;
                if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
                else if (x > a[m]) return rBinarySearch(a, x, m + 1, l);
                else return m;
            }

            int f = 0;
            int l = sizeof(a) - 1;
            int m;
            rBinarySearch(a, 7); rBinarySearch(a, 7, f, l);

            while (f < l) {
                m = (f + l) / 2;
                if (x < a[m]) l = m - 1;
                else if (x > a[m]) l = m + 1;
                else return m;
            }
        }

};


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class SortingAlgorithms {

    public: 
    
        SortingAlgorithms::SortingAlgorithms () {}
        SortingAlgorithms::~SortingAlgorithms () {}

};



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// 




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void main(int argc, char argv[]) {
    cout << "Hello, World!" << endl;
}