'use strict'

/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  CODING STYLES
////////////////////////////////////////

const Imperative = _ => { // Directly changing the state
    let sum = 0
    for (let i = 1; i <= 10; i++) {
        sum += i
    }
    console.log(sum) // Output: 55
}

const Functional = (_ => { // Using functions as first-class citizens
    const add = (a: number, b: number): number => a + b
    const multiply = (a: number, b: number): number => a * b

    const numbers = [1, 2, 3, 4]
    const result = numbers.reduce((acc, num) => add(acc, num), 0)

    return {
        test() {
            console.log(result) // Output: 10
        }
    }
})()

// AMD (Asynchronous Module Definition)
define(['Declarative', _ => { // Describing what to do, not how to do it

    const numbers = [1, 2, 3, 4]
    const doubled = numbers.map(num => num * 2)

    return {
        test() {
            console.log(doubled) // Output: [2, 4, 6, 8]
        }
    }
}])

// todo: More 'ModuleTypes' at bottom of file

const OOP = (_ => { // Object-Oriented Programming: Using classes and inheritance

    class Animal {
        constructor(public name: string) {}
        
        speak(): void {
            console.log(`${this.name} makes a sound.`)
        }
    }
    
    class Dog extends Animal {
        speak(): void {
            console.log(`${this.name} barks.`)
        }
    }
    
    return {
        test() {
            const dog = new Dog('Rex')
            dog.speak() // Output: Rex barks.
        }
    }
})()

const AOP = (_ => { // Aspect-Oriented (AOP): Adding behavior (logging) to methods

    function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        const originalMethod = descriptor.value
        
        descriptor.value = function(...args: any[]) {
            console.log(`Calling ${propertyKey} with`, args)
            return originalMethod.apply(this, args)
        }
    }
    
    class Calculator {
        @Log
        add(a: number, b: number): number {
            return a + b
        }
    }

    return {
        test() {
            const calc = new Calculator()
            calc.add(5, 3) // Output: Calling add with [5, 3]        
        }
    }
})()

const Promises_AsyncAwait = (_ => { // Handling asynchronous operations

    const fetchData = (): Promise<string> => {
        return new Promise(resolve => setTimeout(() => resolve('Data'), 1000))
    }
    
    const getData = async () => {
        const data = await fetchData()
        console.log(data) // Output: Data
    }

    return {
        test() {
            getData()
        }
    }
})()

const LazyInit = (_ => { // Delaying initialization until it's needed

    class DatabaseConnection {
        private static instance: DatabaseConnection | null = null
        
        private constructor() {}
        
        static getInstance(): DatabaseConnection {
            if (this.instance === null) {
                this.instance = new DatabaseConnection()
            }
            return this.instance
        }
    }
    
    return {
        test() {
            const db1 = DatabaseConnection.getInstance()
            const db2 = DatabaseConnection.getInstance()
            console.log(db1 === db2) // Output: true
        }
    }
})()

const Callback = (_ => { // Passing a function to be executed later

    function processData(callback: (data: string) => void) {
        const data = 'Processed data'
        callback(data)
    }
    
    return {
        test() {
            processData(data => {
                console.log(data) // Output: Processed data
            })
        }
    }
})()

const Optional_Null_Object = (_ => { // Providing a default implementation

    class User {
        constructor(private name: string) {}
        
        getName(): string {
            return this.name
        }
    }
    
    class NullUser extends User {

        constructor(name: string = '') {
            super(name)
        }

        getName(): string {
            return 'Guest'
        }
    }
    
    function getUser(user: User | null): User {
        return user ?? new NullUser()
    }
        
    return {
        test() {
            const user = getUser(null)
            console.log(user.getName()) // Output: Guest
        }
    }
})()

const Encapsulation = (_ => {
    // Hiding internal state and requiring all interaction to be performed through an object's methods

    class BankAccount {
        private balance: number = 0
        
        deposit(amount: number): void {
            if (amount > 0) {
                this.balance += amount
            }
        }
        
        getBalance(): number {
            return this.balance
        }
    }
        
    return {
        test() {
            const account = new BankAccount()
            account.deposit(100)
            console.log(account.getBalance()) // Output: 100
        }
    }
})()

