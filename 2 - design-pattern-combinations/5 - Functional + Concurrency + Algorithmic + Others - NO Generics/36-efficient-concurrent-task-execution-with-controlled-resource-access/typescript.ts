'use strict'

/*

3. Thread Pool + Synchronization + Multi-Threading Combo
Why These Patterns Are Combined:

Thread Pool: Manages a set of worker threads, improving performance by reusing threads rather than creating new ones.
Synchronization: Ensures that the shared data is safely accessed and manipulated by multiple threads.
Multi-Threading: Runs tasks in parallel, improving performance and responsiveness by executing multiple tasks concurrently.
Best Scaffolding Pattern: Efficient Concurrent Task Execution with Controlled Resource Access

This scaffolding pattern is ideal when you want to efficiently manage concurrent tasks with a limited number of threads and need synchronization to avoid issues like race conditions or deadlocks.
TypeScript Example:

 */

// Thread Pool Implementation
class ThreadPool {
    private tasks: (() => void)[] = []
    private maxThreads: number
    private activeThreads = 0

    constructor(maxThreads: number) {
        this.maxThreads = maxThreads
    }

    addTask = (task: () => void) => (
        this.tasks.push(task),
        this.runTasks()
    )

    private runTasks = () => (
        (
            this.activeThreads < this.maxThreads
            && !!this.tasks.length
        ) && (
            this.tasks.shift()
            |> (
                !!% && (
                    this.activeThreads++,
                    %(),
                    setTimeout(() => (
                        this.activeThreads--,
                        this.runTasks()
                    ), 100)
                )
            )
        )
    )
}

// Synchronization - Protect shared resource access
class SharedResource {
    private lock = false

    access = () => (
        this.lock
        ? console.log('Resource is locked, waiting ... ')
        : (
            this.lock = true,
            console.log('Accessing resource ... '),
            setTimeout(() => (
                this.lock = false,
                console.log('Resource released.')
            ), 1000)
        )
    )
}


// ! Usage

const pool = new ThreadPool(2)
const sharedResource = new SharedResource()

pool.addTask(() => sharedResource.access())
pool.addTask(() => sharedResource.access())
pool.addTask(() => sharedResource.access())
