package main // or lib

import (
	"fmt"
	"sort"
)

/* // TODO: To-Use

Generics
..

*/

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

type Sorting struct {
	i int
}

func (x Sorting) Func() {}

////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

type Searching struct {
	i int
}

func (x Searching) LinearSearch(a []int, n int) int {
	for _, i := range a { // index _, item i
		if n == i {
			return i
		}
	}
	return -1 // * nil if return type was a pointer *int, so i's address &i should be returned instead
}

func (x Searching) BinarySearch(a []int, n int) int {
	if len(a) == 0 {
		return -1
	}

	// sort.Sort(a) // accepts any collection that implements the sort.Interface, which requires three methods: Len(), Less(i, j int), and Swap(i, j int).
	sort.Ints(a) // convenience function for sorting slices of built-in types (.Ints - []int ; .Float64s/Strings/IntsAreSorted/Float64sAreSorted/StringsAreSorted)

	var RBinarySearch func([]int, int) int     // declare function data type var 1st
	RBinarySearch = func(a []int, n int) int { // var has to exist before function value assignment, since it's a recursive function
		len := len(a)
		if len == 0 {
			return -1
		}
		m := floor(len / 2) // todo: Math.floor(..)
		if n == a[m] {
			return a[m]
		} else if n < a[m] {
			return RBinarySearch(a[:m], n)
		} else {
			return RBinarySearch(a[m+1:], n)
		}
	}

	var RBinarySearch2p func([]int, int, int, int) int
	RBinarySearch2p = func(a []int, n int, f int, l int) int {
		if len(a) == 0 {
			return -1
		}
		m := floor(f + (l - f) / 2)
		if n == a[m] {
			return m
		} else if n < a[m] {
			return RBinarySearch2p(a, n, f, m-1)
		} else {
			return RBinarySearch2p(a, n, m+1, l)
		}
	}

	var (
		f int = 0
		l int = len(a) - 1
		m int
	)
	RBinarySearch(a, 7)
	RBinarySearch2p(a, 7, f, l)

	for f < l {
		m = floor(f + (l - f) / 2)
		if n == a[m] {
			return m
		} else if n < a[m] {
			l = m - 1
		} else {
			f = m + 1
		}
	}

	return -1
}

////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//

////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

func main() {
	fmt.Println("Hello, World!")
}
