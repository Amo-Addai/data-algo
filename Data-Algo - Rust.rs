/*

Lambda, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    private let mut i:i32 = 0;

    fn linearSearch(a: &[T], mut x: T) -> i32? {
        for i in 0..a.len()-1 if x == a[i] return i; // index
    }

    fn binarySearch(a: Vec<T>, mut x: T) -> i32? {
        // a.sort()
        if a.len() == 0 return null; // length

        let rBinarySearch: (Vec<T>, T) -> i32? = { (a: Vec<T>, x: T) -> { // lambda
                if a.len() == 0 return null;
                let m = a.len() / 2;
                if x < a[m] return rBinarySearch(a, x);
                else if x > a[m] return rBinarySearch(a, x);
                else return m;
            }
        }

        let rBinarySearch2p: (Vec<T>, T) -> i32? = { (a: Vec<T>, x: T, f:i32, l:i32) -> {
                if a.len() == 0 return null;
                let m = (f + l) / 2;
                if x < a[m] return rBinarySearch2p(a, x, f, m - 1);
                else if x > a[m] return rBinarySearch2p(a, x, m + 1, l);
                else return m;
            }
        }

        let mut f:i32 = 0;
        let mut l:i32 = a.len() -1;
        let mut m:i32;

        rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l);

        while f < l {
            m = (f + l) / 2;
            if x < a[m] l = m - 1;
            else if x > a[m] f = m + 1;
            else return m;
        }
        return null;
    }

}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

    private let i:i32 = 0;
    
}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//





////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

fn main(args: Vec<String>) {
    pri32ln!("Hello, World!")
}