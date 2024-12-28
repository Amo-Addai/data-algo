'use strict'

/*

3. Builder + Memento + Synchronization Combo
Why These Patterns Are Combined:

Builder: Separates the construction of a complex object from its representation, allowing the construction process to be controlled step by step.
Memento: Captures and externalizes an object's state so that it can be restored later, typically used for undo functionality or managing state in a controlled manner.
Synchronization: Ensures that shared resources are accessed in a thread-safe manner, which is essential when dealing with concurrent operations or state changes.
Best Scaffolding Pattern: Controlled Object Construction with State Management

This scaffolding pattern works well for systems where you need to build complex objects (via Builder), track and restore object states (via Memento), and ensure thread safety in state modifications (via Synchronization). It's ideal for situations requiring state management and safe construction of objects in a multi-threaded environment.
TypeScript Example:

 */


// Builder - Constructing a product step-by-step

class Product {
    constructor(public name: string, public price: number) {}
}

class ProductBuilder {
    private name: string = ""
    private price: number = 0
    setName = (name: string): this => (
        this.name = name, this
    )
    setPrice = (price: number): this => (
        this.price = price, this
    )
    build = (): Product =>
        !!this.name && !!this.price
        && new Product(this.name, this.price)
}


// Memento - Capturing the state of an object

class ProductMemento {
    constructor(public state: Product) {}
}

class ProductOriginator {
    private product: Product
    constructor(product: Product) {
        this.product = product
    }
    createMemento = (): ProductMemento =>
        new ProductMemento(this.product)
    restore = (memento: ProductMemento): void =>
        (this.product = memento.state, null)
    getProduct = (): Product => this.product
}


// Synchronization - Thread-safe object access

class ThreadSafeProductManager {
    private product: Product | null = null
    private lock = new Mutex() // Mutex class for thread-safe operations

    setProduct = async (product: Product) => (
        await this.lock.lock(),
        this.product = product,
        this.lock.unlock()
    )

    getProduct = async (): Promise<Product | null> => (
        await this.lock.lock(),
        this.product |> (
            this.lock.unlock(),
            % // TODO: Remember to use Babel for compiling the pipeline-operator
        )
    )
}


// ! Usage

const builder = new ProductBuilder()
let product = builder.setName('Product A').setPrice(100).build()

const originator = new ProductOriginator(product)
const memento = originator.createMemento()

const manager = new ThreadSafeProductManager()

manager.setProduct(product).then(() =>
    manager.getProduct().then(product =>
        console.log('Thread-safe product access: ', product?.name || '-')
    )
)

originator.restore(memento)
product = originator.getProduct()

console.log('Restored Product: ', product?.name || '-')
