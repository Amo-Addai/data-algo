'use strict'

/*

5. Singleton + Command + Mediator Scaffold
Why These Patterns Are Combined:

Singleton: Ensures only one instance of a class exists.
Command: Encapsulates a request as an object, allowing parameters to be passed.
Mediator: Centralizes communication between components, reducing dependencies.
Best Scaffolding Pattern: Centralized Command Execution with Singleton Control

This scaffold ensures that command requests are handled centrally by a singleton, facilitating communication via a mediator.
TypeScript Example:

 */

interface Command {
    execute(): void
}

class TurnOnLightCommand implements Command {
    constructor(private light: Light) {}
    execute = () => this.light.turnOn()
}

// Receiver
class Light {
    turnOn = () => console.log('Light is ON')
    turnOff = () => console.log('Light is OFF')
}

// Singleton Mediator
class Mediator {
    private static instance: Mediator | null = null
    private commands: Command[] = []
    private constructor() {}

    static getInstance: () => Mediator = () => (
        Mediator.instance
        || (Mediator.instance = new Mediator),
        Mediator.instance
    )

    addCommand = (command: Command) => this.commands.push(command)
    executeCommands = () => this.commands.forEach(cmd => cmd.execute())
}


// ! Usage

const light = new Light()
const turnOnLightCommand = new TurnOnLightCommand(light)
const mediator = Mediator.getInstance()

mediator.addCommand(turnOnLightCommand)
mediator.executeCommands()
