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

class Searching
{

private:
    int i;

public:
    Searching::Searching() {}
    Searching::~Searching() {}

    int linearSearch(int a[], int x)
    {
        for (int i = 0; i < sizeof(a); i++)
        {
            if (x == a[i])
                return i;
        }
    }

    int binarySearch(int a[], int x)
    {
        // a = rsort(a);
        if (sizeof(a) == 0)
            return;

        int f = 0, l = sizeof(a) - 1, m;
        rBinarySearch(a, 7);
        rBinarySearch(a, 7, f, l);

        while (f < l)
        {
            m = (f + l) / 2;
            if (x < a[m])
                l = m - 1;
            else if (x > a[m])
                l = m + 1;
            else
                return m;
        }
    }

    int rBinarySearch(int a[], int x)
    {
        if (sizeof(a) == 0)
            return;
        int m = sizeof(a) / 2;
        if (x < a[m])
            return rBinarySearch(a, x); // slice a
        else if (x > a[m])
            return rBinarySearch(a, x); // slice a
        else
            return m;
    }

    int rBinarySearch(int a[], int x, int f, int l)
    {
        if (sizeof(a) == 0)
            return;
        int m = sizeof(a) / 2;
        if (x < a[m])
            return rBinarySearch(a, x, f, m - 1);
        else if (x > a[m])
            return rBinarySearch(a, x, m + 1, l);
        else
            return m;
    }
};
// returnType Searching::method(args) {} // defined outside of class scope

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting
{

public:
    Sorting::Sorting() {}
    Sorting::~Sorting() {}
};

////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//

////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void main(int argc, char argv[])
{
    cout << "Hello, World!" << endl;
}