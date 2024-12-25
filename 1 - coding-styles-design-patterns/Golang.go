package main // or lib

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

/* // TODO: To-Use

Generics
..

*/

////////////////////////////////////////
//  CODING STYLES
////////////////////////////////////////

type User struct {
	ID   int
	Name string
	Age  int
}

func Functional() {

	filter := func(users []User, fn func(User) bool) []User {
		var result []User
		for _, u := range users {
			if fn(u) {
				result = append(result, u)
			}
		}
		return result
	}

	mapUsers := func(users []User, fn func(User) string) {
		for _, u := range users {
			fmt.Println(fn(u))
		}
	}

	users := []User{
		{ID: 1, Name: "Alice", Age: 25},
		{ID: 2, Name: "Bob", Age: 30},
	}

	user := filter(users, func(u User) bool {
		return u.ID == 1
	})

	if len(user) > 0 {
		fmt.Println(user[0].Name)
	}

	mapUsers(users, func(u User) string {
		return u.Name
	})

}

func Declarative() {

	mapSlice := func(slice []int, fn func(int) int) []int {
		var result []int
		for _, v := range slice {
			result = append(result, fn(v))
		}
		return result
	}

	numbers := []int{1, 2, 3, 4, 5}
	doubled := mapSlice(numbers, func(x int) int {
		return x * 2
	})

	for _, v := range doubled {
		fmt.Println(v) // 2, 4, 6, 8, 10
	}
}

// OOP

func (u User) GetDetails() string {
	return fmt.Sprintf("%s, Age: %d", u.Name, u.Age)
} // TODO: convert owned func to func var

func OOP() {
	user := User{ID: 1, Name: "Alice", Age: 25}
	fmt.Println(user.GetDetails())
}

func GoRoutines_AsyncAwait() {

	fetchUserData := func(userId int) chan User {
		userChan := make(chan User)
		go func() {
			time.Sleep(1 * time.Second) // Simulate a network call
			userChan <- User{ID: userId, Name: "Alice", Age: 25}
		}()
		return userChan
	}

	userChan := fetchUserData(1)
	user := <-userChan
	fmt.Println(user.Name)
}

func Callback() {

	type ReadFileCallback func(error, string)

	readFile := func(filePath string, callback ReadFileCallback) {
		file, err := os.Open(filePath)
		if err != nil {
			callback(err, "")
			return
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)
		var content string
		for scanner.Scan() {
			content += scanner.Text() + "\n"
		}

		if err := scanner.Err(); err != nil {
			callback(err, "")
			return
		}

		callback(nil, content)
	}

	readFile("example.txt", func(err error, data string) {
		if err != nil {
			fmt.Println("Error:", err)
		} else {
			fmt.Println(data)
		}
	})
}

// ObjectComposition

type EatBehavior interface {
	Eat()
}

type WalkBehavior interface {
	Walk()
}

type Eat struct{}
type Walk struct{}

func (e Eat) Eat() {
	fmt.Println("Eating...")
}

func (w Walk) Walk() {
	fmt.Println("Walking...")
}

type Person struct {
	eatBehavior  EatBehavior
	walkBehavior WalkBehavior
}

func (p Person) Eat() {
	p.eatBehavior.Eat()
}

func (p Person) Walk() {
	p.walkBehavior.Walk()
}

func ObjectComposition() {
	person := Person{eatBehavior: Eat{}, walkBehavior: Walk{}}
	person.Eat()
	person.Walk()
}

////////////////////////////////////////
//  DESIGN PATTERNS
////////////////////////////////////////

// * Creational

// Prototype

func (u User) Clone() User {
	return User{ID: u.ID, Name: u.Name, Age: u.Age}
}

func Prototype() {
	user := User{ID: 1, Name: "Alice", Age: 25}
	userClone := user.Clone()
	fmt.Println(userClone.GetDetails())
}

// * Structural

// * Behavioral

// * Others

// Module

var users = []User{}

func addUser(user User) {
	users = append(users, user)
}

func getUser(id int) *User {
	for _, u := range users {
		if u.ID == id {
			return &u
		}
	}
	return nil
}

func Module() {
	addUser(User{ID: 1, Name: "Alice", Age: 25})
	user := getUser(1)
	if user != nil {
		fmt.Println(user.Name)
	}
}

// Middleware

type Middleware func(string, func())

type MiddlewareChain struct {
	middlewares []Middleware
	index       int
}

func (mc *MiddlewareChain) Use(middleware Middleware) {
	mc.middlewares = append(mc.middlewares, middleware)
}

func (mc *MiddlewareChain) Next(context string) {
	if mc.index < len(mc.middlewares) {
		current := mc.middlewares[mc.index]
		mc.index++
		current(context, func() { mc.Next(context) })
	}
}

func Middleware_Pattern() {
	middlewareChain := &MiddlewareChain{}
	middlewareChain.Use(func(context string, next func()) {
		fmt.Println("Logging: " + context)
		next()
	})
	middlewareChain.Use(func(context string, next func()) {
		fmt.Println("Handling: " + context)
	})

	middlewareChain.Next("GET /home")
}

////////////////////////////////////////
//  OTHER PATTERNS
////////////////////////////////////////

// Event-Driven

type EventListener func(interface{})

type EventEmitter struct {
	listeners map[string][]EventListener
}

func NewEventEmitter() *EventEmitter {
	return &EventEmitter{
		listeners: make(map[string][]EventListener),
	}
}

func (e *EventEmitter) On(event string, listener EventListener) {
	e.listeners[event] = append(e.listeners[event], listener)
}

func (e *EventEmitter) Emit(event string, data interface{}) {
	for _, listener := range e.listeners[event] {
		listener(data)
	}
}

func EventDriven() {

	/*

		type EventListener func(interface{})

		type EventEmitter struct {
			listeners map[string][]EventListener
		}

		NewEventEmitter := func() *EventEmitter {
			return &EventEmitter{
				listeners: make(map[string][]EventListener),
			}
		}

		(e *EventEmitter) On func (event string, listener EventListener)
		On := (e *EventEmitter) func (event string, listener EventListener) {
			e.listeners[event] = append(e.listeners[event], listener)
		}

		Emit := func (e *EventEmitter) (event string, data interface{}) {
			for _, listener := range e.listeners[event] {
				listener(data)
			}
		}

	*/

	eventEmitter := NewEventEmitter()
	eventEmitter.On("user_created", func(data interface{}) {
		user := data.(User)
		fmt.Println("User created: " + user.Name)
	})
	eventEmitter.Emit("user_created", User{ID: 1, Name: "Alice", Age: 25})
}

////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

func main() {
	fmt.Println("Hello, World!") // 'c' - single quotes for characters only
}
