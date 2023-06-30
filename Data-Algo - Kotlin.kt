/*

LEARN

Lambda, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

fun linearSearch(a: Array<T>, x: T): Int? {
    for (var i in 0..a.length-1) if (x == a[i]) return i // index
}

fun binarySearch(a: Array<T>, x: T): Int? {
    // a.sort()
    if (a.length == 0) return null // length

    val rBinarySearch: (Array<T>, T) -> Int? = { (a: Array<T>, x: T) -> { // lambda
            if (a.length == 0) return null
            val m = a.length / 2
            if (x < a[m]) return rBinarySearch(a, x)
            else if (x > a[m]) return rBinarySearch(a, x)
            else return m
        }
    }

    val rBinarySearch: (Array<T>, T) -> Int? = { (a: Array<T>, x: T, f: Int, l: Int) -> {
            if (a.length == 0) return null
            val m = (f + l) / 2
            if (x < a[m]) return rBinarySearch(a, x, f, m - 1)
            else if (x > a[m]) return rBinarySearch(a, x, m + 1, l)
            else return m
        }
    }

    val f: Int = 0, l: Int = a.length -1, m: Int
    rBinarySearch(a, 7); rBinarySearch(a, 7, f, l)

    while (f < l) {
        m = (f + l) / 2
        if (x < a[m]) l = m - 1
        else if (x > a[m]) f = m + 1
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
