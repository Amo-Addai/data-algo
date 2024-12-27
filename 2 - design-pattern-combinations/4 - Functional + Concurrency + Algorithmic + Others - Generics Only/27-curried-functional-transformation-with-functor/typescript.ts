'use strict'

/*

1. Pure Function + Currying + Functor Combo
Why These Patterns Are Combined:

Pure Function: Ensures that each transformation of data is side-effect-free and predictable.
Currying: Allows partial application of functions, making them more flexible for reusable operations.
Functor: A container that allows transformations over its contents without changing the underlying structure, preserving immutability.
Best Scaffolding Pattern: Curried Functional Transformation with Functor

Currying enables partial application for flexibility, Pure Functions ensure transformations are clean, and Functors preserve the structure of data while applying transformations.
TypeScript Example:

 */

// Currying with Functor of Pure Functions - performs a simple transformation
const add = (x: number) => (y: number): number => x + y
// usage - add(xVal)(yVal) => returns :number - xVal + yVal

// Functor - Custom Class for applying transformations
class Functor<T> {
    constructor(private value: T) {}

    map = <U>(fn: (value: T) => U): Functor<U> =>
        new Functor(fn(this.value))

    flatMap = <U>(fn: (value: T) => Functor<U>): Functor<U> =>
        fn(this.value)

    // TODO: auto-map through a list of values in a Functor pattern
    // return Functor value for each list-item, but auto-map through each next-item
    // then .getValue() should return final result of all items being mapped through

    getValue = (): T => this.value
}


// ! Usage

const curriedAdd5 = add(5)
const functor = new Functor(10)

const result = functor.map(curriedAdd5) // map through only value - 10 with curried function
console.log(result.getValue()) // Output: 15 (5 added to 10)


// ! Usage 2

const add10 = add(10)
const functor1 = new Functor(5)

// Functor - Applying a transformation to a value wrapped inside a Monadic structure
const result1 = functor1
    .map(add10).map(add10)
    .map(x => x * 2)

console.log(result1.getValue())


// ! Usage 3 - Map-Reduce - map with functor argument, reduce to summation

const double = (x: number): number => x * 2

const mapReduce = <T>(
    arr: Functor<T>[],
    fn: (x: T) => T,
    initialValue: T
): T =>
    arr.map(
        functor =>
            functor.map(fn).getValue()
    )
    .reduce(
        (acc, curr) =>
            acc + curr,
        initialValue
    )

// Wrapping numbers in Functors
const numbers = [1, 2, 3, 4, 5].map(num => new Functor(num))

// Doubling each number & summing up
const result2 = mapReduce<number>(numbers, double, 0)

console.log(result2) // Output: 30 (2+4+6+8+10)
