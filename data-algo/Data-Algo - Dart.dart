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
