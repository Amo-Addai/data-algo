/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

  Sorting();

}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

  var _i;

  Searching([this._i]);

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