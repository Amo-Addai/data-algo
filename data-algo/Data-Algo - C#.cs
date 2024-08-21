using System;
using System.Collections.Generics;
using System.Linq;


/* // TODO: To-Use

Keywords - sealed, partial, virtual, 
In-built DataStructure classes
'event' Handlers
delegate methods - with Func<..> & lambda functions
Generics
LanguageExt, Optional
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
            private Int i;

            public void Searching() {
                this.i = -1;
            }
                
            public Int LinearSearch(Int[] a, Int x) 
            {
                var FLinearSearch = () => a.Where(i => i == x).Select(i); // Functional Linq Usage

                return from i in a where i == x select i; // * best to return i as index, instead of item
            }

            public Int BinarySearch(Int[] a, Int x) 
            {
                if (a.Length == 0) return null;

                Array.Sort(a);
                // a.BinarySearch(x); // * C# in-built Array Method

                var RBinarySearch = (Int[] a, Int x) => {
                    if (a.Length == 0) return null;
                    var m = Math.Floor(a.Length / 2);
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

                Int f = 0, l = a.Length - 1;
                RBinarySearch(a, 7); RBinarySearch2p(a, 7, f, l);

                Int m;

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


/*

* // TODO: C#

String.Meths == string.Meths (& other data types)

*/




/*

* // TODO: Visual Studio



* // TODO: V-Studio - Config



* // TODO: V-Studio - Issues



* // TODO: V-Studio - Notes



* // TODO: MAUI - Config



* // TODO: MAUI - Issues



* // TODO: MAUI - Main


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





* enum / switch cases for generics-validations




*/