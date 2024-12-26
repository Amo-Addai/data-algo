'use strict'

/*

2. Flyweight + Composite + Visitor
Scaffolding: Hierarchical Flyweight Scaffold - for managing lightweight shared objects with hierarchical traversal.

The Flyweight ensures efficient use of memory by sharing objects.
The Composite organizes objects hierarchically.
The Visitor traverses the hierarchical structure and performs operations.

 */

class Flyweight {
    constructor(public sharedState: string) {}
}

interface Visitor {
    visit(composite: Composite): void
}

class PrintVisitor implements Visitor {
    visit = (composite: Composite) => console.log(`Visiting Flyweight: ${composite['flyweight']?.sharedState || '-'}`)
}

class Composite {
    private children: Composite[] = []
    constructor(private flyweight: Flyweight) {}

    addChild = (child: Composite) => this.children.push(child)

    accept = (visitor: Visitor) => (
        visitor.visit(this),
        this.children.forEach(child => child.accept(visitor))
    )
}


// ! Usage

const flyweight = new Flyweight('Shared State')
const root = new Composite(flyweight)
const child1 = new Composite(flyweight)
const child2 = new Composite(flyweight)

root.addChild(child1); root.addChild(child2)

const visitor = new PrintVisitor()
root.accept(visitor)

// Output:
// Visiting Flyweight: Shared State
// Visiting Flyweight: Shared State
// Visiting Flyweight: Shared State
