import kotlin.math.floor
import kotlin.math.ceil

/* // TODO: To-Use

data, sealed, lateinit, inner, open, abstract, final, 
companion, 
Generics
Arrow, Kategory
..

*/


////////////////////////////////////////
//  OOP
////////////////////////////////////////

class OOP(
    val prop1: Any,
    private var prop2: Any
) {

    // props

    private var prop3: Any? = null

    // constructors

    init {

    }

    constructor(prop1: Any) {

    }

    // methods
    
    fun meth() {}

    var meth1 = {

    }

    val meth2 = {
        a: Int, b: Double -> 
        // 
    }

    val meth3: ((Int, Double) -> Double) = {
        a, b ->
        a + b
    }

}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    private var i: Int = 0

}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    private var i: Int = 0

    fun linearSearch(a: Array<Int>, x: Int): Int? {
        for (i in 0..a.size-1) if (x == a[i]) return i // index
        return -1
    }

    fun binarySearch(arr: Array<Int>, num: Int): Int? {
        if (arr.size == 0) return null

        arr.sort()

        /*
         * With Recursive lambdas (like Java's recursive lambdas for Functional Interfaces), define function var (not val) before assigning the lambda value
         * defined function var must initialized before being invoked recursively too, so should be assigned a null value
         * this means that it's overall function data type definition should also be Optional
         * to invoke (or re-invoke - recursively) call the ?.invoke() method
         */

        /* // todo: Similar to Java's new Functional Interfaces
         * Sample:
         Function<ArrayList<Integer>, Integer, Integer>[] meth = new Function[1]; // * should be defined as a array when required for recursive-calls, because the 1st item is held in memory during the lambda's implementation as it's being assigned to the same 1st item
         meth[0] = (x, y) -> { ... meth[0].apply(..); ... }; meth[0].apply(..);
         * NB: ?.invoke(..) works similar to Java's .apply(..) .accept(..) , etc invoke-methods for its Functional Interfaces
        */

        var rBinarySearch: ((Array<Int>, Int) -> Int?)? = null // * use var in this case (val cannot be reassigned)
        rBinarySearch = { a, x ->
            if (a.size == 0) null // return keyword is optional in lambda expressions and single-expression functions
            val m = floor((a.size / 2) as Double) as Int // tdoo: type-castings
            // * Optional / "Safe" call reference is required in the recursive calls, because rBinarySearch may be null
            if (x == a[m]) a[m] // * return keyword can be omitted in lambda implementations
            else if (x < a[m]) rBinarySearch?.invoke(a.sliceArray(0..m-1), x) // * slice endIndex is inclusive
            else rBinarySearch?.invoke(a.sliceArray(m+1..a.size - 1), x) // * cannot auto-slice to end of array (specify .size - 1 inclusive last-item index)
        }

        // * Lambda with the run keyword - scope
        val rBinarySearch2p: (Array<Int>, Int, Int, Int) -> Int? = run {
            fun rbs2p(a: Array<Int>, x: Int, f: Int, l: Int): Int? {
                if (a.size == 0) return null
                val m = floor((f + (l - f) / 2) as Double) as Int
                if (x == a[m]) return m
                else if (x < a[m]) return rbs2p(a, x, f, m - 1)
                else return rbs2p(a, x, m + 1, l)
            }
            ::rbs2p
        }//() // todo: test auto-exec here vs auto-'run'
    

        var f: Int = 0
        var l: Int = arr.size - 1

        // * Optional / "Safe" call reference is not totally necessary in these outer calls, 
        // because rBinarySearch (even though Optional, so may be null) has been assigned a lambda function value
        rBinarySearch.invoke(arr, 7)
        rBinarySearch2p(arr, 7, f, l) // * this version of lambda function doesn't require .invoke()

        var m: Int

        while (f < l) {
            m = floor((f + (l - f) / 2) as Double) as Int
            if (num == arr[m]) return m
            else if (num < arr[m]) l = m - 1
            else f = m + 1
        }

        return null
    }

}



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//





////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

fun main(args: Array<String>) {
    println("Hello, World!")
}





////////////////////////////////////////
//  Syntax
////////////////////////////////////////

class A {

}

class B : A() {

}

class C : A() {

}



