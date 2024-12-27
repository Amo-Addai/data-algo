'use strict'

/*

3. Monad + Callbacks + Multi-Threading Combo
Why These Patterns Are Combined:

Monad: Encapsulates computation, particularly when there are potential side effects, and allows for chaining operations.
Callbacks: Used to handle asynchronous operations, especially when waiting for tasks to complete.
Multi-Threading: Utilizes multiple threads to execute operations concurrently, improving performance for CPU-bound tasks.
Best Scaffolding Pattern: Asynchronous Monad for Threaded Execution with Callbacks

The Monad encapsulates async operations and side effects, while Callbacks handle task completion asynchronously, and Multi-Threading speeds up execution by leveraging multiple threads.
TypeScript Example:

 */

// Monad - a container for encapsulating async tasks
class AsyncMonad<T> {
    constructor(private value: T) {}

    map = <U>(fn: (value: T) => U): AsyncMonad<U> =>
        new AsyncMonad(fn(this.value))

    flatMap = <U>(fn: (value: T) => AsyncMonad<U>): AsyncMonad<U> =>
        fn(this.value)

    execute = (cb: (value: T) => void): void => (
        setTimeout(() => cb(this.value), 1000), // returns number
        null // so explicitly return null (for void return-type)
    )
}

// Multi-Threading - Simple simulation using Web Workers
const threadTask = (task: () => void) => (
    new Worker(
        URL.createObjectURL(
            new Blob(
                [
                    `(${task.toString()})()`
                ]
            )
        )
    )
    |> (
        %.onmessage = e => console.log('Task Completed: ', e.data)
    )
)


// ! Usage Example - Creating a Monad that uses Multi-Threading and Callbacks

const monadTask = new AsyncMonad<number>(5)
    .map(value => value * 2)
    .flatMap(value => new AsyncMonad(value + 3))

monadTask.execute(value => console.log('Final Result: ', value)) // Output: Final Result: 13

// Multi-Threading Usage with Web Workers
threadTask(() => postMessage('Threaded Task Completed'))
