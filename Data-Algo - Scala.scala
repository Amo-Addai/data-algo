import java.io._

/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting(val prop: Any) {

}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching(val prop: Any) {

    def linearSearch(a: Array[Int], x: Int): Int = {
        for (var i <- a if x == i) return i // item
        // tip - a.length times | for (var i <- i to a) |  for (var i <- 0 until a)
    }

    def binarySearch(a: Array[Int], x: Int): Int = {
        // * a.sort()
        if (a.length == 0) return Nil

        var rBinarySearch = (a: Array[Int], x: Int): Int => {
            if (a.length == 0) return Nil
            val m: Int = a.length / 2
            if (x < a(m)) return rBinarySearch(a.range(0, m - 1), x)
            else if (x > a(m)) return rBinarySearch(a.range(m + 1, a.length - 1), x)
            else return m
        }

        var rBinarySearch2p = (a: Array[Int], x: Int, f: Int, l: Int): Int => {
            if (a.length == 0) return Nil
            val m: Int = (f + l) / 2
            if (x < a(m)) return rBinarySearch2p(a, x, f, m - 1)
            else if (x > a(m)) return rBinarySearch2p(a, x,  m + 1, l)
            else return m
        }

        val f: Int = 0, l: Int = a.length - 1, m: Int
        rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l)

        while (f < l) {
            m = (f + l) / 2
            if (x < a(m)) l = m - 1
            else if (x > a(m)) f = m + 1
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

def main(args: Array[String]) {
    println("Hello, World!")
}