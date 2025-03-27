'use strict';

// * install globally
import * as R from 'ramda'
import * as RA from 'ramda-adjunct'

const fs = require('fs')
const path = require('path')

/* // TODO: To-Use

Generics
lodash/fp, ramda, immutable.js
..

*/


/*
* // TODO:

Test all files' Algo's - Correctness, Speed / Execution Time, Uniqueness
Re-assess all algos' Big Omega (Best-Case / Lower-Bound) & Big Theta (Average-Case / Tight-Bound) - Time & Space Complexities
Compare all cases with stated Big O (Worst-Case / Upper-Bound) - Time & Space Complexities alike

* // TODO: Real-World Applications

- most/all in-app data should come from expected sources (in-house / 3rd apis / device-data)
    - extra data comes from unnecessarily (wastage) created vars, args, 'enums' (for generics), etc
    - if extra data is actually required, coz it's generated from already existing (& required) data, allowed
    - if algo's are leveraged for generating extra (but reqiured) data from already existing & required data, optimize O(t) & O(s)
    - in both Big-O (worst-case - upper bound) & Big-Theta (best-case - lower bound), or Big-Omega (average-case - tight bound)
    - BUT: NO unnecessarily (wastage) created vars, args, 'enums' (for generics), etc 


*/


////////////////////////////////////////
//  UTIL FUNCTIONS - Functional, ... 
////////////////////////////////////////

