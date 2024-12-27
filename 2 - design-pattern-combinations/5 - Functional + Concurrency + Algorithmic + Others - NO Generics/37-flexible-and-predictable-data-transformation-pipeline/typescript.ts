'use strict'

/*

4. Currying + Pure Function + Map-Reduce Combo
Why These Patterns Are Combined:

Currying: Transforms functions that take multiple arguments into a series of functions that each take one argument, which can be partially applied for greater flexibility.
Pure Function: Ensures that functions are predictable, with no side effects, making them ideal for functional programming and higher-order functions like currying.
Map-Reduce: Provides a powerful way to process and transform data through mapping (applying a function) and reducing (aggregating values).
Best Scaffolding Pattern: Flexible and Predictable Data Transformation Pipeline

This scaffolding pattern is ideal for building a modular pipeline of transformations that can handle large data sets, perform predictable computations, and allow for flexible function composition using currying.
TypeScript Example:

 */


// Currying - A function that takes multiple arguments and transforms them into a series of functions

const add = (a: number) => (b: number): number => a + b
const multiply = (a: number) => (b: number): number => a * b


// Pure Function - No side effects, always returns the same output for the same input

const double = (x: number): number => x * 2


// Map-Reduce - Map function applies a transformation, and Reduce aggregates results

const numbers = [1, 2, 3, 4, 5]

// Map - Transform numbers with currying and pure functions
const mappedNumbers = numbers.map(add(5))

// Reduce - Sum up the transformed numbers
const sum = mappedNumbers.reduce((acc, curr) => acc + curr, 0)


// Output: 40
console.log('Mapped and Reduced Sum: ', sum)
