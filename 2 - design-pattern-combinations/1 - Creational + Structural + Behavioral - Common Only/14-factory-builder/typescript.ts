'use strict'

/*

5. Factory + Abstract Factory + Builder
Why These Patterns Are Combined:

Factory handles the creation of specific objects.
Abstract Factory defines families of related objects.
Builder constructs complex objects step by step.
Best Scaffolding Pattern: Factory Builder Scaffold

A factory produces builders for constructing families of objects.
TypeScript Example:

 */

interface Product {
    name: string
}

class ConcreteProductA implements Product {
    name = 'Product A'
}

class ConcreteProductB implements Product {
    name = 'Product B'
}

class Builder {
    private product!: Product
    setProduct = (product: Product) => (this.product = product)
    getResult = () => this.product
}

interface AbstractFactory {
    createProduct(): Product
}

class FactoryA implements AbstractFactory {
    createProduct = () => new ConcreteProductA()
}

class FactoryB implements AbstractFactory {
    createProduct = () => new ConcreteProductB()
}

class FactoryBuilder {
    createBuilder: (AbstractFactory) => Builder
        = factory => (
        new Builder()
        |> (
            %.setProduct(factory.createProduct()),
            %
        )
    )
}


// ! Usage

const builder = new FactoryBuilder()

const factoryA = new FactoryA()
const builderA = builder.createBuilder(factoryA)
console.log(builderA.getResult())

const factoryB = new FactoryB()
const builderB = builder.createBuilder(factoryB)
console.log(builderB.getResult())
