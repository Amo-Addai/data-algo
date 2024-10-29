using System;
using System.Collections.Generics;
using System.Linq;


/* // TODO: To-Use

Keywords - sealed, partial, virtual, event, record, required, readonly, nameof(..), 
In-built DataStructure classes
'event' Handlers
delegate methods - with Func<..> & lambda functions
Generics
LanguageExt, Optional
..

*/



namespace DataAlgo
{
    public class CSharp
    {

        ////////////////////////////////////////
        //  SORTING ALGO'S
        ////////////////////////////////////////

        class Sorting 
        {
            
            public void Sorting() {}

        }


        ////////////////////////////////////////
        //  SEARCHING ALGO'S
        ////////////////////////////////////////

        class Searching 
        {
            private Int i;

            public void Searching() {
                this.i = -1;
            }
            
            public Int LinearSearch(Int[] a, Int x) 
            {
                var FLinearSearch = () => a.Where(i => i == x).Select(i); // Functional Linq Usage

                return from i in a where i == x select i; // * best to return i as index, instead of item
            }

            public Int BinarySearch(Int[] a, Int x) 
            {
                if (a.Length == 0) return null;

                Array.Sort(a);
                // a.BinarySearch(x); // * C# in-built Array Method

                Int RBinarySearch(Int[] a, Int x) => { // named-function lambda
                    if (a.Length == 0) return null;
                    var m = Math.Floor(a.Length / 2);
                    if (x == a[m]) return a[m];
                    else if (x < a[m]) return RBinarySearch(a[..m], x);
                    else return RBinarySearch(a[m+1..], x);
                };

                var RBinarySearch2p = (Int[] a, Int x, Int f, Int l) => { // unnamed-function lambda
                    if (a.Length == 0) return null;
                    var m = Math.Floor(f + (l - f) / 2);
                    if (x == a[m]) return m;
                    else if (x < a[m]) return RBinarySearch2p(a, x, f, m - 1);
                    else return RBinarySearch2p(a, x, f, m + 1);
                };

                Int f = 0, l = a.Length - 1;
                RBinarySearch(a, 7); RBinarySearch2p(a, 7, f, l);

                Int m;

                while (f < l) {
                    m = Math.Floor(f + (l - f) / 2);
                    if (x == a[m]) return m;
                    else if (x < a[m]) l = m - 1;
                    else f = m + 1;
                }

                return null;
            }

        }



        ////////////////////////////////////////
        //  OTHER ALGO'S
        ////////////////////////////////////////


        class DataStructures
        {

            public DataStructures() {}


            // Arrays & Strings

            // (Array) Lists & Tuples

            // Sets & Sequences

            // WeakMaps & WeakSets

            // HashMaps & HashTables

            // Matrices

            // Linked Lists

            // Stacks

            // Queues

            // Heaps (max & min)

            // Binary Heaps

            // Priority Queues

            // Trees

            // Binary (Search) Trees

            // Tries
                
            // Graphs

            // Bits


        }



        ////////////////////////////////////////
        //  Cracking Coding Interview Qs
        ////////////////////////////////////////


        // Arrays & Strings

        // ...






        ////////////////////////////////////////
        //  TEST CASES
        ////////////////////////////////////////

        public static void Main(string[] args) 
        {
            Console.WriteLine("Hello, World!");
        }
        
    }
}


