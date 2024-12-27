'use strict'

/*

2. Producer-Consumer + Synchronization + Barrier Combo
Why These Patterns Are Combined:

Producer-Consumer: Separates the task creation (producer) from task consumption (consumer), often used for handling data streams or task queues.
Synchronization: Controls access to shared resources to ensure thread safety and avoid race conditions.
Barrier: Synchronizes multiple threads, ensuring they reach a certain point before proceeding further. This is useful for cases where you need threads to coordinate at specific stages.
Best Scaffolding Pattern: Task Coordination with Safe Resource Management

This scaffolding pattern is perfect for applications where multiple threads work on tasks concurrently and must synchronize at key points while ensuring that resource contention does not occur. For example, in a server handling requests, where threads wait for all data to be prepared before processing.
TypeScript Example:

 */

// Producer-Consumer - Simple task queue system
class TaskQueue {
    private queue: (() => void)[] = []
    private lock = false

    addTask = (task: () => void) => (
        this.queue.push(task),
        this.processQueue()
    )

    private processQueue = () => (
        (
            this.lock
            || !this.queue.length
        ) ? null
        : (
            this.queue.shift()
            |> (
                !!% && (
                    this.lock = true,
                    %(),
                    setTimeout(() => (
                        this.lock = false,
                        this.processQueue()
                    ), 100)
                )
            )
        )
    )
}

// Barrier - Synchronizes threads at a specific point
class Barrier {
    private count: number
    private resolve: (x?: any) => void = () => {}

    constructor(count: number) {
        this.count = count
    }

    wait = () => (
        this.count--,
        this.count === 0
        && this.resolve(),
        new Promise<void>(resolve =>
            (this.resolve = resolve)
        )
    )
}

// Synchronization with Barrier and Producer-Consumer
const taskQueue = new TaskQueue()
const barrier = new Barrier(2)

// Producer
taskQueue.addTask(() => (
    console.log('Task 1: Preparing data ..'),
    barrier.wait().then(() => console.log('Task 1: Processing completed.'))
))

// Producer
taskQueue.addTask(() => (
    console.log('Task 2: Preparing data .. '),
    barrier.wait().then(() => console.log)('Task 2: Processing completed.')
))

// Synchronizing tasks using barrier
barrier.wait().then(() => console.log('All tasks prepared, proceeding with processing.'))
