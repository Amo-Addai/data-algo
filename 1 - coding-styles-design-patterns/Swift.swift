import Foundation
import SwiftUI
import ObjectiveC.runtime

/* // TODO: To-Use

Generics
some, convenience, ..
..

*/


////////////////////////////////////////
//  CODING STYLES
////////////////////////////////////////

class Obj {
    
    class User {
        private var _id: Int
        private var _name: String
        private var _age: Int?
        
        init(id: Int, name: String, age: Int?) {
            self._id = id
            self._name = name
            self._age = age
        }
        
        var id: Int {
            get { return _id }
            set { _id = newValue }
        }
        
        var name: String {
            get { return _name }
            set { _name = newValue }
        }
        
        var age: Int? {
            get { return _age }
            set {
                if newValue ?? 0 >= 0 {
                    _age = newValue
                } else {
                    print("Age cannot be negative")
                }
            }
        }
        
        public func getDetails() -> String {
            guard self.age != nil
            else {
                return "\(self.name)"
            }
            return "\(self.name), Age: \(self.age!)"
        }
    }
    
    class Car {
        var color: String

        init(color: String = "black") {
            self.color = color
        }

        func drive() {
            print("Driving a \(color) car")
        }
    }
    
}

let Imperative = {
    let numbers = [1, 2, 3, 4, 5]
    var sum = 0

    for number in numbers {
        sum += number
    }

    print("Sum: \(sum)")
}

let Functional = {
    let numbers = [1, 2, 3, 4, 5]
    let sum = numbers.reduce(0, +)

    print("Sum: \(sum)")
}

let Declarative = {
    struct ContentView: View {
        var body: some View {
            Text("Hello, World!")
                .padding()
        }
    }

    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            ContentView()
        }
    }

    // todo: Use Views
}

let OOP = {
    let car = Obj.Car(color: "red")
    car.drive()
}

// Aspect-Oriented Programming

// using protocol extension
protocol Logged {
    func log()
}

extension Logged {
    func log() {
        print("Logging...")
    }
}

// Aspect-Oriented Programming (AOP) is not directly supported in Swift,
// but you can use method swizzling as an approximation

extension NSObject {
    static func swizzleMethod(originalSelector: Selector, swizzledSelector: Selector) {
        guard
            let originalMethod = class_getInstanceMethod(self, originalSelector),
              let swizzledMethod = class_getInstanceMethod(self, swizzledSelector)
        else {
            return
        }

        let didAddMethod = class_addMethod(self,
                                           originalSelector,
                                           method_getImplementation(swizzledMethod),
                                           method_getTypeEncoding(swizzledMethod))
        
        if didAddMethod {
            class_replaceMethod(self,
                                swizzledSelector,
                                method_getImplementation(originalMethod),
                                method_getTypeEncoding(originalMethod))
        } else {
            method_exchangeImplementations(originalMethod, swizzledMethod)
        }
    }
}

