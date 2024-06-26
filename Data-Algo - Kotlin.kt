/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    private var i: Int = 0
    
}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    private var i: Int = 0

    fun linearSearch(a: Array<Int>, x: Int): Int? {
        for (i in 0..a.size-1) if (x == a[i]) return i // index
        return -1
    }

    fun binarySearch(arr: Array<Int>, num: Int): Int? {
        // * a.sort()
        if (arr.size == 0) return null

        /*
         * With Recursive lambdas (like Java's recursive lambdas for Functional Interfaces), define function var (not val) before assigning the lambda value
         * defined function var must initialized before being invoked recursively too, so should be assigned a null value
         * this means that it's overall function data type definition should also be Optional
         * to invoke (or re-invoke - recursively) call the ?.invoke() method
         */

        /* // todo: Similar to Java's new Functional Interfaces
         * Sample:
         Function<ArrayList<Integer>, Integer, Integer>[] meth = new Function[1]; // * should be defined as a array when required for recursive-calls, because the 1st item is held in memory during the lambda's implementation as it's being assigned to the same 1st item
         meth[0] = (x, y) -> { ... meth[0].apply(..); ... }; meth[0].apply(..);
         * NB: ?.invoke(..) works similar to Java's .apply(..) .accept(..) , etc invoke-methods for its Functional Interfaces
        */

        var rBinarySearch: ((Array<Int>, Int) -> Int?)? = null // * use var in this case (val cannot be reassigned)
        rBinarySearch = { a, x ->
            if (a.size == 0) null // return keyword is optional in lambda expressions and single-expression functions
            val m = a.size / 2
            // * Optional / "Safe" call reference is required in the recursive calls, because rBinarySearch may be null
            if (x < a[m]) rBinarySearch?.invoke(a, x) // todo: slice a
            else if (x > a[m]) rBinarySearch?.invoke(a, x) // todo: slice a
            else m // * return keyword can be omitted in lambda implementations
        }

        // * Lambda with the run keyword - scope
        val rBinarySearch2p: (Array<Int>, Int, Int, Int) -> Int? = run {
            fun rbs2p(a: Array<Int>, x: Int, f: Int, l: Int): Int? {
                if (a.size == 0) return null
                val m = (f + l) / 2
                if (x < a[m]) return rbs2p(a, x, f, m - 1)
                else if (x > a[m]) return rbs2p(a, x, m + 1, l)
                else return m
            }
            ::rbs2p
        }//() // todo: test instant-exec
    

        // var f = 0, l = arr.size - 1, m = -1
        var f: Int = 0
        var l: Int = arr.size - 1
        var m: Int

        // * Optional / "Safe" call reference is not totally necessary in these outer calls, 
        // because rBinarySearch (even though Optional, so may be null) has been assigned a lambda function value
        rBinarySearch.invoke(arr, 7)
        rBinarySearch2p(arr, 7, f, l) // * this version of lambda function doesn't require .invoke()

        while (f < l) {
            m = (f + l) / 2
            if (num < arr[m]) l = m - 1
            else if (num > arr[m]) f = m + 1
            else return m
        }
        return null
    }

}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//





////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

fun main(args: Array<String>) {
    println("Hello, World!")
}