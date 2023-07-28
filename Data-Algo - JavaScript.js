'use strict';

/*

LEARN

Js/Ts/Sw
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

var Searching = function() {

    function linearSearch(a, x) { // O(n)
        for (i of a) if (i === x) return i
        return null
    }

    function binarySearch(a, x) { // O(log n)
        // a.sort()
        if (a.length === 0) return null

        function rBinarySearch(a, x) {
            if (a.length === 0) return null
            m = a.length / 2
            if (x < a[m]) return rBinarySearch(a.slice(0, m - 1), x)
            else if (x > a[m]) return rBinarySearch(a.slice(m + 1, a.length - 1), x)
            else return m
        }

        function rBinarySearch(a, x, f, l) {
            if (a.length === 0 || f > l) return null
            m = (f + l) / 2 // better: f + (l - f) / 2
            if (x < a[m]) return rBinarySearch(a, x, f, m - 1)
            else if (x > a[m]) return rBinarySearch(a, x, m + 1, l)
            else return m
        }

        f = 0, l = a.length - 1 
        rBinarySearch(a, 3); rBinarySearch(a, 3, f, l)

        while (f < l) {
            m = (f + l) / 2 // better: f + (l - f) / 2
            if (x < a[m]) l = m - 1
            else if (x > a[m]) f = m + 1
            else return m
        }
        return null
    }

}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

var Sorting = function() {

    Sorting.prototype.check = (a) => {
        return [0, 1].includes(a.length)
    }

    Sorting.prototype.swap = (a, b) => {
        let t = a; a = b; b = t
        // (a, b) = (b, a) // faster, but () by value
        return (a, b)
    }

    Sorting.prototype.compare = (a, b) => {
        return a < b
    }

    // regular

    function insertion(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    function selection(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    function shell(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    // bad

    function bubble(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    function slow(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    // special

    function counting(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    function radix(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    function topological(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    // hybrid

    function intro(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    // fast

    function heap(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    function merge(a) {
        if (this.check(a)) return a
        // 
        return a
    }

    function quick(a) {
        if (this.check(a)) return a
        // 
        return a
    }

}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////




////////////////////////////////////////
//  Cracking Coding Interview Qs
////////////////////////////////////////

// Arrays & Strings

function sortStringArray(a) {
    // O(n * s log s) + O(n log n) t ; O(1) s
    a.map((s, i) => s.sort())
    a.sort() // or
    a.sort((a, b) => a - b) // -ve (a<b) for ascending, ASCII character order
}

function isUnique(s) {
    if (s.length == 0) return false
    else if (s.length == 1) return true
    // O(s) t ; O(s) s
    let m = {}
    for (let c of s) {
        if (c in m) return false
        else m[c] = c
    }
    // O(s log s) + O(s) t; O(1) s
    s.sort()
    for (let i = 1; i < s.length; i++){
        if (s[i] == s[i-1]) return false
    }
    return true
}

function checkPermutation(a, b) {
    if (a.length != b.length) return false
    // O(a) + O(b) t ; O(a) s 
    let m = {}
    for (let x of a) {
        m[x] = x in m ? ++m[x] : 1
    }
    for (x of b) {
        if (m?.[x] >= 1) --m?.[x]
        else return false
    }
    return true
    // O(a log a) + O(b log b) t
    return a.sort() === b.sort()
}

function URLify(s) {
    if (s.length == 0) return null
    // O(?)
    s.replace(" ", "%20")
    // O(s) t ; O(1) s
    s = [...s] // find t-complexity
    for (let i = 0; i < s.length; i++) {
        if (s[i] === " ") s[i] = "%20"
    }
    s.join("") // convert s back to string
    // NB: toString() array method returns a string with array values separated by commas
    return s
}

function palindromePermutation(s) {
    // O(s + m) t ; O(m) s [NB: s>m]
    let m = {}, f = false
    for (let x of s) {
        m[x] = x in m ? ++m[x] : 1
    }
    for (x of m) {
        if (Math.abs(x) % 2 == 1) {
            if (f) return false
            else f = true
        }
    }
    return true
    // O(s) t ; O(m) s
    let odd = 0
    for (x of s) {
        m[x] = x in m ? ++m[x] : 1
        odd += Math.abs(m[x]) % 2 == 1 ? 1 : -1
    }
    return odd <= 1 // s cannot be a palindrome if odd > 1
}

function oneAway(a, b) {
    let d = i = j = 0
    while (d !== 2) {
        
    }
    return d === 2
}

function stringCompression(s) {
    if (s.length <= 1) return s
    // s = s.toLowerCase() // only if s's chars are not Case-Sensitive
    // O(s) t; O(1) s
    let cs = "", c = 0
    for (let i = 0; i < s.length; i++) {
        c++
        if ((i+1 == s.length) || (s[i] != s[i+1])) {
            cs += s[i] + c // NB: String Concatenation can operate in O(n^2) t; confirm
            c = 0
        }
    }
    // O(s + m) t ; O(m) s [NB: s>m]
    let m = {}
    for (let x of s) {
        m[x] = x in m ? ++m[x] : 1
    }
    for (x in m) {
        cs += x + m[x] // NB: String Concatenation can operate in O(n^2) t; confirm
    }
    return cs.length < s.length ? cs : s
}

// Matrices

// TODO: Understand this problem.
function rotateMatrix(mat) {
    // O(n^2)
    if (mat.length == 0 || mat.length != mat[0].length) return false
    let n = mat.length, first = last = offset = top = i = null
    for (let layer = 0; layer < n/2; layer++) {
        first = layer; last = n - layer - 1
        for (i = first; i < last; i++) {
            offset = i - first
            // NB PATTERN: t: first -> i -> last -> last-offset
            top = mat[first][i] // save top
            mat[first][i] = mat[last - offset][first] // left -> top
            mat[last - offset][first] = mat[last][last - offset] // bottom -> left
            mat[last][last - offset] = mat[i][last] // right -> bottom
            mat[i][last] = top // top -> right
        }
    }
    return mat
}

function zeroMatrix(mat) {

}

function stringRotation(a, b) {
    let isSubStr = (a, b) => a in b
    // O(n) t, if isSubStr = O(a+b) t
    if (a.length == b.length && a.length > 0) {
        let s = "" + a + a
        return isSubStr(s, b)
    }
    return false
}

// Linked Lists

function removeDuplicates(l) { // doubly-linked

    let node = l?.root, d = [], runner = prev = next = null

    // 1-Pass Traversal; O(n) t; O(n) s

    while (node?.next || node?.prev) {
        if (!(node?.data in d)) {
            d.push(node.data)
        } else {
            node?.prev?.next = node?.next
            node?.next?.prev = node?.prev
            // or, use vars: prev & next (more O(space))
            prev?.next = node?.next
            next?.prev = node?.prev
            prev = node?.prev
            next = node?.next?.next
            // TODO: find out how this affects vars: prev & next (where the issue is ..), & their props
            // next = prev?.next = node?.next
            // prev = next?.prev = node?.prev
        }
        node = node?.next
    }

    // Runner Traversal (2-point); O(n^2) t; O(1) s

    while (node?.next || node?.prev) {
        runner = node?.next
        while (runner?.next || runner?.prev) {
            if (runner?.data === node?.data) {
                runner?.prev?.next = runner?.next
                runner?.next?.prev = runner?.prev
                // or, use vars: prev & next (more O(space))
                prev?.next = runner?.next
                next?.prev = runner?.prev
                prev = runner?.prev
                next = runner?.next?.next
                // TODO: find out how this affects vars: prev & next (where the issue is ..), & their props
                // prev?.next = runner?.next
                // next = runner?.next?.next // ans
                // prev = next?.prev = runner?.prev
            }
            runner = runner?.next
        }
        node = node?.next
    }

    // Runner Traversal (2-point); O(n^2) t; O(n) s (without prev & next vars)

    while (node?.next) {
        runner = node
        while (runner?.next) { // iterating proactively
            if (runner?.next?.data === node?.data) {
                if (!(runner?.next?.data in d)) {
                    d.push(runner.next.data) // hash duplicates instead
                } else // do
                runner?.next = runner?.next?.next
                runner?.next?.next?.prev = runner
            }
            runner = runner?.next?.next
            // might make t O(n^2/2), due to double jumps on each iteration
        }
        node = node?.next
        // TODO: if runner = node by reference, multiple jumps can also occur here
    }

    // Not Needed; Js objects are assigned by reference
    // l?.root = node

    return l
}

function kthToLast(l, k) {
    
}





////////////////////////////////////////
//  CodeSignal
////////////////////////////////////////

function rabinKarp(t, p) {    
    // convert to array of ints

    return -1
}



////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function main() {
    document.write("Hello, World!")
}