'use strict'

/*

3. Iterator + Memento + Generics Combo
Why These Patterns Are Combined:

Iterator: Provides a mechanism to traverse through a collection of objects without exposing the underlying representation.
Memento: Captures and externalizes an object's state so that it can be restored later without violating encapsulation.
Generics: Allows the creation of reusable and type-safe components that can work with any type of data or object, making the solution flexible and scalable.
Best Scaffolding Pattern: State Management and Traversal with Flexibility

This scaffolding pattern is useful for scenarios where you need to traverse collections (via Iterator), capture and restore the state of objects (via Memento), and ensure that your solution works with any data type (via Generics). It provides the flexibility of type-safe handling and state management in traversable collections.
TypeScript Example:

 */

// Memento - Captures an object's state
class Memento<T> {
    constructor(public state: T) {}
}

// Iterator - Allows sequential access to elements of a collection
class Iterator<T> {
    private index = 0
    constructor(private collection: T[]) {}

    next = (): T | null => (
        this.index < this.collection.length
        && this.collection[this.index++],
        null
    )
}

// Product Object - its state will be saved by Memento
class Product {
    constructor(public name: string, public price: number) {}

    createMemento = () => new Memento(this)

    restore = (memento: Memento<Product>) => (
        this.name = memento.state.name,
        this.price = memento.state.price
    )
}


// Generics-based containers

// 'still useless' Option (products - 1 expected type argument - Product)
class ProductCollection<T> {
    constructor(private products: T[]) {}
    getIterator = () => new Iterator<T>(this.products)
}

// Properly Generic Option
class Collection<T> {
    constructor(private items: T[]) {}
    getIterator = () => new Iterator<T>(this.items)
}


// ! Usage

const product1 = new Product('Product 1', 100)
const product2 = new Product('Product 2', 100)

const products = new ProductCollection([product1, product2]) // unnecessary
const items = new Collection<Product>([product1, product2])

const iterator = items.getIterator()

let currentProduct: Product, memento
while ((currentProduct = iterator.next() as Product)) {
    console.log(`Traversing: ${currentProduct?.name || '-'} - $${currentProduct?.price || '-'}`)

    memento = currentProduct.createMemento()

    currentProduct.price = 120 // change state
    console.log(`'price' State changed to: $${currentProduct?.price || '-'}`)

    currentProduct.restore(memento)
    console.log(`'price' State restored to: $${currentProduct?.price || '-'}`)
}
