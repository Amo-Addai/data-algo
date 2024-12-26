'use strict'

/*

1. Abstract Factory + Builder + Object Pool Combo
Why These Patterns Are Combined:

Abstract Factory: Provides an interface for creating families of related or dependent objects without specifying their concrete classes, enabling flexibility and extensibility.
Builder: Separates the construction of a complex object from its representation, allowing for different configurations or variants of an object.
Object Pool: Manages a pool of reusable objects, reducing the overhead of creating and destroying objects frequently.
Best Scaffolding Pattern: Object Creation and Reuse with Flexibility

This scaffolding pattern is ideal for scenarios where you need to create complex objects in different configurations (using Builder) and ensure efficient reuse of these objects (using Object Pool) while abstracting the details of object creation (using Abstract Factory). It's commonly used in systems where object construction is resource-intensive, and object reuse is beneficial.
TypeScript Example:

 */

interface Product {
    name: string
    describe(): void
}

// Abstract Factory - Interface for creating related objects (Products)
interface ProductFactory {
    createProduct(): Product
}

class ConcreteProductA implements Product {
    name = 'Product A'
    describe = () => console.log(`This is ${this.name}`)
}

class ConcreteProductB implements Product {
    name = 'Product B'
    describe = () => console.log(`This is ${this.name}`)
}

class ConcreteFactoryA implements ProductFactory {
    createProduct = () => new ConcreteProductA()
}

class ConcreteFactoryB implements ProductFactory {
    createProduct = () => new ConcreteProductB()
}

// Builder - Constructs a complex object
class ProductBuilder {
    private product: Product

    constructor(factory: ProductFactory) {
        this.product = factory.createProduct()
    }

    build = () => (
        console.log(`Building ${this.product?.name || '-'}`),
        this.product.describe(),
        this.product
    )
}

// Object Pool - Manages a pool of reusable objects
class ObjectPool {
    private pool: Product[] = []

    acquire: (ProductFactory) => Product =
        factory => (
            this.pool.pop()
            |> (
                !% // TODO: Use Babel compiler for pipeline - operator
                ? (
                    console.log('Creating new product'),
                    factory.createProduct()
                ) : (
                    console.log('Reusing product'),
                    % // forced - necessary return when % !== null, for re-pipe
                )
            )
            |> %
        )

    release = (product: Product) => this.pool.push(product)
}


// ! Usage

const factoryA = new ConcreteFactoryA()
const builderA = new ProductBuilder(factoryA)
const pool = new ObjectPool()
const productA = pool.acquire(factoryA)

builderA.build()
pool.release(productA)
