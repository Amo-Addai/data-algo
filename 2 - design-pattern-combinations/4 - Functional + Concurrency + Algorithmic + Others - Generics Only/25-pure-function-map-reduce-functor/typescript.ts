'use strict'

/*

Popular Combinations of Design Patterns in Functional and Concurrency Contexts
Some of the most impactful design pattern combinations for Functional, Concurrency, and Other paradigms often arise from the need to balance immutability, high-performance processing, and effective management of multi-threaded or asynchronous workflows. These combinations are highly relevant in environments where scalability, maintainability, and clarity are prioritized, particularly in TypeScript or JavaScript-based applications.

2. Functional + Algorithmic (Pure Function, Map-Reduce, Functor)
- Pure Function + Map-Reduce + Functor Combo
- Map-Reduce Functor Functional Pipeline
- Pure Function Map-Reduce Functor Transformation
- Functional Data Transformation Pipeline

Why this combination exists:
Functional programming encourages immutability and the use of pure functions, while Map-Reduce provides a mechanism for processing large datasets efficiently. Functors enable a functional approach to data transformations, allowing you to map operations over collections of values.

Key Scaffolding Patterns:
Pure Function (for deterministic computations)
Map-Reduce (for processing collections efficiently)
Functor (for applying transformations over data structures)

Why These Patterns Are Combined:

Pure Function: Ensures that computations are deterministic and side-effect-free. It is the core principle of functional programming, ensuring predictable and easily testable code.
Map-Reduce: This pattern is used for transforming data and reducing it into a final result. It efficiently processes collections, and in functional programming, it aligns with the idea of mapping functions over collections and then reducing the result.
Functor: This allows you to apply transformations over data structures. It enables you to map functions over data types like arrays or objects in a composable manner.
Best Scaffolding Pattern: Map-Reduce Functor Functional Pipeline

This scaffold combines Pure Functions with Map-Reduce and Functors to process collections in a functional pipeline. The map phase applies transformations to elements, while the reduce phase aggregates the results. Functors enable a consistent way to apply transformations to collections or other data structures.

Scaffold Example in TypeScript
Example 2: Pure Function, Map-Reduce, Functor
This combination helps process collections of data efficiently in a functional style.
Excellent for processing and transforming collections of data while keeping the logic pure and declarative.

TypeScript Example:

 */

// Pure Function
const add: (x: number, y: number) => number
    = (x, y) => x + y

// Functor - Transforming a value inside a container
class Box<T> {
    constructor(private value: T) {}

    map: <U>(fn: (value: T) => U) => Box<U>
        = fn => new Box(fn(this.value))

    getValue: () => T = () => this.value
}

// Map-Reduce
const mapReduce: <T>(
    arr: T[],
    mapFn: (x: T) => T,
    reduceFn: (acc: number, x: T) => number // ! x (next item) must ALSO be of generic data-type (if x: number, then T MUST ALSO be :number; then function is not generic anymore)
    // ! This generic method will ONLY work with any Data-Type, if ONLY accumulated-sums are explicitly stated of type 'number'
) => number = (
    arr, mapFn, reduceFn
) => arr.map(mapFn).reduce(reduceFn, 0)

// Fully-Generic Map-Reduce
const TMapReduce: <T>(
    arr: T[],
    mapFn: (x: T, i: number) => T, // * i - index (number)
    reduceFn: (acc: T, x: T) => T
) => T = (
    arr, mapFn, reduceFn
) => arr.map(mapFn).reduce(reduceFn, {})


// ! Usage

const numbers = [1, 2, 3, 4]

const result1 = mapReduce(
    numbers,
    (x: number) => x * 2,
    (acc: number, x: number) => acc + x
)

console.log(result1)

const box = new Box<number>(5)

const transformedBox1 = box.map<number>(x => x * 2) // Type-argument here could've been a string if <U> - string
console.log(transformedBox1.getValue())

const transformedBox2 = box.map<string>(x => `${x}`)
console.log(transformedBox2.getValue()) // Box<string> returned in previous call


// ! Other Usage Examples for Generic Map-Reduce Functions

const objects: any[] = [ // can also be of custom Class data-type
    { prop: 1 },
    { prop: '2' },
    { prop: 7.7 },
    { prop: true },
    { prop: 'abc' }
]

const result2 = mapReduce(
    objects,
    (o: any) => ( // To-do - Try-Parse all ?.prop values to 'number' data-type
        (x: any) => (
            {
                'number': i => +i, // +val - unary operator for ints/doubles (& strings) - Number, Math.floor/round/ceil
                'string': i => parseInt(i, 0) || +i || 0, // parseInt only for strings; NaN on fail; parseInt('') - NaN; +'' - 0
                'boolean': i => +i, // - Number(i),
            }
            |> %[typeof x](x)
        )
        |> (o.prop = %(o?.prop))
    ), // TODO: Remember to use Babel to compile Pipeline operator
    // TODO: Ensure accumulation 'acc' can still be forced :number in this case, if x is :any (an object in this case)
    (acc: number, x: any) => acc + (x?.prop ?? 0)
)

console.log(result2)

const objects1: any[] = [ // can also be of custom Class data-type
    { prop: 1 },
    { prop: '2' },
    { prop: 7.7 },
    { prop: true },
    { prop: 'abc' }
]

const result3 = TMapReduce(
    objects1,
    (o: any, i: number) => (
        o[`prop${i+1}`] = o?.prop,
        delete o.prop
    ),
    (acc: any, x: any) => ({ ...acc, ...x }) // * faster option (still) - Object.assign(a, b) - iterates through only b's props
)

console.log(result3)