/*

* // TODO: C#

Keywords - readonly, nameof(..), required, init, delegate, 

New Types - Guid, 


$"{String} : {Interpolation}"

* // todo: check - is [not] null/Type (confirm non-null value), 

var x; - wrong - Implicitly-typed variables must be initialized
var x = null; - wrong - Cannot assign <null> to an implicitly-typed variable
var x = non_null_value; - correct - var-var given non-null value
Type x; - correct - typed-var not requiring any (null / non-null) value yet

nameof(var) - returns "var" identifier as a string 

String.Meths == string.Meths (& other data types)

public string Prop { get; set; } = null!; - prop with both get-set & (default) value assignment

class Object { ... Prop; User(... prop) { this.Prop = prop } }
new Object(propval, .. ) - object instantiation

class Object { ... Prop; }
new Object() { Prop = val, .. }; - object instantiation with obj {} literal

Lambda - x => {} / (x[, y]) => {}
void method([x..]) => {..} - named-function lambda
var method = ([x..]) => {..}; - unnamed-function lambda

[public/private] async Task<ReturnType> MethName() { ..await .. } - async method

arr.Where(x => x.Prop == val) - shorter-syntax than - from x in arr where x.Prop == val select x
arr.OrderBy(x => x.Prop).Select(x => x.Prop1) - from x in arr orderby x.Prop select x.Prop1
(linq).(Distinct.ToList.Count)

Elem.EventProp += Event_Handler; - add event-listener (-= removes it)
void Event_Handler(object sender, EventArgs e) {..}

int? x - primitive-type vars can also be null

abstract class - Entities with props & abstract methods only - encapsulate implementations ..

'record' in place of 'class' - immutable classes, for data-integrity
- for 'data-record' OOP-objects eg. BankAccount, Dto's, ..

public record A([NO accessor eg. public with 'init-constructor()'] string X, [.Net-Attribute] int Y);
* or record A { .. }

A x - new { X = 'v', Y = 1 }; A y - x with { Y = 2 }; // * 'with' keyword to make updated-copy of record

private required Type x { get => value, internal set; init; } - init not normally used with set

* required & init; for both classes / records
* // todo: check record's init / constructor methods
“init-only properties” (also known as readonly properties).
These properties allow you to initialize them directly in the constructor and then set them only during object initialization.

is not null === != null - is (not) used with dtypes / null

T? Meth<T>(..) where T : ClassName {..}

static class A
{ static Meth(this Type a, Type b) { .. } } - // todo: 'this' ?

private readonly Type x; - ..

* ternary with statements (instead of values to assign) - wrong
true ? Console.WriteLine("aa") : Console.WriteLine("aa");
- Only assignment, call, increment, decrement, await, and new object expressions can be used as a statement, with ternary's

* destructuring
var (x, y) = FunctionReturningTuple(..) - // todo: check for list/object return values

private Type Prop = value
private Type Prop => returnedValue // * named lambda as a (prop) variable - 'Prop' when called (without function '()' args)

interfaces with async methods don't require 'async' keyword; just Task<Type> meth(..); definitions
sub-class implementations of methods require 'async' keyword with Task<Type> return-type definitions

* Delegate-Types (.java Functional Interfaces)

Func<ArgType, [ArgType, .. , <16 args,] ReturnType> x = (a, b, [.. ,]) => returnTypeValue; // * .java Function<..>
Func<ReturnType> x = ([no argument]) => returnTypeValue;

Action<ArgType, [ArgType, .. , <16 args - no ReturnType]> x (a, b, [.. ,]) => execWithNoReturnValue; // * .java Consumer<..>

Predicate<ArgType, [ArgType, .. , <16 args - Default bool ReturnType]> x (a, b, [.. ,]) => bool; // * .java 

* custom delegates
delegate void CustomDelegate(int x, string y); CustomDelegate handler = (a, b) => exec; // * .java custom Functional Interfaces





--


Libs

System.Text.Json.Serialization
- [Attributes/Directives] - JsonPropertyName, JsonIgnore, 



*/




/* // TODO: .NET -  [Directives], Lifecycles

* // TODO: Visual Studio



* // TODO: V-Studio - Config



* // TODO: V-Studio - Issues



* // TODO: .NET - Notes



* // TODO: .NET - Config



* // TODO: .NET - Issues



* // TODO: .NET - Main



* Libraries - System[.(Collections.Generic)/(Text.Json.Serialization)/(Threading.Tasks)/..], 

* Classes - ControllerBase, ServiceResponse, 

* Interfaces - IComparable, IFormattable, ICloneable, IEnumerable, IDisposable, IAsyncDisposable, IServiceProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, IAsyncMethodBuilder, IAsyncQueryProvider, IAsyncEnumerable, IAsyncEnumerator, IProgress, IFormatProvider, ICustomFormatter, IAsyncStateMachine, 

* 'Language' Classes - Exception, HttpClient, HttpServer, 

* 3rd-Party Classes - 

* 'Language' Data-Types - Guid, DateTime, TimeSpan, 

* Special Data-Types - TEntity, IRepository, IActionResult, IFormFile, 

* Attributes / Directives - [Attribute] - ApiController, Route("[controller]/route/.."), Http(Get/Post/..)[("route/{param}")], FromQuery, FromBody, 
Consumes/Produces("mediaType eg. application/json"), Authorize(AuthenticationSchemes/Policy/..), AllowAnonymous, ProducesResponseType(StatusCodes, Type=typeof(SampleDto)), 
Key, DatabaseGenerated(DatabaseGeneratedOption.Identity) - Auto-increment, 
ServiceFilter(typeof(SampleFilter)), 

* 'Language' Directives - JsonPropertyName("key"), 

* Functions - 

* Methods - StatusCode()

* Enumerations - DateTime.(Now/..), StatusCodes.(Status201Created/Status404NotFound/Status409Conflict/..), 






* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes

- Interfaces - 'I'-prefixed (IComparable, IEnumerable, ..), 




* enum / switch cases for generics-validations






*/






