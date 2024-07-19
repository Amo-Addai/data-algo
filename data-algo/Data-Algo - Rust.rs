/* // TODO: To-Use

Generics
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

pub mod Sorting {

    priv let i:i32 = 0;
    
}


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

pub mod Searching {

    priv let mut i:i32 = 0;

    fn linearSearch(a: &[i32], mut x: i32) -> Option<i32> {
        for i in 0..a.len()-1 if x == a[i] return i; // index
    }

    fn binarySearch(a: Vec<i32>, mut x: i32) -> Option<i32> {
        // * a.sort()
        if a.len() == 0 return None; // length

        let rBinarySearch: fn(Vec<i32>, i32) -> Option<i32> = | a: Vec<i32>, x: i32 | -> i32 {
            if a.len() == 0 return None;
            let m = a.len() / 2;
            if x < a[m] return rBinarySearch(a, x);
            else if x > a[m] return rBinarySearch(a, x);
            else return m;
        }

        let rBinarySearch2p: fn(Vec<i32>, i32) -> Option<i32> = | a: Vec<i32>, x: i32, f:i32, l:i32 | -> i32 {
            if a.len() == 0 return None;
            let m = (f + l) / 2;
            if x < a[m] return rBinarySearch2p(a, x, f, m - 1);
            else if x > a[m] return rBinarySearch2p(a, x, m + 1, l);
            else return m;
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
        return None;
    }

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