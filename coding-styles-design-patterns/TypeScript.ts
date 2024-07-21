'use strict'

/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  CODING STYLES
////////////////////////////////////////


////////////////////////////////////////
//  DESIGN PATTERNS
////////////////////////////////////////

// * Creational


// * Structural


// * Behavioral


// * Others

const Module = (_ => {

    // todo: Sample Modules 1st (un-used)

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

    // todo: Now, main User Module (used)

})()


////////////////////////////////////////
//  OTHER PATTERNS
////////////////////////////////////////




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

function mainT() {
    console.log("Hello, World!")
}
