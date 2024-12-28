'use strict'

/*

4. Map-Reduce + Pure Function + Functor Combo
Why These Patterns Are Combined:

Map-Reduce: A pattern that processes collections by applying a function (map) and reducing them to a single value, making it great for parallel processing or aggregate operations.
Pure Function: Ensures the function has no side effects and always produces the same output for the same input, leading to predictable transformations.
Functor: Allows mapping a function over the values in a container without modifying the container's structure.
Best Scaffolding Pattern: Functional Data Transformation and Aggregation

This scaffolding pattern excels in scenarios where you need to transform and aggregate data in a functional, pure, and modular way. It combines the flexibility of functors with the powerful data processing capability of map-reduce and the predictability of pure functions.
TypeScript Example:

 */

class Functor<T> {
    constructor(private value: T) {}

    map = <U>(fn: (x: T) => U): Functor<U> =>
        new Functor(fn(this.value))

    getValue = (): T => this.value
}


// ! Usage

// Pure Functions
const add1 = (x: number): number => x + 1
const mult2 = (x: number): number => x * 2

const numbers = [1, 2, 3, 4, 5]

// Map-Reduce

// Map through list, & apply custom Functor.map to each item, with add1 Transformation
const functors = numbers.map(num => new Functor(num).map(add1)) // list of Functors now
// Reduce list of Functors to summed total
const total = functors.reduce((acc, functor) => acc + functor.getValue(), 0)

console.log('Mapped & Reduced Total: ', total)
