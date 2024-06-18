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
        for (var i in 0..a.length-1) if (x == a[i]) return i // index
    }

    fun binarySearch(a: Array<Int>, x: Int): Int? {
        // a.sort()
        if (a.length == 0) return null // length

        val rBinarySearch: (Array<Int>, Int) -> Int? = { (a: Array<Int>, x: Int) -> {
                if (a.length == 0) return null
                val m = a.length / 2
                if (x < a[m]) return rBinarySearch(a, x)
                else if (x > a[m]) return rBinarySearch(a, x)
                else return m
            }
        }

        val rBinarySearch2p: (Array<Int>, Int) -> Int? = { (a: Array<Int>, x: Int, f: Int, l: Int) -> {
                if (a.length == 0) return null
                val m = (f + l) / 2
                if (x < a[m]) return rBinarySearch2p(a, x, f, m - 1)
                else if (x > a[m]) return rBinarySearch2p(a, x, m + 1, l)
                else return m
            }
        }

        val f: Int = 0, l: Int = a.length - 1, m: Int
        rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l)

        while (f < l) {
            m = (f + l) / 2
            if (x < a[m]) l = m - 1
            else if (x > a[m]) f = m + 1
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