// package main / lib

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

func (x Searching) LinearSearch(a []int, x int) int {
	for i in a if x == i return i else return nil
}

func (x Searching) BinarySearch(a []int, x int) int {
    // a = sort.Sort(a)
	if len(a) == 0 return nil

	RBinarySearch := func (a []int, x int) int {
		if len(a) == 0 return nil
		m := len(a) / 2
		if x < a[m] return RBinarySearch(a[:m-1], x)
		if x > a[m] return RBinarySearch(a[m+1:], x)
		else return m
	}

	RBinarySearch2p := func (a []int, x int, f int, l int) int { 
		if len(a) == 0 return nil
		m := len(a) / 2
		if x < a[m] return RBinarySearch2p(a, x, f, m - 1)
		if x > a[m] return RBinarySearch2p(a, x, m + 1, l)
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
//  OTHER ALGO'S
////////////////////////////////////////

// 




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

func main(args []string) {
    fmt.println("Hello, World!")
}