/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

def linearSearch(a: Array[Any], x: Any): Int = {
    for (var i <- a if x == i) return i // item
    // tip - a.length times | for (var i <- i to a) |  for (var i <- 0 until a)
}

def binarySearch(a: Array[Any], x: Any): Int = {
    // a.sort()
    if (a.length == 0) return Nil

    var rBinarySearch = (a: Array[Any], x: Any): Int => {
        if (a.length == 0) return Nil
        val m: Int = a.length / 2
        if (x < a(m)) return rBinarySearch(a.range(0, m - 1), x)
        else if (x > a(m)) return rBinarySearch(a.range(m + 1, a.length - 1), x)
        else return m
    }

    var rBinarySearch = (a: Array[Any], x: Any, f: Int, l: Int): Int => {
        if (a.length == 0) return Nil
        val m: Int = (f + l) / 2
        if (x < a(m)) return rBinarySearch(a, x, f, m - 1)
        else if (x > a(m)) return rBinarySearch(a, x,  m + 1, l)
        else return m
    }

    val f: Int = 0, l: Int = a.length - 1, m: Int
    rBinarySearch(a, 7); rBinarySearch(a, 7, f, l)

    while (f < l) {
        m = (f + l) / 2
        if (x < a(m)) l = m - 1
        else if (x > a(m)) f = m + 1
        else return m
    }
    return null
}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

//


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//
