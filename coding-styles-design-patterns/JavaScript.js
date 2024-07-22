'use strict'

/* // TODO: To-Use

Generics
..

*/

////////////////////////////////////////
//  CODING STYLES
////////////////////////////////////////

const Imperative = _ => {
    let sum = 0
    for (let i = 1; i <= 10; i++) {
        sum += i
    }
    console.log(sum) // Output: 55
}

const Functional = (_ => {
    const users = [
        { id: 1, name: 'Alice', age: 25 },
        { id: 2, name: 'Bob', age: 30 }
    ]

    const getUserById = (id) => users.find(user => user.id === id)
    const getAllUserNames = () => users.map(user => user.name)

    return {
        test() {
            console.log(getUserById(1)) // { id: 1, name: 'Alice', age: 25 }
            console.log(getAllUserNames()) // ['Alice', 'Bob']
        }
    }
})()

define(['Declarative'], _ => { // AMD (Asynchronous Module Definition)

    const numbers = [1, 2, 3, 4, 5]
    const doubled = numbers.map(n => n * 2)

    return {
        test() {
            console.log(doubled) // [2, 4, 6, 8, 10]
        }
    }

})

const OOP = (_ => {

    class User {
        constructor (id, name, age) {
            this.id = id
            this.name = name
            this.age = age
        }

        getDetails () {
            return `${this.name}, Age: ${this.age}`
        }
    }

    return {
        test() {
            const user = new User(1, 'Alice', 25)
            console.log(user.getDetails())            
        }
    }
})()

const Promises_AsyncAwait = (_ => {
    const fetchUserData = (id) => {
        return new Promise((resolve) => {
            setTimeout(() => {
            resolve({ id: id, name: 'Alice', age: 25 })
            }, 1000)
        })
    }
    
    const displayUser = async (id) => {
        const user = await fetchUserData(id)
        console.log(user)
    }
    
    return {
        test() {
            displayUser(1) // { id: 1, name: 'Alice', age: 25 }
        }
    }
})()

const Callback = (_ => {
    const fs = require('fs')

    const readFile = _ =>
        fs.readFile('example.txt', 'utf8', (err, data) =>
            err
                ? console.error(err)
                : console.log(data)
        )

    return {
        test() {
            readFile()
        }
    }
})()

const ObjectComposition = (_ => {
    const canEat = {
        eat: function() {
            console.log('Eating...')
        }
    }
    
    const canWalk = {
        walk: function() {
            console.log('Walking...')
        }
    }
    
    const person = Object.assign({}, canEat, canWalk)
    
    return {
        test: _ => {
            person.eat() // Eating...
            person.walk() // Walking...            
        }
    }
})()


////////////////////////////////////////
//  DESIGN PATTERNS
////////////////////////////////////////

// * Creational

const Prototype = (_ => {
    function User(id, name, age) {
        this.id = id
        this.name = name
        this.age = age
    }
    const x = {}
    const y = { ...x }
    
    User.prototype.getDetails = function() {
        return `${this.name}, Age: ${this.age}`
    }

    User.prototype.clone = _ => // * { ...(this) } -> ...this / ...(this) - syntax not interpreted yet
        { this.id, this.name, this.age }
    
    const user = new User(1, 'Alice', 25)
      
    return {
        test() {
            console.log(user.getDetails())
            console.log(user.clone().getDetails())            
        }
    }
})()

// * Structural


// * Behavioral


// * Others

const Module = (_ => {

    const UserModule = (function() {
        const users = []
        
        const addUser = (user) => {
            users.push(user)
        }
        
        const getUser = (id) => users.find(user => user.id === id)
        
        return {
            addUser,
            getUser,
        }
    })()
  
    return {
        test() {
            UserModule.addUser({ id: 1, name: 'Alice', age: 25 })
            console.log(UserModule.getUser(1)) // { id: 1, name: 'Alice', age: 25 }
        }
    }    
})()

const Middleware = (_ => {
    const express = require('express')
    const app = express()

    const logger = (req, res, next) => {
        console.log(`${req.method} ${req.url}`)
        next()
    }

    app.use(logger)

    app.get('/', (req, res) => {
        res.send('Hello, world!')
    })

    app.listen(3000, () => {
        console.log('Server is running on port 3000')
    })

    return {
        test() {
            return app
        }
    }
})()


////////////////////////////////////////
//  OTHER PATTERNS
////////////////////////////////////////

const EventDriven = (_ => {
    const EventEmitter = require('events')
    class UserEmitter extends EventEmitter {}

    const userEmitter = new UserEmitter()

    userEmitter.on('userCreated', (user) => {
        console.log(`User created: ${user.name}`)
    })

    const triggerEmit = _ => 
        userEmitter.emit('userCreated', { name: 'Alice' }) // User created: Alice

    return {
        test() {
            triggerEmit()
        }
    }
})()



const ModuleTypes = (_ => {

    { // CommonJS (Node.js)

        // module.js
        const sayHello = () => {
            console.log('Hello, world!')
        }
        
        module.exports = sayHello // * Module Exports
        
        /*

        module.exports = { sayHello } // * Module Exports
        exports.sayHello = sayHello // * Module-Named Exports

        export = sayHello // * Module Exports
        export = { sayHello } // * Module Exports
        export default sayHello // * Default Exports
        export const _sayHello = sayHello // * Named Exports
        export { sayHello as sH } from './module' // * Re-exports

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

    { // AMD (Asynchronous Module Definition) 1

        define(['dependency'], function(dependency) {
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

        const module = (function() {
            const sayHello = () => {
              console.log('Hello, world!')
            }
          
            return {
              sayHello: sayHello
            }
        })()

        export default module
          
    }

    { // main.js

        // * CommonJS
        const sayHello = require('./module')
        sayHello()

        /* 

        * CommonJS - Import assignment
        import sayHello = require('./module')

        * ES 6
        import { sayHello } from './module'
        
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

function main () {
    document.write('Hello, World!')
}
