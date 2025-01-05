'use strict'

/*

4. Barrier + Read-Write Lock + Synchronization Combo
Why These Patterns Are Combined:

Barrier: Ensures that multiple threads wait for each other to reach a certain point before proceeding.
Read-Write Lock: Allows multiple readers but only one writer, optimizing for scenarios where data is read frequently but written less often.
Synchronization: Ensures that critical sections are safely accessed by only one thread at a time.
Best Scaffolding Pattern: Concurrency Control with Read-Write Lock and Barrier

Read-Write Lock allows efficient concurrent reads while ensuring exclusive writes, Barrier ensures that threads are synchronized, and Synchronization manages access to shared resources safely.
TypeScript Example:

 */

class ReadWriteLock {
    private readCount = 0
    private writeCount = 0

    acquireReadLock = () => (
        (
            shouldLoop: (any) => boolean,
            fn: (any) => void,
            init = {},
            [iter] = []
        ) => (
            iter = x => shouldLoop(x) ? iter(fn(x)) : x,
            iter(init)
        ) |> %(
            shouldLoop: ({ loop: !!this.writeCount }) => !!loop,
            fn: () => setTimeout(() => this.writeCount--, 100)
        ),
        this.readCount++
    )

    releaseReadLock = () => this.readCount--

    acquireWriteLock = () => (
        (
            shouldLoop: (any) => boolean,
            fn: (any) => void,
            init = {},
            [iter] = []
        ) => (
            iter = x => shouldLoop(x) ? iter(fn(x)) : x,
            iter(init)
        )
        |> %(
            shouldLoop: ({
                loop = this.readCount > 0
                || this.writeCount > 0
            }) => !!loop,
            fn: () => setTimeout(() => (this.readCount--, this.writeCount--), 100)
        ),
        this.writeCount++
    )

    releaseWriteLock = () => this.writeCount--
}

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
        new Promise<void>(resolve => (this.resolve = resolve))
    )
}


// ! Usage

const lock = new ReadWriteLock()

lock.acquireReadLock()
console.log('Reading data')
lock.releaseReadLock()

// TODO: Add more examples for: acquireWriteLock, releaseWriteLock

const barrier = new Barrier(3)
barrier.wait()
       .then(() => console.log('All threads reached the barrier'))
