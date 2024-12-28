'use strict'

/*

1. Abstract Factory + Functor + Algorithmic - BigO Combo
Why These Patterns Are Combined:

Abstract Factory: Provides a way to create families of related objects without specifying their concrete classes, ensuring that objects from a specific family can be created with consistency.
Functor: Helps apply functions to wrapped values (like objects or arrays) in a structured way, allowing functional transformations of data while maintaining the structure.
Algorithmic - BigO: Focuses on the efficiency of algorithms, ensuring the system performs well by optimizing time complexity (BigO), especially when dealing with large datasets.
Best Scaffolding Pattern: Efficient and Flexible Object Creation and Transformation

This scaffolding pattern works great for systems where you need both flexible and efficient object creation (via Abstract Factory), functional transformations on data (via Functor), and optimized performance for large-scale data (via BigO). It enables modular, performant, and scalable solutions that can handle complex data transformations efficiently.
TypeScript Example:

 */

interface Product {
    name: string
    price: number
}

interface ProductFactory {
    createProduct(): Product
}

class ConcreteProductA implements Product {
    name = 'Product A'
    price = 100
}

class ConcreteProductB implements Product {
    name = 'Product B'
    price = 150
}

class ProductFactoryA implements ProductFactory {
    createProduct = (): Product =>
        new ConcreteProductA()
}

class ProductFactoryB implements ProductFactory {
    createProduct = (): Product =>
        new ConcreteProductB()
}

class Functor<T> {
    constructor(private value: T) {}
    map = <U>(fn: (x: T) => U): Functor<U> =>
        new Functor(fn(this.value))
    getValue = (): T => this.value
}


// Algorithmic - BigO - Optimized processing
const optimizedSort = (data: number[]): number[] =>
    data.sort((a, b) => a - b) // Quick Sorting with Big O(n log n)


// ! Usage

const factory = new ProductFactoryA()
const product = factory.createProduct()

const productFunctor = new Functor<Product>(product)
const discountedProduct =
    productFunctor.map(
        p => ({ ...p, price: p.price * 0.9 })
    )

console.log('Discounted Product: ', discountedProduct.getValue())

// Optimized data processing
const numbers = [5, 1, 3, 8, 2]
const sortedNumbers = optimizedSort(numbers)

console.log(sortedNumbers)
