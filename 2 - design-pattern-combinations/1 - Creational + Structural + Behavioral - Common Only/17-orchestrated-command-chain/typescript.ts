'use strict'

/*

6. Mediator + Chain of Responsibility + Command
Why These Patterns Are Combined:

Mediator orchestrates communication between objects.
Chain of Responsibility delegates requests across handlers.
Command encapsulates requests into reusable objects.
Best Scaffolding Pattern: Orchestrated Command Chain Scaffold

Commands are passed through a chain of handlers, managed by a mediator.
TypeScript Example:

 */

interface Command {
    execute(): void
}

class ConcreteCommand implements Command {
    constructor(private name: string) {}
    execute = () => console.log(`Executing Command: ${this.name}`)
}

class Mediator {
    notify = (handler: Handler, command: Command) =>
        handler.handle(command)
}

// Chain of Responsibility
abstract class Handler {
    private nextHandler?: Handler

    setNext: (Handler) => Handler =
        handler => (this.nextHandler = handler, handler)

    handle = (command: Command) => (
        !!this.nextHandler
        ? this.nextHandler.handle(command)
        : console.log('End of Chain: No handler executed')
    )
}

class ConcreteHandler extends Handler {
    handle = (command: Command) => (
        console.log('Handler processing command ...'),
        command.execute(),
        super.handle(command)
    )
}

// Pattern Combination
class OrchestratedCommandChain {
    private mediator = new Mediator()
    private rootHandler!: Handler

    setHandlerChain = (handler: Handler) => (this.rootHandler = handler)
    processCommand = (command: Command) => this.mediator.notify(this.rootHandler, command)
}


// ! Usage

const chain = new OrchestratedCommandChain()
const handler1 = new ConcreteHandler()
const handler2 = new ConcreteHandler()

handler1.setNext(handler2)
chain.setHandlerChain(handler1)

const command = new ConcreteCommand('Command 1')
chain.processCommand(command)
