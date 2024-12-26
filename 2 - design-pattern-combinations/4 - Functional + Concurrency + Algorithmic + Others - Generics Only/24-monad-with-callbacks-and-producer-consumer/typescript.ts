'use strict'

/*

Popular Combinations of Design Patterns in Functional and Concurrency Contexts
Some of the most impactful design pattern combinations for Functional, Concurrency, and Other paradigms often arise from the need to balance immutability, high-performance processing, and effective management of multi-threaded or asynchronous workflows. These combinations are highly relevant in environments where scalability, maintainability, and clarity are prioritized, particularly in TypeScript or JavaScript-based applications.

1. Functional + Concurrency Patterns (Monad, Callbacks, Producer-Consumer)
Why this combination exists:
In modern applications, you often need to process data in a functional way, but also handle concurrency for tasks like network requests or parallel computations. This combination is powerful because Monads allow for handling side-effects (like asynchronous operations), while Callbacks manage those side-effects, and Producer-Consumer ensures data flow in a thread-safe manner.

Key Scaffolding Patterns:
Monad (for chaining functional transformations)
Callbacks (to handle asynchronous operations)
Producer-Consumer (to manage concurrency and flow of data)

Scaffold Example in TypeScript
Example 1: Monad with Callbacks and Producer-Consumer
This pattern combines Monads (for chaining), Callbacks (to handle async tasks), and Producer-Consumer (to ensure smooth flow of tasks across threads).
This combination is ideal for managing side effects in an asynchronous environment, while also enabling smooth data flow.

 */

// Monad - Encapsulating side-effects
class Task<T> {
    constructor(private value: T) {}

    map: <U>(fn: (value: T) => U) => Task<U>
        = fn =>  new Task(fn(this.value))

    // Chain tasks
    flatMap: <U>(fn: (value: T) => Task<U>) => Task<U>
        = fn => fn(this.value)
}

// Callbacks
const asyncTask: (cb: (string) => void) => void
    = cb => setTimeout(() => cb('Data from async task'), 1000)

// Producer-Consumer pattern using queues
class TaskQueue {
    private queue: string[] = []
    private isProcessing = false

    enqueue = task => (
        this.queue.push(task),
        this.process()
    )

    private process = async () => (
        (this.isProcessing || this.queue.length === 0)
        ? null
        : (
            this.isProcessing = true,
            this.queue.shift()
            |> !!% // * outer-scope for piped-operator not required (&& 1-liner)
            && (
                console.log('Processing: ', %),
                await new Promise(
                    resolve => setTimeout(resolve, 500)
                )
            ),
            this.isProcessing = false,
            this.process()
        )
    )
}


// ! Usage

const taskQueue = new TaskQueue()
taskQueue.enqueue('Task 1')

const monadTask = new Task('Initial Value')
    .map(value => `${value} processed`)
    .flatMap(value => new Task(`${value} further processed`))

asyncTask(data => console.log(data))
