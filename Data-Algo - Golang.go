// package main

import (
	"fmt"
	"sort"
)

/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

func LinearSearch(a []int, x int ) int {
	for i in a if x == i return i else return nil
}

func BinarySearch(a []int, x int) int {
	if len(a) == 0 return nil

	RBinarySearch := { (a []int, x int) int // TODO: confirm syntax
		if len(a) == 0 return nil
		m := len(a) / 2
		if x < a[m] return RBinarySearch(a[:m-1], x)
		if x > a[m] return RBinarySearch(a[m+1:], x)
		else return m
	}

	RBinarySearch2p := { (a []int, x int, f int, l int) int
		if len(a) == 0 return nil
		m := len(a) / 2
		if x < a[m] return RBinarySearch(a, x, f, m - 1)
		if x > a[m] return RBinarySearch(a, x, m + 1, l)
		else return m
	}

	var (f int = 0, l int = a.size - 1, m int)
	RBinarySearch(a, 7); RBinarySearch2p(a, 7, f, l)

	for f < l {
		m = (f + l) / 2
		if x < a[m] l = m - 1
		else if x > a[m] f = m + 1
		else return m
	}
    return nil
}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

//



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// 