const ObjectComposition = (_ => { // Combining objects to achieve functionality

    interface Address {
        street: string
        city: string
    }
    
    class Person {
        constructor(public name: string, public address: Address) {}
    }
    
    return {
        test() {
            const address: Address = { street: '123 Main St', city: 'Somewhere' }
            const person = new Person('John Doe', address)
            console.log(person) // Output: Person { name: 'John Doe', address: { street: '123 Main St', city: 'Somewhere' } }
        }
    }
})()

const FluentInterface = (_ => { // Chaining method calls

    class Builder {
        private value: string = ''
        
        setPart1(part1: string): this {
            this.value += part1
            return this
        }
        
        setPart2(part2: string): this {
            this.value += part2
            return this
        }
        
        build(): string {
            return this.value
        }
    }
    
    return {
        test() {
            const result = new Builder()
            .setPart1('Hello, ')
            .setPart2('world!')
            .build()

            console.log(result) // Output: Hello, world!
        }
    }
})()

const State = (_ => { // Allowing an object to alter its behavior when its internal state changes

    interface State {
        handle(): void
    }
    
    class Context {
        private state: State
        
        constructor(state: State) {
            this.state = state
        }
        
        setState(state: State): void {
            this.state = state
        }
        
        request(): void {
            this.state.handle()
        }
    }
    
    class ConcreteStateA implements State {
        handle(): void {
            console.log('Handling request in State A')
        }
    }
    
    class ConcreteStateB implements State {
        handle(): void {
            console.log('Handling request in State B')
        }
    }

    return {
        test() {
            const context = new Context(new ConcreteStateA())
            context.request() // Output: Handling request in State A
            
            context.setState(new ConcreteStateB())
            context.request() // Output: Handling request in State B

            // todo: check .swift for an interchanging state implementation
        }
    }
})()

const Interpreter = (_ => { // Evaluating expressions

    interface Expression {
        interpret(context: string): boolean
    }
    
    class TerminalExpression implements Expression {
        private word: string
        
        constructor(word: string) {
            this.word = word
        }
        
        interpret(context: string): boolean {
            return context.includes(this.word)
        }
    }

    return {
        test() {
            const isJava = new TerminalExpression('Java')
            console.log(isJava.interpret('I am learning Java')) // Output: true
        }
    }
})()

const DAO = (_ => { // Data Access Object: Encapsulating data access logic

    class User {
        constructor(public id: number, public name: string) {}
    }
    
    class UserDAO {
        private users: Map<number, User> = new Map()
        
        insert(user: User): void {
            this.users.set(user.id, user)
        }
        
        find(id: number): User | undefined {
            return this.users.get(id)
        }
        
        delete(id: number): void {
            this.users.delete(id)
        }
    }
    
    return {
        test() {
            const userDAO = new UserDAO()
            const user = new User(1, 'Alice')
            userDAO.insert(user)
            console.log(userDAO.find(1)?.name) // Output: Alice
        }
    }
})()

const DTO = (_ => { // Data Transfer Object: A simple container for transferring data

    class UserDTO {
        constructor(public id: number, public name: string) {}
    }
    
    return {
        test() {
            const userDTO = new UserDTO(1, 'Bob')
            console.log(userDTO) // Output: UserDTO { id: 1, name: 'Bob' }
        }
    }
})()


////////////////////////////////////////
//  DESIGN PATTERNS
////////////////////////////////////////

// * Creational

const Singleton = (_ => { // Ensuring a class has only one instance

    class Singleton {
        private static instance: Singleton | null = null
        
        private constructor() {}
        
        static getInstance(): Singleton {
            if (this.instance === null) {
                this.instance = new Singleton()
            }
            return this.instance
        }
    }
    
    return {
        test() {
            const instance1 = Singleton.getInstance()
            const instance2 = Singleton.getInstance()
            console.log(instance1 === instance2) // Output: true
        }
    }
})()

