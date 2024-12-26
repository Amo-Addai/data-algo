'use strict'

/*

3. Observer + Mediator + Chain of Responsibility
Why These Patterns Are Combined:

Observer ensures notifications among subscribers.
Mediator coordinates interactions between objects.
Chain of Responsibility allows dynamic handling of requests.
Best Scaffolding Pattern: Event Dispatch Scaffold

Observers subscribe to a Mediator that dispatches requests to a chain of handlers.
TypeScript Example:

 */

interface Observer {
    update(message: string): void
}

class ConcreteObserver implements Observer {
    update = message => console.log(`Observer received: ${message}`)
}

class Mediator {
    private observers: Observer[] = []

    addObserver = (observer: Observer) => this.observers.push(observer)
    notify = message => this.observers.forEach(observer => observer.update(message))
}

// Chain of Responsibility
abstract class Handler {
    private nextHandler?: Handler

    setNext: (handler: Handler) => Handler = handler => (
        this.nextHandler = handler, handler
    )

    handle = request => !!this.nextHandler && this.nextHandler.handle(request)
}

class ConcreteHandler extends Handler {
    handle = request => (
        console.log(`Handling request: ${request}`),
        super.handle(request)
    )
}

class EventDispatch {
    private mediator = new Mediator()
    private rootHandler = new ConcreteHandler()

    registerObserver = (observer: Observer) => this.mediator.addObserver(observer)

    addHandler = (handler: Handler) => this.rootHandler.setNext(handler)

    processEvent = message => (
        this.mediator.notify(message),
        this.rootHandler.handle(message)
    )
}


// ! Usage

const dispatcher = new EventDispatch()
dispatcher.registerObserver(new ConcreteObserver())

const handler = new ConcreteHandler()

dispatcher.addHandler(handler)
dispatcher.processEvent('Test Event')
