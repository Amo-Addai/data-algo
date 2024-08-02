// #include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <map>
#include <iterator>
#include <vector>
#include <algorithm>
#include <functional>
#include <future>
#include <optional>
#include <memory>
#include <unordered_map>

using namespace std;

/* // TODO: To-Use

Generics
MemMan, ..
..

*/


////////////////////////////////////////
//  CODING STYLES
////////////////////////////////////////

// * Imperative - Sample Module format

// Imperative.ixx - Module Interface File

export module Imperative;

export void imperativeExample();
export void test();

// Imperative.cpp - Module Implementation File

// module Imperative;
// #include <iostream>

void imperativeExample() {
    int x = 10;
    int y = 20;
    int sum = x + y;
    std::cout << "Sum: " << sum << std::endl;
}

void test() {
    imperativeExample();
}

// main.cpp - Using the Module in Another File

// import Imperative;

int main() {
    test();
    return 0;
}

// Functional

// #include <iostream>
// #include <functional>

int add(int x, int y) {
    return x + y;
}

void test() {
    std::function<int(int, int)> add_func = add;
    int sum = add_func(10, 20);
    std::cout << "Sum: " << sum << std::endl;
}

// Declarative

// #include <iostream>
// #include <algorithm>
// #include <vector>

void test() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::for_each(vec.begin(), vec.end(), [](int n) { std::cout << n << " "; });
    std::cout << std::endl;
}


// TODO: Procedural (study basic, pascal, c..)


// TODO: Scripting (study bash, perl, ruby, py, node)


// TODO: Logic (study prolog, absys, datalog, alma-0)


// TODO: Markup (study html, css, xml - all ns, js, react)


// OOP

// #include <iostream>

class Point {
public:
    Point(int x, int y) : x(x), y(y) {}
    void print() {
        std::cout << "Point(" << x << "," << y << ")" << std::endl;
    }
private:
    int x, y;
};

void test() {
    Point p(10, 20);
    p.print();
}

// Aspect-Oriented (AOP)

// #include <iostream>

#define LOG(func) \
    std::cout << "Calling function: " << #func << std::endl; \
    func;

void exampleFunction() {
    std::cout << "Function executed" << std::endl;
}

void test() {
    LOG(exampleFunction());
}

// Promises / Async-Await

// #include <iostream>
// #include <future>

void asyncTask() {
    std::cout << "Async task executed" << std::endl;
}

void test() {
    std::future<void> result = std::async(std::launch::async, asyncTask);
    result.get();
}

// Lazy Initialization

// #include <iostream>

class Lazy {
public:
    int& getValue() {
        static int value = 0;
        static bool initialized = false;
        if (!initialized) {
            value = 42;
            initialized = true;
        }
        return value;
    }
};

void test() {
    Lazy lazy;
    std::cout << "Lazy value: " << lazy.getValue() << std::endl;
}

// Callback

// #include <iostream>
// #include <functional>

void callbackFunction(int result) {
    std::cout << "Callback called with result: " << result << std::endl;
}

void executeWithCallback(std::function<void(int)> callback) {
    int result = 42; // Simulated result
    callback(result);
}

void test() {
    executeWithCallback(callbackFunction);
}

// Optional / Null Object

// #include <iostream>
// #include <optional>

std::optional<int> getOptionalValue(bool returnNull) {
    if (returnNull)






////////////////////////////////////////
//  DESIGN PATTERNS
////////////////////////////////////////

// * Creational


// * Structural


// * Behavioral


// * Concurrency


// * Functional


// * Others

// Module

// my_module.h
#ifndef MY_MODULE_H
#define MY_MODULE_H

void printMessage();

#endif // MY_MODULE_H
// my_module.cpp
// #include "my_module.h"
// #include <iostream>

void printMessage() {
    std::cout << "Hello from my module!" << std::endl;
}

// main.cpp
// #include "my_module.h"

void test() {
    printMessage();
}

// Middleware

// #include <iostream>
// #include <vector>
// #include <functional>

void middleware1() {
    std::cout << "Middleware 1" << std::endl;
}

void middleware2() {
    std::cout << "Middleware 2" << std::endl;
}

void executeMiddlewares(const std::vector<std::function<void()>>& middlewares) {
    for (const auto& middleware : middlewares) {
        middleware();
    }
}

void test() {
    std::vector<std::function<void()>> middlewares = { middleware1, middleware2 };
    executeMiddlewares(middlewares);
}





////////////////////////////////////////
//  ARCHITECTURE PATTERNS
////////////////////////////////////////





////////////////////////////////////////
//  OTHER PATTERNS
////////////////////////////////////////




// * Module Types

// mymodule.ixx - Module Interface File

export module mymodule;

export void printMessage();

// mymodule.cpp - Module Implementation File

module mymodule;

#include <iostream>

void printMessage() {
    std::cout << "Hello from the module!" << std::endl;
}

// main.cpp - Using the Module in Another File

import mymodule;

int main() {
    printMessage();
    return 0;
}

/* // * Compiling with a Compiler that Supports Modules (e.g., g++, clang++)

g++ -std=c++20 -fmodules-ts -c mymodule.cpp -o mymodule.o
g++ -std=c++20 -fmodules-ts -c main.cpp -o main.o
g++ main.o mymodule.o -o main
./main

*/


////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

int main(int argc, char** argv) {
    auto i = 0;
    cout << "Hello, World (" << i << ") !" << endl;

    return 0;
}

/** NOTES:

- 1 break statement in a nested loop, breaks out of both loops

*/