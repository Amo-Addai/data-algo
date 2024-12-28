'use strict'

/*

2. Decorator + Proxy + Functor Combo
Why These Patterns Are Combined:

Decorator: Adds additional functionality to an object dynamically without altering its core structure.
Proxy: Controls access to an object by intercepting method calls and adding additional behavior, such as lazy loading, logging, or access control.
Functor: Enables you to map a function over a value or structure while preserving the structure, allowing for functional transformations over collections of objects.
Best Scaffolding Pattern: Flexible Object Enhancement and Access Control

This scaffolding pattern works well for systems where you need to enhance objects dynamically (via Decorator), control access to them (via Proxy), and apply functional transformations (via Functor). It ensures that object behaviors are flexible, access is properly managed, and transformations are applied in a functional style.
TypeScript Example:

 */

interface Product {
    name: string
    price: number
    describe(): void
}

// ConcreteProduct already defines interface Product's props: name & price in constructor, then defines .describe()
class ConcreteProduct implements Product {
    constructor(public name: string, public price: number) {}
    describe = () => console.log(`Product: ${this.name}, Price: ${this.price}`)
}

// Decorator - Adds functionality

/*
Both ProductDecorator and ProductProxy accept a Product object in their constructors
and delegate the describe method to this wrapped product.
They rely on the wrapped Product instance to have Product's properties name & price.
TypeScript cannot verify that the wrapped product will always satisfy the Product interface.
So they need to define name or price as properties themselves
 */

class ProductDecorator implements Product {
    name: string
    price: number
    constructor(private product: Product) {}
    describe = () => (
        this.product.describe(),
        console.log('This product is enhanced with additional features.')
    )
}

// Proxy - Controls access to the product
class ProductProxy implements Product {
    name: string
    price: number
    constructor(private product: Product) {}
    describe = () => (
        console.log('Proxy: Accessing product details ... '),
        this.product.describe()
    )
}


// Functor
class Functor<T> {
    constructor(private value: T) {}

    map = <U>(fn: (x: T) => U): Functor<U> =>
        new Functor(fn(this.value))

    getValue = (): T => this.value
}


// ! Usage

const product = new ConcreteProduct('Gadget', 200)
const decoratedProduct = new ProductDecorator(product)
const proxiedProduct = new ProductProxy(decoratedProduct)

proxiedProduct.describe()

const productFunctor = new Functor(product)
const discountedProduct = productFunctor.map(
    p => ({ ...p, price: p.price * 0.8 })
)

console.log(discountedProduct.getValue())
