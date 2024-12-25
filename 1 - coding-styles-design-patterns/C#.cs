using System;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;


/* // TODO: To-Use

Generics
In-built DataStructure classes
..

*/


namespace CSharp
{

    ////////////////////////////////////////
    //  CODING STYLES
    ////////////////////////////////////////

    namespace Obj
    {
        public class User
        {
            public int ID { get; set; }
            public string Name { get; set; }
            public int Age { get; set; }

            public string GetDetails()
            {
                return $"{Name}, Age: {Age}";
            }
        }

        public static class UserModule
        {
            private static List<User> users = new List<User>();

            public static void AddUser(User user)
            {
                users.Add(user);
            }

            public static User GetUser(int id)
            {
                return users.Find(u => u.ID == id);
            }
        }

        public class CloneableUser : User, ICloneable
        {
            public object Clone()
            {
                return (User) this.MemberwiseClone();
            }
        }

    }

    namespace Imperative
    {
        public static class Sample
        {
            public static void Test()
            {
                int[] numbers = { 1, 2, 3, 4, 5 };
                int sum = 0;

                foreach (int number in numbers)
                {
                    sum += number;
                }

                Console.WriteLine($"Sum of numbers: {sum}");  // Sum of numbers: 15
            }
        }

    }

    namespace Functional
    {
        public static class Sample
        {
            public static void Test()
            {
                var users = new List<Obj.User>
                {
                    new Obj.User { ID = 1, Name = "Alice", Age = 25 },
                    new Obj.User { ID = 2, Name = "Bob", Age = 30 }
                };

                var user = users.Where(u => u.ID == 1).FirstOrDefault();
                if (user != null)
                {
                    Console.WriteLine(user.Name);
                }

                var userNames = users.Select(u => u.Name).ToList();
                userNames.ForEach(Console.WriteLine);
            }
        }

    }

    namespace Declarative
    {
        public static class Sample
        {
            public static void Test()
            {
                var numbers = new List<int> { 1, 2, 3, 4, 5 };
                var doubled = numbers.Select(x => x * 2).ToList();

                doubled.ForEach(Console.WriteLine);  // 2, 4, 6, 8, 10
            }
        }

    }

    namespace OOP
    {
        public static class Sample
        {
            public static void Test()
            {
                var user = new Obj.User { ID = 1, Name = "Alice", Age = 25 };
                Console.WriteLine(user.GetDetails());
            }
        }

    }

    namespace AsyncAwait
    {
        public static class Sample
        {

            public static async Task<Obj.User> FetchUserDataAsync(int userId)
            {
                await Task.Delay(1000); // Simulate a network call
                return new Obj.User { ID = userId, Name = "Alice", Age = 25 };
            }

            public static async Task Run()
            {
                var user = await FetchUserDataAsync(1);
                Console.WriteLine(user.Name);
            }

            public static void Test()
            {
                Run();
            }
        }

    }

    namespace Callback
    {
        public static class Sample
        {

            public delegate void ReadFileCallback(Exception error, string data);

            public static void ReadFile(string filePath, ReadFileCallback callback)
            {
                try
                {
                    var data = File.ReadAllText(filePath);
                    callback(null, data);
                }
                catch (Exception ex)
                {
                    callback(ex, null);
                }
            }

            public static void Test()
            {
                ReadFile("example.txt", (error, data) =>
                {
                    if (error != null)
                    {
                        Console.WriteLine("Error: " + error.Message);
                    }
                    else
                    {
                        Console.WriteLine(data);
                    }
                });
            }
        }

    }

    namespace ObjectComposition
    {
        public static class Sample
        {

            public interface IEatBehavior
            {
                void Eat();
            }

            public interface IWalkBehavior
            {
                void Walk();
            }

            public class ToEat : IEatBehavior
            {
                public void Eat()
                {
                    Console.WriteLine("Eating...");
                }
            }

            public class ToWalk : IWalkBehavior
            {
                public void Walk()
                {
                    Console.WriteLine("Walking...");
                }
            }

            public class Person
            {
                private IEatBehavior eatBehavior;
                private IWalkBehavior walkBehavior;

                public Person(IEatBehavior eatBehavior, IWalkBehavior walkBehavior)
                {
                    this.eatBehavior = eatBehavior;
                    this.walkBehavior = walkBehavior;
                }

                public void Eat()
                {
                    eatBehavior.Eat();
                }

                public void Walk()
                {
                    walkBehavior.Walk();
                }
            }

            public static void Test()
            {
                var person = new Person(new ToEat(), new ToWalk());
                person.Eat();
                person.Walk();
            }
        }

    }


    ////////////////////////////////////////
    //  DESIGN PATTERNS
    ////////////////////////////////////////

    // * Creational

    namespace Prototype
    {
        public static class Sample
        {
            public static void Test()
            {
                var user = new Obj.CloneableUser { ID = 1, Name = "Alice", Age = 25 };
                var userClone = (Obj.CloneableUser) user.Clone();
                Console.WriteLine(userClone.GetDetails());
            }
        }

    }


    // * Structural


    // * Behavioral


    // * Others

    namespace Module
    {
        public static class Sample
        {
            public static void Test()
            {
                Obj.UserModule.AddUser(new Obj.User { ID = 1, Name = "Alice", Age = 25 });
                var user = Obj.UserModule.GetUser(1);
                if (user != null)
                {
                    Console.WriteLine(user.Name);
                }
            }
        }
    }

    namespace Middleware
    {
        public static class Sample
        {

            public delegate void Middleware(string context, Action next);

            public class MiddlewareChain
            {
                private List<Middleware> middlewares = new List<Middleware>();
                private int index = 0;

                public void Use(Middleware middleware)
                {
                    middlewares.Add(middleware);
                }

                public void Next(string context)
                {
                    if (index < middlewares.Count)
                    {
                        var current = middlewares[index];
                        index++;
                        current(context, () => Next(context));
                    }
                }
            }

            public static void Test()
            {
                var middlewareChain = new MiddlewareChain();
                middlewareChain.Use((context, next) =>
                {
                    Console.WriteLine("Logging: " + context);
                    next();
                });
                middlewareChain.Use((context, next) =>
                {
                    Console.WriteLine("Handling: " + context);
                });

                middlewareChain.Next("GET /home");
            }
        }
    }


    ////////////////////////////////////////
    //  OTHER PATTERNS
    ////////////////////////////////////////

    namespace EventDriven
    {
        public static class Sample
        {

            public class EventEmitter
            {
                public event Action<Obj.User> UserCreated;

                public void CreateUser(Obj.User user)
                {
                    UserCreated?.Invoke(user);
                }
            }

            public static void Test()
            {
                var eventEmitter = new EventEmitter();
                eventEmitter.UserCreated += user => Console.WriteLine("User created: " + user.Name);

                eventEmitter.CreateUser(new Obj.User { ID = 1, Name = "Alice", Age = 25 });
            }
        }

    }



    public static class Main // TODO: Change filename to 'Main.cs'
    {

        ////////////////////////////////////////
        //  TEST CASES
        ////////////////////////////////////////

        public static void Main(string[] args)
        {
            // CSharp.Obj.User x = non_null;
            Console.WriteLine("Hello, World!");
        }

    }
}

/* NOTES:
 * all non-class members in a static class should be static (unlike Java)
 *
 */