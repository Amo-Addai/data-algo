'use strict'

/*

1. Abstract Factory + Functional-Units + Map-Reduce Combo
Why These Patterns Are Combined:

Abstract Factory: Provides a way to create families of related objects without specifying their concrete classes, enabling flexibility in product creation.
Functional-Units: Organizes code into small, reusable functions that follow the principles of functional programming, making it easier to compose and maintain.
Map-Reduce: A powerful pattern for processing large datasets by mapping a function over each element and reducing the results, commonly used for data transformations and aggregations.
Best Scaffolding Pattern: Flexible Data Processing and Object Creation

This scaffolding pattern is ideal for systems where you need to create families of objects with flexible configurations (via Abstract Factory) while processing large datasets using functional programming techniques (via Functional-Units and Map-Reduce). The combination ensures that data processing is efficient and that the right objects are created for each scenario, making the system extensible and modular.
TypeScript Example:

 */

// Abstract Factory - Creates related objects

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
    price = 100
}

class ProductFactoryA implements ProductFactory {
    createProduct = (): Product => new ConcreteProductA()
}

class ProductFactoryB implements ProductFactory {
    createProduct = (): Product => new ConcreteProductB()
}


// Functional-Units - Helper functions for data transformations

const calculateDiscount = (product: Product): Product =>
    ({ ...product, price: (product?.price ?? 0) * 0.9 })

const formatProductName = (product: Product): string =>
    `Name: ${product?.name || '-'}, Price: ${product?.price || '-'}`


// Map-Reduce

const products = [new ProductFactoryA(), new ProductFactoryB()]

const processedProducts = products
    .map(factory => factory.createProduct())
    .map(calculateDiscount)
    .map(formatProductName)

console.log(processedProducts)