const Factory = (_ => { // Creating objects without specifying the exact class

    interface Product {
        use(): void
    }
    
    class ConcreteProductA implements Product {
        use(): void {
            console.log('Using Product A')
        }
    }
    
    class ConcreteProductB implements Product {
        use(): void {
            console.log('Using Product B')
        }
    }
    
    class ProductFactory {
        static createProduct(type: string): Product {
            if (type === 'A') {
                return new ConcreteProductA()
            } else if (type === 'B') {
                return new ConcreteProductB()
            }
            throw new Error('Invalid product type')
        }
    }
    
    return {
        test() {
            const product = ProductFactory.createProduct('A')
            product.use() // Output: Using Product A
        }
    }
})()

const Prototype = (_ => { // Creating new objects by copying existing ones

    interface Prototype {
        clone(): Prototype
    }
    
    class ConcretePrototype implements Prototype {
        constructor(public name: string) {}
        
        clone(): Prototype {
            return new ConcretePrototype(this.name)
        }
    }
    
    return {
        test() {
            const prototype = new ConcretePrototype('Prototype 1')
            const clone = prototype.clone()
            console.log(clone instanceof ConcretePrototype) // Output: true
        }
    }
})()

const AbstractFactory = (_ => { // Creating families of related objects

    interface Button {
        render(): void
    }
    
    class WindowsButton implements Button {
        render(): void {
            console.log('Rendering Windows button')
        }
    }
    
    class MacButton implements Button {
        render(): void {
            console.log('Rendering Mac button')
        }
    }
    
    interface GUIFactory {
        createButton(): Button
    }
    
    class WindowsFactory implements GUIFactory {
        createButton(): Button {
            return new WindowsButton()
        }
    }
    
    class MacFactory implements GUIFactory {
        createButton(): Button {
            return new MacButton()
        }
    }
    
    return {
        test() {
            const factory: GUIFactory = new WindowsFactory()
            const button = factory.createButton()
            button.render() // Output: Rendering Windows button
        }
    }
})()

const Builder = (_ => { // Constructing complex objects step-by-step

    class Car {
        private parts: string[] = []
        
        addPart(part: string): void {
            this.parts.push(part)
        }
        
        listParts(): void {
            console.log(`Car parts: ${this.parts.join(', ')}`)
        }
    }
    
    class CarBuilder {
        private car: Car = new Car()
        
        addEngine(): this {
            this.car.addPart('Engine')
            return this
        }
        
        addWheels(): this {
            this.car.addPart('Wheels')
            return this
        }
        
        addDoors(): this {
            this.car.addPart('Doors')
            return this
        }
        
        build(): Car {
            return this.car
        }
    }
    
    return {
        test() {
            const car = new CarBuilder()
                .addEngine()
                .addWheels()
                .addDoors()
                .build()
            car.listParts() // Output: Car parts: Engine, Wheels, Doors
        }
    }
})()


// * Structural

const Decorator = (_ => { // Adding behavior to objects dynamically

    interface Coffee {
        cost(): number
    }
    
    class SimpleCoffee implements Coffee {
        cost(): number {
            return 5
        }
    }
    
    class MilkDecorator implements Coffee {
        constructor(private coffee: Coffee) {}
        
        cost(): number {
            return this.coffee.cost() + 2
        }
    }
    
    class SugarDecorator implements Coffee {
        constructor(private coffee: Coffee) {}
        
        cost(): number {
            return this.coffee.cost() + 1
        }
    }
    
    return {
        test() {
            const coffee = new SimpleCoffee()
            const milkCoffee = new MilkDecorator(coffee)
            const sweetMilkCoffee = new SugarDecorator(milkCoffee)
            
            console.log(sweetMilkCoffee.cost()) // Output: 8
        }
    }
})()

