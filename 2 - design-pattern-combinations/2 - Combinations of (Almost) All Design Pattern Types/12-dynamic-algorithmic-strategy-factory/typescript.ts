'use strict'

/*

1. Factory + Strategy + Map-Reduce Scaffold
Why These Patterns Are Combined:

Factory: Provides a flexible way to create objects based on parameters or conditions.
Strategy: Allows the runtime switching of algorithms without modifying the client code.
Map-Reduce: Efficiently processes large data sets, transforming and reducing them as needed.
Best Scaffolding Pattern: Dynamic Algorithmic Strategy Factory

This scaffold allows dynamic object creation based on conditions (Factory), then lets you choose or switch strategies (Strategy) at runtime, and finally, process large data sets efficiently using a map-reduce approach.
TypeScript Example:

 */

// Strategy Interface
interface SortingStrategy {
    sort(data: number[]): number[]
}

// Concrete Strategies
class BubbleSortStrategy implements SortingStrategy {
    sort: (data: number[]) => number[] = data => data.sort((a, b) => a - b)
}

class QuickSortStrategy implements SortingStrategy {
    sort: (data: number[]) => number[] =
        (
            data,
            [left, right] = []
        ) => (
            data.length <= 1
            ? data
            : (
                data[0]
                |> ( // TODO: use Babel Compiler for pipeline - operator
                    left = data.slice(1).filter(x => x <= %),
                    right = data.slice(1).filter(x => x > %),
                    [
                        ...this.sort(left),
                        %,
                        ...this.sort(right)
                    ]
                )
            )
        )
}

// Factory to create sorting strategies
class SortingStrategyFactory {
    static getStategy: (string) => SortingStrategy =
        type => (
            type === 'bubble'
            ? new BubbleSortStrategy()
            : type === 'quick'
            ? new QuickSortStrategy()
            : throw new Error('Unknown Strategy')
        )
}

// Map-Reduce Example
const mapReduce: (
    arr: number[],
    strategyType: string
) => number = (
    arr, strategyType,
) => (
    SortingStrategyFactory.getStategy(strategyType)
    |> %.sort(arr)
    |> %.reduce((acc, val) => acc + val, 0)
)

// Example
const data = [5, 2, 8, 1, 4]
const result = mapReduce(data, 'quick')
console.log(result)