var Functions = {

    // main functions

    sortBaseCheck: (a) => {
        return [0, 1].includes(a.length)
    },
    
    swap: (a, b) => {
        let t = a; a = b; b = t
        // (a, b) = (b, a) // faster, but () by value
        return (a, b)
    },
    
    compare: (a, b) => {
        return a < b
    },
    
    sort: a => {
    
        a.sort((a, b) => a - b); // O(n log n) t // sort in-place
        // compare func - for int arrays only
        // -ve - a before b (a < b) - ascending order
        // +ve - b before a (a > b) - descending order
        // 0 - a & b (equal) - adjacent items
    
        // can also return +/-ve 1 / 0 based on a </> b - longer (wrong) implementation
        a.sort((a, b) => a < b ? -1 : a > b ? 1 : 0)
    
        // sort in descending order
        a.sort((a, b) => b - a) // if a < b, b - a -> +ve, so b still before a - descending order
        a.sort((a, b) => a < b ? 1 : a > b ? -1 : 0) // return opposite +/-ve number values
    
        // or - .sort() - without compare func for strings & chars (alphabetical order) only 
        // NB - .toSorted() - returns copy
    
        // * NB: sorting array before proceeding also affects indices (in-case actual array's item's index is required)
        // * undefined array-items placed at end of sorted array
    
        return a
    },
    
    searchBaseCheck: fn => R.ifElse(
        R.isEmpty, // fn should have an array arg
        R.always(null), // null if array is empty
        fn // returned as a functor to then exec with array
    ),

    check: R.curry((c, a, b) => {
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
    }),

    compareNums: (s, a, b) => {

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
        s.split('') // .map() returns new array with updated items
            .forEach(c => { // forEach doesn't return new array; exec's cb on each item, but not updating them in-place
                res.push(
                    check(c)
                )
            })
        
        return R.isNotEmpty(res) // * never wrap return's next syntax elem (in return value) to next line
            && R.includes(true, res)
        
    },

    while: (predicate, transformer, initialValue) => {
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
    },

    // other functions


}


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

    Sorting.prototype.sort = a => {

        a.sort((a, b) => a - b); // O(n log n) t // sort in-place
        // compare func - for int arrays only
        // -ve - a before b (a < b) - ascending order
        // +ve - b before a (a > b) - descending order
        // 0 - a & b (equal) - adjacent items

        // can also return +/-ve 1 / 0 based on a </> b - longer (wrong) implementation
        a.sort((a, b) => a < b ? -1 : a > b ? 1 : 0)

        // sort in descending order
        a.sort((a, b) => b - a) // if a < b, b - a -> +ve, so b still before a - descending order
        a.sort((a, b) => a < b ? 1 : a > b ? -1 : 0) // return opposite +/-ve number values

        // or - .sort() - without compare func for strings & chars (alphabetical order) only 
        // NB - .toSorted() - returns copy

        // * NB: sorting array before proceeding also affects indices (in-case actual array's item's index is required)
        // * undefined array-items placed at end of sorted array

        return a
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
        fn // returned as a functor to then exec with array
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
        s.split('') // .map() returns new array with updated items
            .forEach(c => { // forEach doesn't return new array; exec's cb on each item, but not updating them in-place
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
        // compare func - for int arrays only
        // -ve - a before b (a < b) - ascending order
        // +ve - b before a (a > b) - descending order
        // 0 - a & b (equal) - adjacent items

        // can also return +/-ve 1 / 0 based on a </> b - longer (wrong) implementation
        a.sort((a, b) => a < b ? -1 : a > b ? 1 : 0)

        // sort in descending order
        a.sort((a, b) => b - a) // if a < b, b - a -> +ve, so b still before a - descending order
        a.sort((a, b) => a < b ? 1 : a > b ? -1 : 0) // return opposite +/-ve number values

        // or - .sort() - without compare func for strings & chars (alphabetical order) only 
        // NB - .toSorted() - returns copy

        // * NB: sorting array before proceeding also affects indices (in-case actual array's item's index is required)
        // * undefined array-items placed at end of sorted array

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
            const m = Math.floor(f + (l - f) / 2) // better than (index-wise for edge-cases) - (f + l) / 2 - eg. (5 + 10) / 2 -> 15 / 2 -> 7.5
            // ! difference (l - f) halved (/ 2) is the mid-length + start-index 'f' - eg. 5 + (10 - 5) / 2 -> 5 + 5/2 -> 5 + 2.5 -> 7.5
            // * (NB: pemdas / bodmas - division always before addition)
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
            m = Math.floor(f + (l - f) / 2)
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


// Arrays O(?) - access - O(1), lookup/search - O(1 ~ n), append - O(1 ~ n), insert - O(1 ~ n), delete - O(1 ~ n), copy - O(n), 
// * resize operation - O(n) t - when array gets full, its size in RAM, doubled and in new memory, is allocated
// then array's items are copied from old memory to new memory, hence O(n) t (bottleneck)
// most operations become O(n) in worst-case, if resize operation must take place 1st

// .shift/unshift - O(n), .splice - O(n/2 ~ n),  ... 


// [] - []
new Array(5) // [ <50 empty items> ]
new Array(5).fill(0) // [ 0, 0, 0, 0, 0 ]
new Array('5') // [ '5' ]
new Array(1, 2, 'three', 4, 'five') // [ 1, 2, 'three', 4, 'five' ]
new Array([1, 2, 3, 4, 5]) // [ [1, 2, 3, 4, 5] ]
Array.from(() => { /* iterator */ }) // todo


class SampleArray {

    constructor() {
        this.length = 0
        this.data = {}
    }

    get = index => this.data[index]
    
    push = item => (
        this.data[this.length] = item,
        ++this.length // * increment before returning
    )

    pop() {
        const lastItem = this.data[this.length - 1]
        delete this.data[this.length - 1]
        return lastItem
    }

    delete(index) {
        const item = this.data[index]
        this.shiftItems(index)
        return item
    }

    shiftItems(index) {
        for (let i = index; i < this.length - 1; i++)
            this.data[i] = this.data[i + 1]
        delete this.data[this.length - 1]
        this.length--
    }

    /* // TODO: Setup Babel - TypeScript plugin - pipeline operator

    pop = () => (
        this.data[this.length - 1]
        // |> delete % // TODO: Confirm if % in this case is 'piped' by copy or by reference
        |> (
            delete this.data[this.length - 1],
            this.length--,
            %
        ) // TODO: Confirm if piped 1-liner returns last statement value in function-scope
    )

    delete = index => (
        this.data[index]
        |> (
            this.shiftItems(index),
            %
        )
    )
    shiftItems = index => (
        Array(this.length - 1).fill(0)
            .forEach((_, i) => ( // todo: set starting 'index'; before this works
                this.data[i] = this.data[i + 1],
            )),
        delete this.data[this.length - 1],
        --this.length
    )
    
    */

}


const arr = new SampleArray()
arr.push(1), arr.push(2), arr.push(3)
console.log(arr.get(1)) // 2
console.log(arr) // Outputs .data object
arr.pop(); arr.pop()
console.log(arr)
arr.push(4); arr.delete(0)
console.log(arr)


class ArraysStrings {

    constructor() {}

    static Arrays = class Arrays_ {

        arraySum = arr => arr.reduce((acc, curr) => acc + curr, 0)
        arrayProd = arr => arr.reduce((acc, curr) => acc * curr, 0)

        arrayAvg = arr => arr.reduce((acc, curr, i) => (acc + curr) / (arr.length - 1 === i ? arr.length : 1), 0)
        arrayAvg1 = arr =>
            arr.reduce((acc, curr, i) => (
                acc += curr,
                i === arr.length - 1
                ? acc / arr.length
                : acc
            ), 0)

        flatten2DarrayTo1DArray = arr => arr.reduce((acc, curr) => acc.concat(curr), []) // * accumulator initial value - []
        flatten2DArrayTo1DArray1 = arr => arr.reduce((acc, curr) => (curr.forEach(i => acc.push(i)), acc), [])
        // * reduce: [...acc, ...curr] - accumulative restructuring - slowest (worst) brute-force method of accumulation

        reverse = arr => arr.reverse()

        reverse = arr => { // O(n) t | O(1) s // ! wrong - array reversed at middle-index; beyond that array re-reversed back to original
            let tmp
            for (let i = 0; i < arr.length; i++) {
                tmp = arr[i]
                arr[i] = arr[arr.length - 1 - i]
                arr[arr.length - 1 - i] = tmp
            }
            return arr // reversed, then re-reversed again, in-place - stupid
        }

        reverse = arr => { // O(n/2 ~ n) t | O(1) s - reversed at middle index, after all 'extreme'd items have been swapped
            let tmp
            for (let i = 0; i < arr.length / 2; i++) { // stop iteration at middle-index
                tmp = arr[i]
                arr[i] = arr[arr.length - 1 - i]
                arr[arr.length - 1 - i] = tmp
            }
            return arr // reversed in-place
        }

        reverse = arr => (

            // TODO: foreach exec's lambda throughout array; but break required at middle-index
            // so iterate through arr's indices (with half length) instead

            arr
        )

        mergeSortedArrays = (a1, a2) => {
            if (!a1.length) return a2
            else if (!a2.length) return a1

            const arr = []
            let i1 = a1[0], i2 = a2[0]
            let i = 1, j = 1

            while (i1 || i2) {
                if (!i2 || i1 < i2) { // * check i2 only == undefined, since it has the base-case
                    arr.push(i1)
                    i1 = a1[i]
                    i++
                } else {
                    arr.push(i2)
                    i2 = a2[j]
                    j++
                }
            }

            return arr
        }

        /*

        mergeSortedArrays1 = (
            a1, a2,
            [i1, i2] = []
        ) => (
            !a1.length ? a2
            : a2.length ? a1
            : (
                [i1, i2] = [a1[0], a2[0]],
                [i, j] = [1, 1],
                []
                |> (
                    Functions.while(
                        ({i1, i2}) => i1 || i1,
                        ({i1, i2}) =>
                            (!i2 || i1 < i2)
                            ? (
                                %.push(i1),
                                i1 = a1[i],
                                i++
                            ) : (
                                %.push(i2),
                                i2 = a2[j],
                                j++
                            ),
                        {i1, i2}
                    ),
                    %
                )
            )
        )

        */

        /** // ! Two-Sum / Pairs with Sum - LC #1
         *
         * eg. Given an array of integers, return all pairs that add up to a target
         * sometimes array may have only distinct (non-repeating) integers, or target may be 0 (so there'll be -ve integers)
         *
         * eg. find 2 numbers in an array of integers that add up to a target sum
         *
         * Constraints:
         *      - can be that all numbers < target sum; or not; or target may be 0
         *      - can be that array has only distinct or non-repeating elements; or not
         *      - can be that there's only 1 solution
         *      - can also be that there are multiple solutions, so return them all as an array
         *      - can be that the same element cannot be used 2x
         *      - can also be that the same element can be used 2x
         *      - ... ?
         *
         * Solns:
         *      - using hashmaps / hashtables - O(n) t ; O(n) s
         *      - using 2-pointer algo - O(n/? ~ n) t ; O(1) s
         *
         */

        // using array itself - .js 'in' keyword
        twoSum = (a, t, [arr, d] = [[], 0]) => ( // O(n) t ; O(1) s

            a.forEach((n, i, [i2] = []) => (
                d = t - n,
                d in a
                && ( // ! wrong here
                    // * in the case of t being twice current n
                    // * find index of another spot of the same number
                    // the first index found will always be this same current n's
                    //
                    // * Possible Solns: find a way to return all repetitions' indices ; reverse array 1st (will reverse all indices - wrong) ;
                    //
                    i2 = a.indexOf(d), // * Confirm O(n) or O(1) t ?
                    i2 === i // ! to make sure difference is not this iteration's exact same number (same index)
                    || arr.push([i, i2])
                )
            )),

            arr
        )

        // hashmap
        twoSum = (a, t, [m, arr] = [{}, []]) => ( // O(n) t ; O(n) s
            a.length < 2 ? null
            : (
                a.forEach((n, i, [d] = []) => (
                    d = t - n,
                    d in m && arr.push([m[d], i]),
                    n in m || (m[n] = i) // 'n in m' check only required if a doesn't have distinct elements (has repeating elements)
                )),
                arr
            )
        )

        /*
        // hashtable
        twoSum = (a, t, [m, arr] = [{}, []]) => ( // O(n) t ; O(n) s
            a.forEach(n => (
                a.length < 2 ? null
                : (
                    a.forEach((n, i, [d] = []) => (
                        d = t - n,
                        d in m && arr.push([m[d], i]),
                        n in a && _
                    ))
                )
            ))
        )
        */

        // 2-pointer - sorted array
        // * increase/decrease half-pair if less/greater than sum - only possibility for highest probability
        twoSum = (a, t) => { // O( n log n + n ) t ; O(1) s
            // ! NO 'n/2' t because both pointers do not iterate simultaneously
            // (they iterate 1 after the other, so each item is dealt with singly (iteration-wise) - even though both extremes are dealt with together)

            a.sort() // * should be sorted 1st - O(n log n) t

            let i = 0, j = a.length - 1
            let arr = [] // for the multiple pairs case

            let s
            while (i < j) {
                s = a[i] + a[j]
                s === t // both extremes add up to sum
                ? arr.push([i, j]) // * or: a[i], a[j]
                : s < t ? i++ // both extremes add up to less than sum; so a higher number is required (can only come from left-pointer's next (larger) item)
                : j-- // both extremes add up ot more than sum; so a lower number is required (can only come from right-pointer's next (smaller) item)
            }

            return arr
        }

        // LC #1 - hashmap (or array can help)
        twoSum = (a, s) => { // O(n) t ; O(1) s
            let m = {}, res = [], d
            for (let i = 0; i < a.length; i++) {
                d = s - a[i]
                if (d in m) // * or: m[d] !== undefined
                    res.push([i, m[d]])
                m[a[i]] = i // for distinct non-repeating values
            }
            (res)
        }

        // LC #1 - 2-pointer
        twoSum = (a, s) => { // O() t ; O() s

        }

        /** // ! 3-sum - LC #15
         *
         * Given an array of n integers, find 3 elements that sum up to 0 (or a target value)
         * Find all 'unique' triplets (no duplicates) in the array which sum up to 0
         *
         * Solution must not contain duplicate triplets (no triplet repetition either)
         *
         * Soln: sort array 1st
         * ! - 3-pointer iteration
         *  - main / base-pointer iteration through entire array
         *  - 2-pointer - left-pointer a step ahead (index i0 + 1) of the base-pointer (i0) & right-pointer at end of array
         *
         */

        threeSum = (
            nums, sum = 0,
            [arr, i, j, d, s, exec] = [[]]
        ) => (
            // O( n log n + (n(n/2) ~ n^2) ~ n^2 [getting rid of smaller (nlogn) term, if you have to manually sort array 1st, else n^2 by default] ) t ; O(1) s

            nums.sort((a, b) => a - b),
            j = nums.length - 1,

            nums.forEach((n, i0) => (
                i = i0 + 1, // ! Always put 1st-pointer a step ahead of the base-pointer
                // ! all permutational-combo's of the previous base-pointer were catered for in the previous base-iteration

                // ! ONLY way to prevent duplicate triplets
                // * (test before res.push way's wrong - .pushed triplets may be in different orders ; & array objects are id'd by reference (so find how to check array-equality by values)
                (i0 > 0 && nums[i0] === nums[i0 - 1])
                ? null // ! continue (return 'null') if current base-pointer === previous base-pointer
                : (
                    d = sum - n,

                    exec = ({i, j}) => (
                        s = nums[i] + nums[j],
                        s === d
                        ? (
                            // ! (this way's wrong - .pushed triplets may be in different orders ; & array objects are id'd by reference (so find how to check array-equality by values)
                            // [i0, i, j] in res || res.push([i0, i, j]), // ! in the case soln must not contain any duplicate triplets
                            arr.push([i0, i, j]), // ! or, with indexed numbers: [n, nums[i], nums[j]]
                            i++, // ! even after a successful find, continue iteration towards higher values
                            
                            // ! after moving left-pointer up, keep jumping it up until a non-duplicate number
                            // * to avoid duplicates in future triplets
                            // * consider this constant time (or even speeding up outer-loop)
                            Functions.while(
                                () => nums[i] === nums[i - 1],
                                () => i++,
                                null
                            )
                            
                        ) : s < d
                        ? i++ // iterate towards higher values (left-pointer iterating up)
                        : j-- // iterate towards lower values (right-pointer iterating down)
                    ),

                    Functions.while(
                        ({i, j}) => i < j,
                        exec,
                        {i, j}
                    )
                )
            )),
            arr
        )

        // iterative - 2-pointer (2 pointers within an iteration)
        threeSum = (nums, sum = 0) => {
            // O( n log n + (n(n/2) ~ n^2) ~ n^2 [getting rid of smaller (nlogn) term, if you have to manually sort array 1st, else n^2 by default] ) t ; O(1) s

            nums.sort((a, b) => a - b)
            let i, j = nums.length - 1, res = []
            nums.forEach((n, i0) => {
                i = i0 + 1 // ! Always put 1st-pointer a step ahead of the base-pointer
                // ! all permutational-combo's of the previous base-pointer were catered for in the previous base-iteration

                // ! ONLY way to prevent duplicate triplets
                // * (test before res.push way's wrong - .pushed triplets may be in different orders ; & array objects are id'd by reference (so find how to check array-equality by values)
                if (i0 > 0 && nums[i0] === nums[i0 - 1]) return
                // ! continue (return 'null') if current base-pointer === previous base-pointer

                let d = sum - n, s
                while (i < j) {
                    s = nums[i] + nums[j]
                    s === d
                    ? (
                        // ! (this way's wrong - .pushed triplets may be in different orders ; & array objects are id'd by reference (so find how to check array-equality by values)
                        // [i0, i, j] in res || res.push([i0, i, j]), // ! in the case soln must not contain any duplicate triplets
                        res.push([i0, i, j]), // ! or, with indexed numbers: [n, nums[i], nums[j]]
                        i++, // ! even after a successful find, continue iteration towards higher values

                        // ! after moving left-pointer up, keep jumping it up until a non-duplicate number
                        // * to avoid duplicates in future triplets
                        // * consider this constant time (or even speeding up outer-loop)
                        Functions.while(
                            () => nums[i] === nums[i - 1],
                            () => i++,
                            null
                        )

                    ) : s < d
                    ? i++ // iterate towards higher values (left-pointer iterating up)
                    : j-- // iterate towards lower values (right-pointer iterating down)
                }
            })
            (res) // * return res // ! ensure babel-typescript plugin
        }

        // 3rd-Party (Tutorial) - LC #15
        threeSum = (nums, sum = 0) => { // O(n(n/2) ~ n^2) t ; O(1) s

            // nums.sort((a, b) => a - b) // ! in this case, assume already sorted array

            let res = []

            for (let i = 0; i < nums.length; i++) {
                const target = sum - nums[i]
                let left = i + 1, right = nums.length - 1

                // ! ONLY way to prevent duplicate triplets
                // * (above ways wrong - .pushed triplets may be in different orders ; & array objects are id'd by reference (so find how to check array-equality by values)
                if (i > 0 && nums[i] === nums[i - 1]) continue
                // ! continue if current base-pointer === previous base-pointer

                while (left < right) {
                    if (nums[left] + nums[right] === target) {
                        res.push([nums[i], nums[left], nums[right]])
                        left++

                        // ! after moving left-pointer up, keep jumping it up until a non-duplicate number
                        // * to avoid duplicates in future triplets
                        // * consider this constant time (or even speeding up outer-loop)
                        while (nums[left] === nums[left - 1]) left++

                    } else if (nums[left] + nums[right] < target)
                        left++
                    else right--
                }
            }

            (res)
        }

        /** // ! 4-sum - LC # ??
         *
         * * 4-pointer ?  2 base-pointers + 2 iterative-pointers ??
         *
         */

        fourSum = (nums, sum) => ( // O() t ; O() s
            null
        )

        // 
        fourSum = (nums, sum) => { // O() t ; O() s

        }

        // 3rd-Party (Tutorial) - LC # ??
        fourSum = (nums, sum) => { // O() t ; O() s

        }

        /** // ! Contains Duplicate - LC #217
         *
         */

        containsDuplicate = (nums, [m] = []) => ( // O(n/? ~ n) t ; O(n) s
            nums.forEach(n => (
                n in m // can use a hashmap / an extra array / input array itself, by removing this item before checking if still exists
                ? (true) // ! wrong-code: // TODO: break out of .forEach lambda to main function scope to return
                : m[n] = 1 // for arrays: arr.push(n)
            )),
            false
        )

        containsDuplicate = nums => ( // O(n) t ; O(1) s - no extra space used
            nums.forEach((n, i) => (
                delete nums[i], // 1st delete this 'n' (after working with it)
                n in m && (true) // ! wrong-code:
                // TODO: break out of .forEach lambda to main function scope to return
            )),
            false
        )
        
        /*        
        containsDuplicate = nums => (
            [] // or - {} (x in {})
            |> (
                nums.forEach(n => (
                    %.includes(n) // or - n in {}
                    ? (true) // todo: must break out of .forEach & return 'true'
                    : %.push(n) // or - {}[n] = n/1/true
                ))
            ),
            false
        )
         */

        containsDuplicate = nums => { // O(n) t ; O(n) s
            const ns = []
            for (let n of nums) {
                if (ns.includes(n))
                    return true // todo: (true) - test new Babel-TypeScript syntax
                else ns.push(n)
            }
            return false
        }

        containsDuplicate = nums => { // O(n) t ; O(1) s
            let n
            for (let i in nums) {
                n = nums[i]
                delete nums[i]
                if (n in nums) (true) // if n still exists
            }
            (false)
        }

        // 3rd-Party (Tutorial) - LC #217
        containsDuplicate = nums => { // O(n) t ; O(n) s
            const visitedNums = {}
            for (let i = 0; i < nums.length; i++) {
                const num = nums[i]
                if (visitedNums[num]) return true
                visitedNums[num] = true
            }
            return false
        }

        /**
            * Container with most water - LC #11

            Given n non-negative integers a1, a2, ... , an, where each rep's a point at coords (i, aj).
            n vertical lines are drawn such that the 2 endpoints of line i is at (i, aj) & (i, 0).
            Find 2 lines, which together with x-axis forms a container, such that the container contains the most water.

            * may not slant the container & n is at least 2
        */

        containerWithMostWater = (
            nums,
            [maxArea, i, j, exec] = []
        ) => ( // O(n) t ; O(1) s // ! NO 'n/2' t because both pointers do not iterate simultaneously
            // (they iterate 1 after the other, so each item is dealt with singly (iteration-wise) - even though both extremes are dealt with together)

            [i, j] = [0, nums.length - 1],

            exec = (
                {i, j},
                [area] = []
            ) => (
                area = Math.min(nums[i], nums[j]) * (j - i),
                maxArea = Math.max(maxArea, area),

                // ! iterate the lower height 1st; keep the higher height to maximize the contained area for the next iteration
                /*
                    * perhaps for 'area' reducing length (i -> j) will always reduce area
                    * so iteration will in no way increase area beyond what we already have at the moment
                    * even with a very high height in the next iteration (that could've boosted area),
                    * the lower height will still always be chosen (because of "area covered")
                    * so reducing length (i++ / j--) on iterating, will not help increase area
                    * so always iterate by the lower height (nums[i] < nums[j]),
                    * to keep the higher height for the next iteration's area vs maxArea test
                    * (in the case of this higher height being used (as the lower height) of the next iteration) - higher max-area probability
                */

                (nums[i] < nums[j])
                ? i++ : j--
            ),

            Functions.while(
                ({i, j}) => i < j,
                exec,
                {i, j}
            ),
            maxArea
        )

        containerWithMostWater_MaxArea = (heights, [max, i, j, exec] = []) => ( // O(n/2) t ; O(1) s
            [i, j] = [0, heights.length - 1],

            exec = ({i, j}, [area] = []) => (
                area = Math.min(
                    heights[i], heights[j]
                ) * (j - i),
                max = Math.max(max, area),
                (heights[i] < heights[j])
                ? i++ : j--
            ),
            Functions.while( // ! Recursive O(t) ?
                ({i, j}) => i < j,
                exec,
                {i, j}
            ),
            max
        )

        //
        containerWithMostWater = nums => { // O(n) t ; O(1) s

            let [i, j] = [0, nums.length - 1]
            let maxArea = 0, area

            while (i < j) {
                area = Math.min(nums[i], nums[j]) * (j - 1)
                maxArea = Math.max(maxArea, area)
                nums[i] < nums[j] ? i++ : j--
            }

            return maxArea
        }

        // 3rd-Party (Tutorial) - LC #11
        containerWithMostWater_MaxArea = heights => { // O(n/2) t ; O(1) s
            let [i, j] = [0, heights.length - 1]
            let max = 0

            while (i < j) {
                // ! constant / any var in loop's scope is gc'd at scope-end
                const area = Math.min( // minimum (pillar) height is maximum height containing water
                    heights[i], heights[j]
                ) * (j - i) // times maximum length - from i to j - [area = length * breadth]
                max = Math.max(max, area)
                // or - (area > max) && (max = area)
                // i < j ? i++ : j-- - // ! DO NOT shift by lower-index, but by lower height
                heights[i] < heights[j] // * shift by lower height
                ? i++ : j-- // ! correct 2-pointer shifting
            }

            return max
        }

        // 3rd-Party (Tutorial) - LC #11
        containerWithMostWater = nums => { // O(n) t ; O(1) s
            let i = 0, j = nums.length - 1
            let maxArea = 0, area

            while (i < j) {
                area = Math.min(nums[i], nums[j]) * (j - i)
                maxArea = Math.max(maxArea, area)
                nums[i] < nums[j] ? i++ : j--
            }

            (maxArea)
        }

        /** // ! Product of array Except Self - LC #238
         *
         * multiply all items, except current item, in array (both in-place & not in-place)
         *
         */

        // multiply all items, except current item, in array (not in-place)
        productOfArrayExceptSelf = (nums, [arr] = []) => ( // O(n^2) t ; O(n ~ 1) s (extra array not actually required for the algo itself; only holding reduced product-values)
            // * cannot .map in-place since same arr-items required for .reduced accumulated product
            nums.forEach((n, i) => (
                arr.push(
                    nums.reduce((acc, curr, j) => ( // O(n) t ? // ! can .reduce() be reduced from O(n) ~ O(1) t ? functional-programming math-wise ?
                            j === i
                            || (acc *= curr), // ! returning acc here happens before last self-product multiplication
                            acc // ! must still return acc after self-product accumulation
                        ), 1) // acc should start from 1 as an accumulated product
                        // (0 * 1st item still 0, so it's neglected)
                )
            )),
            arr
        )

        /*

        productOfArrayExceptSelf = nums => ( // O(n^2) t ; O(n ~ 1) s (extra array not actually required for the algo itself; only holding reduced product-values)
            []
            |> (
                // * cannot .map in-place since same arr-items required for .reduced accumulated product
                nums.forEach((n, i) => (
                    %.push(
                        nums.reduce((acc, x, j) => ( // O(n) t ? // ! can .reduce() be reduced from O(n) ~ O(1) t ? functional-programming math-wise ?
                            j === i
                            || (acc *= x),
                            acc
                        ), 1)
                    )
                )),
                %
            )
        )

        */

        // manual multiplication
        productOfArrayExceptSelf = (
            nums,
            [output, product] = []
        ) => ( // O(3n ~ n) t ; O(1) s
            output = nums.map(n => 1),
            product = 1,

            // multiply from left
            nums.forEach((n, i) => (
                output[i] *= product,
                product *= n
            )),

            product = 1,

            // multiply from right
            nums.reverse().forEach((n, i, [oldI] = []) => (
                oldI = nums.length - 1 - i, // reverse 'reversed-index' to (old) 'oldI' index
                output[oldI] *= product,
                product *= n
            )),

            output
        )

        // manual multiplication
        productOfArrayExceptSelf = nums => { // O(3n ~ n) t ; O(1) s
            let output = nums.map(n => 1),
                product = 1
            // multiply from left
            for (let i in nums) {
                output[i] *= product
                product *= nums[i]
            }
            product = 1
            // multiply from right
            for (let i = nums.length - 1; i >= 0; i--) {
                output[i] *= product
                product *= nums[i]
            }
            (output)
        }

        // * 3rd-Party (Tutorial) - LC #238
        productOfArrayExceptSelf = nums => { // O(3n ~ n) t ; O(1) s [my chosen option] ? O(n) s ['output' array as 'extra space' - No] ?
            let output = nums.map(n => 1) // O(n) t ; // ! still O(1) s argument ? even with array space doubled with 'newly-returned' 'output' array
            let product = 1

            // multiply from left
            for (let i = 0; i < nums.length; i++) { // O(n)
                output[i] *= product // ! newly returned array (by computation) still only accessed by constant time - O(1) t
                product *= nums[i] // * both arrays iterated through in the same O(n) time ..
                /*
                    but same constant time to access from 'output' array, with NO linear time to push/pop to/from it ..
                    while no linear time computation with 'output' based on 'nums' computation, should maintain stable space-complexity ?
                    TODO: Confirm - "The 'output' array does not count as "EXTRA SPACE" for the purpose of space-complexity analysis"
                */
            }

            product = 1

            // multiply from right
            for (let j = nums.length - 1; j >= 0; j--) { // O(n)
                output[j] *= product // * same relationship in computation between 'output' & 'nums' arrays here
                product *= nums[j]
            }

            return output
        }

        // 3rd-Party (Tutorial) - LC #238
        productOfArrayExceptSelf = nums => { // O(3n ~ n) t ; O(1) s

            let output = nums.map(n => 1)
            let product = 1

            // multiply from left
            for (let i = 0; i < nums.length; i++) {
                output[i] = output[i] * product
                product = product * nums[i]
            }

            product = 1

            // multiply from right
            for (let i = nums.length - 1; i >= 0; i--) {
                output[i] = output[i] * product
                product = product * nums[i]
            }

            (output)
        }

        /** // ! Maximum Sub-Array - LC #53
         *
         * like 'House Robber' - Dynamic Programming problem
         *
         * max sub-array sum - sub-array with the maximum sum
         * only adjacent sub-array items
         *
         * can use a Dynamic Programming 'extra' array
         * or can transform the input array into the DP array itself
         *
         */

        maximumSubArray = (
            nums,
            [dpArr, max] = []
        ) => ( // O(n) t ; O(n) s
            max = nums[0],
            dpArr = [max],
            nums.forEach((num, i) => (
                i === 0 // skip 1st iteration - but wrong syntax for algo; for unnecessary check on each iteration
                || (
                    dpArr[i] = Math.max(num, num + dpArr[i - 1]),
                    max = Math.max(max, dpArr[i])
                )
            )),
            max
        )

        maximumSubArray = nums => { // O(n) t ; O(n) s
            let max = nums[0]
            let dpArr = [max]

            nums.forEach((num, i) => (
                i === 0 // skip 1st iteration - but wrong syntax for algo; for unnecessary check on each iteration
                || (
                    dpArr[i] = Math.max(num, num + dpArr[i - 1]),
                    max = Math.max(max, dpArr[i])
                )
            ))

            (max)
        }

        // this time - transforming the input array-arg into the dp-array itself
        maximumSubArray = (
            nums,
            [max] = []
        ) => ( // O(n) t ; O(1) s
            // O(1) s this time - by transforming the input array-arg into the dp-array itself
            max = nums[0],
            nums.forEach((num, i) => (
                i === 0
                || (
                    nums[i] = Math.max(num, num + nums[i - 1]),
                    max = Math.max(max, nums[i])
                )
            )),
            max
        )

        // this time - transforming the input array-arg into the dp-array itself
        maximumSubArray = nums => { // O(n) t ; O(1) s
            // O(1) s this time - by transforming the input array-arg into the dp-array itself
            let max = nums[0], num
            for (let i = 1; i < nums.length; i++) {
                num = nums[i]
                nums[i] = Math.max(num, num + nums[i - 1])
                max = Math.max(max, nums[i])
            }
            (max)
        }

        // 3rd-Party (Tutorial) - LC #53 - using extra array - DP
        maximumSubArray = nums => { // O(n) t ; O(n) s
            let max = nums[0]
            let dpArr = [max], num

            for (let i = 1; i < nums.length; i++) {
                num = nums[i]
                dpArr[i] = Math.max(num, num + dpArr[i - 1])
                max = Math.max(max, dpArr[i])
            }

            (max)
        }

        // 3rd-Party (Tutorial) - LC #53 - transforming input array
        maximumSubArray = nums => { // O(n) t ; O(1) s
            // O(1) s this time - by transforming the input array-arg into the dp-array itself
            let max = nums[0]
            let num

            for (let i = 1; i < nums.length; i++) {
                num = nums[i]
                nums[i] = Math.max(num, num + nums[i - 1])
                max = Math.max(max, nums[i])
            }

            (max)
        }

        // TODO: Test
        /** // ! Maximum Product Sub-Array - LC #152
         *
         * max sub-array product - sub-array with the maximum product
         * only adjacent sub-array items
         *
         * can use a Dynamic Programming 'extra' array
         * or can transform the input array into the DP array itself
         *
         */

        /** // ! WRONG replication (sum -> product)
         * - whether using DP array / transforming the input array-arg into the dp-array itself

         maximumProductSubArray = nums => { // O() t ; O(1) s

            // using DP array

            let maxProduct = nums[0]
            let dpArr = [maxProduct]

            nums.forEach((n, i) => (
                dpArr[i] = Math.max(n, n * nums[i - 1]),
                maxProduct = Math.max(maxProduct, dpArr[i])
            ))

            // transforming input array

            let maxProduct = nums[0], product

            for (let i in nums) {
                product = Math.max(nums[i], nums[i] * nums[i - 1])
                maxProduct = Math.max(maxProduct, product)
            }

            return maxProduct
         }

         */

        // using an extra DP arrays
        maximumProductSubArray = (
            nums,
            [maxProduct, maxTillIndex, minTillIndex] = []
        ) => ( // O(n) t ; O(2n ~ n) s
            maxProduct = nums[0],
            maxTillIndex = [maxProduct], // * don't use double assignment to both ([max] array assigned by reference)
            minTillIndex = [maxProduct],
            nums.forEach((num, i) => (
                i === 0 ||
                (
                    // ! ??
                    maxTillIndex[i] = Math.max(
                        num,
                        num * maxTillIndex[i - 1],
                        num * minTillIndex[i - 1]
                    ),

                    // ! ??
                    minTillIndex[i] = Math.min(
                        num,
                        num * maxTillIndex[i - 1],
                        num * minTillIndex[i - 1]
                    ),

                    // * ??
                    maxProduct = Math.max(maxProduct, maxTillIndex[i])
                )
            )),
            maxProduct
        )

        // using an extra DP arrays
        maximumProductSubArray = nums => { // O(n) t ; O(2n ~ n) s
            let maxProduct = nums[0]
            let maxTillIndex = [maxProduct],
                minTillIndex = [maxProduct]

            nums.forEach((num, i) => {
                maxTillIndex[i] = Math.max(
                    num,
                    num * maxTillIndex[i - 1],
                    num * minTillIndex[i - 1]
                )
                minTillIndex[i] = Math.min(
                    num,
                    num * maxTillIndex[i - 1],
                    num * minTillIndex[i - 1]
                )
                maxProduct = Math.max(maxProduct, maxTillIndex[i])
            })

            (maxProduct)
        }

        // this time not possible - transforming the input array-arg into the dp-array itself
        maximumProductSubArray = nums => null

        // 3rd-Party (Tutorial) - LC #152 - using extra array - DP
        maximumProductSubArray = nums => { // O(n) t ; O(2n ~ n) s

            let max = nums[0]
            let maxTillIndex = [max],
                minTillIndex = [max]

            let num
            for (let i = 1; i < nums.length; i++) {
                num = nums[i]

                maxTillIndex[i] = Math.max(
                    num,
                    num * maxTillIndex[i - 1],
                    num * minTillIndex[i - 1]
                )

                minTillIndex[i] = Math.min(
                    num,
                    num * maxTillIndex[i - 1],
                    num * minTillIndex[i - 1]
                )

                max = Math.max(max, maxTillIndex[i])
            }

            return max
        }

        /** // ! Find Minimum in Rotated Sorted array - LC #153
         *
         * given an array sorted in ascending order is rotated at some unknown pivot
         * find the minimum element ( - the minimum element's new index too)
         *
         * eg. [0,1,2,3,4,5] -> [3,4,5,0,1,2] - rotated at pivot 2-3
         *
         * assume no duplicate exists (or not) in the array
         *
         * trick: find the largest -ve difference between 2 adjacent elements
         * (from maximum number - in previously sorted array - to the minimum number)
         *
         */

        // slower - linear-search - until sort-discrepancy - O(n) t
        findMinimumInRotatedSortedArray = (rotatedNums, res = null) => ( // O(n) t ; O(1) s
            rotatedNums.forEach((n, i) => (
                n > rotatedNums[i + 1]
                // && ( [rotatedNums[i + 1], i + 1] ) // ! Confirm: how to break out of .forEach() to also return this value (in main function-scope)
                && (res = [rotatedNums[i + 1], i + 1]) // or find a way to break out of .forEach, for 'res' to be returned manually
            )),
            res
        )

        // slower - linear-search - until sort-discrepancy - O(n) t
        findMinimumInRotatedSortedArray = rotatedNums => { // O(n) t ; O(1) s
            for (let i in rotatedNums) {
                rotatedNums[i] > rotatedNums[i + 1]
                && ( [rotatedNums[i + 1], i + 1] ) // * Confirm (auto-return) syntax - babel-typescript plugin
            }
        }

        // slower - linear-search - until sort-discrepancy - O(n) t
        findMinimumInRotatedSortedArray = rotatedNums => { // O(n) t ; O(1) s
            for (let i in rotatedNums)
                if (rotatedNums[i] > rotatedNums[i + 1])
                    return [rotatedNums[i + 1], i + 1]
        }

        // ! Faster - using binary-search - in O(log n) t
        /** // ! using binary - search
         *
         * binary search while left index <= right index
         * (<= - less/equal in this binary-search - because .. ? )
         *
         * calculate mid value, check if inflection point (where highest number meets lowest)
         *
         * - if mid lands on inflection point:
         *
         *      - if number to the left of mid is larger, mid is minimum already
         *      - if number to the right of mid is smaller, at minimum already,
         *          & mid is the (smaller number) right of mid
         *      - the minimum number is the smaller of both numbers at the minimum index (if found)
         *
         * - if mid doesn't land on inflection point:
         *      NB: only check if mid < leftmost number
         *
         *      - if mid > left-most number:
         *          - then mid-pointer is currently on the left-side of the inflection point
         *          - so mid is all the way at the right-side
         *          - where the minimum number with right-neighbors were rotated to
         *          - therfore, mid is on the right-side:
         *              - so move left up to mid's right-section
         *              - left = mid + 1
         *
         *      - else: right = mid - 1
         *          - meaning mid < left-most number
         *          - which means, mid-pointer is currently on the right-side of the inflection point
         *          - because the left-most number, all the way on the left-side, is still larger than current mid
         *          - so actual mid is around the left-side of the mid-pointer:
         *              - so move right down to mid's left-section
         *              - right = mid - 1
         *
         * - repeat binary search until mid lands on inflection point
         *
         */
        findMinimumInRotatedSortedArray = (
            nums,
            [f, l, m, exec, res] = [],
            [
                midNum, leftNum, // rightNum, // * only 1 not used
                leftOfMid, rightOfMid
            ] = []
        ) => ( // O(log n) t ; O(1) s
            nums.length < 1
            ? nums[0] || -1
            : (
                f = 0, l = nums.length - 1,
                nums[f] < nums[l]
                ? nums[f]
                : (
                    exec = ({f, l}) => (
                        // ! ensure this transformer returns required values
                        // * for outside-scope caller to leverage them

                        m = Math.floor((f + l) / 2),

                        midNum = nums[m],
                        leftNum = nums[f],
                        // rightNum = nums[l], // * only 1 not used
                        leftOfMid = nums[m - 1],
                        rightOfMid = nums[m + 1],

                        // ! inflection point checks (eg. [.., 5, 1, ..] )
                        midNum > rightOfMid
                        ? { res: rightOfMid }
                        : midNum < leftOfMid
                        ? { res: midNum }
                        : (

                            // * not at inflection point
                            // * only check if mid < left-most number,
                            // then mid is all the way at the right-side,
                            // where the minimum number with right-neighbors were rotated to
                            // ! remember, there's only 1 direction of rotation
                            midNum > leftNum
                            ? f = m + 1
                            : l = m - 1,
                            {f, l} // return indices, for next functional-iteration
                        )

                    ),

                    { res } = Functions.while(
                        // ! less/equal-to in this binary-search
                        ({f, l}) => f <= l,
                        exec,
                        { f, l, res: null }
                    ),
                    res || -1
                )
            )
        )

        // ! Faster - using binary-search - in O(log n) t
        findMinimumInRotatedSortedArray = nums => { // O(log n) t ; O(1) s

            if (nums.length < 2) (nums[0] || -1)

            let f = 0, l = nums.length - 1

            if (nums[f] < nums[l]) (nums[f])

            let m, midNum, leftNum, // rightNum, // * only 1 not used
                leftOfMid, rightOfMid

            while (f <= l) {

                m = Math.floor( (f + l) / 2 )
                leftNum = nums[f]
                // rightNum = nums[l] // * only 1 not used
                leftOfMid = nums[m - 1]
                rightOfMid = nums[m + 1]

                // ! inflection point checks (eg. [.., 5, 1, ..] )
                if (midNum > rightOfMid) (rightOfMid)
                else (midNum < leftOfMid) (midNum)

                // * not at inflection point
                // * only check if mid < left-most number,
                // then mid is all the way at the right-side,
                // where the minimum number with right-neighbors were rotated to
                // ! remember, there's only 1 direction of rotation
                if (midNum > leftNum) f = m + 1
                else l = m - 1

            }

            (-1)
        }

        // 3rd-Party (Tutorial) - LC #153
        findMinimumInRotatedSortedArray = rotatedNums => { // O(log n) t ; O(1) s

            if (rotatedNums.length === 1) return rotatedNums[0]

            let left = 0, right = rotatedNums.length - 1

            if (rotatedNums[left] < rotatedNums[right])
                return rotatedNums[left]

            let mid, midNum, leftNum, // rightNum, // * only 1 not used
                leftOfMid, rightOfMid

            while (left <= right) { // ! less/equal-to in this binary-search

                mid = Math.floor((left + right) / 2)

                midNum = rotatedNums[mid]
                leftNum = rotatedNums[left]
                // rightNum = rotatedNums[right] // * only 1 not used
                leftOfMid = rotatedNums[mid - 1]
                rightOfMid = rotatedNums[mid + 1]

                // ! inflection point checks (eg. [.., 5, 1, ..] )
                if (midNum > rightOfMid) return rightOfMid
                else if (midNum < leftOfMid) return midNum

                // * not at inflection point
                // * only check if mid < left-most number,
                // then mid is all the way at the right-side,
                // where the minimum number with right-neighbors were rotated to
                // ! remember, there's only 1 direction of rotation
                if (midNum > leftNum) left = mid + 1
                else right = mid - 1

            }

            return -1
        }

        /** // ! Search In Rotated Sorted Array - LC #33
         *
         * remember, rotated sorted arrays have an inflection index at rotation
         * (where highest value meets lowest value in array)
         *
         * 1st find the inflection index,
         * then do Binary Search for the target value on 2 sorted arrays
         * rather than 1 rotated sorted array
         *
         * re-use solution from 'findMinimumInRotatedSortedArray - O(log n) t'
         * to find the inflection index, then split into 2 sorted arrays
         *
         * then, do a recursive Binary Search on both sorted arrays for the target value
         *
         */

        // ! modifying above problem-function 'findMinimumInRotatedSortedArray'
        // ! to finding the minimum's middle index alone, this time (not the number itself)
        findIndexOfMinimumInRotatedSortedArray = nums => {

            let left = 0, right = nums.length - 1

            if (nums.length === 1) return 0

            if (nums[left] < nums[right]) return 0

            while (left <= right) {
                const mid = Math.floor((left + right) / 2)

                // return inflection points
                if (nums[mid] < nums[mid - 1]) return mid
                if (nums[mid] > nums[mid + 1]) return mid + 1

                // or shift left & right pointers
                if (nums[mid] < nums[left]) right = mid - 1
                else left = mid + 1

            }

            return -1
        }

        // ! Faster - binary search - O(log n) t
        searchInRotatedSortedArray = (
            nums, target,
            [m, rBinarySearch, i1, i2] = []
        ) => ( // O(2logn ~ log n) t ; O(1) s

            m = this.findIndexOfMinimumInRotatedSortedArray(m), // O(log n) t ; O(1) s

            rBinarySearch = (
                arr, f, l, target,
                [m] =[]
            ) => ( // O(log n) t ; O(1) s
                arr.length < 1 ? -1 // ! todo: confirm base-case for -1 return
                : (
                    m = Math.floor(f + (l - f) / 2),
                    arr[m] === target
                    ? m
                    : arr[m] < target
                    ? rBinarySearch(arr, m + 1, l, target)
                    : rBinarySearch(arr, f, m - 1, target) // arr[m] > target
                )
            ),

            // ! DO NOT add minimum index at inflection point to 1st array
            // m points to lowest value in rotated array, so it spoils 1st sub-array's sorting
            // m must be in 2nd array where it's the lowest value in that sorted array
            i1 = rBinarySearch(nums, 0, m - 1, target), // ending index - m - 1 (points to highest value)
            i2 = rBinarySearch(nums, m, nums.length - 1, target), // starting index - m (points to lowest value)

            i1 === -1 ? i2 === -1 ? -1 : i2 : i1
            // return i1 if not -1, or i2 if not -1
        )

        // ! Faster - binary search - O(log n) t
        searchInRotatedSortedArray = (nums, target) => { // O(log n) t ; O(1) s

            let m = this.findIndexOfMinimumInRotatedSortedArray(nums)

            const rBinarySearch = (arr, f, l, t) => {
                if (arr.length < 1) (-1)
                let m = Math.floor(f + (l - f) / 2)
                if (a[m] === t) (m)
                else if (a[m] > t) (rBinarySearch(arr, f, m - 1, t))
                else (rBinarySearch(arr, m + 1, l, t)) // * a[m] < t
            }

            let i1 = rBinarySearch(nums, 0, m - 1, target),
                i2 = rBinarySearch(nums, m, nums.length - 1, target)

            (i1 === -1 ? i2 === -1 ? -1 : i2 : i1)
            // return i1 if not -1, or i2 if not -1
            // * or: Math.max(i1, i2) // * the higher return value > -1
        }

        // 3rd-Party (Tutorial) - LC #33
        searchInRotatedSortedArray = (nums, target) => { // O(log n) t ; O(1) s

            const findIndexOfMinimumInRotatedSortedArray = nums => {

                let left = 0, right = nums.length - 1

                if (nums.length === 1) return 0

                if (nums[left] < nums[right]) return 0

                while (left <= right) {
                    const mid = Math.floor((left + right) / 2)

                    // return inflection points
                    if (nums[mid] < nums[mid - 1]) return mid
                    if (nums[mid] > nums[mid + 1]) return mid + 1

                    // or shift left & right pointers
                    if (nums[mid] < nums[left]) right = mid - 1
                    else left = mid + 1

                }

                return -1
            }

            const binarySearch = (nums, target, left, right) => {
                while (left <= right) {
                    const mid = Math.floor((left + right) / 2)
                    if (nums[mid] === target) return mid
                    else if (nums[mid] < target) left = mid + 1
                    else right = mid - 1
                }
                return -1
            }

            const minI = findIndexOfMinimumInRotatedSortedArray(nums)
            const left = binarySearch(nums, target, 0, minI) // ! ** minI - 1
            const right = binarySearch(nums, target, minI, nums.length - 1)
            // ! minI in this case not updated (to minI - 1) to not be a part of 'left' binarySearch
            // * should still pass test cases; find out why; create other test cases where this fails

            return Math.max(left, right)
        }

        /**
            * Best time to buy & sell stock - LC #121

            with array with ith element being price of a stock on day i

            if only permitted to complete at most 1 transaction within all the days given (i.e. buy 1 & sell 1 share of the stock),
            find the max-profit

            * cannot sell a stock before buying 1 (so min-price - to buy - must always come before max-price - to sell)

            - algo option - for each price, find the smallest value before it
        */

        // using a 'hashmap' lead to this thought - storing a 'minimum price' instead
        bestTimeToBuyAndSellStock = (
            nums,
            [maxProfit, minPrice] = []
        ) => ( // O(n) t ; O(1) s
            minPrice = nums[0],
            nums.forEach((n, i) => (
                i === 0 || (
                    maxProfit = Math.max(maxProfit, n - minPrice),
                    minPrice = Math.min(minPrice, n)
                )
            )),
            maxProfit
        )

        bestTimeToBuyAndSellStock_MaxProfit = // O(n) t ; O(1) s
            (prices, [minPrice, maxProfit] = []) => (
                minPrice = prices[0],
                prices.forEach((price, i) => (
                    i == 0
                    || (
                        price > minPrice // faster logic - check 1st
                        && (
                            // todo: options ?
                            maxProfit = Math.max(maxProfit, price - minPrice)
                        ),
                        price < minPrice && (minPrice = price) // faster logic - check 1st
                    )
                )),
                maxProfit
            )

        bestTimeToBuyAndSellStock = nums => { // O(n) t ; O(1) s
            let minPrice = nums[0], maxProfit
            for (let n of nums) {
                n > minPrice && (maxProfit = Math.max(maxProfit, n - minPrice))
                n < minPrice && (minPrice = n)
            }
            (maxProfit)
        }

        // 3rd-Party (Tutorial) - LC #121
        bestTimeToBuyAndSellStock_MaxProfit = prices => { // O(n) t ; O(1) s
            let maxProfit = 0, minPrice = prices[0]
            for (let i = 1; i < prices.length; i++) {
                maxProfit = Math.max(maxProfit, prices[i] - minPrice)
                prices[i] < minPrice && (minPrice = prices[i]) // * should always come after maxProfit line
            }
            return maxProfit
        }

        // 3rd-Party (Tutorial) - LC #121 // ! TEST - shouldn't pass all test cases (especially hidden ones)
        bestTimeToBuyAndSellStock = prices => { // O(n) t ; O(1) s
            let maxProfit = 0, cheapestPrice = prices[0]

            for (let i = 0; i < prices.length; i++) {

                // ! Confirm: why set cheapestPrice if lower 'price' before setting maxProfit
                const price = prices[i]
                if (price < cheapestPrice)
                    cheapestPrice = price

                // ! if above checks 'true' & cheapestPrice = price, currentProfit == 0
                const currentProfit = price - cheapestPrice // ! currentProfit should be based on cheapestPrice from the past
                maxProfit = Math.max(currentProfit, maxProfit) // ! if currentProfit == 0, should be some lost logic

                // ! best to set cheapestPrice (min-price) after setting maxProfit (which is based on previous min-price)

            }

            return maxProfit
        }

        /**
            Cyclic Rotation - LC # ??

            shift array k times to the right

            algo - a2[i + k) % a1.size] = a1[i]
        */

        cyclicRotation = (arr, k) => ( // O(n) t ; O(1) s
            // todo: confirm re-setting (restructuring) array on each iteration-pop as O(1) s
            Array(k).fill(0).forEach(_ => (
                arr = [arr.pop(), ...arr]
            )),
            arr
        )

        // 3rd Party (Tutorial) - LC # ??
        cyclicRotation = (arr, k) => { // O(n) t ; O(1 / n ?) s
            // todo: confirm new array index-setters as O(1) t, & 2 arrays as doubled-space
            let res = new Array(arr.length)
            for (let i = 0; i < res.length; i++) {
                res[(i + k) % arr.length] = arr[i]
            }
            return res
        }
    
    }

    static Strings = class Strings_ {

        reverse = str => str.split('').reverse().join('') // O(1 ~ 3n) t - all 3 operations O(n) by 'character' 'array' but O(1) t by finite-length 'string'
        
        reverse = str => [...str].reverse().join('') // O(1 ~ 3n) t

        reverse = str => {
            if ( !str || str.length < 2
            || typeof str !== 'string' )
                return -1
            
            const backwards = [], backwardsStr = ''
            for (let i = str.length - 1; i == 0; i--) {
                // backwards.push(str[i])
                backwardsStr.append(str[i]) // += str[i]
            }

            // return backwards.join('') // O(1 ~ n) here, to join all characters
            return backwardsStr // O(1) here; characters already appended to string
        }

        /*

        reverse = str => (
            !str || str.length < 2
            || typeof str !== 'string'
            ? -1
            : (
                []
                |> (
                    str.split('').reverse() // * extra (& unnecessary) O(2n) by splitting & reversing
                    .forEach(c => %.push(c)), // * why iterate & append an already reversed array anyway ?
                    %.join('')
                )
            )
        )

        */

        // Revere String's Words:
        // reverse each word in a string; NOT reverse all words in string
        // (NOT 'string in words all reverse'; BUT 'esrever lla ... ')

        reverseStringWords = str =>
            str.split(' ').map(word => word.split('').reverse().join('')).join(' ')

        reverseStringWords = str => {
            let words = str.split(' ')
            let rWords = []

            words.forEach(word => {
                let rWord = ''
                for (let i = word.length - 1; i >= 0; i--)
                    rWord += word[i]
                rWords.push(rWord)
            })

            return rWords.join(' ')
        }

        /**
         * Given a string, find length of the longest substring
         * without repeating characters (either repeating / adjacently repeating characters)
         */

        longestSubstringLength = str => ( // O(n) t ; O(1) s
            null // TODO
        )

        // Sliding Window - custom method - adjacently repeating characters
        longestSubstringLength = str => { // O(n [ / ? - nested loop only accelerates parent loop ]) t ; O(1) s
            let start = maxLength = 0
            let i // ! pre-declare index here, because it will be required after loop-scope
            for (i = 0; i < str.length; i++) {
                if (str[i] === str[i - 1]) {
                    // ! go back 2x (non-repeating), minus start index, but re-add 1 since start is exclusive
                    maxLength = Math.max(maxLength, i - 2 - start + 1) // ! i - start - 1
                    while (
                        i < str.length - 1 // to ensure i not pre-incremented over-board, to string's length (out of array exception raised)
                        && str[i] === str[++i]
                    ) // * pre-increment i for 1st next-index
                        console.log('incrementing i until next non-repeating character')
                    start = i // ! don't worry about i as start, not being tested yet
                    // * it'll be tested as the previous index in next iteration (if str[i] === str[i - 1])
                }
            }
            // ! required in case loop ends with non-repeating characters
            maxLength = Math.max(maxLength, i - start) // ! don't re-add 1 this time; i == string length; so start & last item are already inclusive
            return maxLength
        }

        // Sliding Window - custom method - no repeating characters at all - using a HashMap
        longestSubstringLength = (str, [m, max] = [{}, 0]) => ( // O(n) t ; O(n) s
            str.forEach(c =>
                c in m
                ? (
                    max = Math.max(max, Object.keys(m).length),
                    m = {[c]: 1} // * re-start hashmap, with current item, for length = 1
                ): m[c] = 1
            ),
            Math.max(max, Object.keys(m).length) // todo: confirm O(n ?) t of .keys(m)
        )

        // Sliding Window - custom method - no repeating characters at all - using an extra array
        longestSubstringLength = (
            str,
            [arr, max] = [[], 0]
        ) => ( // O(n) t ; O(n) s
            str.forEach(c =>
                c in arr
                ? (
                    max = Math.max(max, arr.length),
                    arr = [c] // * re-start array, with current item, for length = 1
                ): arr.push(c)
            ),
            Math.max(max, arr.length)
        )
        
        // Sliding Window - using a HashMap (no repeating characters at all)
        longestSubstringLength = ( // O(n) t ; O(n) s
            str,
            [m, max, start] = []
        ) => ( // O(n) t ; O(n) s
            m = {}, max = start = 0,
            str.forEach((c, i) => (
                c in m &&  i >= 0
                && (start = i),
                m[c] = i,
                max = Math.max(max, i - start + 1) // * + 1 for exclusive 'start' indexed-item
            )),
            max
        )
        
        // 3rd-Party (Tutorial) - Sliding Window
        // * sliding window rep's current substring of non-repeating characters in iteration
        // sliding window not of fixed size; can grow / shrink during iterations
        longestSubstringLength = str => { // O(n) t ; O(1) s
            // TODO
        }

        // 3rd-Party (Tutorial) - LC #3 - Sliding Window - using a HashMap (no repeating characters at all)
        longestSubstringLength = str => { // O(n) t ; O(min(m,n)) s - number of keys in HashMap bounded by size of string n & size of charset/alphabet m
            let windowChars = {}, start = maxLength = 0,
            endChar
            
            for (let i = 0; i < str.length; i++) {
                endChar = s[i]
                if (windowChars[endChar] >= start)
                    start = windowChars[endChar] + 1
                windowChars[endChar] = i
                maxLength = Math.max(maxLength, i - start + 1)
            }

            (maxLength) // * get babel-ts plugin
        }

        /**
         * Given a string s, find the longest palindromic substring
         */

        longestPalindromicSubstring = str => { // O(n/2) t ; O(1) s
            let isPalindrome = false,
                i = 0, j = str.length - 1,
                start = end = -1
            
            while (i < j) {

                str[i] === str[j]
                ? (
                    isPalindrome || (
                        start = i,
                        end = j
                    ),
                    isPalindrome = true
                ) : (
                    start = end = -1,
                    isPalindrome = false
                )

                i++; j--
            }

            isPalindrome
            && start != -1 && end != -1
            && (str.substr(start, end)) // .substr - O( n ~ 1 ? ) t ?
            // * return `` // ! TODO: Ensure above (stmt) 
            // * is still returned in conjunction with &&-conditionals
            //  ! [confirm with Babel-TypeScript plugin]
        }

        // 3rd-Party (Tutorial) - LC #5 - expand around middle
        longestPalindromicSubstring = str => { // O(n^2) t ; O(1) s
            // ! O(n^2) t - expanding palindrome around its center (~ O(n) t), done in iteration, for each character

            let startIndex = 0, maxLength = 1

            let expandAroundMiddle = (i, j) => {
                let l
                while (
                    i >= 0
                    && j < str.length
                    && str[i] === str[j]
                ) {
                    l = j - i + 1
                    l > maxLength
                    && (
                        maxLength = l,
                        startIndex = i
                    )
                    i--; j++ // ! this time, expanding from middle (start - i moving left ; end - j moving right)
                }
            }

            // * not advisable to str.split().forEach() - .split should already be O(n) on 'str'
            // raw-loops faster if data-type conversions add more O(t)
            for (let i = 0; i < str.length; i++) {
                expandAroundMiddle(i - 1, i + 1)
                expandAroundMiddle(i, i + 1)
            }

            // now, slice str from startIndex through maxLength
            return str.slice(startIndex, startIndex + maxLength) // can also use: .substr / .substring

        }
        
        /**
         * Valid Parentheses - ({[]})
         * ( .. ) / { .. } / [ .. ] / Combos
         */

        validParentheses = str => ( // O(n) t ; O(1) s
            null // TODO
        )

        // TODO: Test - using 2-pointers
        validParentheses = str => { // O(n/2 ~ 1 ? ) t ; O(1) s
            // ! NB: O(n/2) t for half-iteration | ~ O(1) t for half-iteration of a string ? (expected finite length)
            
            let i = 0, j = str.length - 1,
                valid = '({[]})'

            while (i < j) {
                str[i] in valid
                && str[j] in valid
                && str[i] === str[j]
                || (false) // todo: Confirm, or: return false
            }

            (true) // todo: confirm babel-typescript plugin
        }
        
        /**
            Valid Parentheses - ({[]}) - // ! using a Stack
            
            iterate through string's characters
            push to stack when character is left-half of any valid parenthesis
            pop from stack on the 1st iteration with right-half of previously pushed left-half parenthesis
            keep popping from stack until empty, while confirming next right-half of pairs
            Valid Parentheses if stack is empty when string iteration complete
        */
        // TODO: Test - using Stack
        validParentheses = (
            str,
            [stack, match] = []
        ) => ( // O(n) t ; O(n) s - for stack only (not constant-space hash-map)
            match = (
                a, b,
                m = {
                    '(': ')',
                    '{': '}',
                    '[': ']'
                }
            ) => m[a] === b,
            stack = new Stack(),
            str.forEach(c => (
                match(stack.peek(), c)
                ? stack.pop()
                : stack.push(c)
            )),
            stack.isEmpty() // invalid parentheses if stack not empty
        )
        // TODO: Test - using Stack
        validParentheses = (
            str,
            [stack, map] = []
        ) => ( // O(n) t ; O(n) s
            stack = [],
            map = {
                '(': ')',
                '{': '}',
                '[': ']'
            },
            str.forEach(c => (
                c in map // if c in map, 'opening bracket'
                ? stack.push(c) // so push to stack
                : ( // * else, 'closing bracket', so peek-check & pop, or push (new closing bracket) again
                    c === map[ // * null / undefined values can also be compared
                        stack[stack.length - 1]
                    ] ? stack.pop()
                    : stack.push(c)
                )
            )),
            !stack.length
        )

        // 3rd-Party (Tutorial) - LC #20 - using a Stack
        validParentheses = str => { // O(n) t ; O(n) s
            let stack = []
            let map = {
                '(': ')',
                '{': '}',
                '[': ']'
            }
            
            let c, top
            for (let i = 0; i < str.length; i++) {
                c = str[i]
                // if (map[c]) stack.push(c) // ! Confirm: Boolean(map[existingKey]) & !!map[existingKey] == STILL false
                if (c in map) stack.push(c)
                else { // * doesn't exist if c is a closing bracket
                    top = stack[stack.length - 1]
                    char === map[top]
                    ? stack.pop()
                    : stack.push(c)
                }
            }
            
            return !stack.length
        }

        /**
         * Valid - string reversed is the same as before
         */

        validPalindrome = str => // O(3n ~ n) t ; O(1) s
            str === str.split('').reverse().join('')
        
        validPalindrome = str => { // O(n/2) t ; O(1) s
            let i = 0, j = str.length - 1

            while (i < j) {
                str[i] === str[j] || (false)
                // or: if (!..) return false 
                // todo: confirm (returnValue) syntax (babel-typescript plugin) 
                // * even with compound || conditional statement
                i++; j--
            }
            
            (true)
        }

        /**
         * Given a string, determine if it's a palindrome, 
         * considering only alphanumeric characters & ignoring cases
         * (sanitize out only lowercase characters & numbers)
         * 
         * @param str
         * @returns {boolean}
         */
        // 3rd-Party (Tutorial) - LC #125 - sanitizing case-sensitive alphanumeric characters 1st
        validPalindrome = str => { // O(n/2) t ; O(1) s

            // sanitize string by removing non-alphanumeric characters & lowercasing string

            // ! LC doesn't test for underscores '_' ; but some other interviews might
            str = str.toLowerCase().replace(/[\W_]/g, '') // ! '_' included in regex

            // use 2-pointer from start & end of string, & check equality on each iteration
            
            let i = 0, j = str.length - 1

            while (i < j) {
                if (str[i] !== str[j])
                    return false
                i++; j--
            }

            return true
        }

        /**
         * Valid Anagram - words can be rearranged to be the exact same word
         */

        validAnagram = (s1, s2) => { // O(n) t ; O(1) s

            // Option 2: sort both strings & compare equality

            // TODO: sort better (use fastest in-built way)
            // O( n + n log n + n ~ n ) t - sorting for both strings)
            [s1, s2] = [s1, s2].map(s =>
                s.split('').sort().join('')
            )

            return s1 === s2
        }

        validAnagram = (s1, s2, res = true) => ( // O(n) t ; O(1) s
            
            // Option 1: delete any s1-item found in s2; return false if not found
            
            // * return false by default if any string is empty
            !s1.length || !s2.length
            ? (res = false)
            : s1.forEach(s => (
                s in s2
                ? delete s2[s2.indexOf(s)]
                : (res = false) // ! wrong implementation: break out of .forEach; on this iteration
            )),
            res
        )

        validAnagram = (
            s1, s2,
            [m, valid] = [{}, true]
        ) => ( // O(2n ~ n) t ; O(n ~ 1) s
            // ! O(1) s still; map can only have 26-total (alphabets) k-v pairs at most; so constant space
            s1.length !== s2.length ? false
            : (
                s1.map(c => (m[c] = m[c] + 1 || 1)),
                s2.map(c => (
                    c in m && !!m[c]
                    ? m[c]--
                    : (valid = false)
                    /* * or:
                    !m[c] ? (valid = false) : m[c]--
                     */
                )),
                valid
            )
        )

        // 3rd-Party (Tutorial) - LC #242 - using a HashMap
        validAnagram = (s1, s2) => { // O(2n ~ n) t ; O(n ~ 1) s
            if (s1.length !== s2.length) return false
            let m = {}, c
            
            for (let i = 0; i < s1.length; i++) {
                c = s1[i]; m[c] = (m[c] + 1) || 1 // increment char-count / init to 1
            }
            
            for (let i = 0; i < s2.length; i++) {
                c = s2[c];
                if (c in m && !!m[c]) m[c]--
                else return false
                /* * or:
                if (!m[c]) return false
                else m[c]--
                 */
            }
            
            return true
        }

        /**
         * Group Anagrams - group / arrange all anagrams in array of strings
         * 
         * @param strs
         * @returns {null}
         */

        groupAnagrams = (strs, [m, s] = [{}]) => ( // O(n s log s) t ; O(ns) s - grouped HashTable
            strs.map(str => (
                // * sort key 1st ~ O( (n ~ 1) (s log s) ) t for a string (n ~ 1 for splitting & joining)
                s = str.split('').sort().join(''),
                !m[s] && (m[s] = []), // hash-table for array-values
                m[s].push(str)
            )),
            m
        )

        groupAnagrams = strs => { // O(n s log s) t ; O(ns) s - grouped HashTable
            let m = {}, s
            for (let i in strs) {
                s = strs[i].split('').sort().join('')
                !m[s] && (m[s] = [])
                m[s].push(strs[i])
            }
            (Object.values(m)) // * this time, return m's values as a matrix with sub-array groupings
            // ! confirm babel-typescript plugin - (returnValue)
        }

        // 3rd-Party (Tutorial) - LC #49
        groupAnagrams = strs => { // O(n s log s) t ; O(ns) s - grouped HashTable
            let m = {}, s, k
            for (let i = 0; i < strs.length; i++) {
                s = strs[i]
                // * sort key 1st ~ O( (n ~ 1) (s log s) ) t for a string (n ~ 1 for splitting & joining)
                k = s.split('').sort().join('')
                if (!m[k]) m[k] = [] // hash-table for array-values
                m[k].push(s)
            }
            return Object.values(m)
        }
        
    }

}

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

    // Option 1: O(n) t ; O(1) s
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


// Stacks - peek - O(1), pop - O(1), push - O(1), lookup/search - O(n), insert - O(?), delete - O(?), copy - O(?), 

class Stack {
    constructor() {
        this.items = [];
    }
    
    length = () => this.items.length

    // Add an element to the top of the stack
    push(element) {
        this.items.push(element);
    }

    // Remove and return the top element from the stack
    pop() {
        if (this.isEmpty()) {
            throw new Error('Stack Underflow');
        }
        return this.items.pop();
    }

    // View the top element without removing it
    peek() {
        if (this.isEmpty()) {
            return null;
        }
        return this.items[this.items.length - 1];
    }

    // Check if the stack is empty
    isEmpty() {
        return this.items.length === 0;
    }

    // Get the size of the stack
    size() {
        return this.items.length;
    }

    // Clear all elements from the stack
    clear() {
        this.items = [];
    }
}

// Example usage
const stack = new Stack();
stack.push(10);
stack.push(20);
console.log(stack.peek()); // Output: 20
console.log(stack.pop());  // Output: 20
console.log(stack.size()); // Output: 1
console.log(stack.isEmpty()); // Output: false


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

function isSameTree(t1, t2) { // O(n1 + n2 ~ n) t (n - if trees are same) ; O(1) s

    // traverse both trees simultaneously (with b/c/d-fs) and compare current node values at each iteration
    
    if (!t1 || !t2 || !t1.root || !t2.root) return false
    let n1 = t1.root, n2 = t2.root
    if (n1.value !== n2.value) return false

    // BFS

    let q1 = q2 = []
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
function isSameTree(t1, t2) { // O(n1 + n2 ~ n) t (n - if trees are same) ; O(1) s
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
        super();
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
    let root = tree.root, node
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
    let q = [root], node
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
    a = a.map((s, i) => s.split('').sort().join(''))
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
    // O(s + s log s + s) + O(s) t; O(1) s

    // strings do not have in-built .sort() method // TODO: Fix with the in-built ways of sorting strings
    s.split('').sort().join('') // todo: wrong way to sort a string (splitting it, then joining sorted splits)
    // * adds unnecessary extra time-complexity (pseudo - linear), iterating through entire string to .split() & entire char-array to .join()

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
        if (m?.[x] >= 1) --m?.[x] // ! @babel/plugin-proposal-optional-chaining-assign plugin required
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
    let m = {}, x
    for (x of s) {
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
                } else {
                    // TODO
                }
                // ! optional-chaining in left-hand assignment in new babel-typescript plugin 
                // * @babel/plugin-proposal-optional-chaining-assign
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
// PROBLEM-SOLVING ALGO'S
////////////////////////////////////////


class DynamicProgramming {

    calculations = 0

    // 3rd-Party (Tutorial) - REGULAR recursion - Top-Down
    fibonacci = n => ( // O(2^n) t ; O(1) s
        // O(2^n) t - recursive calls - default time-complexity
        // O(1) s - no space required
        
        calculations++, // can run this recursive function ..
        // & compare number of 'calculations' made (WAY slower than below)
        n < 2 ? n
        : fibonacci(n - 1) + fibonacci(n - 2)
    ) // eg: fibonacci(30)


    // ! 3rd-Party (Tutorial) - DP (DFS) recursion, with Caching - Top-Down (BEST & FASTEST Option)
    // BEST & FASTEST Option - since it avoids unnecessary recursive re-calculations
    // plus fibo-numbers will never repeat, since lower ones add up to higher ones

    cache = {}
    fibonacci = n => ( // O(n) t ; O(n) s

        // O(n) t - recursive calls, BUT with caching - to remove unnecessary re-calculations
        // algo ends up only recursing through only unique n values
        // O(n) s - extra hashmap or hashtable - used as a cache data-structure

        calculations++, // can run this recursive function ..
        // & compare number of 'calculations' made (WAY faster than above)
        n in cache
        ? cache[n]
        : (
            // ! 'calculations++' doesn't have to be placed here ..
            // * because above base-case still prevents below recursive calls
            n < 2
            ? n
            : (
                cache[n] =
                    fibonacci(n - 1)
                    + fibonacci(n - 2),
                cache[n] // return cached-number, after storing
                // so it's still accessible in future recursive calls
            )
        )
    ) // eg: fibonacci(30)

    // 3rd-Party (Tutorial) - DP (BFS) iterative, without Caching - Bottom-Up (ALSO BEST & FASTEST Option)
    // using same resulting array to save previous calculations
    fibonacci = n => {
        let a = [0, 1]
        for (let i = 2; i <= n; i++)
            a.push(a[i - 1] + a[i - 2])
        (a) // return entire fibo-series ; or: a.pop() - last a[n] item
    }

}


class DivideAndConquer {

}


class Greedy {


    /*

        Maximum Non-Overlapping Segments
        
        Given a number of segments,
        find the maximum number of these segments that do not overlap with each other

        - similar to: Activity Selection Problem
            - where to choose the max non-overlapping tasks

    */


    maxNonOverlappingSegments = (a, b) => ( // O() t ; O() s
        null
    )

    // 3rd-Party (Tutorial) - comparison of 2 segments only
    maxNonOverlappingSegments = (
        a1, a2,
        [lastEndSegment, chosenCount, i] = []
    ) => ( // O(n) t ; O(1) s
        lastEndSegment = -1,
        chosenCount = 0,

        i = 0, // ! TODO: fix for-loop replacement - for (let i = 0; i < a.length; i++)
        Array(a1.length).fill(i++).forEach(i => ( // ! i++ (or ++i) increments only once, after/before  .fill() on each item
            a1[i] > lastEndSegment
            && (
                chosenCount++,
                lastEndSegment = a2[i]
            )
        )),

        chosenCount
    )

    // 3rd-Party (Tutorial) - comparison of 2 segments only
    maxNonOverlappingSegments = (a1, a2) => { // O(n) t ; O(1) s
        let lastEndSegment = -1
        let chosenCount = 0

        for (let i = 0; i < a1.length; i++)
            if (a1[i] > lastEndSegment) {
                chosenCount++
                lastEndSegment = a2[i]
            }
        
        (chosenCount)
    }


    /*

        Tie Ropes

        Given a number of ropes, each with a different length,
        and a constant, k, 1 of the ropes' length,
        2 ropes are adjacent if they're next to each other,
        & only 2 adjacent ropes can be tied together
        
        - when 2 adjacent ropes are tied:
            - new length = sum of both ropes' lengths
        - aim is to find max number of adjacent ropes (or a single rope):
            - with tied length-sum (or a single rope's length) >= k

    */


    // can only tie 2 adjacent ropes
    tieRopes = (a, k, [c, a1] = [0, []]) => ( // O(n) t ; O(1 - resulting array a1 ignored) s
        a.forEach((n, i) => (
            i + 1 == a.length - 1 ? null : ( // * cannot iterate from index 1 ; 
            // * has to iterate up to last-but-1 index [(length - 1) - 1]
                n >= k
                ? (
                    c++, a1.push(n)
                ) : n + a[i + 1] >= k
                && (
                    c++, a1.push(n + a[i + 1])
                )
            )
        )),
        [a1, c]
    )

    // can tie 2+ adjacent ropes
    tieRopes = (a, k, [l, c, a1] = [0, 0, []]) => ( // O(n) t ; O(1 - resulting array a1 ignored) s
        a.forEach((n, i) => (
            l += n, // increment rope length-sum
            l >= k
            && (
                c++, a1.push(l), l = 0
            )
        )),
        [a1, c]
    )

    // 3rd-Party (Tutorial) - can tie 2+ adjacent ropes
    tieRopes = (a, k) => { // O(n) t ; O(1) s
        let count = 0
        let ropeLength = 0
        a.forEach(rope => {
            ropeLength += rope
            ropeLength >= k && (
                count++,
                ropeLength = 0
            )
        })
        (count)
    }

}


class BackTracking {

}


class Iteration {

}


class Recursion {

}


class Mathematical {

}



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
//  EXTRA Qs
////////////////////////////////////////

const directoryToTree = (
  rootDir, depth,
  [processDirectory] = []
) => (
  depth < 0
  ? {} // ( throw new Error('Depth must be >= 0') )
  : (
    processDirectory = (
      currentDir, currentDepth,
      [
        stats, dirNode, children,
        childPath, childStats
      ] = []
    ) => (
      stats = fs.statSync(currentDir),
      !stats.isDirectory()
      ? {} // ( throw new Error('not a directory') )
      : (
        dirNode = {
          name: path.basename(currentDir),
          path: path.relative(process.cwd(), currentDir),
          type: 'dir',
          size: stats.size,
          children: []
        },
        currentDepth === 0
        ? dirNode
        : (
          children = fs.readdirSync(currentDir),
          children.forEach(
            child => (
              childPath = path.join(currentDir, child),
              childStats = fs.statSync(childPath),
              childStats.isDirectory()
              ? dirNode.children.push(
                processDirectory(childPath, currentDepth - 1)
              )
              : childStats.isFile()
              && (
                dirNode.children.push({
                  name: child,
                  path: path.relative(process.cwd(), childPath),
                  type: 'file',
                  size: childStats.size
                })
              )
            )
          ),
          dirNode
        )
      )
    ),
    processDirectory(rootDir, depth)
  )
)


////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function main() {
    document.write("Hello, World!")
}


{ // * 


    // Array methods
    
    [].map().filter().concat().push().pop().splice().shift().unshift().reverse().forEach() 
    // .includes/reduce/reduceRight/find/findIndex/indexOf/lastIndexOf/

    // * since above method calls are on an empty array, .call them with other binded array data
    let arr = [1, 2, 3, 4, 5] // arr binded on [].filter's .call(..)
    console.log([].filter.call(arr, (elem, _) => elem > 2)) // [ 3, 4, 5 ]
    console.log([].filter.call('John Doe', (_, i) => i > 4)) // [ 'D', 'o', 'e' ] - will filter out letters in string, into an array
    console.log(Array.prototype.filter.call('John Doe', (_, i) => i > 4)) // [ 'D', 'o', 'e' ] - will filter out letters in string, into an array

    // * abstract data-typed (arrays, objects, custom classes) objects referenced by object reference-ids
    let x = {}, y = []; [{}, []].indexOf(x) // with y too: returns -1; x ({}) & y ([]) by reference-ids still don't exist in [{}, []]
    // * primitive data-typed values (int, string, boolean, .. ) can be used to find their indices, with .indexOf
    // null, undefined, Infinity, -Infinity can also be used to find their indices
    // [NaN].indexOf(NaN) is still -1; NaN (might be primitive - confirm) still returns -1, by being NaN ? // todo: - confirm
    [x, y].indexOf(x) // 0 & .indexOf(y) - 1; because exact same abstract objects (with their reference-ids) are in array
    let x1 = x, y1 = y // these are assigned by reference too, so x1 points to x's value in memory; // todo: confirm if they both also have the same reference-ids, even though they both reference the same data in memory
    [x, y].indexOf(x1) // 0 &.indexOf(y1) - 1; because both x/x1 & y/y1 reference-alike (as pairs)

    
    // * can only use read-only Array-methods (filter, forEach, map, some, every, .. ) on Strings
    // cannot use write array-methods (push, pop, splice, shift, unshift, sort, reverse, join, .. ) on Strings (because write-methods manipulate / change the array)


    // String methods

    ''.trim().substr().substring() // todo: ... ?

    let s = 'John Doe'; 
    [...s] // ['J', 'o', 'h', 'n', ' ', 'D', 'o', 'e']
    s.split() // [ 'John Doe' ]
    s.split(' ') // [ 'John', 'Doe' ]
    s.split('') // ['J', 'o', 'h', 'n', ' ', 'D', 'o', 'e']
    ''.split.call(s) // [ 'John Doe' ] - empty string .call binded on s
    ''.split.call(s, '') // [ 'J', 'o', 'h', 'n', ' ', 'D', 'o', 'e' ]
    ''.split.call(s).filter((_, i) => i > 4) // [ 'D', 'o', 'e' ] - will filter out items in split character array this time
    String.prototype.split.call(s) // [ 'John Doe' ] - empty string .call binded on s
    String.prototype.split.call(s, '') // [ 'J', 'o', 'h', 'n', ' ', 'D', 'o', 'e' ]

    /*

    ['a', 'b', 'c'].join() - 'a,b,c'
    .join('') - 'abc'
    s.split('').reverse().join('') - reverse s properly (without unnecessary ','s)

    */


    // Other methods
    
    // deep-clone object
    const deepClone = obj => ({ ...obj }) // JSON.parse(JSON.stringify(obj))

    // random number generator
    const randomNumber = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min

    // check empty array
    const isEmptyArray = arr => Array.isArray(arr) && !arr.length // arr.length === 0

    // unique array elems
    const uniqueArray = arr => [ ... new Set(arr) ]
    
    // convert CamelCase to snake_case
    const camelToSnake = str => str.replace(/([A-Z])/g, '_$1').toLowerCase()

    // get url params
    const getUrlParams = () => Object.fromEntries(new URLSearchParams(window.location.search))

    // capitalize first-letter of each word
    const capitalizeWords = str => str.replace(/\b\w/g, char => char.toUpperCase())

    // check empty object
    const isEmptyObj = obj => !Object.keys(obj).length // Object.keys(obj).length === 0

    // reverse string
    const reverseString = str => str.split('').reverse().join('')

    // check palindrome
    const isPalindrome = (str, cleanedStr = null) => (
        cleanedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase(),
        cleanedStr === reverseString(cleanedStr) // cleanedStr.split('').reverse().join('') - reversed string
    )

    // fetch data from api
    const fetchData = async url => (await fetch(url))?.json() ?? {}

    // random color generator
    const randomColor = () => `#${Math.floor(Math.random() * 16777215).toString(16)}`

    // convert string to Title Case
    const toTitleCase = str => str.toLowerCase().replace(/\b\w/g, char => char.toUpperCase())

    // current date & time
    const now = new Date().toLocaleString()

    // check even/odd number
    const isEven = num => num % 2 === 0

    // find array max-value
    const arrayMax = arr => Math.max(...arr) // Math.max.apply(null, arr) / arr.reduce((a, b) => Math.max(a, b))

    // sort array of numbers
    const sortedArray = arr => arr.sort((a, b) => a - b)

    // flatten nested arrays
    const flattenArray = arr => arr.flat(Infinity)

    // shuffle array
    const shuffleArray = arr => arr.sort(() => Math.random() - 0.5)

    // merge 2 arrays
    const mergeArrays = (a1, a2) => [...a1, ...a2]

}

