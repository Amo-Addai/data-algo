'use strict'

/*

4. Functor + Callbacks + Multi-Threading Combo
Why These Patterns Are Combined:

Functor: Allows functions to be mapped over data inside containers, maintaining a clean and functional flow of operations.
Callbacks: Provides an asynchronous mechanism for execution, ensuring that functions are executed after an operation completes.
Multi-Threading: Enables parallel execution of tasks, improving performance in concurrent environments.
Best Scaffolding Pattern: Asynchronous Functional Data Transformation

This combination supports functor-based data transformations, handles asynchronous execution with callbacks, and boosts multi-threading to improve performance in parallel processing scenarios.
TypeScript Example:

 */

class Functor<T> {
    constructor(private value: T) {}

    map = <U>(fn: (x: T) => U): Functor<U> =>
        new Functor(fn(this.value))

    getValue = (): T => this.value
}

// Callback Function
const delayCallback = (
    value: number,
    cb: (result: number) => void
) => setTimeout(
    () => cb(value * 2), 1000
)

// Multi-Threading
const simulateWorker = (task: () => void) =>
    setTimeout(() => task(), 500)


// ! Usage

const functor = new Functor<number>(10)

const result = functor.map(x => x * 2).map(x => x + 3)
console.log(result.getValue())

simulateWorker(() => delayCallback(5, result => console.log(`Callback result: ${result}`)))
