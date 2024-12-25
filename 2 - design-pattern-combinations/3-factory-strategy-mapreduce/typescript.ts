'use strict'

/*

1. Factory + Strategy + Map-Reduce
Why These Patterns Are Combined:

Factory: Creates objects without specifying the exact class, allowing flexibility in object creation.
Strategy: Allows the selection of algorithms or behaviors at runtime. It enables switching between different strategies based on the context.
Map-Reduce: A functional pattern for transforming data in parallel, useful for processing large datasets efficiently.
Best Scaffolding Pattern: Factory-Strategy-MapReduce Scaffold

This scaffold pattern works best for systems where you need flexible object creation (Factory), dynamic algorithm selection (Strategy), and the ability to process data concurrently or in parallel (Map-Reduce). It's highly applicable in data processing systems, API handling, or systems that involve multiple transformation strategies.
TypeScript Example:

 */

interface Algorithm {
    execute(data: number[]): number;
}

class SumStrategy implements Algorithm {
    name: string // TODO: FIX - remove all 'interface-properties: name: string' from implementing classes
    execute = data => data.reduce((sum, num) => sum + num, 0)
}

class AverageStrategy implements Algorithm {
    name: string
    execute = data => data.reduce((sum, num) => sum + num, 0) / data.length
}

class StrategyFactory { // todo: confirm 'type' as 'data-type-argument'
    static createStrategy: (type: 'sum' | 'average') => Algorithm =
        type => type === 'sum' ? new SumStrategy() : new AverageStrategy()
    // TODO: Confirm 'type' in this case still works as a data-type
}

const mapReduce = <T>(
    data: T[],
    mapFn: (item: T) => T,
    reduceFn: (accm: T, value: T) => T
) => data.map(mapFn).reduce(reduceFn)

// Usage - 'number' example (generics)
const strategy = StrategyFactory.createStrategy('sum')
const data = [1, 2, 3, 4, 5]
const result = mapReduce<number>(
    data,
    num => num * 7,
    (acc, value) => acc + value
)

console.log('Strategy Result', strategy.execute(data))
console.log('Map-Reduce Result', result)
