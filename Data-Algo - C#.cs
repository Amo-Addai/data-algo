using System;
using System.Linq;

/*

..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching 
{
    public void Searching() {}
        
    public Int LinearSearch(Int[] a, Int x) 
    {
        return from i in a where i == x select i; // todo: return i as index, instead of item
        // return a.Where(i => i == x).Select(i); // Alternative Linq Usage
    }

    public Int BinarySearch(Int[] a, Int x) 
    {
        // a = Array.sort(a);
        // a.BinarySearch(x); // C# in-built Array Method
        if (a.Length == 0) return null;

        var RBinarySearch = (Int[] a, Int x) => {
            if (a.Length == 0) return null;
            var m = a.Length / 2;
            if (x < a[m]) return RBinarySearch(a, x); // slice a
            else if (x > a[m]) return RBinarySearch(a, x); // slice a
            else return m;
        };

        var RBinarySearch2p = (Int[] a, Int x, Int f, Int l) => {
            if (a.Length == 0) return null;
            var m = a.Length / 2;
            if (x < a[m]) return RBinarySearch2p(a, x, f, m - 1);
            else if (x > a[m]) return RBinarySearch2p(a, x, f, m + 1);
            else return m;
        };

        Int f = 0, l = a.Length - 1, m;
        RBinarySearch(a, 7); RBinarySearch2p(a, 7, f, l);

        while (f < l) {
            m = (f + l) / 2;
            if (x < a[m]) l = m - 1;
            else if (x > a[m]) f = m + 1;
            else return m;
        }
        return null;
    }

}

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting 
{
    public void Sorting() {}

}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// 




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void Main(String[] args) 
{
    Console.WriteLine("Hello, World!");
}