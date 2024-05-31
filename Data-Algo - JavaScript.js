'use strict';

/*

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


// TODO: class DataStructures


// Arrays & Strings

// Matrices

function spiralMatrix(mat) { // spiralOrder | O(n) / O(nm) t; O(n) / O(nm) s
    let arr = []
    if (mat.length === 0) return arr

    let rs = mat.length, cs = mat[0].length
    let top = 0, bottom = rs - 1,
    left = 0, right = cs - 1,
    dir = 'right', i = 0

    while (top <= bottom && left <= right) {
        switch (dir) {
            case 'right':
                for (i = left; i <= right; i++) arr.push(mat[top][i])
                top++; dir = 'down'
                break
            case 'down':
                for (i = top; i <= bottom; i++) arr.push(mat[i][right])
                right--; dir = 'left'
                break
            case 'left':
                for (i = right; i >= left; i--) arr.push(mat[bottom][i])
                bottom--; dir = 'up'
                break
            case 'up':
                for (i = bottom; i >= top; i--) arr.push(mat[i][left])
                left++; dir = 'right'
                break
        }
    }
    return arr
}

function setMatrixZeroes(mat) { // O(nm) t | O(1) s
    let firstColHasZero = firstRowHasZero = false
    let rs = mat.length, cs = mat[0].length

    // check if 1st col has zero
    for (let i = 0; i < rs; i++) {
        if (mat[i][0] === 0) {
            firstColHasZero = true
            break
        }
    }

    // check if 1st row has zero
    for (let i = 0; i < cs; i++) {
        if (mat[0][i] === 0) {
            firstRowHasZero = true
            break
        }
    }

    // use 1st row & col as flags, if rest of cells have zeroes
    for (let r = 1; r < rs; r++) {
        for (let c = 1; c < cs; c++) {
            if (mat[r][c] === 0) {
                mat[0][c] = 0
                mat[r][0] = 0
            }
        }
    }

    // zero out cells based on flags in 1st row & col
    for (let r = 1; r < rs; r++) {
        for (let c = 1; c < cs; c++) {
            if (mat[r][0] === 0 || mat[0][c] === 0)
                mat[r][c] = 0
        }
    }

    // zero out 1st col
    if (firstColHasZero)
        for (let i = 0; i < rs; i++)
            mat[i][0] = 0

    // zero out 1st row
    if (firstRowHasZero)
        for (let i = 0; i < cs; i++)
            mat[0][i] = 0
}

function wordSearch(mat) { // O(nm) t | O(1) s
    // check if word exists in matrix of letters

    const exist = (mat, word) => {

        let found = false, rs = mat.length, cs = mat[0].length

        const dfs = (r, c, count, word) => {
            if (count === word.length) {
                found = true; return
            }
            if (
                r < 0 || r >= rs ||
                c < 0 || c >= cs ||
                mat[r][c] !== word[count] ||
                found
            ) return

            let tmp = mat[r][c]
            mat[r][c] = ''

            dfs(r + 1, c, count + 1, word)
            dfs(r - 1, c, count + 1, word)
            dfs(r, c + 1, count + 1, word)
            dfs(r, c - 1, count + 1, word)

            mat[r][c] = tmp
        }

        for (let r = 0; r < rs; r++) {
            for (let c = 0; c < cs; c++) {
                if (mat[r][c] === word[0])
                    dfs(r, c, 0, word)
            }
        }

        return found
    }

    return exist(mat, 'word')
}

// HashMaps & HashTables

class HashTable {

    constructor(size) {
        this.data = new Array(size)
    }

    _hash(key) {
        let hash = 0
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length
        }
        return hash
    }

    set(key, value) {
        let address = this._hash(key)
        if (!this.data[address])
            this.data[address] = []
        this.data[address].push([key, value])
        return this.data
    }

    get(key) {
        const address = this._hash(key)
        const currentBucket = this.data[address]
        if (currentBucket) {
            for (let i = 0; i < currentBucket.length; i++) {
                if (currentBucket[i][0] === key)
                    return currentBucket[i][1]
            }
        }
        return null
    }

    keys() {
        const keysArray = []
        console.log(this.data.length)
        for (let i = 0; i < this.data.length; i++) {
            if (this.data[i])
                keysArray.push(this.data[i][0][0])
        }
        return keysArray
    }

}

/* // todo: Test
const ht = new HashTable(50)
ht.set('grapes', 10000)
ht.get('grapes')
ht.set('apples', 9)
ht.get('apples')
ht.keys()
*/