const Adapter = (_ => { // Adapting one interface to another

    class OldSystem {
        oldMethod(): string {
            return 'Old system method'
        }
    }
    
    interface NewSystem {
        newMethod(): string
    }
    
    class Adapter implements NewSystem {
        private oldSystem: OldSystem
        
        constructor(oldSystem: OldSystem) {
            this.oldSystem = oldSystem
        }
        
        newMethod(): string {
            return this.oldSystem.oldMethod()
        }
    }
    
    return {
        test() {
            const oldSystem = new OldSystem()
            const adapter = new Adapter(oldSystem)
            console.log(adapter.newMethod()) // Output: Old system method
        }
    }
})()

const Composite = (_ => { // Building tree structures

    interface Component {
        operation(): string
    }
    
    class Leaf implements Component {
        operation(): string {
            return 'Leaf operation'
        }
    }
    
    class Composite implements Component {
        private children: Component[] = []
        
        add(child: Component): void {
            this.children.push(child)
        }
        
        operation(): string {
            return 'Composite operation with children: ' +
                this.children.map(child => child.operation()).join(', ')
        }
    }
    
    return {
        test() {
            const leaf1 = new Leaf()
            const leaf2 = new Leaf()
            const composite = new Composite()
            
            composite.add(leaf1)
            composite.add(leaf2)
            
            console.log(composite.operation())
            // Output: Composite operation with children: Leaf operation, Leaf operation
        }
    }
})()

const Flyweight = (_ => { // Sharing objects to minimize memory usage

    class SharedCharacter {
        constructor(private symbol: string) {}
        
        display(): void {
            console.log(this.symbol)
        }
    }
    
    class CharacterFactory {
        private characters: Map<string, SharedCharacter> = new Map()
        
        getCharacter(symbol: string): SharedCharacter {
            if (!this.characters.has(symbol)) {
                this.characters.set(symbol, new SharedCharacter(symbol))
            }
            return this.characters.get(symbol)!
        }
    }
    
    return {
        test() {
            const factory = new CharacterFactory()
            const charA1 = factory.getCharacter('A') // will set, then get 'A'
            const charA2 = factory.getCharacter('A')
            console.log(charA1 === charA2) // Output: true
        }
    }
})()

const ProxyPattern = (_ => { // Controlling access to an object

    interface RealSubject {
        request(): void
    }
    
    class RealSubjectImpl implements RealSubject {
        request(): void {
            console.log('RealSubject request')
        }
    }
    
    class Proxy implements RealSubject {
        private realSubject: RealSubjectImpl
        
        constructor() {
            this.realSubject = new RealSubjectImpl()
        }
        
        request(): void {
            console.log('Proxy before request')
            this.realSubject.request()
            console.log('Proxy after request')
        }
    }
    
    return {
        test() {
            const proxy = new Proxy()
            proxy.request()
            // Output:
            // Proxy before request
            // RealSubject request
            // Proxy after request
        }
    }
})()


// * Behavioral

const Observer = (_ => { // Notifying multiple objects about changes

    interface Observer {
        update(message: string): void
    }
    
    class Subject {
        private observers: Observer[] = []
        
        addObserver(observer: Observer): void {
            this.observers.push(observer)
        }
        
        notify(message: string): void {
            this.observers.forEach(observer => observer.update(message))
        }
    }
    
    class ConcreteObserver implements Observer {
        constructor(private name: string) {}
        
        update(message: string): void {
            console.log(`${this.name} received: ${message}`)
        }
    }
    
    return {
        test() {
            const subject = new Subject()
            const observer1 = new ConcreteObserver('Observer 1')
            const observer2 = new ConcreteObserver('Observer 2')
            
            subject.addObserver(observer1)
            subject.addObserver(observer2)
            
            subject.notify('Update available')
            // Output:
            // Observer 1 received: Update available
            // Observer 2 received: Update available
        }
    }
})()

