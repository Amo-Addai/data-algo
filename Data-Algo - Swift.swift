/* // TODO: To-Use

Generics
some, convenience, ..
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    init() {}
    
}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    init() {}

    func linearSearch(a: [Int], x: Int) -> Int? {
        for i in 0..<a.count where x == a[i] {
            return i
        }
        return nil
    }

    func binarySearch(a: [Int], x: Int) -> Int? {
        // * a.sort()
        guard a.count > 0 else {
            return nil
        }

        let rBinarySearch: ([Int], Int) -> Int? = { (a: [Int], x: Int) -> Int? in
            guard a.count > 0 else {
                return nil
            }
            var m = a.count / 2
            if x < a[m] {
                return rBinarySearch(a: a[0..<m], x: x)
            } else if x > a[m] {
                return rBinarySearch(a: a[(m+1)...], x: x)
            } else {
                return m
            }
        }
        
        let rBinarySearch2p: ([Int], Int, Int, Int) -> Int? = { (a: [Int], x: Int, f: Int, l: Int) -> Int? in
            guard a.count > 0 else {
                return nil
            }
            var m = (f + l) / 2
            if x < a[m] {
                return rBinarySearch2p(a: a, x: x, f: f, l: m - 1)
            } else if x > a[m] {
                return rBinarySearch2p(a: a, x: x, f: m + 1, l: l)
            } else {
                return m
            }
        }

        var f: Int = 0, l: Int = a.count - 1, m: Int
        // rBinarySearch(a: a, x: 7); rBinarySearch2p(a: a, x: 7, f: f, l: l)
        var res: Int? = rBinarySearch(a, 7); 
        var res2p: Int? = rBinarySearch2p(a, 7, f, l)

        while f < l {
            m = (f + l) / 2
            if x < m {
                l = m - 1
            } else if x > m {
                f = m + 1
            } else {
                return m
            }
        }
        return nil
    }
}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////



// CODE SIGNAL

func rabinKarp(t: String, p: String) -> Int {
    // convert to array of ints
    var pArr = p.flatMap { Int(String($0)) }
    var tArr = t.flatMap { Int(String($0)) }

    if tArr.count < pArr.count {
        return -1
    }

    let pHash = hash(array: pArr)
    var endIndex = pArr.count - 1
    let firstChars = Array(tArr[0...endIndex])
    let firstHash = hash(array: firstChars)

    if pHash == firstHash {
        // verify this was not a hash collision
        if firstChars == pArr {
            return 0
        }
    }

    var prevHash = firstHash, window: [Int]?, windowHash: Any

    // Now slide the window across the text to be searched
    for i in 1...(tArr.count - pArr.count) {
        endIndex = i + (pArr.count - 1)
        window = Array(tArr[i...endIndex])
        windowHash = nextHash(prevHash: prevHash, dropped: tArr[i - 1], 
        added: tArr[endIndex], patternSize: pArr.count - 1)

        if window == pHash, let pArr = window {
            return i
        }

        prevHash = windowHash
    }

    return -1
}




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

func main(args: [String]) {
    print("Hello, World!")
}