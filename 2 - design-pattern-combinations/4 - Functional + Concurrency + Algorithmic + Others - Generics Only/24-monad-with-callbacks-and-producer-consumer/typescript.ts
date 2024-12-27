'use strict'

/*

Popular Combinations of Design Patterns in Functional and Concurrency Contexts
Some of the most impactful design pattern combinations for Functional, Concurrency, and Other paradigms often arise from the need to balance immutability, high-performance processing, and effective management of multi-threaded or asynchronous workflows. These combinations are highly relevant in environments where scalability, maintainability, and clarity are prioritized, particularly in TypeScript or JavaScript-based applications.

1. Functional + Concurrency Patterns (Monad, Callbacks, Producer-Consumer)
- Monad + Callbacks + Producer-Consumer Combo
- Producer-Consumer Monad Callback Integration
- Producer-Consumer Monad Callback Coordination
- Asynchronous Task Flow with Monadic State Handling

Why this combination exists:
In modern applications, you often need to process data in a functional way, but also handle concurrency for tasks like network requests or parallel computations. This combination is powerful because Monads allow for handling side-effects (like asynchronous operations), while Callbacks manage those side-effects, and Producer-Consumer ensures data flow in a thread-safe manner.

Key Scaffolding Patterns:
Monad (for chaining functional transformations)
Callbacks (to handle asynchronous operations)
Producer-Consumer (to manage concurrency and flow of data)

Why These Patterns Are Combined:

Monad: Monads help encapsulate side-effects and manage the chaining of operations. In this case, it handles async operations and maintains immutability, ensuring predictable operations in an asynchronous workflow.
Callbacks: These are used for handling asynchronous tasks and responses, enabling the handling of async code flow in an orderly manner.
Producer-Consumer: This pattern helps manage data flow in an asynchronous environment, providing thread-safe data handling while ensuring that data produced by one process is consumed by another in an efficient manner.

Best Scaffolding Pattern: Producer-Consumer Monad Callback Integration

This scaffold integrates Monads with Callbacks and Producer-Consumer to create an asynchronous task pipeline where tasks can be produced, consumed, and chained using Monads to encapsulate side-effects. The flow is controlled with Callbacks, which enable smooth transitions between operations while ensuring concurrency control with Producer-Consumer.

Scaffold Example in TypeScript
Example 1: Monad with Callbacks and Producer-Consumer
This pattern combines Monads (for chaining), Callbacks (to handle async tasks), and Producer-Consumer (to ensure smooth flow of tasks across threads).
This combination is ideal for managing side effects in an asynchronous environment, while also enabling smooth data flow.

TypeScript Example:

 */

// Monad - Encapsulating side-effects
class Task<T> {
    constructor(private value: T) {}

    map: <U>(fn: (value: T) => U) => Task<U>
        = fn => new Task(fn(this.value))

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
