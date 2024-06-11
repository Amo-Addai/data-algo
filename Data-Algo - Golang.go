package main // / lib

import (
	"fmt"
	"sort"
)

/*

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
	return -1 // nil if return type was a pointer *int, so address of &i should be returned instead
}

func (x Searching) BinarySearch(a []int, n int) int {
    // sort.Sort(a) // accepts any collection that implements the sort.Interface, which requires three methods: Len(), Less(i, j int), and Swap(i, j int).
	sort.Ints(a) // convenience function for sorting slices of built-in types (.Ints - []int ; .Float64s/Strings/IntsAreSorted/Float64sAreSorted/StringsAreSorted)
	if len(a) == 0 {
		return -1
	}

	var RBinarySearch func([]int, int) int // declare function data type var 1st
	RBinarySearch = func (a []int, n int) int { // var has to exist before function value assignment, since it's a recursive function
		if len(a) == 0 {
			return -1
		}
		m := len(a) / 2
		if n < a[m] {
			return RBinarySearch(a[:m-1], n)
		}
		if n > a[m] {
			return RBinarySearch(a[m+1:], n)
		} else {
			return m
		}
	}

	var RBinarySearch2p func([]int, int, int, int) int
	RBinarySearch2p = func (a []int, n int, f int, l int) int { 
		if len(a) == 0 {
			return -1
		}
		m := len(a) / 2
		if n < a[m] {
			return RBinarySearch2p(a, n, f, m - 1)
		}
		if n > a[m] {
			return RBinarySearch2p(a, n, m + 1, l)
		} else {
			return m
		}
	}

	var (f int = 0; l int = len(a) - 1; m int)
	RBinarySearch(a, 7); RBinarySearch2p(a, 7, f, l)

	for f < l {
		m = (f + l) / 2
		if n < a[m] {
			l = m - 1
		} else if n > a[m] {
			f = m + 1
		} else {
			return m
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
    fmt.println("Hello, World!")
}