// Linked Lists

function Node(value, next, prev) {
    this.value = value
    this.next = next
    this.prev = prev
}

var LinkedList = function() {
    this.head = null
    this.tail = null
}

LinkedList.prototype.addToHead = function(value) { // O(1) t ; 
    var node = new Node(value, this.head, null)
    if (this.head) this.head.prev = node
    else this.tail = node // if no head, ll was empty
    this.head = node
}

LinkedList.prototype.addToTail = function(value) { // O(1) t ; 
    var node = new Node(value, null, this.tail)
    if (this.tail) this.tail.next = node
    else if (this.head) this.head.next = node // if no tail & head, 
    else this.head = node // if no head either, ll was empty
    this.tail = node
}

LinkedList.prototype.removeHead = function() { // O(1) t ; 
    if (!this.head) return null
    let value = this.head.value
    this.head = this.head.next
    if (this.head) this.head.prev = null
    else this.tail = null // if ll had only 1 node (head), so it's now empty
    return value
}

LinkedList.prototype.removeTail = function() { // O(1) t ; 
    if (!this.tail) return null
    let value = this.tail.value
    this.tail = this.tail.prev
    if (this.tail) this.tail.next = null
    else this.head = null // if ll had only 1 node (tail), so it's now empty
    // this option is invalid if every ll must have a head, before having a tail
    return value
}

LinkedList.prototype.removeTail = function() { // todo: test option 2
    if (!this.head) return null
    // this option is only valid if every ll must have a head, before having a tail
    let value = null
    if (!this.tail) {
        value = this.head.value
        this.head = null
        return value
    }
    value = this.tail.value
    this.tail = this.tail.prev
    if (this.tail) this.tail.next = null
    else this.head = null // if ll had only 1 node (tail), so it's now empty
    return value
}

LinkedList.prototype.search = function(value) { // O(n) t ; n = number of ll nodes
    let currentNode = this.head
    while (currentNode) {
        if (value === currentNode.value)
            return currentNode.value
        currentNode = currentNode.next
    }
    return null
}

LinkedList.prototype.indexOf = function(value) {
    let currentNode = this.head
    let is = [], i = 0
    while (currentNode) {
        if (value === currentNode.value) is.push(i)
        currentNode = currentNode.next; i++
    }
    return is
}

// Leetcode Q19
function removeNthFromEnd(ll, n) { // O(nl / n) t (nl = ll node num) ; O(1) s
    let slow = fast = ll.head
    for (let i = 0; i < n; i++) 
        fast = fast.next
    while (fast.next) {
        slow = slow.next
        fast = fast.next
    }
    // this only removes nth node
    let nthNode = slow.next
    let nextNode = nthNode.next
    slow.next = nextNode
    nextNode.prev = slow
    // ll.tail = slow // this removes all nodes from nth to tail
    return nthNode // or ll / ll.head
}

// Leetcode Q21
function merge2SortedLinkedLists(l1, l2) { // O(n1 + n2) t ; O(1) s
    let l1Node = l1.head, l2Node = l2.head
    let dummyHead = Node(0, null, null)
    let ll = LinkedList(); ll.addToHead(dummyHead.value)
    // todo: test Option 1: ensure this adds longer ll's remaining nodes' values
    while (l1Node.next || l2Node.next) {
        if (l1Node.value <= l2Node.value) {
            ll.addToTail(l1Node.value)
            if (l1Node.next) l1Node = l1Node.next
            else {
                while (l2Node.next) {
                    ll.addToTail(l2Node.value)
                    l2Node = l2Node.next
                }
                break
            }
        } else {
            ll.addToTail(l2Node.value)
            if (l2Node.next) l2Node = l2Node.next
            else {
                while (l1Node.next) {
                    ll.addToTail(l1Node.value)
                    l1Node = l1Node.next
                }
                break
            }
        }
    }
    /* // todo: test Option 2: ensure this adds longer ll's remaining nodes' values
    while (l1Node.next && l2Node.next) {
        if (l1Node.value <= l2Node.value) {
            ll.addToTail(l1Node.value)
            if (l1Node.next) l1Node = l1Node.next
        } else {
            ll.addToTail(l2Node.value)
            if (l2Node.next) l2Node = l2Node.next
        }
    }
    while (l1Node.next) {
        ll.addToTail(l1Node.value)
        l1Node = l1Node.next
    }
    while (l2Node.next) {
        ll.addToTail(l2Node.value)
        l2Node = l2Node.next
    }
    */

    ll.removeHead() // remove dummyHead when done
    return ll
}

