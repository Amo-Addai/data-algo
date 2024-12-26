'use strict'

/*

4. Prototype + Flyweight + Pure Function Scaffold
Why These Patterns Are Combined:

Prototype: Provides a way to clone objects efficiently.
Flyweight: Reduces memory usage by sharing common parts of objects.
Pure Function: Ensures that functions do not cause side effects and are predictable.
Best Scaffolding Pattern: Memory-Efficient Object Cloning with Pure Computation

This scaffold is designed for systems where memory efficiency is crucial, and the logic must remain pure and side-effect-free.
TypeScript Example:

 */

interface Prototype {
    clone(): Prototype
}

class ConcretePrototype implements Prototype {
    constructor(private data: string) {}
    clone: () => Prototype = () => new ConcretePrototype(this.data)
    getData = () => this.data
}

class FlyweightFactory {
    private flyweights: Map<string, ConcretePrototype>
        = new Map()

    getFlyweight: (data: string) => ConcretePrototype
        = data => (
            this.flyweights.has(data)
            || this.flyweights.set(data, new ConcretePrototype(data)),
            this.flyweights.get(data)
        )
}

// Pure Function - to compute hash-value based on Flyweight data
const computeHash: (string) => string = data =>
    data.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0).toString()


// ! Usage

const factory = new FlyweightFactory()
const flyweight = factory.getFlyweight('data')

console.log(flyweight.getData())

const hash = computeHash(flyweight.getData())
console.log(hash)
