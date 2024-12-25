'use strict'

/*

3. State + Observer + Command
Scaffolding: Stateful Command Scaffold - to maintain state transitions while notifying observers and executing commands.

The State allows an object to change behavior based on its state.
The Observer notifies observers when the state changes.
The Command encapsulates requests as objects.

 */

interface State {
    handle(context: Context): void
}

class OnState implements State {
    handle = (context: Context) => (
        console.log('Turning off ..'),
        context.setState(new OffState())
    )
}

class OffState implements State {
    handle = (context: Context) => (
        console.log('Turning on ..'),
        context.setState(new OnState())
    )
}

// Context
class Context {
    private state: State

    constructor(state: State) {
        this.state = state
    }

    setState = (state: State) => (
        this.state = state,
        this.notifyObservers()
    )

    request = () => this.state.handle(this)

    // * Observer Management

    private observers: Observer[] = []

    addObserver = (observer: Observer) => this.observers.push(observer)

    notifyObservers = () => this.observers.forEach(observer => observer.update(this.state))
}

interface Observer {
    update(state: State): void
}

class ConsoleObserver implements Observer {
    update = (state: State) => console.log(`State changed to: ${state.constructor.name}`)
}

class Command {
    execute = (context: Context) => context.request()
}

// Usage
const context = new Context(new OffState())
const observer = new ConsoleObserver()

context.addObserver(observer)

const command = new Command()
command.execute(context) // Turning On ..
command.execute(context) // Turning Off ..