/*

* // TODO: Kotlin


data-class, sealed-class, inner-class, lateinit-var, open-fun, abstract (for vars), final, 
companion-object, 

ArrayList, Random, TimeUnit, Handler, Runnable, Uri, 

* - Any type
val arr: ArrayAdapter<*>


val x = arrayOf("")

when (x) { // * switch-case
    0 -> { .. }
    1 -> { .. }
    else -> { .. }
}

when { // * without arg (x)
    bool -> { .. } 
    bool -> { .. } 
    else -> { .. } // can return without else->case
}

casting - x as Type
- .toType() - eg. toString/Int/Double/Long/Float/..

lateinit - // todo: check 'lazy' init

var x: Type = Type() - 'new' not required

val SomeRunnable: Runnable = object : Runnable {
    override fun run() {..}
}

* data class DataClassModel(constructor-props as vars) - for defining model-classes (or view-models)

data class ViewModel(
    var a: Int, val b: String
) // * class-implementation not required

class ClassName { inner class InnerClassName {..} }

class A(x: T) : B(x) {..} // * inheritance with class-constructor-props & parent class / super-constructor-instantiation

class A(private var x: T) : B(x) {..} // 

class A {

    * // constructors
    init {}
    constructor(x: T) {}

}

arguments?.let { // * in-class {..}
    prop1 = it.getString("val")
    prop2 = it.getString("val")
}


*/