// * Leetcode Q141 - hasCycle or isCircular
function hasCycle(ll) { 

    // Option 1: O(n) t; O(1) s
    // todo: test for true Circularity (to be sure slow & fast iterations always intersect on every cycle-check)
    let slow = fast = ll.head
    // NB: not O(n/2 ~ n) t because fast shifts 2x for every slow shift
    // because fast node keeps iterating in cycles until it intersects with slow node
    // so O(n) t is based on slow node's iteration through the entire linked list, once
    while (slow && fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
        // check slow & fast obj id's, not values
        if (slow === fast) return true
    }

    // Option 2: Wrong
    // TODO: this checks values only, and slow/fast node values always intersect

    let d = {} // store ll node values on every fast-node iteration
    // in order to check existence of every slow-node iteration
    // todo: find out how to achieve this without a hashmap (so O(1) s)
    while (slow.next) {
        // don't double iterate fast in a loop to keep to constant time
        if (fast.next) { // but find any possibly more-optimized option
            fast = fast.next
            d[fast.value] = true
            if (fast.next) {
                fast = fast.next
                d[fast.value] = true
            }
        }
        if (!!d[slow.value]) return true // break fast, to keep to O(n/2 ~ n) t & x
        slow = slow.next
    }

    return false
}

// Leetcode Q206 - Reverse LinkedList (singly for more simplicity)
function reverseLinkedList(ll) { // O(n) t ; O(1) s
    let node = ll.head, next = null, prev = null
    ll.head = ll.tail
    ll.tail = node
    // now iterate through ll while reversing pointers
    // with doubly-lls, reverse both next & prev pointers on each iteration
    while (node) { // will break when node is null (previous iteration's next to last node is null)
        next = node.next
        node.next = prev
        // node.prev = next // reverse .prev pointer too, for doubly lls
        prev = node
        node = next

    }
    return ll // or ll.head / prev (new head)
}


/* // todo: tests
var ll = new LinkedList()
ll.addToHead(100)
ll.addToHead('Hello')
ll.addToHead(200)
ll.addToHead('World')
ll.addToTail(300)
ll.addToTail(100)
let val1 = ll.removeHead()
let val2 = ll.removeTail()
let val3 = ll.search('World')
let val4 = ll.search('Earth')
let vals = lls.indexOf(100)
console.log(ll, val1, val2, val3, val4, vals)
*/


// todo: Test out this shorthand JS Object notation

var LL = {

    N: function(value, next, prev) {
        this.value = value
        this.next = next
        this.prev = prev
    },

    _head: null,
    get head() { return this._head },
    set head(node) { this._head = node },

    _tail: null,
    get tail() { return this._tail },
    set tail(node) { this._tail = node },

    addToHead: (value) => {
        var node = new this.N(value, this.head, null)
        if (this.head) this.head.prev = node
        else this.tail = node
        this.head = node
    },

    addToTail: (value) => {
        var node = new this.N(value, null, this.tail)
        if (this.tail) this.tail.next = node
        else if (this.head) this.head.next = node
        else this.head = node
        this.tail = node
    },

    removeHead: () => {
        if (!this.head) return null
        let value = this.head.value
        this.head = this.head.next
        if (this.head) this.head.prev = null
        else this.tail = null
        return value
    },

    removeTail: () => {
        if (!this.tail) return null
        let value = this.tail.value
        this.tail = this.tail.prev
        if (this.tail) this.tail.next = null
        else this.head = null
        return value
    },

    search: (value) => {
        let currentNode = this.head
        while (currentNode) {
            if (value === currentNode.value)
                return currentNode.value
            currentNode = currentNode.next
        }
        return null
    },

    indexOf: (value) => {
        let currentNode = this.head
        let is = [], i = 0
        while (currentNode) {
            if (value === currentNode.value) is.push(i)
            currentNode = currentNode.next; i++
        }
        return is
    }

}


// todo: Test out this JS class notation

class LL {

    static Node = class {

        constructor(v, n = null) {
            this.value = v
            this.next = n
        }
        
    }

    static SNode = class extends Node {

        constructor(v, n = null) {
            super(v, n)
        }

    }

