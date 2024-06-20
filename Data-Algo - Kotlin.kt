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

        val rBinarySearch: (Array<Int>, Int) -> Int? = { a, x ->
            if (a.size == 0) null // return keyword is optional in lambda expressions and single-expression functions
            val m = a.size / 2
            if (x < a[m]) rBinarySearch(a, x) // todo: slice a
            else if (x > a[m]) rBinarySearch(a, x) // todo: slice a
            else m
        }

        val rBinarySearch2p: (Array<Int>, Int, Int, Int) -> Int? = { a, x, f, l -> 
            if (a.size == 0) null
            val m = (f + l) / 2
            if (x < a[m]) rBinarySearch2p(a, x, f, m - 1)
            else if (x > a[m]) rBinarySearch2p(a, x, m + 1, l)
            else m
        }

        // var f = 0, l = arr.size - 1, m = -1
        var f: Int = 0
        var l: Int = arr.size - 1
        var m: Int

        rBinarySearch(arr, 7); rBinarySearch2p(arr, 7, f, l)

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