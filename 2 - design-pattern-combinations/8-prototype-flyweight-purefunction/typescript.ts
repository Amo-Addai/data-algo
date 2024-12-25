'use strict'

/*

4. Prototype + Flyweight + Pure Function
Why These Patterns Are Combined:

Prototype: Allows for object cloning to create new instances without creating new objects from scratch, reducing overhead.
Flyweight: Reduces memory usage by sharing objects that are similar rather than creating new ones.
Pure Function: Ensures that functions do not have side effects and always return the same output for the same input.
Best Scaffolding Pattern: Prototype-Flyweight-PureFunction Scaffold

This scaffold is best for scenarios where efficient object creation and memory management are important (Prototype + Flyweight), while ensuring that the system is predictable and does not have unintended side effects (Pure Function). It’s suited for rendering large objects in memory, such as game objects or UI components.
TypeScript Example:

 */

// Prototype
class CarPrototype {
    constructor(public model: string, public color: string) {}
    clone: () => CarPrototype = () => new CarPrototype(this.model, this.color)
}

// Flyweight - Factory
class CarFactory {
    private cars: { [key: string]: CarPrototype } = {}

    getCar: (model: string, color: string) => CarPrototype =
        (model, color) => (
            `${model}-${color}`
            |> (
                !!this.cars[%]
                || (this.cars[%] = new CarPrototype(model, color)),
                this.cars[%]
            )
        )
}

// Pure Function
const calculatePrice: (basePrice: number, tax: number) => number
    = (basePrice, tax) => basePrice + (basePrice * tax)

// Usage
const carFactory = new CarFactory()

const car1 = carFactory.getCar('Sedan', 'Red')
const car2 = carFactory.getCar('Sedan', 'Red')
const car3 = carFactory.getCar('SUV', 'Blue')

console.log(car1 === car2) // true, reused the same object
console.log(car1 === car3) // false, different object

const price = calculatePrice(10000, 0.15)
console.log(`Price: $${price}`)
