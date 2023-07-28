/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

  Searching([this.i]);

  int linearSearch(Array<T> a, T x) {
    for (var i = 0; i < a.length; i++) { // length
      if (x == a[i]) return i;
    }
  }

  int binarySearch(Array<T> a, T x) {
    // a.sort()
    if (a.length == 0) return null;

    Function rBinarySearch = (Array<T> a, T x) {
      if (a.length == 0) return null;
      var m = a.length / 2;
      if (x < a[m]) return rBinarySearch(a, x); // slice a
      else if (x > a[m]) return rBinarySearch(a, x); // slice a
      else return m;
    }

    Function rBinarySearch2p = (Array<T> a, T x, int f, int l) {
      if (a.length == 0) return null;
      var m = (f + l) / 2;
      if (x < a[m]) return rBinarySearch2p(a, x, f, m - 1);
      else if (x > a[m]) return rBinarySearch2p(a, x, m + 1, l);
      else return m;
    }

    int f = 0, l = a.length - 1, m;
    rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l);

    while (f < l) {
      m = (f + l) / 2;
      if (x < a[m]) l = m - 1;
      else if (x > a[m]) f = m + 1;
      else return m;
    }
    return null;
  }

}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

  Sorting([this.i]);

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