const Command = (_ => { // Encapsulating a request as an object

    interface Command {
        execute(): void
    }
    
    class Light {
        on(): void {
            console.log('Light is ON')
        }
        
        off(): void {
            console.log('Light is OFF')
        }
    }
    
    class LightOnCommand implements Command {
        constructor(private light: Light) {}
        
        execute(): void {
            this.light.on()
        }
    }
    
    class LightOffCommand implements Command {
        constructor(private light: Light) {}
        
        execute(): void {
            this.light.off()
        }
    }
    
    return {
        test() {
            const light = new Light()
            const lightOn = new LightOnCommand(light)
            const lightOff = new LightOffCommand(light)
            
            lightOn.execute() // Output: Light is ON
            lightOff.execute() // Output: Light is OFF
        }
    }
})()

const Strategy = (_ => { // Defining a family of algorithms and making them interchangeable

    interface Strategy {
        execute(a: number, b: number): number
    }
    
    class AddStrategy implements Strategy {
        execute(a: number, b: number): number {
            return a + b
        }
    }
    
    class SubtractStrategy implements Strategy {
        execute(a: number, b: number): number {
            return a - b
        }
    }
    
    class Context {
        constructor(private strategy: Strategy) {}
        
        doOperation(a: number, b: number): number {
            return this.strategy.execute(a, b)
        }
    }
    
    return {
        test() {
            const addStrategy = new AddStrategy()
            const context = new Context(addStrategy)
            
            console.log(context.doOperation(5, 3)) // Output: 8
            
            const subtractStrategy = new SubtractStrategy()
            context.strategy = subtractStrategy
            
            console.log(context.doOperation(5, 3)) // Output: 2
        }
    }
})()

const Iterator = (_ => { 
    // Providing a way to access elements without exposing the underlying structure

    class Iterator<T> {
        private index: number = 0
        
        constructor(private items: T[]) {}
        
        hasNext(): boolean {
            return this.index < this.items.length
        }
        
        next(): T {
            return this.items[this.index++]
        }
    }
    
    return {
        test() {
            const items = [1, 2, 3, 4]
            const iterator = new Iterator(items)
            
            while (iterator.hasNext()) {
                console.log(iterator.next()) // Output: 1 2 3 4
            }
        }
    }
})()

const Template = (_ => { // Defining the skeleton of an algorithm

    abstract class AbstractClass {
        abstract step1(): void
        abstract step2(): void
        
        templateMethod(): void {
            this.step1()
            this.step2()
        }
    }
    
    class ConcreteClass extends AbstractClass {
        step1(): void {
            console.log('Step 1')
        }
        
        step2(): void {
            console.log('Step 2')
        }
    }
    
    return {
        test() {
            const concrete = new ConcreteClass()
            concrete.templateMethod()
            // Output:
            // Step 1
            // Step 2
        }
    }
})()

const Mediator = (_ => { // Defining an object that encapsulates how objects interact

    interface Mediator {
        notify(sender: object, event: string): void
    }
    
    class ConcreteMediator implements Mediator {
        private component1: Component1
        private component2: Component2
        
        constructor(component1: Component1, component2: Component2) {
            this.component1 = component1
            this.component2 = component2
            this.component1.setMediator(this)
            this.component2.setMediator(this)
        }
        
        notify(sender: object, event: string): void {
            if (sender === this.component1 && event === 'A') {
                console.log('Mediator reacts to A')
            }
            if (sender === this.component2 && event === 'B') {
                console.log('Mediator reacts to B')
            }
        }
    }
    
    class Component1 {
        private mediator: Mediator
        
        setMediator(mediator: Mediator): void {
            this.mediator = mediator
        }
        
        doA(): void {
            console.log('Component1 does A')
            this.mediator.notify(this, 'A')
        }
    }
    
    class Component2 {
        private mediator: Mediator
        
        setMediator(mediator: Mediator): void {
            this.mediator = mediator
        }
        
        doB(): void {
            console.log('Component2 does B')
            this.mediator.notify(this, 'B')
        }
    }
    
    return {
        test() {
            const component1 = new Component1()
            const component2 = new Component2()
            const mediator = new ConcreteMediator(component1, component2)
            
            component1.doA() // Output: Component1 does A
                               //         Mediator reacts to A
            component2.doB() // Output: Component2 does B
                               //         Mediator reacts to B
        }
    }
})()

