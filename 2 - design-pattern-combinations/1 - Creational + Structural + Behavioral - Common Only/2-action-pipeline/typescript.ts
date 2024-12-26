'use strict'

/*

2. Strategy + Template Method + Command
Why These Patterns Are Combined:

Strategy encapsulates algorithms.
Template Method defines skeletons for algorithms with hooks.
Command decouples method invocation.
Best Scaffolding Pattern: Action Pipeline

Commands are dynamically injected into a pipeline, with strategies applied at each step and templates defining execution flow.
TypeScript Example:

 */

interface Command {
    execute(): void
}

class ConcreteCommand implements Command {
    execute = () => console.log('Executing cmd')
}

interface Strategy {
    executeAlgo(data: string): void;
}

class ConcreteStrategy implements Strategy {
    executeAlgo = data => console.log(`Processing: ${data}`)
}

abstract class Template {
    abstract step1(): void
    abstract step2(): void

    execute = () => (
        this.step1,
        this.step2
    )
}

class ConcreteTemplate extends Template {
    step1 = () => console.log('Step 1 executed')
    step2 = () => console.log('Step 2 executed')
}

class ActionPipeline {
    private commands: Command[] = []
    private strategy!: Strategy // todo: confirm why forced-prop when no constructor
    private template!: Template

    setStrategy = (strategy: Strategy) => (this.strategy = strategy)
    setTemplate = (template: Template) => (this.template = template)
    addCommand = (command: Command) => this.commands.push(command)

    executePipeline = (data: string) => (
        this.commands.forEach(cmd => cmd.execute()),
        this.strategy.executeAlgo(data),
        this.template.execute()
    )
}


// ! Usage - wrong - sync Template's with different Strategy's, with algo's having different Command's
const pipeline = new ActionPipeline()
pipeline.setStrategy(new ConcreteStrategy())
pipeline.setTemplate(new ConcreteTemplate())
pipeline.addCommand(new ConcreteCommand())
pipeline.executePipeline('Data Input')
