// 'use strict'

/*

1. Functor + Monad + Pure Function Combo
Why These Patterns Are Combined:

Functor: Transforms values inside a container while preserving the structure, which allows for composable transformations.
Monad: Extends the functor concept by allowing chaining operations, and ensuring that computations are context-preserving.
Pure Function: Ensures predictability and consistency by avoiding side effects, which is essential for functional programming patterns.
Best Scaffolding Pattern: Functional Composition with Contextual Operations

These patterns are ideal for situations where you want to work with predictable, composable, and side-effect-free transformations of data inside a container (like a monad). This scaffolding pattern is commonly used in functional programming to maintain data flow consistency and compose operations cleanly.
TypeScript Example:

 */

// Functor Implementation
class Functor<T> {
    constructor(private value: T) {}

    map = <U>(fn: (x: T) => U): Functor<U> =>
        new Functor(fn(this.value))

    getValue = (): T => this.value
}

// Monad Implementation - extends Functor
// Monad is basically a Functor that can flatten its mapped value (& other features)
class Monad<T> extends Functor<T> {

    // ! Override (explicitly returning Monad<U>) not required
    // * due 'as' type-casting on usage (after calling super.map(add1) )
    // ! 'as Monad<T>' type-casting; NOT (Monad<T>) type-casting

    // override map = <U>(fn: (x: T) => U): Monad<U> =>
    //     new Monad<U>(fn(this.getValue()))

    flatMap = <U>(fn: (x: T) => Monad<U>): Monad<U> =>
        fn(this.getValue()) // .value - parent private prop
}


// Pure Functions

const add1 = (x: number): number => x + 1
const mult2 = (x: number): number => x * 2


// ! Usage

const monad = new Monad<number>(5)

const result1 = (
    monad.map(add1) as Monad<number> // * cast returned Functor back to Monad, for .flatMap()
).flatMap(x => new Monad(mult2(x)))

console.log(result1.getValue())

const result2 = (
        monad.map<number>(add1) as Monad<number>
    )
    .flatMap<number>(
        (x: number) =>
            new Monad<number>(mult2(x))
    )

console.log(result2.getValue())


// ! Fluent Interface solution to .map override / type-cast
// * Redesigning Functor & Monad to support Fluent Chaining, with proper return types

class Functor<T> {
    constructor(private value: T) {}

    map = <U>(fn: (x: T) => U): this => (
        this.value = fn(this.value),
        this
    )

    getValue = (): T => this.value
}

class Monad<T> extends Functor<T> {
    flatMap = <U>(fn: (x: T) => Monad<U>): this => (
        fn(this.getValue()) as this
    )
}


// ! Usage

const monad1 = new Monad(5)

const result3 = monad1
    .map(add1)
    // ! This time: x (unknown data-type) arg in this case raises an error on mult(x) call
    // * most-likely due to fluent interfaced 'this'-context return-value across parent .map & child .flatMap methods
    /* // TODO: Confirm
        'this' object before this.flatMap call being the parent-child context of Functor-Monad could be raising ambiguity
        that might require strict typing in lambda passed in on this.flatMap

        * NB: x's strict typing not required in first usage example, with type-casting & not a Fluent Interface
     */
    // .flatMap(x => new Monad(mult2(x)))
    .flatMap((x: number) => new Monad(mult2(x)))

console.log(result3.getValue())

const monad2 = new Monad<number>(10)

const result4 = monad2
    .map<number>(add1)
    .flatMap<number>(
        (x: number) =>
            new Monad<number>(mult2(x))
    )

console.log(result4.getValue())
