/*

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

  var _i;

  Searching([this._i]);

  int? linearSearch(List<dynamic> a, int x) {
    for (var i = 0; i < a.length; i++) { // length
      if (x == a[i]) return i;
    }
    return null;
  }

  int? binarySearch(List<dynamic> a, int x) {
    // a.sort()
    if (a.length == 0) return null;

    Function rBinarySearch = (List<dynamic> a, int x) {
      if (a.length == 0) return null;
      int m = (a.length / 2).truncate();
      if (x < a[m]) return rBinarySearch(a, x); // slice a
      else if (x > a[m]) return rBinarySearch(a, x); // slice a
      else return m;
    };

    Function rBinarySearch2p = (List<dynamic> a, int x, int f, int l) {
      if (a.length == 0) return null;
      int m = ((f + l) / 2).truncate();
      if (x < a[m]) return rBinarySearch2p(a, x, f, m - 1);
      else if (x > a[m]) return rBinarySearch2p(a, x, m + 1, l);
      else return m;
    };

    int f = 0;
    int l = a.length - 1;
    int m;
    rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l);

    while (f < l) {
      m = ((f + l) / 2).truncate();
      if (x < a[m]) l = m - 1;
      else if (x > a[m]) f = m + 1;
      else return m;
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