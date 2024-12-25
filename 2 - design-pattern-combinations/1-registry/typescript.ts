'use strict'

/*

1. Singleton + Factory + Prototype
Why These Patterns Are Combined:

Singleton ensures a single instance of critical classes.
Factory abstracts object creation logic.
Prototype supports cloning objects, reducing overhead for complex creations.
Best Scaffolding Pattern: Registry Scaffolding

A central registry stores prototypes and singleton instances, with the factory acting as the interface for retrieval or instantiation.
TypeScript Example:

 */

class Prototype {
    private state: string

    constructor(state: string) {
        this.state = state
    }

    clone: () => Prototype = () => new Prototype(this.state)
}

class Factory {
    private prototypes: Map<string, Prototype> = new Map()

    registerPrototype: (string, Prototype) => void =
        (key, prototype) => this.prototypes.set(key, prototype)

    createClone: (string) => Prototype | undefined = (
        key,
        [prototype] = [] // todo: confirm forced-arguments not required in function-type definition
    ) => (
        prototype = this.prototypes.get(key),
        prototype?.clone()
    )
}

class Singleton {
    private static instance: Singleton

    private factory: Factory

    private constructor() {
        this.setup()
    }

    static getInstance: () => Singleton = () => (
        !Singleton.instance
        && (Singleton.instance = new Singleton),
            Singleton.instance
    )

    private setup = (
        [prototype, factory, cloned] = []
    ) => (
        prototype = new Prototype('State'),
        this.factory = new Factory(),
        factory.registerPrototype('proto', prototype),
        cloned = factory.createClone('proto') // use cloned if required
    )

    public getFactoryPrototype = (key: string) => this.factory.createClone(key)
}

// Usage - as the Singleton
const singleton = Singleton.getInstance()
console.log(singleton.getFactoryPrototype('proto'))
