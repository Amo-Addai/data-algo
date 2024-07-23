using System;
using System.Collections.Generics;
using System.Linq;


/* // TODO: To-Use

Generics
In-built DataStructure classes
..

*/



namespace DataAlgo
{
    public class CSharp
    {

        ////////////////////////////////////////
        //  SORTING ALGO'S
        ////////////////////////////////////////

        class Sorting 
        {
            
            public void Sorting() {}

        }


        ////////////////////////////////////////
        //  SEARCHING ALGO'S
        ////////////////////////////////////////

        class Searching 
        {
            public void Searching() {}
                
            public Int LinearSearch(Int[] a, Int x) 
            {
                var FLinearSearch = () => a.Where(i => i == x).Select(i); // Functional Linq Usage

                return from i in a where i == x select i; // todo: return i as index, instead of item
            }

            public Int BinarySearch(Int[] a, Int x) 
            {
                if (a.Length == 0) return null;

                a = Array.Sort(a); // todo: sort
                // a.BinarySearch(x); // * C# in-built Array Method

                var RBinarySearch = (Int[] a, Int x) => {
                    if (a.Length == 0) return null;
                    var m = Math.Floor(a.Length / 2); // todo: Math.floor
                    if (x == a[m]) return a[m];
                    else if (x < a[m]) return RBinarySearch(a[..m], x);
                    else return RBinarySearch(a[m+1..], x);
                };

                var RBinarySearch2p = (Int[] a, Int x, Int f, Int l) => {
                    if (a.Length == 0) return null;
                    var m = Math.Floor(f + (l - f) / 2);
                    if (x == a[m]) return m;
                    else if (x < a[m]) return RBinarySearch2p(a, x, f, m - 1);
                    else return RBinarySearch2p(a, x, f, m + 1);
                };

                Int f = 0, l = a.Length - 1, m;
                RBinarySearch(a, 7); RBinarySearch2p(a, 7, f, l);

                while (f < l) {
                    m = Math.Floor(f + (l - f) / 2);
                    if (x == a[m]) return m;
                    else if (x < a[m]) l = m - 1;
                    else f = m + 1;
                }

                return null;
            }

        }



        ////////////////////////////////////////
        //  OTHER ALGO'S
        ////////////////////////////////////////


        class DataStructures
        {

            public DataStructures() {}


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


        }



        ////////////////////////////////////////
        //  Cracking Coding Interview Qs
        ////////////////////////////////////////


        // Arrays & Strings

        // ...






        ////////////////////////////////////////
        //  TEST CASES
        ////////////////////////////////////////

        public static void Main(string[] args) 
        {
            Console.WriteLine("Hello, World!");
        }
        
    }
}