'use strict'

/*

2. Decorator + Proxy + Wrapper Combo
Why These Patterns Are Combined:

Decorator: Adds new behavior to an object dynamically by wrapping it in a decorator, without altering the original object.
Proxy: Controls access to another object, typically to add lazy initialization, logging, or access control.
Wrapper: Similar to Proxy but focused on simplifying interfaces by encapsulating complexities and providing a consistent API.
Best Scaffolding Pattern: Extensible Object Modification and Access Control

This scaffolding pattern is useful when you want to add functionality to an object dynamically (Decorator), control its access or modify its behavior (Proxy), and simplify its interface (Wrapper) while keeping the core logic intact. This combination allows for flexible and reusable object enhancements, access control, and abstraction.
TypeScript Example:

 */

interface Product {
    describe(): void
}

class ConcreteProduct implements Product {
    describe = () => console.log('This is a concrete product')
}

// Decorator - Adds additional functionality to an object
class ProductDecorator implements Product {
    constructor(private product: Product) {}
    describe = () => (
        this.product.describe(),
        console.log('This product has been decorated')
    )
}

// Proxy - Controls access to the product
class ProductProxy implements Product {
    constructor(private product: Product) {}
    describe = () => (
        console.log('Proxy: Accessing product'),
        this.product.describe()
    )
}

// Wrapper - Simplifies the interface of the product
class ProductWrapper implements Product {
    constructor(private product: Product) {}
    describe = () => (
        console.log('Wrapper: Simplified description:'),
        this.product.describe()
    )
}


// ! Usage

const concreteProduct = new ConcreteProduct()
const decoratedProduct = new ProductDecorator(concreteProduct)
const proxyProduct = new ProductProxy(decoratedProduct)
const wrapperProduct = new ProductWrapper(proxyProduct)
wrapperProduct.describe()
