'use strict';

// * install globally
import * as R from 'ramda'
import * as RA from 'ramda-adjunct'

/* // TODO: To-Use

Generics
lodash/fp, ramda, immutable.js
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

var Sorting = function() {

    Sorting.prototype.baseCheck = (a) => {
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
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    function selection(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    function shell(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    // bad
    
    function bubble(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    function slow(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    // special
    
    function counting(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    function radix(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    function topological(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    // hybrid
    
    function intro(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    // fast
    
    function heap(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    function merge(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
    function quick(a) {
        if (this.baseCheck(a)) return a
        // 
        return a
    }
    
}



////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

var Searching = function() {

    // prototype methods

    const _this = Searching.prototype

    _this.baseCheck = fn => R.ifElse(
        R.isEmpty, // fn should have an array arg
        R.always(null), // null if array is empty
        fn // return as a functor to then exec with array
    )

    _this.check = R.curry((c, a, b) => {
        const ops = {
            '>': R.gt,
            '>=': R.gte,
            '<': R.lt,
            '<=': R.lte,
            '=': R.equals,
            '==': R.equals,
        }
        const comparator = ops[c]
        return comparator 
            ? comparator(a, b) 
            : null
    })

    _this.compareNums = (s, a, b) => {

        const check = R.ifElse(
            c => R.equals(c, '>'),
            _ => R.gt(a, b),
            R.ifElse(
                c => R.equals(c, '<'),
                _ => R.lt(a, b),
                R.ifElse(
                    c => R.equals(c, '='),
                    _ => R.equals(a, b),
                    _ => null
                )
            )
        )
        
        const res = []
        s.split('')
            .map(c => {
                res.push(
                    check(c)
                )
            })
        
        return R.isNotEmpty(res) // * never wrap return's next syntax elem (in return value) to next line
            && R.includes(true, res)
        
    }

    _this.while = (predicate, transformer, initialValue) => {
        const iter = R.ifElse(
            x => !predicate(x), // when predicate check fails ..
            x => x, // break while loop
            x => iter(transformer(x))
        )
        return iter(initialValue)

        /* 
            * Example usage 1
            const isLessThan10 = x => x < 10;
            const addOne = x => x + 1;
            const startValue = 0;

            const result = while(isLessThan10, addOne, startValue);
            console.log(result); // Outputs: 10

            * Example usage 2
            const predicate = ({ x, y }) => x < y;
            const transformer = ({ x, y }) => ({ x: x + 1, y });
            const initialState = { x: 0, y: 5 };
            
            const result = while(predicate, transformer, initialState);
            console.log(result); // Outputs: { x: 5, y: 5 }

            * Example usage
            const predicate = ({ x, y }) => x < y;
            const transformer = ({ x, y }) => {
            const randomBool = Math.random() >= 0.5;
            return randomBool ? { x: x + 1, y } : { x, y: y - 1 };
            };
            const initialState = { x: 0, y: 5 };
            
            const result = while(predicate, transformer, initialState);
            console.log(result); // Outputs: final state of { x, y }
        */
    }

    // other functions

    function linearSearch(a, x) { // O(n) t

        const fLinearSearch = (a, x) => a.find(i => i === x) // .find() - also O(n) t

        for (i of a) if (i === x) return i // * 2 constructs can be used in 1 line
        // * never force 1-line or tabs in production (only scopes {}) | unless in-built - .py/rb/sh/erl/fs/qs/..
        return null
    }

    function binarySearch(a, x) { // O(log n)
        if (a.length === 0) return null

        a.sort((a, b) => a - b); // O(n log n) t // sort in-place
        // compare func for int arrays only
        // or - .sort() - without compare func for strings & chars (alphabetical order) only 
        // NB - .toSorted() - returns copy

        // * NB: sorting array before proceeding also affects indices (in-case actual array's item's index is required)

        function rBinarySearch(a, x) {
            if (a.length === 0) return null
            const m = Math.floor(a.length / 2) // avoid float
            if (x < a[m]) return rBinarySearch(a.slice(0, m), x) // .slice excludes endIndex; .splice(0, m) doesn't 
            else if (x > a[m]) return rBinarySearch(a.slice(m + 1, a.length), x)
            // else - (x === a[m]) - best to check for this before other if-cases (imperfect way for memory)
            else return a[m] // or return a bool instead of same x arg - index m decreasing recursively, as a's length decreases
            // * or call - rBinarySearch2p(a, x, 0, a.length - 1) - returns found index
        }

        const fRBinarySearch = (a, x) => {
            // todo: base check of a.length at function bottom

            const exec = a => {

                const m = Math.floor(
                    R.divide(a.length, 2)
                )
                // * const m = R.compose(Math.floor, R.divide(a.length))(2)
                
                const wrongRecurse = R.ifElse(
                    x => _this.check('<', x, a[m]),
                    x => fRBinarySearch(
                        a.slice(0, m),
                        x
                    ),
                    R.ifElse(
                        x => _this.check('>', x, a[m]),
                        x => fRBinarySearch(
                            a.slice(
                                m + 1,
                                a.length
                            ),
                            x
                        ),
                        // * wrongRecurse because:
                        // else - (x === a[m]) - best to check for this before other if-cases (imperfect way chosen, for memory)
                        _ => a[m]
                    )
                )
    
                const recurse = R.ifElse(
                    x => _this.check('=', x, a[m]),
                    _ => a[m], // or return a bool instead of same x arg - index m decreasing recursively, as a's length decreases
                    R.ifElse(
                        x => _this.check('<', x, a[m]),
                        x => fRBinarySearch( // couldv've recurse(..)d instead, if it also took in args a & x
                            a.slice(0, m),
                            x
                        ),
                        // else - (x > a[m])
                        x => fRBinarySearch(
                            a.slice(
                                m + 1,
                                a.length
                            ),
                            x
                        )
                    )
                )
    
                return recurse(x) // * cannot call R.ifElse without an arg
                // * in case you wanted to do away with re-passing in x

            }

            return _this.baseCheck(exec)(a) // * will return null if a is null / empty

        }

        function rBinarySearch2p(a, x, f, l) {
            if (a.length === 0 || f > l) return null
            const m = Math.floor(f + (l - f) / 2) // better than - (f + l) / 2
            if (x === a[m]) return m
            else if (x < a[m]) return rBinarySearch2p(a, x, f, m - 1)
            // else - (x > a[m]) 
            else return rBinarySearch2p(a, x, m + 1, l)
        }

        const fRBinarySearch2p = (a, x, f, l) => {

            const exec = a => {
                
                const recurse = (f, l) => {
                    const m = R.compose(
                        Math.floor,
                        R.add(f),
                        R.divide(R.__, 2),
                        R.subtract(R.__, f)
                    )(l)
                    const check = R.ifElse(
                        m => _this.check('=', x, a[m]),
                        m => m,
                        _ => R.ifElse(
                            m => _this.check('<', x, a[m]),
                            m => recurse(f, l=m-1),
                            m => recurse(f=m+1, l)
                        )
                    )
                    return check(m)
                }

                const wrongRecurse = (f, l) => {
                    const [
                        check1, 
                        check2 // only required if check 1 fails
                    ] = [
                        R.ifElse(
                            m => _this.check('=', x, a[m]),
                            m => m,
                            m => m, // return same arg even if it fails, for check 2
                        ),
                        R.ifElse(
                            m => _this.check('<', x, a[m]),
                            m => wrongRecurse(f, l=m-1),
                            m => wrongRecurse(f=m+1, l)
                        )
                    ]
                    const checks = R.compose(check2, check1)
                    // composing both checks means check2 will exec even if check1 succeeds
                    return checks(m) // * so unecessary when chained if-check is bool-dependent
                }

                return recurse(f, l)

            }

            return _this.baseCheck(exec)(a)

        }

        const fBinarySearch2p = (a, x, f, l) => {

            const exec = a => {

                let startValue = {f, l, b: false}
                let predicate = ({f, l, b}) => RA.notEqual(b, true) || R.lt(f, l)

                let decL = ({f, l, m}) => ({ f, l: m - 1 })
                let incF = ({f, l, m}) => ({ f: m + 1, l })

                let checkFoundX = R.ifElse(
                    ({m}) => _this.check('=', x, a[m]),
                    ({f, l, m}) => ({ res: m, b: true, f, l }), // return m as res; will also 'b'reak out of loop after predicate check fails
                    // * NB: should also return f & l for predicate check, but since result m is found, passed in b: true will fail predicate check before f < l check
                    // * decided to add f & l later; optimizations like that may cause arg buffer issues later
                    R.ifElse(
                        ({m}) => _this.check('<', x, a[m]),
                        ({f, l, m}) => ({ b: false, ...decL({f, l, m}) }), // still ensure b == false to keep loop until predicate check fails
                        ({f, l, m}) => ({ b: false, ...incF({f, l, m}) })
                    )
                )

                let transformer = ({f, l}) => {

                    let m = Math.floor(
                        R.add(
                            R.divide(
                                R.subtract(
                                    l, 
                                    f
                                ), 
                                2
                            ), 
                            f
                        ) // f + (l - f) / 2 - 1st f 'addition' can be a 2nd arg
                    )
                    
                    /*
                    m = R.compose(
                        Math.floor,
                        R.add(f),
                        R.divide(R.__, 2),
                        R.subtract(R.__, f) // * without R.__ 'ignore' arg, would be 'f - l' (divide would also be 2 / result)
                    )(l)
                    */
                
                    return checkFoundX({f, l, m})
                }

                let res = _this.while(predicate, transformer, startValue)
                console.log(res) // should include .res with index m

                return R.propOr(null, 'res')(res)
        
            }

            return _this.baseCheck(exec)(a)

        }

        let f = 0, l = a.length - 1
        
        rBinarySearch(a, 3); rBinarySearch2p(a, 3, f, l)
        fRBinarySearch(a, 3); fRBinarySearch2p(a, 3, f, l); fBinarySearch2p(a, 3, f, l)

        let m

        while (f < l) {
            m = Math.floor(f + (l - f) / 2) // better than - (f + l) / 2
            if (x === a[m]) return m
            else if (x < a[m]) l = m - 1
            // else - (x > a[m]) 
            else f = m + 1
        }

        return null
    }

}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////


