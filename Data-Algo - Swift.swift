

// RABIN-KARP STRING SEARCH ALGO
public func search(t: String, p: String) -> Int {
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
