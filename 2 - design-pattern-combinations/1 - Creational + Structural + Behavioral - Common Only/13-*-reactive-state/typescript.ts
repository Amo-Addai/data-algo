'use strict'

/*

4. State + Strategy + Observer
Why These Patterns Are Combined:

State manages transitions between states.
Strategy applies varying behaviors dynamically based on the state.
Observer notifies dependent components of state changes.
Best Scaffolding Pattern: Reactive State Scaffold

Observers subscribe to changes in state, while strategies define the behavior for each state.
TypeScript Example:

 */

interface Observer {
    update(state: string): void
}

class ConcreteObserver implements Observer {
    update = state => console.log(`Observer notified: State changed to ${state}`)
}

interface State {
    handle(): void
}

class ConcreteStateA implements State {
    handle = () => console.log('State A handled')
}

class ConcreteStateB implements State {
    handle = () => console.log('State B handled')
}

interface Strategy {
    execute(stateBehavior: string): void
}

class ConcreteStrategy implements Strategy {
    execute = stateBehavior => console.log(`Executing strategy for: ${stateBehavior}`)
}

// Reactive-State Pattern Combo
class ReactiveState {
    private state!: State
    private observers: Observer[] = []
    private strategy!: Strategy
    
    setState = (state: State) => (
        this.state = state,
        this.notifyObservers()
    )
    
    setStrategy = (strategy: Strategy) => (this.strategy = strategy)
    
    addObserver = (observer: Observer) => this.observers.push(observer)
    
    notifyObservers = () => (
        this.state.handle()
        |> (
            this.observers.forEach(observer => observer.update(%)),
            this.strategy.execute(%)
        )
    )
}


// ! Usage

const scaffold = new ReactiveState()
scaffold.setStrategy(new ConcreteStrategy())
scaffold.addObserver(new ConcreteObserver())
scaffold.setState(new ConcreteStateA())
scaffold.setState(new ConcreteStateB())
