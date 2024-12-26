'use strict'

/*

7. Composite + Visitor + Flyweight
Why These Patterns Are Combined:

Composite manages hierarchical structures.
Visitor applies operations across a composite structure.
Flyweight reduces memory usage by sharing objects.
Best Scaffolding Pattern: Flyweight Visitor Scaffold

A visitor operates on a composite structure, utilizing shared flyweight objects.
TypeScript Example:

 */

class Flyweight {
    constructor(public sharedState: string) {}
}

// Composite
interface Component {
    accept(visitor: Visitor): void
}

class Composite implements Component {
    private children: Component[] = []

    addChild = (child: Component) => this.children.push(child)

    accept = (visitor: Visitor) => (
        visitor.visitComposite(this),
        this.children.forEach(child => child.accept(visitor))
    )
}

class Leaf implements Component {
    constructor(private flyweight: Flyweight) {}
    accept = (visitor: Visitor) => visitor.visitLeaf(this.flyweight)
}

interface Visitor {
    visitComposite(composite: Composite): void
    visitLeaf(flyweight: Flyweight): void
}

class ConcreteVisitor implements Visitor {
    visitComposite = (composite: Composite) => console.log('Visiting Composite ..')
    visitLeaf = (flyweight: Flyweight) => console.log(`Visiting Leaf with shared state: ${flyweight.sharedState || '-'}`)
}


// ! Usage

const flyweight = new Flyweight('Shared State')
const leaf1 = new Leaf(flyweight)
const leaf2 = new Leaf(flyweight)
const composite = new Composite()

composite.addChild(leaf1)
composite.addChild(leaf2)

const visitor = new ConcreteVisitor()
composite.accept(visitor)
