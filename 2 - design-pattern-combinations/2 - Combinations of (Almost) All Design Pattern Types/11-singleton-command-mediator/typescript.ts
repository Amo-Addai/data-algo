'use strict'

/*

5. Singleton + Command + Mediator
Why These Patterns Are Combined:

Singleton: Ensures that a class has only one instance and provides a global point of access to it.
Command: Encapsulates a request as an object, allowing parameterization of clients with different requests.
Mediator: Allows for communication between objects without them having direct references to each other, reducing dependencies.
Best Scaffolding Pattern: Singleton-Command-Mediator Scaffold

This scaffold is ideal for applications where you need a global controller (Singleton), encapsulate commands to decouple the request sender and receiver (Command), and facilitate communication between components without direct interaction (Mediator). It's perfect for complex event-driven systems or orchestrated workflows.
TypeScript Example:

 */

// Singleton
class Logger {
    private static instance: Logger
    private constructor() {}

    static getInstance: () => Logger = () => (
        !!Logger.instance
        || (Logger.instance = new Logger()),
        Logger.instance
    )

    log = message => console.log(message)
}

// Receiver
class Light {
    turnOn = () => console.log('Light on')
}

interface Command {
    execute(): void
}

class LightOnCommand implements Command {
    constructor(private light: Light) {}
    execute = () => this.light.turnOn()
}

// Mediator
class Controller {
    private commands: Command[] = []
    addCommand = (command: Command) => this.commands.push(command)
    executeCommands = () => this.commands.forEach(cmd => cmd.execute())
}


// ! Usage

const light = new Light()
const command = new LightOnCommand(light)

const controller = new Controller()
controller.addCommand(command)
controller.executeCommands()

Logger.getInstance().log('Command executed')
