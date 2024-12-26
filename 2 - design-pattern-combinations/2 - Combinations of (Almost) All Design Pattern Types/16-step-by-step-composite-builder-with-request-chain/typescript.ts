'use strict'

/*

3. Builder + Composite + Chain of Responsibility Scaffold
Why These Patterns Are Combined:

Builder: Helps construct complex objects step by step, enabling different representations.
Composite: Manages tree-like structures, allowing clients to treat individual objects and compositions uniformly.
Chain of Responsibility: Passes requests along a chain of handlers, allowing each handler to process or forward the request.
Best Scaffolding Pattern: Step-by-Step Composite Builder with Request Chain

This scaffold allows complex objects to be constructed in stages (Builder), composed into tree-like structures (Composite), and processed through a chain of handlers (Chain of Responsibility).
TypeScript Example:

 */

interface Component {
    operation(): void
}

class Leaf implements Component {
    constructor(private name: string) {}
    operation = () => console.log(`Leaf: ${this.name}`)
}

class Composite implements Component {
    private children: Component[] = []
    add = (child: Component) => this.children.push(child)
    operation = () => console.log(`Composite: [${this.children.map(child => child.operation()).join(', ')}]`)
}

class ComponentBuilder {
    private root: Composite = new Composite()
    addLeaf: (string) => ComponentBuilder =
        name => (this.root.add(new Leaf(name)), this)
    build: () => Composite = () => this.root
}

// Chain of Responsibility Handlers
interface Handler {
    setNext(handler: Handler): Handler
    handle(request: string): void
}

class ConcreteHandlerA implements Handler {
    private nextHandler: Handler | null = null

    setNext: (Handler) => Handler =
        handler => (this.nextHandler = handler, handler)

    handle = request => (
        request === 'A'
        ? console.log('Handler A processing request')
        : !!this.nextHandler
        && this.nextHandler.handle(request)
    )
}

class ConcreteHandlerB implements Handler {
    private nextHandler: Handler | null = null

    setNext: (Handler) => Handler =
        handler => (this.nextHandler = handler, handler)

    handle = request => (
        request === 'B'
        ? console.log('Handler B processing request')
        : !!this.nextHandler
        && this.nextHandler.handle(request)
    )
}


// ! Usage

const builder = new ComponentBuilder()
builder.addLeaf('Leaf 1').addLeaf('Leaf 2')

const composite = builder.build()
console.log(composite.operation())

const handlerA = new ConcreteHandlerA()
const handlerB = new ConcreteHandlerB()

handlerA.setNext(handlerB)
handlerA.handle('B')