let AOP = {
    
    class BusinessLogic: Logged {
        func performTask() {
            log()
            print("Performing task")
        }
    }

    let logic = BusinessLogic()
    logic.performTask()
    
    class MyClass {
        @objc dynamic func originalMethod() {
            print("Original method")
        }
        
        @objc dynamic func swizzledMethod() {
            print("Swizzled method")
        }
    }
    
    // Example of method swizzling
    NSObject.swizzleMethod(originalSelector: #selector(MyClass.originalMethod),
                          swizzledSelector: #selector(MyClass.swizzledMethod))
    
    let instance = MyClass()
    instance.originalMethod()  // Output: Swizzled method
    
}

let AsyncAwait = {
    
    let fetchData = { () async -> String in
        return await withCheckedContinuation { continuation in
            DispatchQueue.global().asyncAfter(deadline: .now() + 2) {
                continuation.resume(returning: "Data fetched")
            }
        }
    }

    Task {
        let data = await fetchData()
        print(data)
    }
    
}

let LazyInit = {
    
    class LazyExample {
        lazy var expensiveComputation: Int = {
            print("Computing...")
            return 42
        }()
    }

    let example = LazyExample()
    print(example.expensiveComputation) // Output: Computing... 42
    print(example.expensiveComputation) // Output: 42

}

let Callback = {
    
    let fetchData = { (callback: @escaping (String) -> Void) in
        DispatchQueue.global().asyncAfter(deadline: .now() + 2) {
            callback("Data fetched")
        }
    }

    fetchData { data in
        print(data)
    }
    
}

let Optional_Null_Object = {
    
    class NullCar: Obj.Car {
        override init(color: String = "none") {
            super.init(color: color)
        }

        override func drive() {
            print("No car to drive")
        }
    }

    let car: Obj.Car? = nil
    (car ?? NullCar()).drive() // Output: No car to drive
    
}

let Encapsulation = {
    
    class BankAccount {
        private var balance: Double = 0

        func deposit(amount: Double) {
            balance += amount
        }

        func getBalance() -> Double {
            return balance
        }
    }

    let account = BankAccount()
    account.deposit(amount: 100)
    print("Balance: \(account.getBalance())")

}

// ObjectComposition

protocol Engine {
    func start()
}

let ObjectComposition = {
    
    class GasEngine: Engine {
        func start() {
            print("Starting gas engine")
        }
    }

    class ElectricEngine: Engine {
        func start() {
            print("Starting electric engine")
        }
    }

    class Vehicle {
        private let engine: Engine

        init(engine: Engine) {
            self.engine = engine
        }

        func start() {
            engine.start()
        }
    }

    let gasVehicle = Vehicle(engine: GasEngine())
    gasVehicle.start() // Output: Starting gas engine

    let electricVehicle = Vehicle(engine: ElectricEngine())
    electricVehicle.start() // Output: Starting electric engine

}

// Data Access Object (DAO)

protocol UserDAO {
    func getUser(byId id: Int) -> Obj.User?
}

let DAO = {
    
    class UserDAOMemory: UserDAO {
        private var users = [1: Obj.User(id: 1, name: "John Doe", age: nil)]

        func getUser(byId id: Int) -> Obj.User? {
            return users[id]
        }
    }

    // Example usage
    let userDao = UserDAOMemory()
    if let user = userDao.getUser(byId: 1) {
        print("User found: \(user.name)")
    } else {
        print("User not found")
    }

}

// Data Transfer Object (DTO)

let DTO = {
    
    struct UserDTO {
        let id: Int
        let name: String
    }

    // Example usage
    let userDto = UserDTO(id: 1, name: "John Doe")
    print("User DTO: \(userDto.name)")

}


////////////////////////////////////////
//  DESIGN PATTERNS
////////////////////////////////////////

// * Creational

let Singleton = {
    
    class Singleton {
        static let shared = Singleton()

        private init() {}

        func doSomething() {
            print("Doing something")
        }
    }

    // Example usage
    Singleton.shared.doSomething() // Output: Doing something

}

// Factory

protocol Shape {
    func draw()
}

let Factory = {
    
    class Circle: Shape {
        func draw() {
            print("Drawing Circle")
        }
    }

    class Square: Shape {
        func draw() {
            print("Drawing Square")
        }
    }

    class ShapeFactory {
        enum ShapeType {
            case circle, square
        }

        static func createShape(type: ShapeType) -> Shape {
            switch type {
            case .circle:
                return Circle()
            case .square:
                return Square()
            }
        }
    }

    // Example usage
    let circle = ShapeFactory.createShape(type: .circle)
    circle.draw() // Output: Drawing Circle

    let square = ShapeFactory.createShape(type: .square)
    square.draw() // Output: Drawing Square

}

// Prototype

protocol Copying {
    init(copy: Self)
}

let PrototypePattern = {
    
    class Prototype: Copying {
        var value: String

        init(value: String) {
            self.value = value
        }

        required init(copy: Prototype) {
            self.value = copy.value
        }

        func clone() -> Prototype {
            return Prototype(copy: self)
        }
    }

    // Example usage
    let original = Prototype(value: "Hello")
    let copy = original.clone()
    print("Original: \(original.value), Copy: \(copy.value)")

}

// Abstract Factory

protocol Button {
    func click()
}

protocol GUIFactory {
    func createButton() -> Button
}

let AbstractFactory = {
    
    class WindowsButton: Button {
        func click() {
            print("Windows button clicked")
        }
    }

    class MacButton: Button {
        func click() {
            print("Mac button clicked")
        }
    }

    class WindowsFactory: GUIFactory {
        func createButton() -> Button {
            return WindowsButton()
        }
    }

    class MacFactory: GUIFactory {
        func createButton() -> Button {
            return MacButton()
        }
    }

    // Example usage
    func createUI(factory: GUIFactory) {
        let button = factory.createButton()
        button.click()
    }

    let windowsFactory = WindowsFactory()
    createUI(factory: windowsFactory) // Output: Windows button clicked

    let macFactory = MacFactory()
    createUI(factory: macFactory) // Output: Mac button clicked

}


// * Structural


// * Behavioral


// * Others

// Module

// File: MathOperations.swift
public struct MathOperations { // - Attribute 'public' can only be used in a non-local scope
    public static func add(_ a: Int, _ b: Int) -> Int {
        return a + b
    }
}

let Module = {

    let result = MathOperations.add(3, 5)
    print("Result: \(result)")

}

let Middleware = {
    
    // Middleware style
    typealias Middleware = (String) -> String

    let uppercaseMiddleware = { (input: String) -> String in
        return input.uppercased()
    }

    let exclamationMiddleware = { (input: String) -> String in
        return "\(input)!"
    }

    let applyMiddlewares = { (_ input: String, middlewares: [Middleware]) -> String in
        return middlewares.reduce(input) { result, middleware in
            middleware(result)
        }
    }

    let middlewares: [Middleware] = [uppercaseMiddleware, exclamationMiddleware]
    let result = applyMiddlewares("hello", middlewares)
    print(result) // Output: HELLO!

}

let FluentInterface = {
    
    class QueryBuilder {
        private var query = ""

        func select(_ fields: String) -> QueryBuilder {
            query += "SELECT \(fields) "
            return self
        }

        func from(_ table: String) -> QueryBuilder {
            query += "FROM \(table) "
            return self
        }

        func whereCondition(_ condition: String) -> QueryBuilder {
            query += "WHERE \(condition)"
            return self
        }

        func build() -> String {
            return query
        }
    }

    let query = QueryBuilder()
        .select("*")
        .from("users")
        .whereCondition("age > 21")
        .build()

    print(query) // Output: SELECT * FROM users WHERE age > 21
    
}

// State

protocol State {
    func handle(context: Context)
}

class Context {
    var state: State?

    func request() {
        state?.handle(context: self)
    }
}

let StatePattern = {

    class ConcreteStateA: State {
        func handle(context: Context) {
            print("State A handling request")
            context.state = ConcreteStateB()
        }
    }

    class ConcreteStateB: State {
        func handle(context: Context) {
            print("State B handling request")
            context.state = ConcreteStateA()
        }
    }

    // Example usage
    let context = Context()
    context.state = ConcreteStateA()
    context.request() // Output: State A handling request
    context.request() // Output: State B handling request
    context.request() // Output: State A handling request
    context.request() // Output: State B handling request

}

// Interpreter

protocol Expression {
    func interpret(context: String) -> Bool
}

let Interpreter = {

    class TerminalExpression: Expression {
        private let data: String

        init(data: String) {
            self.data = data
        }

        func interpret(context: String) -> Bool {
            return context.contains(data)
        }
    }

    class OrExpression: Expression {
        private let expr1: Expression
        private let expr2: Expression

        init(expr1: Expression, expr2: Expression) {
            self.expr1 = expr1
            self.expr2 = expr2
        }

        func interpret(context: String) -> Bool {
            return expr1.interpret(context: context) || expr2.interpret(context: context)
        }
    }

    class AndExpression: Expression {
        private let expr1: Expression
        private let expr2: Expression

        init(expr1: Expression, expr2: Expression) {
            self.expr1 = expr1
            self.expr2 = expr2
        }

        func interpret(context: String) -> Bool {
            return expr1.interpret(context: context) && expr2.interpret(context: context)
        }
    }

    // Example usage
    let robert = TerminalExpression(data: "Robert")
    let john = TerminalExpression(data: "John")
    let julie = TerminalExpression(data: "Julie")
    let married = TerminalExpression(data: "Married")

    let isMale = OrExpression(expr1: robert, expr2: john)
    let isMarriedWoman = AndExpression(expr1: julie, expr2: married)

    print("John is male? \(isMale.interpret(context: "John"))")  // Output: John is male? true
    print("Julie is a married woman? \(isMarriedWoman.interpret(context: "Married Julie"))")  // Output: Julie is a married woman? true

}

// Dependency Injection

protocol Service {
    func execute()
}

let DependencyInjection = {
    
    class ConcreteService: Service {
        func execute() {
            print("Executing service")
        }
    }

    class Client {
        private let service: Service

        init(service: Service) {
            self.service = service
        }

        func doWork() {
            service.execute()
        }
    }

    // Example usage
    let service = ConcreteService()
    let client = Client(service: service)
    client.doWork() // Output: Executing service

}


////////////////////////////////////////
//  OTHER PATTERNS
////////////////////////////////////////

let EventDriven = {
    
    class EventManager {
        var listeners = [String: [(String) -> Void]]()

        func subscribe(eventType: String, listener: @escaping (String) -> Void) {
            if listeners[eventType] != nil {
                listeners[eventType]?.append(listener)
            } else {
                listeners[eventType] = [listener]
            }
        }

        func notify(eventType: String, data: String) {
            listeners[eventType]?.forEach { $0(data) }
        }
    }

    // Example usage
    let eventManager = EventManager()

    eventManager.subscribe(eventType: "onDataReceived") { data in
        print("Data received: \(data)")
    }

    eventManager.notify(eventType: "onDataReceived", data: "Hello World")
    // Output: Data received: Hello World

}

let EventAggregatorPattern = {
    
    class EventAggregator {
        static let shared = EventAggregator()
        private var listeners = [String: [(String) -> Void]]()

        private init() {}

        func subscribe(event: String, listener: @escaping (String) -> Void) {
            if listeners[event] != nil {
                listeners[event]?.append(listener)
            } else {
                listeners[event] = [listener]
            }
        }

        func publish(event: String, data: String) {
            listeners[event]?.forEach { $0(data) }
        }
    }

    // Example usage
    EventAggregator.shared.subscribe(event: "TestEvent") { data in
        print("Received: \(data)")
    }

    EventAggregator.shared.publish(event: "TestEvent", data: "Hello World")
    // Output: Received: Hello World

}



////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

func main(args: [String]? = nil) {
    print("Hello, World!")
}
main()