const Memento = (_ => { // Capturing and restoring an object's internal state

    class Memento {
        constructor(public state: string) {}
    }
    
    class Originator {
        private state: string = ''
        
        setState(state: string): void {
            this.state = state
        }
        
        save(): Memento {
            return new Memento(this.state)
        }
        
        restore(memento: Memento): void {
            this.state = memento.state
        }
        
        showState(): void {
            console.log(`State: ${this.state}`)
        }
    }
    
    return {
        test() {
            const originator = new Originator()
            originator.setState('State1')
            const memento = originator.save()
            
            originator.setState('State2')
            originator.showState() // Output: State: State2
            
            originator.restore(memento)
            originator.showState() // Output: State: State1
        }
    }
})()

const Visitor = (_ => { // Defining new operations without changing the classes of the elements

    interface Visitor {
        visitA(element: ElementA): void
        visitB(element: ElementB): void
    }
    
    class ConcreteVisitor implements Visitor {
        visitA(element: ElementA): void {
            console.log('Visited ElementA')
        }
        
        visitB(element: ElementB): void {
            console.log('Visited ElementB')
        }
    }
    
    interface Element {
        accept(visitor: Visitor): void
    }
    
    class ElementA implements Element {
        accept(visitor: Visitor): void {
            visitor.visitA(this)
        }
    }
    
    class ElementB implements Element {
        accept(visitor: Visitor): void {
            visitor.visitB(this)
        }
    }
    
    return {
        test() {
            const visitor = new ConcreteVisitor()
            const elementA = new ElementA()
            const elementB = new ElementB()
            
            elementA.accept(visitor) // Output: Visited ElementA
            elementB.accept(visitor) // Output: Visited ElementB
        }
    }
})()

const ChainOfResponsibility = (_ => { // Passing a request along a chain of handlers

    interface Handler {
        setNext(handler: Handler): Handler
        handle(request: string): void
    }
    
    class BaseHandler implements Handler {
        private nextHandler: Handler | null = null
        
        setNext(handler: Handler): Handler {
            this.nextHandler = handler
            return handler
        }
        
        handle(request: string): void {
            if (this.nextHandler) {
                this.nextHandler.handle(request)
            }
        }
    }
    
    class ConcreteHandlerA extends BaseHandler {
        handle(request: string): void {
            if (request === 'A') {
                console.log('Handler A processed request A')
            } else {
                super.handle(request)
            }
        }
    }
    
    class ConcreteHandlerB extends BaseHandler {
        handle(request: string): void {
            if (request === 'B') {
                console.log('Handler B processed request B')
            } else {
                super.handle(request)
            }
        }
    }
    
    return {
        test() {
            const handlerA = new ConcreteHandlerA()
            const handlerB = new ConcreteHandlerB()
            
            handlerA.setNext(handlerB)
            
            handlerA.handle('A') // Output: Handler A processed request A
            handlerA.handle('B') // Output: Handler B processed request B
            handlerA.handle('C') // (No output, as no handler for 'C')
        }
    }
})()


// * Others

const Module = (_ => { // Organizing code into modules

    const UserModule = (_ => {
        type User = {
            id: string
        }

        const users: User[] = []

        const addUser = user => users.push(user)

        const getUser = id => users.find(user => user?.id === id)

        return {
            addUser,
            getUser
        }
    })()

    return {
        test() {
            UserModule.addUser({ id: 1, name: 'Alice', age: 25 })
            console.log(UserModule.getUser(1)) // { id: 1, name: 'Alice', age: 25 }
        }
    }
})()

