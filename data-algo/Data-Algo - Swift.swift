import Foundation

/* // TODO: (or MARK:) To-Use

some (View), convenience, ..
@unknown, @escaping, @inlinable, 
#available - API Availability
'Directives' - @testable
Generics
Swiftz, FunctionalSwift
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    private var i: Int

    init() {}
    
}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    private let i: Int

    init() {
        self.i = -1
    }

    func linearSearch(a: [Int], x: Int) -> Int? {
        for i in 0..<a.count where x == a[i] {
            return i
        }
        return nil
    }

    func binarySearch(a: [Int], x: Int) -> Int? {
        guard a.count > 0 else {
            return nil
        }

        a.sort() //  in-place | or .sorted() - not in-place

        let rBinarySearch = { (a: [Int], x: Int) -> Int? in
            guard a.count > 0 else {
                return nil
            }
            let m = floor(a.count / 2) // m never mutated, so let constant
            if x == a[m] {
                return a[m]
            } else if x < a[m] {
                return rBinarySearch(Array(a[0..<m]), x) // ..< - end exclusive
            } else {
                return rBinarySearch(Array(a[(m+1)...]), x)
            } 
        }
        
        let rBinarySearch2p = { (a: [Int], x: Int, f: Int, l: Int) -> Int? in
            guard a.count > 0 else {
                return nil
            }
            let m = floor(f + (l - f) / 2)
            if (x == a[m]) {
                return m
            } else if x < a[m] {
                return rBinarySearch2p(a, x, f, m - 1)
            } else {
                return rBinarySearch2p(a, x, m + 1, l)
            }
        }

        var f: Int = 0, l: Int = a.count - 1

        let res: Int? = rBinarySearch(a, 7)
        let res2p: Int? = rBinarySearch2p(a, 7, f, l)
        print("\(res ?? -1) | \(res2p ?? -1)")

        var m: Int

        while f < l {
            m = floor(f + (l - f) / 2)
            if (x == a[m]) {
                return m
            } else if x < m {
                l = m - 1
            } else {
                f = m + 1
            }
        }
        
        return nil
    }
}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////



// CODE SIGNAL

func rabinKarp(t: String, p: String) -> Int {
    
    let hash = { (arr: [Int]) -> Int in
        var hasher = Hasher()
        for s in arr {
            hasher.combine(s)
        }
        return hasher.finalize()
    }
    
    // convert to array of ints
    var pArr = p.compactMap { Int(String($0)) } // flatMap deprecated
    var tArr = t.compactMap { Int(String($0)) }

    if tArr.count < pArr.count {
        return -1
    }
    
    let pHash = hash(pArr)
    var endIndex = pArr.count - 1
    let firstChars = Array(tArr[0...endIndex])
    let firstHash = hash(firstChars)

    if pHash == firstHash {
        // verify this was not a hash collision
        if firstChars == pArr {
            return 0
        }
    }

    var prevHash = firstHash, window: [Int]?, windowHash: Int

    // Now slide the window across the text to be searched
    for i in 1...(tArr.count - pArr.count) {
        endIndex = i + (pArr.count - 1)
        window = Array(tArr[i...endIndex])
        windowHash = nextHash( // todo: 
            prevHash: prevHash,
            dropped: tArr[i - 1],
            added: tArr[endIndex],
            patternSize: pArr.count - 1
        )

        if window == [pHash], let newPArr = window {
            return i
        }

        prevHash = windowHash
    }

    return -1
}




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

func main(args: [String]? = nil) {
    print("Hello, World!")
}
main()


""" // * mega-string - like with python (but not a comment here)


strings - "" | chars - ''
func meth(_ x: String) {} - meth("x label can be _ omitted/ignored")

guard condition else { code }
Error in cases of using it within a closure (solution - return at end of scope)
- 'guard' body must not fall through, consider using a 'return' or 'throw' to exit the scope

// TODO: Wrong - find out what @escaping means
func meth( arg: @escaping (..) -> ..) ) .. | meth { closure code for arg: (can be 'escaped') }



// TODO: SwiftUI


in most meths:

- Double (not Int) args
- width arg precedes height



Method Definition - 

@available(iOS 13.0, macOS 10.15, tvOS 13.0, watchOS 6.0, *)
public func withAnimation<Result>(_ animation: Animation? = .default, _ body: () throws -> Result) rethrows -> Result

Call - withAnimation { code for last arg _ body: } (with _ animation: omitted in this case)


"""





/*

* // TODO: XCode

Collapse scope - Opt + Cmd + Left



* // TODO: SwiftUI

* Special Data-Types - CGFloat, CGSize, 

* Functions - withHooks (withAnimation, withTransaction, withCGContext, .. ), DispatchQueue.main.asyncAfter(deadline:execute: {..})

* Containers - ZStack (centered alignment), VStack (vertical), HStack (horizontal), Alignment, List, Group, 

* Components - Spacer, Text, Button, Color, URL, Image, AsyncImage, Transaction, Capsule, 

* Shapes - Color, Circle, Line, Capsule, 

* Props / Modifiers - .customORextensionModifiers, padding (always mid-prop by convention, then animation, .. ), 
opacity, color.opacity, spacing, font, fontWeight, resizable, scaledToFit, frame, foregroundColor, ignoresSafeArea, stroke, offset, imageScale, buttonStyle, buttonBorderShape, controlSize, blur, 

* Animations - animation: / .animation(_ animation:value:) / .customAnimations(..) / withAnimation(.animation(..)){..} - spring, transition (move, scale, rotate, slide, .. ), easeIn, easeOut, easeInOut, easeInOut, repeatForever, linear, scaleEffect, 

* Gestures - .gesture( .. Gesture() .. ) - DragGesture . onChanged {gesture:}, onEnded {_ action:}

* Event Handlers - .modifierEventHandler {}, onAppear(perform:), onTapGesture, onDragGesture, 

* Enumerations (raw) - Enum.enum / .enum / .enumMeth(Type - let var validation / _) / .enumCaseOnly / .enum.concatEnum().concatEnum.. : - 
.default, .all, color (primary/secondary/white/black/..), system(size:), success(Image), failure(Error), empty, title3, top/right/bottom/left, heavy/light, center, vertical/horizontal, scale, largeTitle, borderedProminent, capsule/.., large, 







* Specific Component-Prop-Enum Combos - 

Component(args: value / .enum / { code }, .. ) { content-closure - children } arg: { content-closure - again } .modifier().customModifier().modifier {..}.modifier(.enum).modifier(.enum(value)) .. .padding(value)



VStack/HStack(spacing:[, 'all' content:]) { children } . spacing, .. , padding, animation(.easeIn(duration:), Bool), animation(.easeInOut(duration:).repeatForever, Bool), 

ZStack(alignment:) {} . frame(height:alignment:), padding() [default padding value given] / padding(10), onAppear(perform: { code }) onTapGesture { code }, gesture(Gesture), blur(radius:), 

Alignment(horizontal:vertical:)

Spacer

Text("") . font(.title3/largeTitle/.. / .system(.title3/.. / size: 50)), fontWeight(.heavy/light/..), foregroundColor(.color), multilineTextAlignment(.center/..), offset(x:y: val/-val), padding(.horizontal, 10)

Button(action: { event-handler }) . buttonStyle(.borderedProminent/..), buttonBorderShape(.capsule/..), controlSize(.large/..)

Image(systemName: "ios.system.img/font.name.id") . resizable, scaledToFit, imageScale(.large), transition(.move(edge: .bottom/top/..)), font(.system(size: 24, weight: .bold))

AsyncImage(url:scale:transaction:content:placeholder:) . padding

Transaction(animation: .spring(..)/..)

Circle . stroke(.white.opacity(0.5), lineWidth: 50), frame(width:height:alignment)

Color("pre/custom-defined color") . ignoresSafeArea(.all/.., edges: all/..)

Capsule() . fill(Color.white.opacity(0.2) / .white.opacity(0.2) / Color("color")), 







* IDE Features

Scaffolding - Screens/Views, Views/Components, Utilities/Utils, 'custom' Assets, 
StoryBoarding - CocoaTouch UI, 
X-Assets - Default AccentColor (all default elem-colors), AppIcon (all sizings), Asset Uploads, Image & Color Sets, Data & Symbol Image Sets, 
Custom 'Assets' folder gets auto-deleted, with AI changing its path in build settings to the closest 'Assets/' path to the app (even outside the app is included)
    - recreating custom 'Assets/' solves this; but best to not use 'Assets' or any other in-built directory/file names for custom directories/files
    - Best Solution - go to X-Code in-built 'Assets' GUI-pane; create another 'Assets/' directory, then upload asset files to that directory
    - Can also create other asset directories like 'Characters, Colors, Images, etc' inside the X-'Assets' GUI-pane





* Notes

containers have flattened / absolute (all) children by default, taking up entire available space - each child's alignments, paddings, & frame-sizes re-positions it
Text("""multi-line string literal content textwrapping to a new line distort alignment on render - re-align beginning syntax with 'Text(' to re-render, then revert to preferred tab-scoping to prevent mis-alignment""")
Button's children content - horizontally aligned by default





* enum / switch cases with let-var validations

public enum AsyncImagePhase {
    case empty
    case success(Image)
    case failure(Error)

    public var image: Image? { get }
    public var error: Error? { get }
}

switch phase { // : AsyncImagePhase
case .success(let image): // * switch / enum case with let-var validation
    image.imageModifier()
case .failure(_): // * nullified var (find out if cases with var-lidations 'have' to be handled/nullified - can't be ignored)
    Image(systemName: "ant.circle.fill")
        .iconModifier()
case .empty:
    Image(systemName: "photo.circle.fill")
        .iconModifier()
@unknown default: // todo: find out what @unknown is for
    ProgressView()
}


@PropertyWrappers - directives for swift frameworks' features
- uses get-setters under the hood for storing app's state data

@AppStorage("unique-storage-property-key")
var someVar: Type = initial_value


*/