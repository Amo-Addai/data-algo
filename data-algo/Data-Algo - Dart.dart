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

  method() { // default void-return (can be omitted)
    
  }

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
    rBinarySearch2p = (List<dynamic> a, int x, int f, int l, int m) => {
      // todo: * in '=>' lambdas 
      // all preceding statements in a scope end with ',' (except for last statement)

      if (a.length == 0) null, // 'return' not required
      // int m, // vars can't be declared (declared  in lambda definition)
      m = (f + (l - f) / 2).truncate(),
      if (x == a[m]) m, // only if-only (/ else) statements don't require {} scope-syntax
      if (x < a[m]) { // if-else statements require {} scope-syntax between them
        rBinarySearch2p!(a, x, f, m - 1, null)
      } else rBinarySearch2p!(a, x, m + 1, l, null)
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

; mandatory

lambda - (..) { .. ; .. ; } 

lambda - (..) => { .. , .. , [no 'return] } | ..?

string interpolation - '${var}'

- constant class / const constructor - (by making all of the fields of the class, including inherited fields, final)
  - then add the const keyword when instantiating constructor

- args' default values

Future<type> - .js Promises
eg. Future<void> meth() async {}



*/





/*

* // TODO: Anroid Studio


Beginning of File - stful, stless, stanim - New Stateful widget, Stateless widget, Stateful AnimationController



* // TODO: A-Studio - Config

- mobile-native config
  - ios/ - Runner/Info.plist - add key-value pairs to base of main </dict>
  - android/ - app/build.gradle - add gradile-config to android { .. }



* // TODO: A-Studio - Issues



* // TODO: A-Studio - Notes

Widget (page/view) + State 



* // TODO: Flutter - Config



* // TODO: Flutter - Issues

- The import of 'package:flutter/cupertino.dart' is unnecessary because all of the used elements are also provided by the import of 'package:flutter/material.dart'
  - both libs have same component versions

- Prefer const with constant constructors.
  - when all its args constantly take in non-null values - make constructor's call constant

- The constructor being called isn't a const constructor | Try removing 'const' from the constructor invocation.
  - Add 'const' modifier (or everywhere in file)

- A value of type 'Null' can't be assigned to a parameter of type 'String' in a const constructor.
  - in case a const constructor's arg takes in an optional value (ensure optional chaining wherever necessary)
  - constructor cannot be constant anymore because its arg takes in an optional value (may/not be a null value)

- // todo: what to do when multiple items in a <Widget>[] array are constant constructors (const each item ?)



* - Warnings:

- Avoid unnecessary containers. - can replace Containers with SizedBox, for whitespace







* // TODO: Flutter - Main


* Libraries - widget, cupertino, material, splashscreen, tflite, image_picker, camera, 

* Main Containers - MaterialApp, State, StatefulWidget, StatelessWidget, 

* Classes - MediaQuery, BuildContext, File, Size, CameraController, 

* Special Data-Types - 

* Functions - 

* Widget / Containers - Widget, Container, SafeArea, Position, Padding, Scaffold, Column, 'Row', Center, SizedBox (empty space), EdgeInsets, EdgeInsetsGeometry (for margin/padding), 

* Components - AppBar, Text, Button, FloatingActionButton, Icon, Image, CameraImage, CameraPreview, 

* Shapes - AspectRatio, 

* Args - title, home, padding, child, children, height, width, body, style, fontWeight, fontSize, color, backgroundColor, appBar, onPressed, tooltip,  ...   , debugShowCheckedModeBanner, floatingActionButton, mainAxisAlignment, 

* Props - ImageSource.(camera/gallery), file.(path), Image.(file), Size.(height/width), cameraController.value.initialized, 

* Methods - EdgeInsets.(only/symmetric), 

* Styles - Theme, Color, TextStyle, BoxDecoration, 

* Animations - 

* Gestures - 

* Event Handlers - GestureDetector, 

* Enumerations (raw) - Colors.(white/blueAccent), FontWeight.(bold/'light'/w500), Alignment.(center), CrossAxisAlignment.(start/baseline/), ResolutionPreset.(medium), 






* Specific Component-Prop-Enum Combos - 


MaterialApp(title:home:debugShowCheckedModeBanner:)

Widget

Container(height:width:padding:margin:alignment:decoration:child:) - NO arg: children:<Widget>[]

SafeArea(child:)

Position(top:left:width:) - absolute-positioning

Padding(padding:child:)

Scaffold(appBar:body:backgroundColor:floatingActionButton:)

Column(mainAxisAlignment:crossAxisAlignment:children:<Widget>[])

Center(child:)

SizedBox(height:) - empty space (SwiftUI - Spacer())

AppBar(title:backgroundColor:)

Text("",style:TextStyle)

TextStyle(fontWeight:fontSize:color:)

Button()

FloatingActionButton(onPressed:tooltip:child)

Icon(IconData)

Color('hex')

Colors . white, redAccent, blueAccent, yellowAccent, 

Image . asset, 

EdgeInsets . only(top:), symmetric(horizontal:vertical:)

EdgeInsetsGeometry 

GestureDetector(onTap:)

BoxDecoration(color:borderRadius:)

BorderRadius . circular(radius:double)

AspectRatio(aspectRatio:child:)





* Special Classes & Methods / Props - Class(args)[// default scope-end comment] . meths(..) / props


* WidgetsFlutterBinding . ensureInitialized() - 

setState( () {} )

Widget . build(BuildContext), 

setState(cb), 

Theme . of(BuildContext), 

Image . asset('path/'), file(File), 

MediaQuery . of(context).size.(height/width), 

ImageSource . camera, gallery, 

availableCameras() - camera.dart, 

ResolutionPreset . medium





* IDE Features


Scaffolding - lib, (default - android, ios, web, .. ), assets, 

Naming Conventions - Class (filename.dart)






* Notes





* enum / switch cases for generics-validations




*/