    static DNode = class extends Node {

        constructor(v, n = null, p = null) {
            super(v, n)
            this.prev = p
        }
        
    }

    constructor(v) {
        this.head = {
            value: v, next: null, prev: null
        } // todo: or new Node(v) / DNode(v)
        this.tail = this.head
        this.length = 1
    }

    // prepend O(1), append O(1), 
    // lookup O(n), insert O(n), remove O(n)
    
    print() {
        const arr = []
        let node = this.head
        while (node) {
            arr.push(node.value)
            node = node.next
        }
        console.log(arr)
    }

    prepend(v) {
        const node = {
            value: v, next: this.head, prev: null
        }
        // with js class objects, even if this.head is assigned to node.next by reference ..
        this.head.prev = node
        // changing this.head object itself, once done after, doesn't affect the node.next object
        this.head = node
        this.length++
        return this
    }

    append(v) {
        const node = {
            value: v, next: null, prev: this.tail
        }
        // with js class objects, even if this.tail changes .next by reference ..
        this.tail.next = node
        // changing this.tail object itself, once done after, doesn't affect the this.tail.next object
        this.tail = node
        this.length++
        return this
    }

    lookup(i) {
        let c = 0
        let node = this.head
        while (c !== i) {
            node = node.next
            c++
        }
        return node
    }

    insert(i, v) {
        if (!v) return null
        if (i >= this.length)
            return this.append(v)
        const node = {
            value: v, next: null, prev: null
        }
        const prev = this.lookup(i-1)
        // prev.next will never be null due to the index check above (to append v instead)
        node.prev = prev
        node.next = prev.next
        prev.next.prev = node // or node.next.prev = node
        prev.next = node
        this.length++
        return this
    }

    remove(i) {
        const prev = this.lookup(i-1)
        const toRemove = prev.next
        prev.next = toRemove.next
        toRemove.next.prev = prev
        toRemove = null // not toRemove.next, because that'd affect the new next node to prev
        this.length--
        return this
    }

    reverse() {
        if (this.length == 1 || !this.head.next)
            return this.head
        let node = this.head
        let next = node.next
        this.head = this.tail
        this.tail = node
        let tmp = null
        while (next) {
            tmp = next.next
            next.next = node
            node.prev = next
            node = next
            next = tmp
        }
        this.head.prev = null
        this.tail.next = null
        return this
    }

    // Alt (3rd Party) logic
    reverse(dummyOverrideArg) {
        if (!this.head.next)
            return this.head
        let first = this.head
        this.tail = this.head
        let second = first.next
        let tmp = null
        while (second) {
            tmp = second.next
            second.next = first
            first = second
            second = tmp
        }
        this.head.next = null
        this.head = first
        return this
    }

}


// Stacks & Queues

// Heaps (max & min)

// Binary Heaps & Priority Queues

// Trees

// Binary (Search) Trees

// Tries
    
// Graphs

// Bits


////////////////////////////////////////
//  Cracking Coding Interview Qs
////////////////////////////////////////

// Arrays & Strings

function sortStringArray(a) {
    // O(n * s log s) + O(n log n) t | O(1) s
    a.map((s, i) => s.sort())
    a.sort() // or
    a.sort((a, b) => a - b) // -ve (a<b) for ascending, ASCII character order
}

function isUnique(s) {
    if (s.length == 0) return false
    else if (s.length == 1) return true
    // O(s) t | O(s) s
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
    // O(a) + O(b) t | O(a) s 
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
    // O(s) t | O(1) s
    s = [...s] // find t-complexity
    for (let i = 0; i < s.length; i++) {
        if (s[i] === " ") s[i] = "%20"
    }
    s.join("") // convert s back to string
    // NB: toString() array method returns a string with array values separated by commas
    return s
}

function palindromePermutation(s) {
    // O(s + m) t | O(m) s [NB: s>m]
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
    // O(s) t | O(m) s
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
    // O(s + m) t | O(m) s [NB: s>m]
    let m = {}
    for (let x of s) {
        m[x] = x in m ? ++m[x] : 1
    }
    for (x in m) {
        cs += x + m[x] // NB: String Concatenation can operate in O(n^2) t; confirm
    }
    return cs.length < s.length ? cs : s
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

// Matrices

function rotateMatrix(mat) { // O(n^2) t

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

// HashMaps & HashTables

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


// Trees


// Graphs





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