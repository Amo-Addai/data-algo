'use strict'

/*

1. Purely-Functional + Functor + Currying Combo
Why These Patterns Are Combined:

Purely-Functional: Functions transform data without side effects, ensuring predictability and reusability.
Functor: Allows transformation of values inside a container while preserving the structure, such as a list or optional value.
Currying: Enables partial application of functions, allowing functions to be reused with different parameters.
Best Scaffolding Pattern: Curried Functor Transformation

Curried functions are applied to values inside a Functor. The curried functions allow for partial application of operations, enabling flexibility, while purely-functional ensures clean data transformations without side effects.
TypeScript Example:

 */

// Curried Pure Function - purely functional
const add = (x: number) => (y: number): number => x + y

// Functor - A container that applies functions to its values
class Functor<T> {
    private hasMapped: boolean = false
    public hasMapped = () => this.hasMapped

    constructor(private index: number = 0, private values: T[]) {}

    map = <U>(fn: (value: T) => U): Functor<U> => (
        this.hasMapped
        ? this
        : (
            fn(this.values[this.index])
            |> (
                this.values[this.index] = %,
                this.index++,
                this.hasMapped = this.index == this.values.length,
                new Functor(this.index, this.values)
            )
        )
    )

    getValues = (): T[] => this.values
}


// ! Usage

const curriedAdd5 = add(5) // create a pure-function that adds 5 to any number
const functor = new Functor<number>(0, [0, 1, 2, 3, 4, 5])

let result
while (!result?.hasMapped()) {
    result = functor.map(curriedAdd5) // Apple the curried function inside the functor, to all its values
}
console.log(result?.getValues()) // Output: [5, 6, 7, 8, 9, 10]