const Middleware = (_ => { // Functions that process requests in a pipeline

    function loggerMiddleware(req: any, res: any, next: () => void) {
        console.log('Request received')
        next()
    }
    
    function requestHandler(req: any, res: any) {
        res.send('Hello World')
    }
    
    // Simulating request pipeline
    function simulateRequest() {
        const req = {}
        const res = { send: (msg: string) => console.log(msg) }
        
        loggerMiddleware(req, res, () => requestHandler(req, res))
    }    
    
    return {
        test() {
            simulateRequest() // Output: Request received [\n] Hello World
        }
    }
})()

const DependencyInjection = (_ => { // Providing dependencies from outside the object

    class Service {
        performAction(): void {
            console.log('Service action performed')
        }
    }
    
    class Client {
        constructor(private service: Service) {}
        
        execute(): void {
            this.service.performAction()
        }
    }
    
    return {
        test() {
            const service = new Service()
            const client = new Client(service)
            client.execute() // Output: Service action performed
        }
    }
})()

const ServiceLocator = (_ => { // Central registry for service instances

    class ServiceLocator {
        private services = new Map<string, any>()
        
        register<T>(key: string, service: T): void {
            this.services.set(key, service)
        }
        
        get<T>(key: string): T {
            return this.services.get(key)
        }
    }
    
    // Example Service
    class LoggingService {
        log(message: string): void {
            console.log(message)
        }
    }
    
    return {
        test() {
            const serviceLocator = new ServiceLocator()
            serviceLocator.register('logging', new LoggingService())
            
            const loggingService = serviceLocator.get<LoggingService>('logging')
            loggingService.log('Hello World') // Output: Hello World
        }
    }
})()

const Repository = (_ => { // Abstracting data access from business logic

    class User {
        constructor(public id: number, public name: string) {}
    }
    
    class UserRepository {
        private users: User[] = []
        
        add(user: User): void {
            this.users.push(user)
        }
        
        findById(id: number): User | undefined {
            return this.users.find(user => user.id === id)
        }
    }
    
    return {
        test() {
            const repository = new UserRepository()
            const user = new User(1, 'Charlie')
            repository.add(user)
            console.log(repository.findById(1)?.name) // Output: Charlie
        }
    }
})()

const ActiveRecord = (_ => { // Combining data access with the domain object

    class User {
        constructor(public id: number, public name: string) {}
        
        save(): void {
            // Simulate saving to a database
            console.log(`User ${this.name} saved`)
        }
    }
    
    return {
        test() {
            const user = new User(1, 'David')
            user.save() // Output: User David saved
        }
    }
})()

const Specification = (_ => { // Encapsulating business rules

    interface Specification<T> {
        isSatisfiedBy(item: T): boolean
    }
    
    class User {
        constructor(public name: string, public age: number) {}
    }
    
    class AgeSpecification implements Specification<User> {
        constructor(private minAge: number) {}
        
        isSatisfiedBy(user: User): boolean {
            return user.age >= this.minAge
        }
    }
    
    return {
        test() {
            const user = new User('Emma', 25)
            const ageSpec = new AgeSpecification(18)
            console.log(ageSpec.isSatisfiedBy(user)) // Output: true
        }
    }
})()


////////////////////////////////////////
//  OTHER PATTERNS
////////////////////////////////////////

const EventDriven = (_ => { // Triggering events and handling them asynchronously

    class EventBus {
        private listeners = new Map<string, ((...args: any[]) => void)[]>()
        
        on(event: string, listener: (...args: any[]) => void): void {
            if (!this.listeners.has(event)) {
                this.listeners.set(event, [])
            }
            this.listeners.get(event)?.push(listener)
        }
        
        emit(event: string, ...args: any[]): void {
            this.listeners.get(event)?.forEach(listener => listener(...args))
        }
    }
    
    return {
        test() {
            const eventBus = new EventBus()
            eventBus.on('dataReceived', data => console.log(`Received: ${data}`))
            eventBus.emit('dataReceived', 'Sample Data') // Output: Received: Sample Data
        }
    }
})()

