'use strict'

/*

1. Bridge + Adapter + Decorator
Scaffolding: Dynamic Wrapping Scaffold - where objects can adapt and layer additional behaviors dynamically.

The Bridge separates an abstraction from its implementation.
The Adapter connects incompatible interfaces.
The Decorator dynamically adds behavior to objects.
This scaffold allows objects to adapt and layer additional behaviors dynamically.

 */

// Bridge
interface Implementation {
    operation(): void
}

class ConcreteImplementation implements Implementation {
    operation = () => console.log('Implementation 1 .. ')
}

class Abstraction {
    constructor(private implementation: Implementation) {}
    operation = () => this.implementation.operation()
}

class Adapter {
    constructor(private adaptee: Abstraction) {}
    adaptedOperation = () => this.adaptee.operation()
}

class Decorator {
    constructor(private component: Adapter) {}
    decoratedOperation = () => this.component.adaptedOperation()
}

// Usage
const implementation = new ConcreteImplementation()
const abstraction = new Abstraction(implementation)
const adapter = new Adapter(abstraction)
const decorator = new Decorator(adapter)

console.log(decorator.decoratedOperation())
