import java.io._
import scala.math._

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
        // * a.length times | for (var i <- i to a) | for (var i <- 0 until a)
    }

    def binarySearch(a: Array[Int], x: Int): Int = {
        if (a.length == 0) return -1

        a = a.sorted

        var rBinarySearch = (a: Array[Int], x: Int): Int => {
            if (a.length == 0) return -1
            val m: Int = floor(a.length / 2).asInstanceOf[Int]
            if (x == a(m)) return a[m]
            else if (x < a(m)) return rBinarySearch(a.slice(0, m), x) // * both slice & range have exclusive endIndex
            else return rBinarySearch(a.range(m + 1, a.length), x) // * NB: range data-type - 1 to (end-inclusive) / until (end-exclusive) 10 by (step) 2
        }

        var rBinarySearch2p = (a: Array[Int], x: Int, f: Int, l: Int): Int => {
            if (a.length == 0) return -1
            val m: Int = floor(f + (l - f) / 2).asInstanceOf[Int]
            if (x == a(m)) return m
            else if (x < a(m)) return rBinarySearch2p(a, x, f, m - 1)
            else return rBinarySearch2p(a, x,  m + 1, l)
        }

        val f: Int = 0, l: Int = a.length - 1, m: Int
        rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l)

        while (f < l) {
            m = floor(f + (l - f) / 2).asInstanceOf[Int]
            if (x == a(m)) return m
            else if (x < a(m)) l = m - 1
            else f = m + 1
        }

        return -1
    }

}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//






////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

object Main extends App {
    println("Hello, World!")
}
