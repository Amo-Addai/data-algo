'use strict'

/*

2. Producer-Consumer + Synchronization + Thread Pool Combo
Why These Patterns Are Combined:

Producer-Consumer: Efficiently manages the flow of data between tasks (producers and consumers).
Synchronization: Ensures that shared resources are accessed safely, preventing race conditions.
Thread Pool: Reuses a fixed number of threads for executing tasks, improving performance by reducing overhead.
Best Scaffolding Pattern: Thread Pool with Synchronization for Producer-Consumer Workflow

Thread Pool helps manage the concurrent execution of tasks, Synchronization ensures safe access to shared resources, and the Producer-Consumer pattern efficiently divides the workload between producers and consumers.
TypeScript Example:

 */

class ThreadPool {
    private pool: (() => void)[] = []
    private maxThreads: number
    private runningThreads = 0

    constructor(maxThreads: number) {
        this.maxThreads = maxThreads
    }

    addTask = (task: () => void) => (
        this.pool.push(task),
        this.runTasks()
    )

    private runTasks = () => (
        (
            this.runningThreads >= this.maxThreads
            || this.pool.length === 0
        ) ? null
        : (
            this.pool.shift()
            |> !!%
            && (
                this.runningThreads++,
                %(),
                setTimeout(() => (
                    this.runningThreads--,
                    this.runTasks()
                ), 100)
            )
        )
    )
}

class ProducerConsumer {
    private queue: number[] = []
    private lock: boolean = false

    addItem = item => this.queue.push(item)

    consumeItem = () => (
        (
            this.queue.length === 0
            || this.lock
        ) ? null
        : (
            this.lock = true,
            this.queue.shift() |> console.log('Consuming: ', %),
            setTimeout(() => (
                this.lock = false,
                this.consumeItem()
            ), 500)
        )
    )
}


// ! Usage

const threadPool = new ThreadPool(2)
const producerConsumer = new ProducerConsumer()

threadPool.addTask(() => (
    producerConsumer.addItem(1),
    producerConsumer.addItem(2)
))

threadPool.addTask(() => producerConsumer.consumeItem())