const EventAggregator = (_ => { // Centralizing event handling

    class EventAggregator {
        private events = new Map<string, ((...args: any[]) => void)[]>()
        
        subscribe(eventName: string, callback: (...args: any[]) => void): void {
            if (!this.events.has(eventName)) {
                this.events.set(eventName, [])
            }
            this.events.get(eventName)?.push(callback)
        }
        
        publish(eventName: string, ...args: any[]): void {
            this.events.get(eventName)?.forEach(callback => callback(...args))
        }
    }
    
    return {
        test() {
            const eventAggregator = new EventAggregator()
            eventAggregator.subscribe('event1', message => console.log(message))
            eventAggregator.publish('event1', 'Hello Event Aggregator!') // Output: Hello Event Aggregator!
        }
    }
})()


const ModuleTypes = (_ => {

    { // CommonJS (Node.js)

        // module.js
        const sayHello = () => {
            console.log('Hello, world!')
        }

        export = sayHello // * Module Exports

        /*
        
        export = { sayHello } // * Module Exports
        export default sayHello // * Default Exports
        export const _sayHello = sayHello // * Named Exports
        export { sayHello as sH } from './module' // * Re-exports

        module.exports = sayHello // * Js-Module Exports
        module.exports = { sayHello } // * Js-Module Exports
        exports.sayHello = sayHello // * Js-Module-Named Exports

        */
        
    }

    { // ES Modules (ECMAScript 6)

        export const sayHello = () => {
            console.log('Hello, world!')
        }

    }

    { // SystemJS
        
        export const sayHello = () => {
            console.log('Hello, world!')
        }
          
    }

    // * set compilerOption: "module": "amd" / "umd", in tsconfig.js for AMD & UMD

    { // AMD (Asynchronous Module Definition) 1

        define(['dependency'], function (dependency) {
            const sayHello = () => {
                console.log('Hello, world!')
            }

            return {
                sayHello: sayHello
            }
        })

    }

    { // AMD (Asynchronous Module Definition) 2

        define(['require', 'exports'], function (require, exports) {
            const sayHello = () => {
                console.log('Hello, world!')
            }

            exports.sayHello = sayHello
        })

    }

    { // UMD (Universal Module Definition) 1

        (function (root, factory) {
            if (typeof define === 'function' && define.amd) {
                // AMD
                define([], factory)
            } else if (typeof module === 'object' && module.exports) {
                // CommonJS
                module.exports = factory()
            } else {
                // Browser global
                root.module = factory()
            }
        }(this, function () {
            const sayHello = () => {
                console.log('Hello, world!')
            }

            return {
                sayHello: sayHello
            }
        }))

    }

    { // UMD (Universal Module Definition) 2

        (function (root, factory) {
            if (typeof define === 'function' && define.amd) {
                // AMD
                define(['exports'], factory)
            } else if (typeof module === 'object' && module.exports) {
                // CommonJS
                factory(exports)
            } else {
                // Browser global
                factory((root.module = {}))
            }
        }(this, function (exports) {
            const sayHello = () => {
                console.log('Hello, world!')
            }

            exports.sayHello = sayHello
        }))

    }

    { // IIFE (Immediately Invoked Function Expression)

        const module = (function () {
            const sayHello = () => {
                console.log('Hello, world!')
            }

            return {
                sayHello: sayHello
            }
        })()

        export default module

    }

    { // main.ts
        
        // * ES 6
        import { sayHello } from './module'
        sayHello()

        /* 

        * CommonJS
        const sayHello = require('./module')

        * CommonJS - Import assignment
        import sayHello = require('./module')

        * AMD
        require(['module'], function (module) {
            module.sayHello()
        })

        * SystemJS
        System.import('./module.js').then(module => {
            module.sayHello()
        })
        
        * ES Modules with Dynamic Import
        import('./module.js').then(module => {
            module.sayHello()
        })

        * ES Modules in HTML (Script Type Module)
        <script type="module">
            import { sayHello } from './module.js'
            sayHello()
        </script>
        
        */

    }

})()


////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function mainT() {
    console.log("Hello, World!")
}
