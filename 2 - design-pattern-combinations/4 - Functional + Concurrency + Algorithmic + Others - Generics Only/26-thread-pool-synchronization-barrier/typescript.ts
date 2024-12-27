'use strict'

/*

Popular Combinations of Design Patterns in Functional and Concurrency Contexts
Some of the most impactful design pattern combinations for Functional, Concurrency, and Other paradigms often arise from the need to balance immutability, high-performance processing, and effective management of multi-threaded or asynchronous workflows. These combinations are highly relevant in environments where scalability, maintainability, and clarity are prioritized, particularly in TypeScript or JavaScript-based applications.

3. Concurrency + Generics (Thread Pool, Synchronization, Barrier)
- Thread Pool + Synchronization + Barrier Combo
- Thread Pool Synchronization Barrier Coordination
- Concurrency Control with Task Synchronization

Why this combination exists:
Concurrency patterns like Thread Pool and Barrier are useful for managing parallel workloads, and Generics allow these patterns to be implemented in a type-safe manner. This combination helps in managing resource pools while maintaining scalability and flexibility with type safety.

Key Scaffolding Patterns:
Thread Pool (to manage concurrency efficiently)
Synchronization (to prevent race conditions)
Barrier (to synchronize threads)

Why These Patterns Are Combined:

Thread Pool: This pattern manages a pool of threads that can execute tasks concurrently. It helps manage the overhead of creating new threads by reusing existing ones.
Synchronization: To ensure that multiple threads can work safely together without corrupting shared data, synchronization mechanisms are used. This prevents race conditions and ensures thread safety.
Barrier: A synchronization primitive that ensures all threads reach a certain point before any can proceed. It is particularly useful when you need all tasks to be completed before continuing.
Best Scaffolding Pattern: Thread Pool Synchronization Barrier Coordination

This scaffold utilizes the Thread Pool to manage concurrent tasks efficiently, Synchronization to manage safe access to shared resources, and the Barrier to synchronize multiple threads at a certain point in the execution, ensuring coordinated progress of all threads.

Scaffold Example in TypeScript
Example 3: Thread Pool, Synchronization, Barrier
This combination efficiently manages concurrent threads with a Thread Pool, ensures safe access with Synchronization, and uses Barriers to sync threads.
Provides scalable concurrency management while maintaining type safety and ensuring synchronization across threads.

TypeScript Example:

 */

// Thread Pool using Generics
class ThreadPool<T> {
    private tasks: (() => T)[] = []
    private maxThreads: number

    constructor(maxThreads: number) {
        this.maxThreads = maxThreads
    }

    addTask = (task: () => T) => // * in the basic example below, tasks are async methods (return Promise<any> by default)
        this.tasks.length < this.maxThreads
        ? this.tasks.push(task)
        : console.log('Maxed Threads')

    addAsyncTask = (task: () => Promise<T>) => // async-functions return Promise<any>
        this.tasks.length < this.maxThreads
        ? this.tasks.push(task)
        : console.log('Maxed Threads')

    run = async (promises: Promise<T>[] = []) => (
        ( // TODO: Node.js Team: 'while-loop' ? : ( bool - value not arg ) => { .. } / ( .. )
            // TODO: Also 'switch-case' possibility ? : ( any value / var ) => { val => ..., val => ..., val => ( ... ), ... }
            loop: boolean,
            fn: () => void
        ) => (loop && fn())
        |> %(
            this.tasks.length > 0
            && promises.length < this.maxThreads,
            () => (
                this.tasks.shift()
                |> !!% && promises.push(%())
            )
        ),
        await Promise.all(promises)
    )
}

// Synchronization using a simple lock
class Lock {
    private isLocked: boolean = false

    lock = async () => (
        (
            loop: boolean,
            fn: () => void
        ) => (loop & fn())
        |> %(
            this.isLocked,
            async () => (
                await new Promise(resolve => setTimeout(resolve, 50))
            ) // wait for unlock
        ),
        this.isLocked = true
    )

    unlock = () => (this.isLocked = false)
}

// Barrier for synchronizing threads
class Barrier {
    private count: number
    private resolve: (x?: any) => void = () => {}

    constructor(count: number) {
        this.count = count
    }

    wait = async () => (
        this.count--,
        this.count === 0
        && this.resolve(),
        new Promise<void>(
            resolve => (this.resolve = resolve)
        )
    )
}


// ! Usage

const threadPool = new ThreadPool<any>(2)
const lock = new Lock()
const barrier = new Barrier(3)

threadPool.addTask(() => (
    console.log('Task 0 executed')
))

threadPool.addAsyncTask(async () => (
    await lock.lock(),
    console.log('Task 1 executed'),
    lock.unlock()
))

threadPool.addAsyncTask(async () => (
    await lock.lock(),
    await barrier.wait(), // wait a while (3 seconds) for other threads (Task 1) to continue
    console.log('Task 2 executed'),
    lock.unlock()
))

threadPool.run()
