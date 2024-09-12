using System;
using System.Collections.Generics;
using System.Linq;


/* // TODO: To-Use

Keywords - sealed, partial, virtual, record, required, 
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

                var RBinarySearch = (Int[] a, Int x) => {
                    if (a.Length == 0) return null;
                    var m = Math.Floor(a.Length / 2);
                    if (x == a[m]) return a[m];
                    else if (x < a[m]) return RBinarySearch(a[..m], x);
                    else return RBinarySearch(a[m+1..], x);
                };

                var RBinarySearch2p = (Int[] a, Int x, Int f, Int l) => {
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

String.Meths == string.Meths (& other data types)

Elem.EventProp += Event_Handler; - add event-listener (-= removes it)
void Event_Handler(object sender, EventArgs e) {..}

int? x - primitive-type vars can also be null

abstract class - Entities with props & abstract methods only - encapsulate implementations ..

'record' in place of 'class' - immutable classes, for data-integrity
- for 'data-record' OOP-objects eg. BankAccount, Dto's, ..

public record A(string X, int Y); // * or record A { .. }
A x - new { X = 'v', Y = 1 }; A y - x with { Y = 2 }; // * 'with' keyword to make updated-copy of record

private required Type x { get => value, internal set; init; } - init not normaly used with set

* required & init; for both classes / records
* // todo: check record's init / constructor methods

is not null === != null - is (not) used with dtypes / null

T? Meth<T>(..) where T : ClassName {..}

static class A
{ static Meth(this Type a, Type b) { .. } } - // todo: 'this' ?

private readonly Type x; - ..





Libs

System.Text.Json.Serialization
- [Directives/Annotations] - JsonPropertyName, JsonIgnore, 



*/




/*

* // TODO: Visual Studio



* // TODO: V-Studio - Config



* // TODO: V-Studio - Issues



* // TODO: .NET - Notes



* // TODO: .NET - Config



* // TODO: .NET - Issues



* // TODO: .NET - Main



* Libraries - 

* Classes - ControllerBase, ServiceResponse, 

* 'Language' Classes - Guid, DateTime, TimeSpan, HttpClient, HttpServer, 

* 3rd-Party Classes - 

* Special Data-Types - TEntity, IRepository, IActionResult, IFormFile, 

* Directives / Annotations - [Directive] - ApiController, Route('route'), Http(Get/Post/..), Consumes/Produces('mediaType eg. application/json'), Authorize, AllowAnonymous, ProducesResponseType(StatusCodes, Type=typeof(SampleDto)), 
FromBody, 

* Functions - 

* Methods - StatusCode()

* Enumerations - DateTime.(Now/..), StatusCodes.(Status201Created/Status404NotFound/Status409Conflict/..), 






* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes





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

    ItemsSource - 
    SelectedItem - 

    Aspect - AspectFill/AspectFit/Fill





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