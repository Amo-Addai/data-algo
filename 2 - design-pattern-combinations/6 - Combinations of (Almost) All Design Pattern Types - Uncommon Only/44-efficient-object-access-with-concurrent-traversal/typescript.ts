'use strict'

/*

2. Proxy + Multi-Threading + Iterator Combo
Why These Patterns Are Combined:

Proxy: Controls access to an object by adding additional behavior (e.g., lazy loading, access control, logging).
Multi-Threading: Allows for the concurrent execution of tasks, making it possible to handle multiple threads of execution efficiently and in parallel.
Iterator: Provides a way to access elements of a collection sequentially, enabling traversal of collections without exposing their internal structure.
Best Scaffolding Pattern: Efficient Object Access with Concurrent Traversal

This scaffolding pattern is perfect for scenarios where you need to manage access to resources (via Proxy), process tasks concurrently (via Multi-Threading), and traverse large datasets or collections in a controlled manner (via Iterator). It provides a way to efficiently manage both object access and large-scale data processing while maintaining separation of concerns.
TypeScript Example:

 */

class Product {
    constructor(public name: string, public price: number) {}
    describe = () => console.log(`Product: ${this.name}, Price: ${this.price}`)
}

class ProductProxy {
    private product: Product | null = null
    constructor(private name: string) {}
    private loadProduct = () => (
        !!this.product || (
            this.product = new Product(
                this.name,
                Math.floor(Math.random() * 100)
            ),
            console.log('Product loaded.')
        )
    )
    describe = () => (
        this.loadProduct(),
        this.product?.describe()
    )
}


// Multi-Threading - Simulated with async/await & Promises
const fetchProductData = async name =>
    new Promise<Product>(resolve =>
        setTimeout(() =>
            resolve(new Product(name, Math.floor(Math.random() * 100)))
        , 1000)
    )


// Iterator - Provides sequential access to collection
class ProductIterator {
    private index = 0
    constructor(private products: Product[]) {}

    next = (): Product | null =>
        this.index < this.products.length
        && this.products[this.index++]
}


// ! Usage

const proxy = new ProductProxy('Product A')
proxy.describe()

const products = [
    new Product('Product 1', 50),
    new Product('Product 2', 60),
    new Product('Product 3', 70)
]

const iterator = new ProductIterator(products)

let currentProduct
while (currentProduct = iterator.next()) {
    console.log(`Iterating product: ${currentProduct?.name || '-'}`)
    currentProduct = iterator.next()
}