/*

* // TODO: Android Studio



* // TODO: A-Studio - Config



* // TODO: A-Studio - Issues



* // TODO: Android - Kotlin - Notes


- global vars / functions - in android lib
- Constraints - 1/2-Way (1-way best)
    - Absolute-Positioning - first, 'absolutely' move elem to its desired location on screen; then add constraints
    - Infer Constraints - all directions; best, but also affects other (neighboring) elems that aren't also affected by inference properly
    - best from parent to child (child constrained to parent) & old-sibling to new-sibling
    - but can specify inner-sibling constrained to both older & newer siblings
    - best to absolutely-position an element 1st (for absolute-x/y-constraints); then constrain its edges to all closest siblings/parent; 
    - to keep element in line with all surrounding-neighbors/parent, with equal spacing in each constrained-direction
    - should be based on design & consistency
    - Top & Bottom; Start - left; End - right;



* // TODO: A-Kotlin - Config



* // TODO: A-Kotlin - Issues



* // TODO: A-Kotlin - Main


* Libraries - android, androidx (newer) - android (os - phone features, widget - components, ), androidx (), R (id, layout, drawable, - Int IDs), 

* Libraries / Classes - android.os.Bundle, 

* Classes - MainActivity, Activity, Intent(packageContext:Activity::class.java), Toast, MediaPlayer, MediaController, ArrayAdapter, RecyclerView.(Adapter/ViewHolder), LayoutInflater, (Linear/Grid/Staggered)LayoutManager, 
FragmentManager, Lifecycle, FragmentStateAdapter(:MainActivity:Lifecycle), ViewPagerAdapter(), TabLayoutMediator(:TabLayout:ViewPager){tab, position -> ..}.attach(), 
ActionBarDrawerToggle(:Activity:DrawerLayout:Toolbar:Int:Int), 

* Dart Classes - Handler, Uri, 

* 3rd-Party Classes - 

* Special Data-Types - MainActivity, 

* Global Vars - in android lib - R, packageName, 

* Global / Default Class Props - this, this@MainActivity, it (general-purpose - scope-based), ; lifecycle, supportFragmentManager, supportActionBar, resources.(getIdentifier/..), 
(ListView/RecyclerView/'GridView/CardView'/..).Adapter.(adapterPosition/..), 

* Lifecycle Methods - 

* Functions - setContentView, startActivity(Intent), findViewById, findViewById<Type> (if var-to-asigned isn't typed), 

* Methods - intent.(putExtra(name:value:), ), textview.(setText, ), Toast.(makeText.show, ), seekBar.(setProgress, ), handler.(postDelayed(:Runnable,delayMillis:), ), 
mediaPlayer.(seekTo, ), MediaPlayer.(create(context:resource:), ), mediaController.(setAnchorView, setMediaPlayer, ), videoView.(setVideoPath, setVideoUri, setMediaController, ), 
Uri.(parse, ), LayoutInflater.(from(context:).inflate(..)), drawerLayout.(addDrawerListener(:ActionBarDrawerToggle)/closeDrawers/..), actionBarDrawerToggle.syncState, supportActionBar?.setDisplayHomeAsUpEnabled, 
fragmentManager.(beginTransaction/..), fragmentTransaction.(replace/commit/..), activity.(getSystemService/..), 

* Containers - 

* Layouts - XxLayout - Constraint, Relative, Grid, Linear, Absolute, Frame, Coordinator, Drawer, Tab, AppBar, Table, 

* Views - XxView - 'Grid', Card, Calendar, Navigation, Scroll, HorizontalScroll, ; List, Recycler, Text, Search, Image, Video, Web, ; 
ViewGroup, 

* Components - View, Fragment, ViewPager, ; TextView, EditText, Button, FloatingActionButton, CheckBox, RadioGroup, RadioButton, Switch, ToggleButton, ImageButton, Toolbar, DatePicker, TimePicker, 
NumberPicker, TabWidget, TableRow, ZoomControls, TextClock, DigitalClock, AnalogClock, Chronometer, ProgressBar, SeekBar, ; 
menu-(group-item)/(item-menu-group-item), 

* Shapes - gradient (shape-gradient), icon (vector-path), 

* Props - id, text, tag, ; elem.(context/..), intent.(extras/..), seekBar.(progress/isClickable/max/..), recyclerView.(layoutManager/..), viewGroup.(context/..), it.(isChecked/..), 
fragmentStateAdapter.(orientation/adapter/..), viewPager.(adapter/..), 

* Props (xml) - android: id, padding, layout_width, layout_height, layout_gravity, layout_margin, layout_marginTop, layout_marginBottom, layout_marginStart, layout_marginEnd, 
theme, background, backgroundTint, hint, textSize, textColor, textStyle, src, tag, fitSystemWindows, checkableBehavior, ; 
app: srcCompat, popupTheme, menu, headerLayout, tabTextColor, ; 
tools: context, showIn, ; 
CardView - android: elevation, ; app: cardCornerRadius, cardElevation, cardMaxElevation, cardPreventCornerOverlap, cardUseCompatPadding, ; 

* Constraints - android: layout_toTopOf, layout_toBottomOf, layout_toStartOf, layout_toEndOf ; tools: layout_editor_(absoluteX|absoluteY|..) ; 
app: layout_constraint(Top_toTopOf|Bottom_toBottomOf|Start_toStartOf|End_toEndOF|Top_toBottomOf|Bottom_toTopOf|Start_toEndOf|End_toStartOf|Vertical_bias|Horizontal_bias|..), ; 

* Styles - gradient (selector-gradient), 

* Animations - 

* Gestures - 

* Event Handlers - setEventHandler { arg1, arg2, -> lambda-code } [(method args can be omitted)] -  setOnClickListener, 

* Event Handlers (xml) - android: onClick, ; 

* Enumerations (xml) - @enum/.. - +id/ , layout/xmlfilename, menu/xmlfilename, drawable/assetname, android:drawable/ , dimen/(fab_margin/..) , style/ , color/(#FFFFFF/white/black/teal_700/..) , 
Theme.Material3.DayNight.(NoActionBar/DarkActionBar/..), 

* Enumerations - Intent.(ACTION_SEND/EXTRA_SUBJECT/EXTRA_TEXT/.., ), Toast.(LENGTH_LONG/LENGTH_SHORT/.., ), LinearLayoutManager.(VERTICAL/HORIZONTAL/INVALID_OFFSET/.., ), ViewPager2.(ORIENTATION_HORIZONTAL/.., ), 
Context.(LAYOUT_INFLATER_SERVICE/..), 

* Values - match_parent/wrap_content, parent/@+id/elem_id/ , 0+(dp - demarcation-sizes - 64dp | sp - text/elem-sizes - 32sp | ..)/0+, bottom|end/ , bold/ , true/false/ , start/end/ , all/none/single, 






* Specific Component-Prop-Enum Combos - 


TimeUnit.(MINUTES/SECONDS/MILLISECONDS/..).(toSeconds/Minutes/..), 





* Special Classes & Methods / Props - Class . meths(..) / props






* IDE Features


Scaffolding - 






* Notes

Recycler View - Flexible UI for re-using views (by only rendering those) currently visible to the user 
    - 'recycles' / 're-uses' views instead of re-creating new ones
    - best for list-views - recycling itemViews onScroll
    - 




* enum / switch cases for generics-validations




*/