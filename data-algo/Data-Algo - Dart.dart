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

  // block-scope method (!;)
  method() { // default void-return (can be omitted)
    
  }

  method0() => null;

  method1() => (

  );

  method2() => {

  };

  amethod() async { // use await if required
    
  }

  amethod0() async => (

  );

}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

  final int i; // named params can't start with _

  const Searching({required this.i}); // const constructors can't have non-final properties

  int? linearSearch(List<dynamic> a, int x) {
    for (var i = 0; i < a.length; i++) // length
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


string interpolation - '${var}' / '$var'

List<type> list = []; list . add(type), 
eg. List<Widget> list = []; list.add(Container(or any other Flutter-components/widgets .. ))
in main Widget build() { .. children: list, .. } -  for <Widget>[..] props

try { code }
on Exception { handler } - on-catch clause

* catch (?) { handler ? }


----------------------------------------------------------------


void meth() {} | Type meth() => {} | Type meth() => v;

block-lambda - (..) { .. ; .. ; } 

arrow-lambda - () => val - all arrow-lambdas return a set of all the statement-args, to be executed by the lambda function

(..) => ( .. , .. , [ only values to return as args | no keywords 'var / return / super / .. ' | no constructs eg. 'if/for/..' | no void statements eg. 'print(..)' ] )

(..) => { .. , .. , [ only values to return as args | no keywords 'var / return' | no new var assignments | not all constructs allowed eg. allowed - 'if/for/..' not allowed - 'try/..' | void statements allowed ] }

| .. ?

named arrow-lambda - meth() => val; | (); | {};

@override
void initState() {} -> initState() => {}; - void override-methods can be arrow-lambdas

@override
Widget build(BuildContext context) { return const Container(..); } -> Widget build(context) => { Container(..) }; 
- Returned-Type override-methods cannot be arrow-lambdas, because its return type is actually Set<dynamic - statements' return types>
error - A value of type 'Set<Container>' can't be returned from the method 'build' because it has a return type of 'Widget'.


* // todo: check if the Set<types> of arrow-lambdas can have multiple same-types within the lambda's statements


----------------------------------------------------------------


NB: String - non-nullable (not optional / cannot be null)

String x; - non-nullable / not optional; no assignment; can't be assigned null values
OOP error - Non-nullable instance field 'x' must be initialized.

String x = null; - error (non-nullable)

String? x; - nullable / optional; no assignment; null by default
NO OOP error

String? x = null; - optional; null assignment (unnecessary)

String? x = ""; - optional; "" value assignment (still necessary)

String x = ""; - no error / warning


----------------------------------------------------------------


Future<String> x; - non-nullable; must be initialized when in static-OOP as a prop; but when in runtime scope as a var, doesn't require an assigned a value on definition
OOP error - Non-nullable instance field 'x' must be initialized

Future<String> x = ""; - error ("" string can't be assigned to Future<String>)

Future<String> x = Future<String>(""); - Future types require a callback (like Promises)
error - The argument type 'String' can't be assigned to the parameter type 'FutureOr<String> Function()'

Future<String> x = new Future(() => ""); - Unnecessary 'new' keyword.

Future<String> x = Future(() => "");

* Future<String>? x; - when to use Optional-syntax; can be assigned a Future((cb) => String) value later
* or when the var is of a 3rd-party library data-type (with unsureties of type's initialization value-options)


NB: Optional<String> x; - (not .dart - may be in other langs - equivalents)


----------------------------------------------------------------


- constant class / const constructor - (by making all of the fields of the class, including inherited fields, final)
  - then add the const keyword when instantiating constructor

- args' default values

Future<type> - .js Promises
eg. Future<void> meth() async {}

* - OOP - Don't access members with `this` unless avoiding 'shadowing'.



*/





/*

* // TODO: Android Studio


Beginning of File - stful, stless, stanim - New Stateful widget, Stateless widget, Stateful AnimationController

control (^) + space - show tip



* // TODO: A-Studio - Config

- mobile-native config
  - ios/ - Runner/Info.plist - add key-value pairs to base of main </dict>
  - android/ - app/build.gradle - add gradle-config to android { .. }



* // TODO: A-Studio - Issues



* // TODO: Flutter - Notes


- Different devices render different UI elements differently


in most meths:

- assume all function, props & modifiers, animations, gestures & event-handlers, enums, etc ..
    - are all ALMOST applicable to all Types / Classes (common, special, containers/components/shapes/custom, etc)
    - Know what each name/identifier applies to; then specifically with which other identifiers it can form a combo
    - ensure that IDE highlights any errors in-between


- Widget (page/view) + State 
- height arg precedes width
* // todo: when to use new Constructor()  (with 'new' keyword)
* // todo: when to replace a Container with an empty 'SizedBox' to add whitespace to a layout



* // TODO: Flutter - Config



* // TODO: Flutter - Issues

- The import of 'package:flutter/cupertino.dart' is unnecessary because all of the used elements are also provided by the import of 'package:flutter/material.dart'
  - both libs have same component versions

- warning - Prefer const with constant constructors.
  - when all its args constantly take in non-null values - make constructor's call constant
- Or, Use 'const' with the constructor to improve performance.
  - Try adding the 'const' keyword to the constructor invocation.

*  - Add 'const' modifier (or everywhere in file - after entire file has been coded)

- error - The constructor being called isn't a const constructor | Try removing 'const' from the constructor invocation.
  - remove const from parent constructor, then add const to any constant child constructor(s)

- A value of type 'Null' can't be assigned to a parameter of type 'String' in a const constructor.
  - in case a const constructor's arg takes in an optional value (ensure optional chaining wherever necessary)
  - constructor cannot be constant anymore because its arg takes in an optional value (may/not be a null value)

- best to set const Constructors from bottom-up in the widget-tree (optional children 'params' determine const constructors)

- // todo: what to do when multiple items in a <Widget>[] array are constant constructors (const each item ?)



* - Warnings:

- Avoid unnecessary containers. - can replace Containers with SizedBox, for whitespace







* // TODO: Flutter - Main


* Libraries - dart, dart:io, cupertino, material, widget, splashscreen, tflite, image_picker, camera, 

* Main Containers - MaterialApp, State, StatefulWidget, StatelessWidget, 

* Classes - Navigator, MediaQuery, BuildContext, File, Size, CameraController, 

* 'Language' Classes - 

* 3rd-Party Classes - ImageSource, ImagePicker, PickedFile, 

* Special Data-Types - 

* Lifecycle Methods - 

* Functions - 

* Methods - 

* Widget / Containers - Placeholder, Container (div equivalent), Widget, LayoutBuilder, SafeArea, Positioned, Padding, Scaffold, Column, Row, Stack, Align, Center, SizedBox (empty space), EdgeInsets, EdgeInsetsGeometry (for margin/padding), SingleChildScrollView, 

* Components - Custom(Combos()), AppBar, Text, TextField, Button, IconButton, ElevatedButton, FloatingActionButton, FlatButton, Icon, Image, CameraImage, CameraPreview, CircularProgressIndicator, 

* Shapes - AspectRatio, BoxConstraints, ClipOval, 

* Args - title, home, padding, child, children, height, width, body, style, fontWeight, fontSize, color, backgroundColor, appBar, onPressed, tooltip,  ...   , debugShowCheckedModeBanner, floatingActionButton, mainAxisAlignment, 

* Props - ImageSource.(camera/gallery), file.(path), Image.(file), Size.(height/width), cameraController.value.(initialized/aspectRatio), pickedFile.path, 

* Methods - EdgeInsets.(only/symmetric), imagePicker.(getImage), Tflite.(loadModel/runModelOnImage/runModelOnFrame/detectObjectOnFrame/runPoseNetOnFrame/close), 

* Styles - Material, Theme, ThemeData, Size, Color, TextStyle, InputDecoration, InkWell, BoxDecoration, DecorationImage, 

* Animations - 

* Gestures - 

* Event Handlers - GestureDetector, 

* Enumerations - Colors.(white/black/black54/blueAccent/pinkAccent/orange/grey/), FontWeight.(bold/'light'/w500), TextAlign.(center), Alignment.(center), ResolutionPreset.(medium), BoxFit.(cover/fill), Icons.(add/camera_alt/photo_camera_front/browse_gallery), 
MainAxisAlignment/CrossAxisAlignment.(center/start/end/baseline/stretch/values), 





* Specific Component-Prop-Enum Combos - 


Placeholder(key:color:strokeWidth:fallbackWidth:fallbackHeight:child:), 

MaterialApp(title:home:debugShowCheckedModeBanner:), 

ThemeData(primarySwatch:), 

LayoutBuilder(builder:)

Widget

Container(height:width:padding:margin:alignment:color:decoration:child:) - NO arg: children:<Widget>[], 

SafeArea(child:), 

Positioned(top:left:width:height:child:) - absolute-positioning, 

Padding(padding:child:), 

Scaffold(appBar:body:backgroundColor:floatingActionButton:), 

Column(mainAxisAlignment:crossAxisAlignment:children:<Widget>[]), 

Row(mainAxisAlignment:crossAxisAlignment:children:<Widget>[]), 

Stack(children:<Widget>[]), 

Align(alignment:child:), 

Center(child:), 

SizedBox(height:) . fromSize(size:child:), 
* - empty space (SwiftUI - Spacer())

AppBar(title:backgroundColor:), 

const Text("",style:TextStyle,textAlign:), - mostly constant (if "" isn't a var - could be null - whether nullable/not
because (const) TextStyle always constant (unless other Text(args:) are likely to be non-constant stringVar / Constructors)

TextStyle(fontFamily:fontWeight:fontSize:color:backgroundColor:), 

TextField(controller:decoration:obscureText:), 

Button(), 

IconButton(icon:onPressed:), 

ElevatedButton(onPressed:child:), 

FloatingActionButton(onPressed:tooltip:child:), 

FlatButton(onPressed:onLongPress:child:), 

CircularProgressIndicator(strokeWidth:), 

InputDecoration(labelText:), 

InkWell(key:child:onTap:), 

Icon(IconData,color:size:), 

Icons . add, camera_alt, photo_camera_front, browse_gallery, 

Size(_height:_width:), 

Color('hex'), 

Colors . white, black, black54, redAccent, blueAccent, yellowAccent, orange, grey, 

Image . file(Image,height:width:fit:), asset (takes asset from project-directory - cannot be constant - asset may not exist), 

AssetImage(""), 

EdgeInsets . only(top:), symmetric(horizontal:vertical:), 

EdgeInsetsGeometry 

GestureDetector(onTap:), 

BoxDecoration(color:borderRadius:image:), 

DecorationImage(image:fit:), 

BorderRadius . circular(radius:double), 

AspectRatio(aspectRatio:child:), 

BoxFit . cover, fill, 

SingleChildScrollView(child:), 

ClipOval(child:), 

Material(color:), 






* Special Classes & Methods / Props - Class(args)[// default scope-end comment] . meths(..) / props


* WidgetsFlutterBinding . ensureInitialized() - 

setState( () {} / () => _ )

Widget . build(BuildContext), 

MainAxisAlignment . center, start, end, baseline, stretch

CrossAxisAlignment . center, start, end, baseline, stretch

Navigator . push, pop, 

Theme . of(BuildContext).textTheme.headline4, 

Image . asset('path/'), file(File), 

MediaQuery . of(BuildContext).size.(height/width), - to find size of current screen-context during Widget build(BuildContext) - used for dynamically adding UI

ImageSource . camera, gallery, 

ResolutionPreset . medium, 

TextAlign . center, 


* 3rd - Parties


Tflite . loadModel(model:labels:numThreads:isAsset:useGpuDelegate:), runModelOnImage(bytesList:path:imageHeight:imageWidth:imageMean:imageStd:rotation:numResults:threshold:asynch:), 
runModelOnFrame(bytesList:imageHeight:imageWidth:imageMean:imageStd:rotation:numResults:threshold:asynch:), detectObjectOnFrame(bytesList:imageHeight:imageWidth:numResultsPerClass:), 
runPoseNetOnFrame(bytesList:imageHeight:imageWidth:numResults:)

CameraPreview(CameraController), 

CameraController(Camera, ResolutionPreset), 





splashscreen.dart - SplashScreen

SplashScreen(

  seconds: 2,
  navigateAfterSeconds: Home(),
  title: const Text('Cat and Dog Classifier',
      style: TextStyle(
          fontWeight: FontWeight.bold,
          fontSize: 25,
          color: Colors.yellowAccent
      )
  ),
  image: Image.asset('assets/cat_dog_icon.png'),
  photoSize: 130,
  backgroundColor: Colors.white,
  loaderColor: Colors.black,
  loadingText: const Text(
    "Auto-Code",
    style: TextStyle(
      color: Colors.black,
      fontSize: 16
    )
  ),

  

);

camera.dart - availableCameras()





* IDE Features


Scaffolding - lib, (default - android, ios, web, .. ), assets, 

Naming Conventions - Class (filename.dart)






* Notes





* enum / switch cases for generics-validations




*/