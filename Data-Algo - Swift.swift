/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class SearchingAlgorithms {

    init() {}

    func linearSearch(a: [Any], x: Any) -> Int? {
        for i in 0..a.count where x == a[i] return i else return nil
    }

    func binarySearch(a: [Any], x: Any) -> Int? {
        // a.sort()
        guard a.count > 0 else return nil

        let rBinarySearch = { (a: [Any], x: Any) -> Int? in
            guard a.count > 0 else return nil
            var m = a.count / 2
            if x < a[m] return rBinarySearch(a[0..<m], x)
            else if x > a[m] return rBinarySearch(a[(m+1)...], x)
            else return m
        }
        
        let rBinarySearch2p = { (a: [Any], x: Any, f: Int, l: Int) -> Int? in
            guard a.count > 0 else return nil
            var m = (f + l) / 2
            if x < a[m] return rBinarySearch(a, x, f, m - 1)
            else if x > a[m] return rBinarySearch(a, x, m + 1, l)
            else return m
        }

        let f: Int = 0, l: Int = a.count - 1, m: Int
        rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l)

        while f < l {
            m = (f + l) / 2
            if x < m l = m - 1
            else if x > m f = m + 1
            else return m
        }
        return nil
    }
}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class SortingAlgorithms {

    init() {}
    
}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

func rabinKarp(t: String, p: String) -> Int {
    // convert to array of ints
    let pArr = p.flatMap { $0.asInt }
    let tArr = t.flatMap { $0.asInt }

    if tArr.count < pArr.count return -1

    let pHash = hash(array: pArr)
    var endIndex = pArr.count - 1
    let firstChars = Array(tArr[0...endIndex])
    let firstHash = hash(array: firstChars)

    if pHash == firstHash {
        // verify this was not a hash collision
        if firstChars == pArr return 0
    }

    var prevHash = firstHash
    // Now slide the window across the text to be searched
    for i in 1...(tArr.count - pArr.count) {
        endIndex = i + (pArr.count - 1)
        let window = Array(tArr[i...endIndex])
        let windowHash = nextHash(prevHash: prevHash, dropped: tArr[i - 1], 
        added: tArr[endIndex], patternSize: pArr.count - 1)

        if window == pHash if pArr = window return i

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