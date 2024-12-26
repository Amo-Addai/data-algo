'use strict'

/*

3. Iterator + Memento + Visitor Combo
Why These Patterns Are Combined:

Iterator: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
Memento: Captures and externalizes an object's state so that it can be restored later without violating encapsulation.
Visitor: Allows adding new operations to objects without changing their classes, useful for traversing and acting upon elements in a structure.
Best Scaffolding Pattern: State and Element Traversal with External Operations

This scaffolding pattern is perfect for scenarios where you need to traverse through a collection of objects (Iterator), capture and restore the state of these objects (Memento), and apply external operations on these objects (Visitor). This combination is often used in systems where the object structure can change over time, but you want to keep operations modular and state management separate.
TypeScript Example:

 */

// Memento - Captures an object's state
class Memento {
    constructor(public state: string) {}
}

// Iterator - Allows sequential access to elements of a collection
class Iterator<T> {
    private index = 0
    constructor(private collection: T[]) {}

    next: () => T | null = () => (
        this.index < this.collection.length
        ? this.collection[this.index++]
        : null
    )
}

// Visitor - Adds new operations to objects without changing their structure
interface Visitor {
    visitProduct(product: Product): void
}

class ProductVisitor implements Visitor {
    visitProduct = (product: Product) =>
        console.log(`Visiting product: ${product?.state || '-'}`)
}

class Product {
    private state: string
    constructor(state: string) {
        this.state = state
    }
    getState = () => this.state
    createMemento = () => new Memento(this.state)
    restore = (memento: Memento) => (this.state = memento.state)
}


// ! Usage

const products = [
    new Product('Product 1'),
    new Product('Product 2'),
    new Product('Product 3')
]

const iterator = new Iterator(products)
const visitor = new ProductVisitor()

let product, memento
while (
    (product = iterator.next())
) {
    visitor.visitProduct(product)
    memento = product.createMemento()
    product.restore(
        new Memento('Restored Product')
    )
}
