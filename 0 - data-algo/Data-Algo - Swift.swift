import Foundation

/* // TODO: (or MARK:) To-Use

_const, 
some (View), convenience, open, 
@unknown, @escaping, @inlinable, 
@available @frozen, 
#available - API Availability
'Directives' - @testable
Generics
Swiftz, FunctionalSwift
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    private var i: Int

    init() {}
    
}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    private let i: Int

    init() {
        self.i = -1
    }

    func linearSearch(a: [Int], x: Int) -> Int? {
        for i in 0..<a.count where x == a[i] {
            return i
        }
        return nil
    }

    func binarySearch(a: [Int], x: Int) -> Int? {
        guard a.count > 0 else {
            return nil
        }

        a.sort() //  in-place | or .sorted() - not in-place

        let rBinarySearch = { (a: [Int], x: Int) -> Int? in
            guard a.count > 0 else {
                return nil
            }
            let m = floor(a.count / 2) // m never mutated, so let constant
            if x == a[m] {
                return a[m]
            } else if x < a[m] {
                return rBinarySearch(Array(a[0..<m]), x) // ..< - end exclusive
            } else {
                return rBinarySearch(Array(a[(m+1)...]), x)
            } 
        }
        
        let rBinarySearch2p = { (a: [Int], x: Int, f: Int, l: Int) -> Int? in
            guard a.count > 0 else {
                return nil
            }
            let m = floor(f + (l - f) / 2)
            if (x == a[m]) {
                return m
            } else if x < a[m] {
                return rBinarySearch2p(a, x, f, m - 1)
            } else {
                return rBinarySearch2p(a, x, m + 1, l)
            }
        }

        var f: Int = 0, l: Int = a.count - 1

        let res: Int? = rBinarySearch(a, 7)
        let res2p: Int? = rBinarySearch2p(a, 7, f, l)
        print("\(res ?? -1) | \(res2p ?? -1)")

        var m: Int

        while f < l {
            m = floor(f + (l - f) / 2)
            if (x == a[m]) {
                return m
            } else if x < m {
                l = m - 1
            } else {
                f = m + 1
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
    
    let hash = { (arr: [Int]) -> Int in
        var hasher = Hasher()
        for s in arr {
            hasher.combine(s)
        }
        return hasher.finalize()
    }
    
    // convert to array of ints
    var pArr = p.compactMap { Int(String($0)) } // flatMap deprecated
    var tArr = t.compactMap { Int(String($0)) }

    if tArr.count < pArr.count {
        return -1
    }
    
    let pHash = hash(pArr)
    var endIndex = pArr.count - 1
    let firstChars = Array(tArr[0...endIndex])
    let firstHash = hash(firstChars)

    if pHash == firstHash {
        // verify this was not a hash collision
        if firstChars == pArr {
            return 0
        }
    }

    var prevHash = firstHash, window: [Int]?, windowHash: Int

    // Now slide the window across the text to be searched
    for i in 1...(tArr.count - pArr.count) {
        endIndex = i + (pArr.count - 1)
        window = Array(tArr[i...endIndex])
        windowHash = nextHash( // todo: 
            prevHash: prevHash,
            dropped: tArr[i - 1],
            added: tArr[endIndex],
            patternSize: pArr.count - 1
        )

        if window == [pHash], let newPArr = window {
            return i
        }

        prevHash = windowHash
    }

    return -1
}




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

func main(args: [String]? = nil) {
    print("Hello, World!")
}
main()
