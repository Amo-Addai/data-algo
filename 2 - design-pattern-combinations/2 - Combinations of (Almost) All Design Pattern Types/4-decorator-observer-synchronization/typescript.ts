'use strict'

/*

2. Decorator + Observer + Synchronization
Why These Patterns Are Combined:

Decorator: Adds additional functionality to an object dynamically, without modifying its structure.
Observer: Enables one-to-many dependencies, where changes in one object can notify other dependent objects.
Synchronization: Ensures thread safety by controlling access to shared resources.
Best Scaffolding Pattern: Decorator-Observer-Synchronization Scaffold

This scaffold pattern is perfect for systems where you need to dynamically enhance an object’s functionality (Decorator), allow multiple observers to listen to changes (Observer), and maintain thread safety (Synchronization). It's ideal for event-driven systems with concurrent operations.
TypeScript Example:

 */

interface Observer {
    update(message: string): void
}

class ConcreteObserver implements Observer {
    update = message => console.log(`Observer received: ${message}`)
}

class Subject {
    private observers: Observer[] = []

    addObserver = (observer: Observer, index = -1) => (
        index = this.observers.indexOf(observer),
        index == -1 || this.observers.splice(index, 1)
    )

    notifyObservers = () => this.observers.forEach(observer => observer.update('Notification'))
}

class NotificationDecorator extends Subject {
    constructor(private subject: Subject) { super() }

    notifyObservers = () => (
        super.notifyObservers(),
        console.log('NotificationDecorator: Adding additional behavior before notifying observers.'),
        this.subject.notifyObservers()
    )
}

class SynchronizedSubject {
    private lock = false

    constructor(private subject: Subject) {}

    notifyObservers: () => Promise<void> = async (whileFn = null) => (
        whileFn = (
            shouldLoop: () => boolean,
            fn: (any) => void,
            init = {},
            [iter] = []
        ) => (
            iter = x =>
                shouldLoop(x) ? iter(fn(x)) : x,
            iter(init)
        ),
        whileFn(
            shouldLoop: ({ loop = this.lock }) => !!loop,
            fn: () => (new Promise(resolve => setTimeout(resolve, 10))).then(res => (this.lock = true))
        ),
        // Iterator not required because fn only returns a Promised-Timeout
        this.lock = true,
        this.subject.notifyObservers(),
        this.lock = false
    )
}


// ! Usage

const subject = new Subject()
const observer1 = new ConcreteObserver()
const observer2 = new ConcreteObserver()

subject.addObserver(observer1)
subject.addObserver(observer2)

const synchronizedSubject1 = new SynchronizedSubject(subject)
const synchronizedSubject2 = new SynchronizedSubject(new NotificationDecorator(subject))

synchronizedSubject1.notifyObservers()
synchronizedSubject2.notifyObservers()