/*

* // TODO: Visual Studio



* // TODO: V-Studio - Config



* // TODO: V-Studio - Issues



* // TODO: MAUI - Notes



* // TODO: MAUI - Config



* // TODO: MAUI - Issues



* // TODO: MAUI - Main



* Libraries - 

* Classes - 

* 'Language' Classes - Guid, TimeSpan, 

* 3rd-Party Classes - 

* Special Data-Types - 

* Lifecycle Methods - 

* Functions - 

* Methods - 

* Containers - 

* Components - 

* Shapes - 

* Props - 

* Styles - 

* Animations - 

* Gestures - 

* Event Handlers - 

* Enumerations - 






* Specific Component-Prop-Enum Combos - 





* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes





* enum / switch cases for generics-validations





* // TODO: Windows-Phone - WinRT


    Application


    Layouts:

    Page, 
    StackPanel, Grid, Canvas, 
    FlipView, GridView, Hub, 

    ..


    Resources:
    
    ResourceDictionary, 

    ..


    Containers:

    RowDefinitions, ColumnDefinition, 

    ..


    Components:

    Pointer, Border, Button, CheckBox, ComboBox, DatePicker,
    Image, ListView, MenuFlyout, Pivot, PivotItem, RadioButton,
    TextBlock, TextBox, TimePicker, toast/tile-visual-binding-text/image/..,
    
    ..


    Shapes:

    Rectangle, 

    ..


    Styles:

    ImageBrush, LinearGradientBrush, WebViewBrush, 

    ..


    Props:

    Content - inner text/html
    Children - inner html
    Margin - l t r b
    Height / Width - v
    Vertical/HorizontalAlignment - 
    Background - 
    TextAlignment - 
    GradientStops - 

    ..




* // TODO: Xamarin


    Application


    Layouts:

    ContentPage, TabbedPage, 
    ContentView, StackLayout, AbsoluteLayout, FlexLayout, 
    
    Page, 
    StackPanel, Grid, Canvas, 
    FlipView, GridView, Hub, 


    Resources:
    
    ResourceDictionary, 

    ..


    Containers:

    Frame, maps:Map, 
    
    RowDefinitions, ColumnDefinition, 


    Components:

    Label, FormattedString, Entry, Button, ListView, DataTemplate, 
    ViewCell, TextCell, 
    
    Pointer, Border, Button, CheckBox, ComboBox, DatePicker,
    Image, ListView, MenuFlyout, Pivot, PivotItem, RadioButton,
    TextBlock, TextBox, TimePicker, toast/tile-visual-binding-text/image/..,
    ...


    Shapes:

    ..
    
    Rectangle, 


    Styles:

    Style, Color, Setter, 

    ImageBrush, LinearGradientBrush, WebViewBrush, 


    Props:

    Content - 
    Resources - 
    FormattedText - 
    ItemTemplate - 
    View - 
    Vertical/HorizontalOptions - Center/CenterAndExpand/End/EndAndExpand/Fill/FillAndExpand/Start/StartAndExpand

    Content - inner text/html
    Children - inner html
    Margin - l t r b
    Height / Width - * (all available), Auto (children's size-related), 
    HeightRequest - 
    Vertical/HorizontalAlignment - 
    Background - 
    Text - 
    FontAttributes - Bold/
    TextAlignment - 
    GradientStops - 

    Grid.Row - v
    Grid.Column - v

    ItemsSource (NOT ItemSource - ItemsS) - 
    SelectedItem - 

    Aspect - AspectFill/AspectFit/Fill



    .cs

    (linq).(Distinct.ToList.Count), 
    DisplayAlert(title,msg,action)





* // TODO: .NET MAUI


    Application


    Layouts:

    ..
    
    Page, 
    StackPanel, Grid, Canvas, 
    FlipView, GridView, Hub, 


    Resources:
    
    ..
    
    ResourceDictionary, 


    Containers:

    ..
    
    RowDefinitions, ColumnDefinition, 


    Components:

    ..
    
    Pointer, Border, Button, CheckBox, ComboBox, DatePicker,
    Image, ListView, MenuFlyout, Pivot, PivotItem, RadioButton,
    TextBlock, TextBox, TimePicker, toast/tile-visual-binding-text/image/..,
    ...


    Shapes:

    ..
    
    Rectangle, 


    Styles:

    ..
    
    ImageBrush, LinearGradientBrush, WebViewBrush, 


    Props:

    ..
    
    Content - inner text/html
    Children - inner html
    Margin - l t r b
    Height / Width - v
    Vertical/HorizontalAlignment - 
    Background - 
    TextAlignment - 
    GradientStops - 



*/