// TODO: class DataStructures


// Arrays & Strings

// (Array) Lists & Tuples

// Sets & Sequences

// WeakMaps & WeakSets

class Weak_DStructs {

    // TODO: Create & Implement Map, Set, WeakMap, & WeakSet Data Structures

    constructor () {}

    playground () {

        // Maps

        let m = new Map()
        m.set('key', 'value')
        m.set('key 2', 'value')
        // keys are ordered; insertion & retrieval always in same order
        m.set(true, 1)
        console.log(m.size)
        console.log(m)
        console.log(m.has('key'))
        console.log(m.get('key'))
        m['key'] = 'new value'
        m.set(1, true).set(false, 0)
        m.delete('key 2')
        console.log(m)
        // m - .entries() .keys() .values() .forEach((value, key, map) => {})
        let obj = Object.fromEntries(m.entries()) // convert map to js obj
        let m2 = new Map(Object.entries(obj)) // convert back
        m.clear()

        // Sets - unique value items

        let s = new Set()
        s.add('1st')
        s.add('2nd')
        s.add('3rd')
        console.log(s.size)
        console.log(s)
        s.delete('2nd')
        s.delete('4th') // no error if not found
        // s = .entries() .values() .forEach((v1, v2, s) => {}) - no need for variadic param syntax for s (...s)
        s.clear()

        // WeakMaps - Garbage Collection removes keys which are null referenced object vars
        // WeakSets - Garbage Collection removes items which are null referenced object vars
        
        // Maps & Sets strongly hold onto objects which are null referenced, when GC is executed
        // eg. obj = {}; m.set(obj, 'val'); obj = null; // m will not lose 'obj' var as its key

        // WeakMaps can only (weakly) hold objects as keys; cannot have any primitive data types as keys
        // will lose 'obj' var as its key, if obj ever becomes null referenced
        // eg. obj = {}; wm.set(obj, 'val'); obj = null; // wm will lose 'obj' as its key

        // WeakSets can only (weakly) hold objects as items; cannot have any primitive data types as items
        // will lose 'obj' var as an item, if obj ever becomes null referenced
        // eg. obj = {}; ws.add(obj, 'val'); obj = null; // wm will lose 'obj' as its item

        // Weak keys (in WeakMaps) are obj var weakmap-keys which have now been null referenced
        // Weak items (in WeakSets) are obj var weakset-items which have now been null referenced

        // Because of weak keys/items, Weak Maps/Sets don't have iterable methods (.entries() .keys() .values())

        let wm = new WeakMap()
        wm.set('key', 'value')
        wm.set('key 2', 'value 2')
        obj = {}
        wm(obj, 'value 2')
        console.log(wm)
        console.log(wm.has(obj))
        console.log(wm.get(obj))
        obj = null
        console.log(wm.get(obj))
        wm.delete('key 2')
        console.log(wm)

        let ws = WeakSet()
        obj = {}
        let obj1 = {}, obj2 = {}
        ws.add(obj, 1)
        ws.add(obj1, 2)
        ws.add(obj2, 3)
        console.log(wm)
        obj = null
        wm.delete(obj1)
        console.log(ws)

    }

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
        // each address hash's value is an array, for multiple values, to handle collisions
        // Collisions - multiple values with the same key / hash (so they have to be grouped together)
        // todo: can also use LinkedList as hash value to handle collisions
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


function HashTable2(size) {
    this.buckets = Array(size)
    this.numBuckets = this.buckets.length
}
// HashTable2's buckets has hash indices pointing to HashNodes

// HashNode is a LinkedList node, for hashed value indices
function HashNode(key, value, next = null) {
    this.key = key
    this.value = value
    this.next = next
}

/* // todo:
O(1) t to hash, insert, get, update, remove, with hash table

even in the case where hashed keys point to linked lists .. 
different keys pointing to different linked lists / singular nodes / primitive value types
is what keeps time complexity constant (all lists have different number of nodes, but they all exist in the same hash table)

O(n) t to getAll() nodes from hash table, because that iterates through all of its nodes/values (inside its linked lists / singular nodes / primitives)
*/

HashTable2.prototype.hash = (key) => {
    let total = 0
    for (let i = 0; i < key.length; i++)
        total += key.charCodeAt(i)
    let bucketIndex = total % this.numBuckets
    return bucketIndex
}

HashTable2.prototype.insert = (key, value) => {
    let bucketIndex = this.hash(key)
    let hashNode = new HashNode(key, value)
    if (!this.buckets[bucketIndex]) 
        this.buckets[bucketIndex] = hashNode
    else {
        let currentNode = this.buckets[bucketIndex]
        while (currentNode.next) // ends on last node (.next == null)
            currentNode = currentNode.next
        currentNode.next = hashNode
    }
}

HashTable2.prototype.get = (key) => {
    let bucketIndex = this.hash(key)
    if (!this.buckets[bucketIndex]) {
        console.error('Bucket/value does not exist')
        return null
    }
    // return this.buckets[bucketIndex] // don't just return the hashed key's value
    // in case this node was linked to others, iterate through them first
    else { // find the HashNode with the same key, then return its value (not the HashNode itself)
        let currentNode = this.buckets[bucketIndex]
        while (currentNode) {
            if (currentNode.key === key)
                return currentNode.value
            currentNode = currentNode.next
        }
        return null
    }
}

HashTable2.prototype.update = (key, value) => {
    let bucketIndex = this.hash(key)
    if (!this.buckets[bucketIndex])
        console.error('Bucket/value to update does not exist')
    else {
        let currentNode = this.buckets[bucketIndex]
        while (currentNode) {
            if (currentNode.key === key) {
                currentNode.value = value
                return // end loop/method
            }
            currentNode = currentNode.next
        }
    }
}

HashTable2.prototype.remove = (key) => {
    let bucktIndex = this.hash(key)
    if (!this.buckets[bucktIndex]) {
        console.error('Bucket/value does not exist')
        return false
    } else {
        let currentNode = this.buckets[bucktIndex]
        while (currentNode) { // treat as a singly-linked list
            // can iterate with 2 pointers (for prev & current), then point prev to next
            // or iterate with 1 pointer for current, then shift next to current
            // by taking next's key (due to HashNode) & value, and pointing to nextNext
            if (currentNode.key === key) {
                // can create new var in this scope, because this iteration will be broken by return
                let tmp = currentNode // assign to tmp by copy because currentNode will be updated, and tmp will be returned
                if (!!currentNode.next) {
                    currentNode.key = currentNode.next.key
                    currentNode.value = currentNode.next.value
                    currentNode.next = currentNode.next?.next
                    // .next will point to null by default, due to optional chaining
                } else currentNode = null
                return tmp // todo: make sure tmp was assigned to by copy, so it doesn't get updated by pointer reference
            }
            currentNode = currentNode.next
        }
    }
}

HashTable2.prototype.getAll = () => {
    let arr = []
    this.buckets.forEach((_, currentNode) => {
        while (currentNode) {
            arr.push(currentNode) // or .key / .value
            currentNode = currentNode.next
        }
    })
    return arr
}


/* // todo: Test
const ht = new HashTable(50)
ht.set('grapes', 10000)
ht.get('grapes')
ht.set('apples', 7)
ht.get('apples')
ht.keys()
console.log(ht)

const ht2 = new HashTable2(30)
console.log(ht2.hash('key'))
ht2.insert('key', 'value')
ht2.insert('key 2', 'value 2')
ht2.insert('apples', 7)
console.log(ht2.get('apples'))
console.log(ht2)
console.log(ht2.buckets)
ht2.update('apples', 1)
ht2.remove('key 2')
console.log(ht2)
console.log(ht2.getAll())
*/


// Matrices - // TODO

// spiralOrder
function spiralMatrix(mat) { // O(n) / O(nm) t ; O(1) / O(n) / O(nm) s (n - square-matrix / n - length, m - width) 
    // or O(1) s if you ignore result array, because it's not actually a part of the algo's execution
    // (if current matrix item was only printed out, and not pushed to any result array to be returned, O(s) would be constant = O(1) s)

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

// Q - Given an m x n matrix, if an element is 0, set its entire row & column to 0
// Brute-force - create another matrix with the expected output - O(nm) s
// Optimized - Do it in-place - O(1) s

function setMatrixZeroes(mat) { // O(nm) t | O(1) s

    let firstColHasZero = firstRowHasZero = false
    let rs = mat.length, cs = mat[0].length

    // check if 1st col has zero
    for (let i = 0; i < rs; i++)
        if (mat[i][0] === 0) {
            firstColHasZero = true
            break
        }

    // check if 1st row has zero
    for (let i = 0; i < cs; i++)
        if (mat[0][i] === 0) {
            firstRowHasZero = true
            break
        }

    // use 1st row & col as flags, if rest of row-col-pair cells have zeroes
    for (let r = 1; r < rs; r++)
        for (let c = 1; c < cs; c++)
            if (mat[r][c] === 0) {
                mat[0][c] = 0
                mat[r][0] = 0
            }

    // zero out row-col-pair cells based on flags in 1st row & col
    for (let r = 1; r < rs; r++)
        for (let c = 1; c < cs; c++)
            if (mat[r][0] === 0 || mat[0][c] === 0)
                mat[r][c] = 0

    // zero out 1st col
    if (firstColHasZero)
        for (let i = 0; i < rs; i++)
            mat[i][0] = 0

    // zero out 1st row
    if (firstRowHasZero)
        for (let i = 0; i < cs; i++)
            mat[0][i] = 0

    return mat // matrix updated in-place
}

function wordSearch(mat, word='word') { // O(nm) t | O(1) s
    // check if word exists in matrix of letters

    const wordExists = (mat, word) => {

        // Graph-Matrix DFS (Depth-First Search)
        const dfs = (r, c, count, word) => {
            if (count === word.length) {
                found = true
                return
            }
            if (
                r < 0 || r >= rs ||
                c < 0 || c >= cs ||
                mat[r][c] !== word[count] ||
                found
            ) return

            let tmp = mat[r][c]
            mat[r][c] = '' // empty's current cell so can't be re-used 
            // "marks it as visited" before the next 4 recursive calls

            dfs(r + 1, c, count + 1, word)
            dfs(r - 1, c, count + 1, word)
            dfs(r, c + 1, count + 1, word)
            dfs(r, c - 1, count + 1, word)

            mat[r][c] = tmp // reset current cell for outmost dfs() calls 
            // so outer for-loop can still traverse
        }

        let found = false, rs = mat.length, cs = mat[0].length

        for (let r = 0; r < rs; r++)
            for (let c = 0; c < cs; c++)
                if (mat[r][c] === word[0])
                    dfs(r, c, 0, word)

        return found
    }

    return wordExists(mat, word)
}


// Linked Lists

function ListNode(value, next, prev) {
    this.value = value
    this.next = next
    this.prev = prev
}

var LinkedList = function() {
    this.head = null
    this.tail = null
}

LinkedList.prototype.addToHead = function(value) { // O(1) t ; 
    var node = new ListNode(value, this.head, null)
    if (this.head) this.head.prev = node
    else this.tail = node // if no head, ll was empty
    this.head = node
}

LinkedList.prototype.addToTail = function(value) { // O(1) t ; 
    var node = new ListNode(value, null, this.tail)
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

// Leetcode #19
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

// Leetcode #21
function merge2SortedLinkedLists(l1, l2) { // O(n1 + n2) t ; O(1) s
    let l1Node = l1.head, l2Node = l2.head
    let dummyHead = new ListNode(0, null, null)
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

// * Leetcode #141 - hasCycle or isCircular
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

// Leetcode #206 - Reverse LinkedList (singly for more simplicity)
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

    // todo: remove 'static' if proves non-feasible when testing
    static ListNode = class {

        constructor(v, n = null) {
            this.value = v
            this.next = n
        }
        
    }

    static SListNode = class extends ListNode {

        constructor(v, n = null) {
            super(v, n)
        }

    }

    static DListNode = class extends ListNode {

        constructor(v, n = null, p = null) {
            super(v, n)
            this.prev = p
        }
        
    }

    constructor(v) {
        this.head = {
            value: v, next: null, prev: null
        } // todo: or new ListNode(v) / DListNode(v)
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


// Stacks

class LinkedStack {
    // * A stack data structure that uses a linked list for managing elements.

    // private fields
    #length
    // linked-list is mainly used for stack data, in this cases
    #node // : LL.Node
    // array could be used instead
    #data

    constructor() {
        this._top = null
        this._bottom = null
        this.#length = 0
        this.#node = null
        this.#data = []
    }

    get top() { return this._top }
    set top(v) { this._top = v }

    get bottom() { return this._bottom }
    set bottom(v) { this._bottom = v }

    get length() { return this.#length }
    set length(v) { this.#length = v }

    get node() { return this.#node }
    set node(v) { this.#node = v }

    get data() { return this.#data }
    set data(v) { this.#data = v }

    isEmpty() {
        if (this.length === 0 || this.data.length === 0) {
            this.top = null
            this.bottom = null
            return true
        }
        return false
    }

    peek() {
        return this.top
    }

    push(v) {
        this.node = LL.Node(v)
        if (this.isEmpty())
            this.top = this.bottom = this.node
        else {
            this.node.next = this.top
            this.top = this.node
            this.node = null
        } // push node on top of 'array' stack
        // treat either index 0 (beginning) or length-1 (end) or array as the top, and other as the bottom
        this.data.push(this.node) // end of array chosen as top of stack
        this.length++
    }

    pop() {
        if (this.isEmpty()) return null
        if (this.length === 1 || this.top === this.bottom)
            this.bottom = null
        this.node = this.top
        this.top = this.node.next
        this.data.splice(this.data.length-1) // can return this spliced[0] top (end of array) to this.node too
        this.length--
        return this.node
    }

}


/*
const stack = new LinkedStack()
stack.push('google')
stack.push('youtube')
stack.push('microsoft')
stack.peek()
stack.pop()
stack.peek()
// */


// Queues

// Heaps (max & min)

// Binary Heaps

// Priority Queues

// Trees

class Tree {

    static TreeNode = class {

        constructor(value=null, left=null, right=null, children=[], parent=null) {
            this.value = value
            this.left = left
            this.right = right
            this.children = children // only for 3+ N-ary Trees
            this.parent = parent // only for doubly-linked tree-nodes (implement STreeNode & DTreeNode)
        }

        dfs() { // Self-DFS, so check child nodes before using them
            // pre-order
            console.log(this.value)
            if (!!this.left) this.left.dfs()
            if (!!this.right) this.right.dfs()
            // in-order
            if (!!this.left) this.left.dfs()
            console.log(this.value)
            if (!!this.right) this.right.dfs()
            // post-order
            if (!!this.left) this.left.dfs()
            if (!!this.right) this.right.dfs()
            console.log(this.value)
        }

        bfs() { // Self-BFS // todo: test out working with an inner queue (inside the recursion)
            console.log(this.value)
            let queue = [this.left, this.right]
            // wrong logic - push 'this' node as starting node
            // then continue with Tree iteration (not recursion) logic
        }

        bfs() { // Self-BFS - correct logic
            let queue = [this], node = null
            while (queue.length) { // same as (queue.length > 0)
                node = queue.shift() // pop out 1st FIFO node
                console.log(node.value)
                if (node.left) queue.push(node.left)
                if (node.right) queue.push(node.right)
            }
        }

    }

    constructor(root=null, tail=null) {
        this.root = root
        this.tail = tail
    }

}

function isSameTree(t1, t2) { // O(n1 + n2 ~ n) t (n - if trees are same); O(1) s

    // traverse both trees simultaneously (with b/c/d-fs) and compare current node values at each iteration
    
    if (!t1 || !t2 || !t1.root || !t2.root) return false
    let n1 = t1.root, n2 = t2.root
    if (n1.value !== n2.value) return false

    // BFS

    q1 = q2 = []
    q1.push(n1); q2.push(n2)

    while ((q1.length > 0) && (q2.length > 0)) {
        // n1 = q1.pop(0); n2 = q2.pop(0) // todo: .pop(takes no arguments) - .pop() always removes last item
        n1 = q1.shift(); n2 = q2.shift()
        if (n1.value !== n2.value) return false

        // assuming t1 & t2 are not binary trees
        // all nodes have 1 or multiple (2+) children
        if (!n1.children && !n2.children) break
        if (n1.children.length !== n2.children.length) return false

        for (let i = 0; i < n1.children.length; i++) {
            if (n1.children[i].value !== n2.children[i].value)
                return false
            q1.push(n1.children[i]); q2.push(n2.children[i])
        }

        /*
        // in-case they were binary trees, enqueue both .left & .right of both nodes
        // you can also check .left and .right for both nodes, before enqueueing
        q1.push(n1.left); q1.push(n1.right)
        q2.push(n2.left); q2.push(n2.right)
        */
    }

    return true
}

// 3rd-Party (Tutorial) Logic - Leetcode #100
function isSameTree(t1, t2) { // O(n1 + n2 ~ n) t (n - if trees are same); O(1) s
    let same = true

    function checkNodes(n1, n2) {
        if (!n1 && !n2) return
        else if (
            !n1 || !n2 ||
            n1.value !== n2.value
        ) {
            same = false
            return
        }
        checkNodes(n1.left, n2.left)
        checkNodes(n1.right, n2.right)
    }

    checkNodes(t1.root, t2.root)
    return same
}

// Binary (Search) Trees

class BTree extends Tree {

    constructor() {
        // TODO:
    }

    // Next 2 methods' logic work best for Binary Trees (NOT Binary SEARCH Trees)

    getMinValue() {
        if (!this.root) return null
        let min = Number.MAX_VALUE

        let cb = (n) => {
            if (n.value < min) min = n.value
        }

        this.dfs(this.root, cb)

        return min
    }

    getMaxValue() {
        if (!this.root) return null
        let max = 0

        let cb = (n) => {
            if (n.value > max) max = n.value
        }

        this.dfs(this.root, cb)

        return max
    }

}

class BST extends Tree {

    constructor(head=null, tail=null) {
        super(head, tail)
    }

    createNode(value=null, left=null, right=null) {
        return new Tree.TreeNode(value, left, right)
    }

    print() {
        console.log(this)
    }

    contains(v) {
        if (!this.root) return false
        let contains = false

        // use inner variable function here, or a outer .dfs(cb) method with a callback
        const dfs = (n) => {
            if (!n) return

            if (n.value == v) {
                contains = true
                return
            }
            dfs(n.left)
            dfs(n.right)
        }

        dfs(this.root)
        return contains
    }

    insert(v) {
        const node = new Tree.TreeNode(v)
        if (!this.root) {
            this.root = this.tail = node
            return this
        }

        // * Code (Value) - 1st (Binary) through BSTs only 
        // todo: Compare with .py (with callback)
        const cfs = (n) => {
            if (!n) return null

            if (n.value === v) {
                console.log(`Node(${v}) already exists`)
                return n
            } else if (!n.left && !n.right) { // leaf node
                if (n.value < v) {
                    node.parent = n
                    n.right = node

                    console.log(`Done with inserting Node(${v})`)
                    return this.root // return tree root node after insertion
                } else {
                    node.parent = n
                    n.left = node

                    console.log(`Done with inserting Node({v})`)
                    return this.root // return tree root node after insertion
                } // n.value == v already checked
            } else { // not leaf node, so recurse // todo: implement iteration version of cfs()
                if (n.value < v) return cfs(n.right)
                else return cfs(n.left)
                // n.value == v already checked
            }

        }

        return cfs(this.root) // can also insert node with callback (decouple cfs traversal from insertion - function's name)
        // todo: Compare with .py (with callback - for decoupled insertion logic)
    }

    cfs(root, v) {

        const iteration = (root, v) => {
            while (root != null && root.value != v) {
                v < root.value
                ? root = root.left
                : root = root.right
                // todo: if-ternary in-place of if-else
                /* // * longer syntax
                bool ? ( stmt, stmt, stmt ) : ( stmt, stmt, stmt )
                */
            }
            return root // Will be null if not found
        }
    
        const recursion = (root, v) => {
            if (root == null || root.value == v)
                return root
            
            return v < root.value
            ? search(root.left, v)
            : search(root.right, v)
        }
    
        console.log(iteration(root, v))
        console.log(recursion(root, v))
        
    }

    dfs() {
        return this.dfs(this.root)
    }

    dfs(n, cb=null) { // use as a helper method to dfs() override
        // cannot access this.root via named param value (dfs(n=this.root))
        // todo: try that option if/when .js feature is out
        if (!n) return

        // pre-order (check .py for others)
        if (!!cb) cb(n)
        else console.log(n.value)
        this.dfs(n.left, cb)
        this.dfs(n.right, cb)
    }

    bfs() { // todo: goto class TreeNode .bfs (Self-BFS)
        // push this Tree's root node first
        let q = [this.root], n = null
        while (q.length) {
            n = q.shift()
            console.log(n.value)
            if (n.left) q.push(n.left)
            if (n.right) q.push(n.right)
        }
    }

    // TODO: No need to check for min/max values with dfs (like in Binary Trees)
    getMinValue() {
        if (!this.root) return null
        if (this.left) return this.left.getMinValue()
        else return this.value
    }
    // For Binary SEARCH Trees, just depth-first straight to the left (for min) or right (max)
    getMaxValue() {
        if (!this.root) return null
        if (this.right) return this.right.getMaxValue()
        else return this.value
    }

}

BST.prototype.anotherMethod = () => {} // also possible with class BST {} syntax


function BST2(v) { // this time, BST2 class is a TreeNode itself
    this.value = v
    this.left = null
    this.right = null
}

BST2.prototype.print = () => console.log(this)

// todo: 3rd-Party (Tutorial) Logic

BST2.prototype.insert = (v) => {
    if (v === this.value)
        console.log(`Node(${v}) already exists`)
    else if (v < this.value) {
        if (!this.left) this.left = new BST(v)
        else this.left.insert(v)
    } else { // v > this.value
        if (!this.right) this.right = new BST(v)
        else this.right.insert(v)
    }
}

BST2.prototype.contains = (v) => {
    if (v === this.value) return true
    else if (v < this.value) {
        if (!this.left) return false
        else return this.left.contains(v)
    } else {
        if (!this.right) return false
        else return this.right.contains(v)
    }
}

BST2.prototype.dfs = () => {
    if (this.left) this.left.dfs()
    console.log(this.value) // in-order
    if (this.right) this.right.dfs()
}

BST2.prototype.dfs = (order) => {

    if (order === 'pre-order')
        console.log(this.value)

    if (this.left) this.left.dfs(order)

    if (order === 'in-order')
        console.log(this.value)

    if (this.right) this.right.dfs(order)

    if (order === 'post-order')
        console.log(this.value)

    // split-up if-checks (instead of singular switch) is fine
    // order will never be 2 different enums at the same time
}

BST2.prototype.bfs = () => {
    let queue = [this], node = null
    while (queue.length) { // same as (queue.length > 0)
        node = queue.shift() // pop out 1st FIFO node
        console.log(node.value)
        if (node.left) queue.push(node.left)
        if (node.right) queue.push(node.right)
    }
}

BST2.prototype.getMinValue = () => {
    if (this.left) return this.left.getMinVal()
    else return this.value
}

BST2.prototype.getMaxValue = () => {
    if (this.right) return this.right.getMaxVal()
    else return this.value
}

// todo: End of 3rd-Party (Tutorial) Logic

/* // TODO: Test

var bst = new BST2(10) // or BST(10)

bst.insert(20)
bst.insert(30)
bst.print()
bst.contains(20)

bst.dfs()
bst.dfs('in-order')
bst.bfs()

bst.getMinValue()
bst.getMaxValue()

*/

function isValidBST(tree) { // O(n) t ; O(1) s

    // traverse tree while current node is always max to left-side and min to right-side

    let root = tree.root
    let minmax = root.value

    let checkBST = (node) => {
        if (!node) return true
        if (node.left) {
            if (
                node.left.value > node.value
                || node.left.value > minmax
            ) return false
            minmax = node.value
            node = node.left
            checkBST(node)
        }
        if (node.right) {
            if (
                node.right.value < node.value
                || node.right.value < minmax
            ) return false
            minmax = node.value
            node = node.right
            checkBST(node)
        }
    }

    let res = true
    res = checkBST(root)

    return res
}

// 3rd-Party (Tutorial) Logic - Leetcode #98
function isValidBST(root) { // O(n) t ; O(1) s
    let valid = true

    function helper(node, min, max) {
        if (!node) return
        if (
            (min !== null && node.value <= min) ||
            (max !== null && node.value >= max)
        ) {
            valid = false
            return
        }
        helper(node.left, min, node.value)
        helper(node.right, node.value, max)
    }
    helper(root, null, null)
    return valid
}

function levelOrder(tree) { // O(n) t ; O(1) s
    let root = tree.root
    let queue = arr = [root]
    let order = [arr]

    // bfs traversal with queue in while loop
    while (queue.length > 0) { // (queue.length) - enough for this specific bool check (Boolean(queue.length) is false)
        // node = queue.pop(0) // todo: .pop(takes no arguments) - .pop() always removes last item
        node = queue.shift()
        arr.push(node.value)
        if (node.left) queue.push(node.left)
        if (node.right) queue.push(node.right)
        // hack-check - only works because tree is binary 
        // (only 2 children - left & right)
        if (arr.length == 2) {
            order.push(arr)
            arr = []
        }
    }

    return order
}

// 3rd-Party (Tutorial) Logic - Leetcode #102
function levelOrder(root) { // O(n) t ; O(1) s
    const res = []

    // dfs traversal with recursion
    function helper(node, depth) {
        if (!node) return
        if (!res[depth]) res[depth] = []
        res[depth].push(node.value)
        helper(node.left, depth + 1)
        helper(node.right, depth + 1)
    }

    helper(root, 0)

    return res
}

function maximumDepth(tree) { // O(n) t ; O(1) s
    if (!tree || !tree.root) return null
    let root = tree.root, d = 0

    function helper(node) {
        if (
            !node ||
            (!node.left && !node.right)
        ) return
        else {
            helper(node.left)
            helper(node.right)
            d++ // todo: test incrementing depth without argument separation
        }
    }

    helper(root)
    return d
}

// 3rd-Party (Tutorial) Logic - Leetcode #104
function maximumDepth(root) { // O(n) t ; O(1) s
    let maxD = 0

    function helper(node, d) {
        if (!node) {
            maxD = Math.max(d - 1, maxD)
            return
        }
        helper(node.left, d + 1)
        helper(node.right, d + 1)
    }

    helper(root, 1)
    return maxD
}

function invertBinaryTree(tree) { // O(n) t ; O(1) s
    if (!tree || !tree.root) return tree

    let root = tree.root, tmp = null

    // can use dfs, and invert .left & .right on every node
    function helper(node) {
        if (!node) return // todo: don't forget base-case in dfs helper recursive function
        tmp = node.left
        node.left = node.right
        node.right = tmp
        helper(node.right)
        helper(node.left)
        // you can still recurse into new .left before new .right
    }
    helper(root)

    // can also use bfs, and invert on every node, before enqueueing
    q = [root]
    while (q.length > 0) {
        node = q.shift() // * not .pop() - takes no params, and returns last item only
        tmp = node.left
        node.left = node.right
        node.right = tmp
        if (node.right) q.push(node.right)
        if (node.left) q.push(node.left)
        // you can still enqueue new .left before new .right
    }
}

// 3rd-Party (Tutorial) Logic - Leetcode #226
function invertBinaryTree(root) { // O(n) t ; O(1) s

    function helper(node) {
        if (!node) return
        let tmp = node.left
        node.left = node.right
        node.right = tmp
        helper(node.left)
        helper(node.right)
    }

    helper(root)
    return root
}

function leastCommonAncestorOfBST(tree, n1, n2) { // O(n) t ; O(1) s
    // find branch node to finding n1 & n2 in tree
    // todo
}

// 3rd-Party (Tutorial) Logic - Leetcode #235
function leastCommonAncestorOfBST(root, n1, n2) { // O(n) t ; O(1) s

    let v1 = n1.value, v2 = n2.value, v
    let node = root // for traversal

    while (node) {
        v = node.value
        if (v < v1 && v < v2)
            node = node.right
        else if (v > v1 && v > v2)
            node = node.left
        else return node // LCA - Lowest Common Ancestor
    }

    return null
}

// Tries

// Graphs

function numberOfIslands(graph) {
    // TODO:
}

// 3rd-Party (Tutorial) Logic - Leetcode #200
function numberOfIslands(grid) { // O(n) / O(m * n) t ; O(1) s (n - num cells of square matrix | m * n - height & width of matrix)
    // island - land surrounded by water
    // cell values: 1 - land ; 0 - water
    // island - 1s surrounded by 0s in graph adjacency matrix

    let count = 0

    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] === '1') {
                count++
                sinkIslandWithDFS(grid, row, col)
            }
        }
    }
    
    function sinkIslandWithDFS(grid, row, col) {
        // sink island - convert land - 1 and surrounding 1s to 0 - water
        
        if ( // return if cell indices are out of bounds
            row < 0 || row >= grid.length || 
            col < 0 || col >= grid[0].length ||
            grid[row][col] === '0' // or on water (1 - land, 0 - water)
        ) return
    
        grid[row][col] = '0'
        sinkIslandWithDFS(grid, row - 1, col)
        sinkIslandWithDFS(grid, row + 1, col)
        sinkIslandWithDFS(grid, row, col - 1)
        sinkIslandWithDFS(grid, row, col + 1)
    }
    
    return count
}

// Bits


/* // TODO: Create classes:

class DynamicProgramming

class DivideAndConquer

class Greedy

class BackTracking

class SystemDesign

class Mathematical

class Geometric

class PatternSearching

*/

class Recursion {

    constructor() {}

    factorial(num) { // O(n) t [not O(n!)]
        if (num === 1) return num
        else return num * factorial(num - 1)
    }

    fibonacci(num) {

    }

}

/* // TODO: Create classes:

class Bitwise

class Randomized

class Hashing

class Compression

class Encryption

class BranchAndBound

class MachineLearning

class DeepLearning

class NaturalLanguageProcessing

class Genetic

class MultiThreading

class Games

class Quant

*/



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
    // TODO:
}


// Trees

// Graphs



////////////////////////////////////////
// LEETCODE
////////////////////////////////////////

// 



////////////////////////////////////////
//  CODESIGNAL
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


/*

* // TODO: EcmaScript (Latest - ?)

strings - "" | chars - '' - forced in most others

*/




/*

* // TODO: WebStorm



* // TODO: WebStorm - Config



* // TODO: WebStorm - Issues



* // TODO: Express - Notes



* // TODO: Express - Config



* // TODO: Express - Issues



* // TODO: Express - Main



* Libraries - 

* Classes - 

* 'Language' Classes - 

* 3rd-Party Classes - 

* Special Data-Types - 

* Directives / Annotations - 

* Functions - 

* Methods - 

* Enumerations - 






* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes





* enum / switch cases for generics-validations






* // TODO: Hapi, NestJS, AdonisJS, FeathersJS, ..

*/






/*

* // TODO: WebStorm



* // TODO: WebStorm - Config



* // TODO: WebStorm - Issues



* // TODO: Web - Js - Notes



* // TODO: Js-Ts - Config



* // TODO: Js-Ts - Issues



* // TODO: Js-Ts - Main


* Libraries - 

* Classes - 

* 'Language' Classes - 

* 3rd-Party Classes - 

* Special Data-Types - 

* Functions - 

* Methods - 

* Containers - 

* Components - 

* Shapes - 

* Props - 

* Styles - 

* Animations - 

* Gestures - 

* Event Handlers - 

* Enumerations - 






* Specific Component-Prop-Enum Combos - 






* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes





* enum / switch cases for generics-validations




*/