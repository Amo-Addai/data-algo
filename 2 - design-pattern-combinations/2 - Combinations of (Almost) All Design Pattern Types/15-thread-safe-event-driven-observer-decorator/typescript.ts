'use strict'

/*

2. Decorator + Observer + Synchronization Scaffold
Why These Patterns Are Combined:

Decorator: Adds functionality to existing objects dynamically.
Observer: Allows objects to subscribe and react to events or state changes.
Synchronization: Ensures thread-safe operations when multiple threads access shared resources.
Best Scaffolding Pattern: Thread-Safe Event-Driven Observer Decorator

This scaffold allows you to dynamically add functionality to objects (Decorator), while observing and reacting to events in a thread-safe manner (Observer and Synchronization).
TypeScript Example:

 */

interface Observer {
    update(data: string): void
}

class ConcreteObserver implements Observer {
    update = data => console.log(`Received data: ${data}`)
}

interface Subject {
    addObserver(observer: Observer): void
    removeObserver(observer: Observer): void
    notifyObservers(): void
}

class ConcreteSubject implements Subject {
    private observers: Observer[] = []
    private state: string = ''private

    addObserver = (observer: Observer) => this.observers.push(observer)
    removeObserver = (observer: Observer) =>
        (this.observers = this.observers.filter(o => o !== observer))
    notifyObservers = () => this.observers.forEach(observer => observer.update(this.state))
    setState = state => (this.state = state, this.notifyObservers())
}

// Synchronization using Mutex
class SynchronizedSubject extends ConcreteSubject {
    private mutex: boolean = false

    setState = state => (
        !!this.mutex ? null // Prevent concurrent state updates
        : (
            this.mutex = true,
            super.setState(state),
            this.mutex = false
        )
    )
}

// Logging Decorator to enhance functionality
class LoggingDecorator implements Observer {
    constructor(private observer: Observer) {}
    update = data => (
        console.log(`Logging data: $data`),
        this.observer.update(data)
    )
}


// ! Usage

const subject = new SynchronizedSubject()
const observer = new ConcreteObserver()
const loggingObserver = new LoggingDecorator(observer)

subject.addObserver(loggingObserver)
subject.setState('New Event')
