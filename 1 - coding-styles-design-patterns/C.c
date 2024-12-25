#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <string.h>
#include <pthread.h>

/* // TODO: To-Use

Generics
MemMan, ..
..

*/


////////////////////////////////////////
//  CODING STYLES
////////////////////////////////////////

// * Imperative - Sample Module format

// Imperative.h - Header File

#ifndef Imperative
#define Imperative

void imperativeExample();
void test();

#endif

// Imperative.c - Implementation File

// #include <stdio.h>
// #include "Imperative.h"

void imperativeExample() {
    int x = 10;
    int y = 20;
    int sum = x + y;
    printf("Sum: %d\n", sum);
}

void test() {
    imperativeExample();
}

// main.c - Using the Module in Another File

// #include "Imperative.h"

int main() {
    test();
    return 0;
}

// Functional

// #include <stdio.h>

int add(int x, int y) {
    return x + y;
}

void test() {
    int sum = add(10, 20);
    printf("Sum: %d\n", sum);
}

// Declarative

// #include <stdio.h>

#define SUM(x, y) ((x) + (y))

void test() {
    int result = SUM(10, 20);
    printf("Sum: %d\n", result);
}


// TODO: Procedural (study basic, pascal, c..)


// TODO: Scripting (study bash, perl, ruby, py, node)


// TODO: Logic (study prolog, absys, datalog, alma-0)


// TODO: Markup (study html, css, xml - all ns, js, react)


// OOP

// #include <stdio.h>
// #include <stdlib.h>

typedef struct {
    int x;
    int y;
} Point;

Point* createPoint(int x, int y) {
    Point* point = (Point*)malloc(sizeof(Point));
    point->x = x;
    point->y = y;
    return point;
}

void printPoint(Point* point) {
    printf("Point(%d, %d)\n", point->x, point->y);
}

void test() {
    Point* p = createPoint(10, 20);
    printPoint(p);
    free(p);
}

// Aspect-Oriented (AOP)

// #include <stdio.h>

#define LOG(func) \
    printf("Calling function: %s\n", #func); \
    func;

void exampleFunction() {
    printf("Function executed\n");
}

void test() {
    LOG(exampleFunction());
}

// Promises / Async-Await

// #include <stdio.h>
// #include <pthread.h>

void* asyncTask(void* arg) {
    printf("Async task executed\n");
    return NULL;
}

void test() {
    pthread_t thread;
    pthread_create(&thread, NULL, asyncTask, NULL);
    pthread_join(thread, NULL);
}

// Lazy Initialization

// #include <stdio.h>

int* lazyInit() {
    static int value = 0;
    static int initialized = 0;
    if (!initialized) {
        value = 42;
        initialized = 1;
    }
    return &value;
}

void test() {
    int* value = lazyInit();
    printf("Lazy value: %d\n", *value);
}

// Callback

// #include <stdio.h>

void callbackFunction(int result) {
    printf("Callback called with result: %d\n", result);
}

void executeWithCallback(void (*callback)(int)) {
    int result = 42; // Simulated result
    callback(result);
}

void test() {
    executeWithCallback(callbackFunction);
}

// Optional / Null Object

// #include <stdio.h>

int* getOptionalValue(int returnNull) {
    static int value = 42;
    if (returnNull) {
        return NULL;
    }
    return &value;
}

void test() {
    int* value = getOptionalValue(1);
    if (value) {
        printf("Value: %d\n", *value);
    } else {
        printf("Null value\n");
    }
}





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

// my_module.c
// #include "my_module.h"
// #include <stdio.h>

void printMessage() {
    printf("Hello from my module!\n");
}

// main.c
// #include "my_module.h"

void test() {
    printMessage();
}

// Middleware

// #include <stdio.h>

void middleware1() {
    printf("Middleware 1\n");
}

void middleware2() {
    printf("Middleware 2\n");
}

typedef void (*middleware_func)();

void executeMiddlewares(middleware_func middlewares[], int count) {
    for (int i = 0; i < count; ++i) {
        middlewares[i]();
    }
}

void test() {
    middleware_func middlewares[] = { middleware1, middleware2 };
    executeMiddlewares(middlewares, 2);
}





////////////////////////////////////////
//  ARCHITECTURE PATTERNS
////////////////////////////////////////





////////////////////////////////////////
//  OTHER PATTERNS
////////////////////////////////////////




// * Module Types

// module.h - Header File

#ifndef MODULE_H
#define MODULE_H

void printMessage();

#endif // MODULE_H

// module.c - Implementation File

#include <stdio.h>
#include "module.h"

void printMessage() {
    printf("Hello from the module!\n");
}

// main.c - Using the Module in Another File

#include "module.h"

int main() {
    printMessage();
    return 0;
}

/* // * Compiling and Linking

gcc -c module.c -o module.o
gcc -c main.c -o main.o
gcc main.o module.o -o main
./main

*/



////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void main(int argc, char* argv[]) {
    printf("Hello, World!");
}