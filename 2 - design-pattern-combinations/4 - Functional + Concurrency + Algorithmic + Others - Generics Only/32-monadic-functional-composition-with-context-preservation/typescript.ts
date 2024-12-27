'use strict'

/*

1. Monad + Functor + Pure Function Combo
Why These Patterns Are Combined:

Monad: Ensures clean, predictable computation by chaining operations that preserve context.
Functor: Provides a mechanism for mapping over data contained in a structure (e.g., an array or optional value) without altering the structure itself.
Pure Function: Guarantees that functions will not have side effects and always return the same output for the same input, making the system more predictable.
Best Scaffolding Pattern: Functional Composition with Context Preservation

These patterns together ensure that operations can be composed in a predictable way, while maintaining context (through the monad) and keeping transformations functional (via functors and pure functions).
TypeScript Example:

 */

// Monad - Encapsulating a value to chain computations
// Works as a Functor in this case
class Monad<T> {
    constructor(private value: T) {}

    map = <U>(fn: (x: T) => U): Monad<U> =>
        new Monad(fn(this.value))

    flatMap = <U>(fn: (x: T) => Monad<U>): Monad<U> =>
        fn(this.value)

    getValue = (): T => this.value
}

// Pure Function - A function that always produces the same output for the same input (without any side-effects; therefore has no splitting logic-flows)
const add10 (x: number): number => x + 10

// Functor - Applying a transformation (as a pure-function) to a value wrapped inside a Monadic structure
const result = new Monad(5).map(add10).map(add10).map(x => x * 2)

console.log(result.getValue()) // 50
