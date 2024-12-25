'use strict'

/*

3. Builder + Composite + Chain of Responsibility
Why These Patterns Are Combined:

Builder: Provides a flexible way to construct complex objects step by step.
Composite: Allows you to compose objects into tree-like structures, treating individual objects and composites uniformly.
Chain of Responsibility: Enables passing a request along a chain of handlers, allowing multiple handlers to process the request.
Best Scaffolding Pattern: Builder-Composite-ChainOfResponsibility Scaffold

This scaffold is suitable for applications that need flexible and modular construction of complex objects (Builder), hierarchical organization of objects (Composite), and the ability to delegate tasks to different handlers (Chain of Responsibility). It's ideal for UI component libraries or systems requiring dynamic construction and delegation of responsibility.
TypeScript Example:

 */

// Builder
class Car {
    constructor(public model: string, public color: string) {}
}

class CarBuilder {
    private model = ''
    private color = ''

    setModel: (string) => CarBuilder =
        model => (this.model = model, this)

    setColor: (string) => CarBuilder =
        color => (this.color = color, this)

    build: () => Car = () => new Car(this.model, this.color)
}

// Composite
interface Component {
    render(): void
}

class CarComponent implements Component {
    constructor(private name: string) {}
    render = () => console.log(`Rendering ${this.name}`)
}

class CarComposite implements Component {
    private components: Component[] = []

    add = (component: Component) => this.components.push(component)
    render = () => this.components.forEach(component => component.render())
}

// Chain of Responsibility
class CarPartHandler {
    private nextHandler: CarPartHandler | null = null

    setNext: (CarPartHandler) => CarPartHandler =
        handler => (this.nextHandler = handler, handler)

    handle = part => (
        !!this.nextHandler
        ? this.nextHandler.handle(part)
        : console.log(`No handler for ${part}}`)
    )
}

// Usage
const builder = new CarBuilder()
const car = builder.setModel('Sedan').setColor('Red').build()

const engine = new CarComponent('Engine')
const wheels = new CarComponent('Wheels')
const compositeCar = new CarComposite()

compositeCar.add(engine)
compositeCar.add(wheels)
compositeCar.render()

const handler = new CarPartHandler()
const engineHandler = new CarPartHandler()

handler.setNext(engineHandler)
handler.handle('Engine')
