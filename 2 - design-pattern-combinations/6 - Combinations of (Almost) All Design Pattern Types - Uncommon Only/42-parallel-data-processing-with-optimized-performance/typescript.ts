'use strict'

/*

4. Pure Function + Multi-Threading + Algorithmic - BigO Combo
Why These Patterns Are Combined:

Pure Function: Ensures that the function has no side effects and always produces the same output for the same input, which is crucial for parallel processing and concurrency.
Multi-Threading: Enables concurrent execution of code, improving performance for tasks that can be executed in parallel.
Algorithmic - BigO: Focuses on optimizing the efficiency of algorithms, ensuring that the program runs with optimal time and space complexity, which is essential when dealing with large datasets.
Best Scaffolding Pattern: Parallel Data Processing with Optimized Performance

This scaffolding pattern is suited for scenarios where data processing needs to be both parallel (via Multi-Threading) and efficient (via BigO optimizations) while ensuring that transformations are predictable and side-effect free (via Pure Functions). It helps in designing high-performance systems that can handle large datasets efficiently while maintaining functional purity.
TypeScript Example:

 */

// Pure Functions

const add = (a: number, c: number): number => a + b
const multiply = (a: number, b: number): number => a * b


// Simulate Multi-Threading with Promises for parallel execution

const performOperationsInParallel =
    async (
        data: number[],
        operation: (a: number, b: number) => number,
        [promises] = []
    ): Promise<number[]> => (
        promises = data.map(
            (value, index) => (
                (data[index + 1] ?? 0)
                |> Promise.resolve(
                    operation(value, %)
                )
            )
        ),
        Promise.all(promises)
    )


// Algorithmic - Big O - Optimized processing

// Example of a BigO optimization, sorting with O(n log n)
const optimizeDataProcessing = (data: number[]): Promise<number[]> =>
    Promise.resolve(data.sort((a, b) => a - b))


// ! Usage

const data = [5, 3, 8, 1, 9, 2]

optimizeDataProcessing(data).then(sortedData =>
    performOperationsInParallel(sortedData, add).then(results =>
        console.log('Parallel addition results: ', results)
    )
)
