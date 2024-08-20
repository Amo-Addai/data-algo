/* // TODO: To-Use

required, 
const Constructors + [const] args & instantiation
Generics
functional.dart, dartz
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

  var _i;

  Sorting([this._i]);

}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

  final int i; // named params can't start with _

  const Searching({required this.i}); // const constructors can't have non-final properties

  int? linearSearch(List<dynamic> a, int x) {
    for (var i = 0; i < a.length; i++)// length
      if (x == a[i]) 
        return i;
    return null;
  }

  int? binarySearch(List<dynamic> a, int x) {
    if (a.length == 0) return null;

    a.sort();

    Function? rBinarySearch = null;
    rBinarySearch = (List<dynamic> a, int x) {
      if (a.length == 0) return null;
      int m = (a.length / 2).truncate();  // or .floor() / floor(..)
      if (x == a[m]) return a[m]; // todo: Function ? / !
      else if (x < a[m]) return rBinarySearch!(a.sublist(0, m), x);
      else return rBinarySearch!(a.sublist(m + 1, a.length), x);
    };

    Function? rBinarySearch2p = null;
    rBinarySearch2p = (List<dynamic> a, int x, int f, int l) {
      if (a.length == 0) return null;
      int m = (f + (l - f) / 2).truncate();
      if (x == a[m]) return m;
      else if (x < a[m]) return rBinarySearch2p!(a, x, f, m - 1);
      else return rBinarySearch2p!(a, x, m + 1, l);
    };

    int f = 0;
    int l = a.length - 1;
    int m;
    rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l);

    while (f < l) {
      m = (f + (l - f) / 2).truncate();
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

//





////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void main() {
  print("Hello, World!");
}


/*

* // TODO: Dart

- constant class / const constructor - (by making all of the fields of the class, including inherited fields, final)
  - then add the const keyword when instantiating constructor






*/





/*

* // TODO: A-Studio


Beginning of File - stful, stless, stanim - New Stateful widget, Stateless widget, Stateful AnimationController



* // TODO: A-Studio - Issues



* // TODO: A-Studio - Notes

Widget (page/view) + State 



* // TODO: Flutter - Issues

- The constructor being called isn't a const constructor | Try removing 'const' from the constructor invocation.
  - Add 'const' modifier (or everywhere in file)


* // TODO: Flutter - Main


* Libraries - widget, cupertino, material, 

* Classes - MaterialApp, State, StatefulWidget, StatelessWidget, BuildContext, Theme, 

* Special Data-Types - 

* Functions - 

* Widget / Containers - Widget, Container, Scaffold, Column, 'Row', Center, SizedBox, EdgeInsets, 

* Components - AppBar, Text, Button, FloatingActionButton, Icon, Image, 

* Shapes - 

* Props / Args - title, home, padding, child, children, height, width, body, style, fontWeight, fontSize, color, backgroundColor, appBar, onPressed, tooltip,  ...   , debugShowCheckedModeBanner, floatingActionButton, mainAxisAlignment, 

* Props / Methods - symmetric, 

* Styles - Color, TextStyle, 

* Animations - 

* Gestures - 

* Event Handlers - 

* Enumerations (raw) - FontWeight.(bold/'light'), Colors.(blueAccent), CrossAxisAlignment.(start/baseline/), 






* Specific Component-Prop-Enum Combos - 


MaterialApp(title:home:debugShowCheckedModeBanner:)

Widget

Container(height:width:padding:child:children:<Widget>[])

Scaffold(appBar:body:backgroundColor:floatingActionButton:)

Column(mainAxisAlignment:crossAxisAlignment:children:<Widget>[])

Center(child:)

SizedBox(height:)

AppBar(title:)

Text("",style:TextStyle)

Button()

FloatingActionButton(onPressed:tooltip:child)

Icon(IconData)

TextStyle(fontWeight:fontSize:color:)

Color('hex')

Image . asset, 

EdgeInsets . symmetric(horizontal:)





* Special Classes & Methods / Props - Class(args)[// default scope-end comment] . meths(..) / props

Widget . build(BuildContext)

setState(cb), 

Theme . of(BuildContext)

Image . asset('path/')






* IDE Features


Scaffolding - lib, (default - android, ios, web, .. ), assets, 

Naming Conventions - Class (filename.dart)






* Notes





* enum / switch cases with let-var validations




*/