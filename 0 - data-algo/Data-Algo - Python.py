import sys
import math
from typing import List, Callable
from collections import deque, defaultdict
import heapq

import numpy as np
import pandas as pd


''' # TODO: To-Use

Generics
functools, toolz, pyrsistent
..

'''


'''

# ! NB: Big O

# * in terms of speed: x-axis (Elements) & y-axis (operations)

O(1) > O(log n) > O(n) > O(n log n) 
> O(n ^ 2) > O(n ^ 3) > ... 
> O(2 ^ n) > O(n!) > ??? 

Excellent - O(1) - constant time
Good - O(log n) - logarithmic time (binary operations)
Fair - O(n) - linear time (loops / iterations - 1D array/list)
Bad - O(n log n) - linearithmic time (fast sorting algo's)
Horrible - O(n ^ 2) (quadratic - 2D arrays) > O(n ^ 3) (cubic - 3D arrays) 
# TODO: > O(2 ^ n) (exponential - ? ) > O(n!) (factorial - ? ) >
Dead Code - ???


# TODO:

Test all files' Algo's - Correctness, Speed / Execution Time, Uniqueness
Re-assess all algos' Big Omega (Best-Case / Lower-Bound) & Big Theta (Average-Case / Tight-Bound) - Time & Space Complexities
Compare all cases with stated Big O (Worst-Case / Upper-Bound) - Time & Space Complexities alike


# TODO: To-Use


Hidden (Forgetful) Keys:

BCR & Visualizations - for all problems with all possible solutions
Base-Cases & Error-Cases - for everything, & wrong inputs

Brute-force methods - for all non / more - optimal solutions

Mathematical Approaches - for all most-optimal solutions for numbers (or numbered data-structures)
"Math Formulae" methods - for all math-problems

HashMap & "Same / Extra" Array methods - for all more-optimal solutions
"Extra" / "Other" Data-Structure methods - for all more-optimal solutions

Sort - 1st methods - for all more-optimal solutions

Mid-Solution Input Argument - for all more-optimal solutions
(eg. given max number of input array, also as an argument,
preventing the need to sort the array 1st, in some cases)

"Hacky Algo" methods - for all most-optimal solutions (eg. 'delete' hack)

While / For / Foreach / .ForEach / .Map loops - for all requiring solutions
(eg. using all types of indices, iteration methods, 2+-pointer methods, etc)

Language / Syntax - Specific Features - methods - for all solutions
(eg. .py special methods operating in O(n ~ 1) t, by optimization
eg. special loop methods - n in a / range(of indices - inclusive/exclusive), enumerated iterations, etd)

Trade-off method options - for all solutions
(eg. 'delete' hack vs extra array / data-structure with 'checked' items;
'in' array (or .includes() method - also O(1~n) t) vs O(1~n) re-looping through same input array to current iteration)

Funny-tricks (cool) options - for all solutions
(eg. rearranging problems / input data in different ways, to achieve multiple solution scenarios)

Funny-stuff (stupid) options - for all solutions
finding extra and unnecessary hacks for solutions
(eg. converting an integer to a string, for concatenation
better option - using Math tactics
- concatenating by (* 10 + n) & trimming by (% 10) )


Cyclomatic Complexity also (per-function-based) - for all solutions
(

software metric used to measure a program's complexity, by counting number of independent paths through the source code.
helps assess code's maintainability, testability, quality assurance, risk management - potential risk areas

M = E - N + 2P - complex code with flow-graphs; 
E - Number of edges (connections between nodes in the flow-graph), 
N - Number of nodes (decision points and code blocks in the flow-graph), 
P - Number of paths / connected components (typically 1 for a single function) 

M = Number of decision points + 1 - simple (1) function without a flow-graph

Decision points include:

    *   Raw statements / Function Calls - 0 / NO d-point - 1 cc

	•	if (1 d-point - 2 cc), else if (another 1 d-point), if else if (combined 2 d-points - 3 cc), switch-case (1 d-point for each case)
	•	for, while, do-while
	•	Logical operators (&&, ||)
	•	Exception handling (try-catch-finally)

)


Data-Structures:

Done - arrays/strings (sorting/searching), lists/tuples, matrices, hash/weak-maps/tables/sets, linked-lists, stacks/queues, trees/b(s)ts, graphs,  …  
# todo - sets/seqs/vectors, dicts/maps/objs, tree-maps/sets, tries, max/min heaps, bi-heaps/p-queues, bits, blobs,  …  


Algorithm Mechanics & Facts:


Mechanic - DataStructure(s), Language-Syntax, Variations, Constraints, Question Constraints, Helpers, Laws & Facts, Combos, Cyclo's


- same data-structure (eg. array - when only values required; not indices too) - language-syntax (eg. x 'in' arr over dict - O(1) t), 

- hashmap/hashtable - when indices (as map-values) also required, 

- variables - storing specific data (instead of extra data-structures), eg. min/max values, any trailing/leading data, 1/2/3 - pointers, 

Iterations: 1 / 2 / .. / n - pointers

- 1-pointer - arrays/strings/linkedlists/matrices?/.. , hashmap/table?, .. 

- 2-pointer - arrays/strings/linkedlists/matrices?/.. , binary/? search, inward/outward iteration, same-time/1-after-other/slow-faster/1-or-n-step(s)-ahead iteration, 
pointer-calculations (eg. middle-index), integer-math laws, int < target, (non-)repeating ints, sorting 'almost always' required (ints/strings/..), 

NB: 1-pointer-step-ahead (better to work with previous item, than with next item - array out-of-bounds exception on last iteration)

Searches: 

- Linear Search - arrays/strings/linkedlists/.. , 

- Binary Search - arrays/trees/.. , 2/? pointers, 

Others: 

- Sliding-window - arrays/strings/matrices?/.. , ranges/sub-arrays/.. , ..

Optimizing Cyclomatic Complexities:

- Use DRY Code (no repetition; only modular code for re-use)
- Refactor (Break) Long Functions into smaller reusable functions
- Use Polymorphism & Strategy Patterns - replace complex switch or if-else chains with polymorphic design
- Remove Redundant Conditions - optimize nested loops & unnecessary branches
- Use Guard Clauses - Reduce deep nesting / unnecessary code execution, by returning early (on input-data validation)
- Utilize Ternary Operators & Lookup Tables - Simplify conditions when possible


- 


'''


########################################
##  SORTING ALGO'S (ascending)
########################################

class Sorting:

    def __init__(self):
        pass

    def check(self, a): # O(1) t ;
        return len(a) in [0, 1]
        
    def swap(self, a, b): # O(1) t ; by ref
        t, a, b = a, b, t
        # (a, b) = (b, a) # faster, but () by value
        return a, b

    def compare(self, a, b): # O(1) t ; generic
        return a < b

    # regular

    def insertion(self, a): # O(n^2) t | O(1) s
        if self.check(a): return a
        for i in range(1, len(a)):
            j = i
            while j > 0 and (a[j] < a[j-1]):
                self.swap(a[j-1], a[j])
                j = j - 1
            # or
            for j in range(i, 0, -1):
                if a[j] < a[j-1]: self.swap(a[j-1], a[j])
                else: break # 1-lvl?
        return a

    def selection(self, a): # O(n^2) t | O(1) s
        if self.check(a): return a
        for i, x in enumerate(a):
            l = i
            for j in range(i + 1, len(a)):
                if a[j] < x: l = j
            if x is not a[l]: self.swap(a[i], a[l]) # x is a[i]
        return a

    def shell(self, a): # O(n^2) t ; 
        if self.check(a): return a
        m = len(a) / 2
        while m > 0:
            for i in range(0, m): self.insertion(a[i : m]) # ensure call by ref
            m = m / 2        
        return a

    # bad

    def bubble(self, a): # O(n^2) t | O(1) s
        if self.check(a): return a
        sorting = True
        while sorting: # fastest loop
            for i in range(0, len(a) - 1):
                if a[i] > a[i+1]: 
                    self.swap(a[i], a[i+1])
                    sorting = False
        # or
        for i in range(1, len(a)):
            sorted = True
            for j in range(0, len(a) - 1):
                if a[j] > a[j+1]: 
                    self.swap(a[j], a[j+1])
                    sorted = False
            if sorted: break
        # or
        for i in range(0, len(a)): # or len(a) - 1/i - both optimizations
            sorted = True
            for j in range(1, len(a)):
                if a[j] < a[j-1]:
                    self.swap(a[j-1], a[j])
                    sorted = False
            if sorted: break
        return a

    def slow(self, a): # O(n^2) t ; 
        if self.check(a): return a
        
        def slow(a, f, l):
            if not f < l: return
            m = math.floor(f + (l - f) / 2)
            slow(a, f, m); slow(a, m + 1, l)
            if a[l] < a[m]: self.swap(a[l], a[m])
            slow(a, f, l - 1)

        f, l = 0, sys.maxsize
        slow(a, f, l)

        return a

    # special

    def counting(self, a): # O(3n) best case t | O(2n) s
        if self.check(a): return a
        
        c, s = {}, []
        for i in a: 
            c[i] = c[i] + 1 if i in c else 0
        for i in range(1, len(c)): c[i] = c[i] + c[i-1]
        for i in range(len(a) - 1, -1, -1):
            it = a[i]
            c[it] = c[it] - 1 # reduce count
            s[c[it]] = it # sort it

        return s
        

    def radix(self, a): # O(kn) t ; 
        if self.check(a): return a
        # TODO
        return a
        

    def topological(self, a): # O(n^2) t ; 
        if self.check(a): return a
        # TODO
        return a

    # hybrid

    def intro(self, a): # O(n^2) t ; 
        if self.check(a): return a
        
        def intro(a, max):
            if len(a) < 20: self.insertion(a)
            elif max == 0: self.heap(a)
            else:
                m = len(a) / 2
                intro(a[:m], max - 1)
                intro(a[m+1 : len(a)], max - 1)

        max = 0 # log(len(a)) * 2
        intro(a, max)

        return a

    # fast

    def heap(self, a): # O(nlogn) t ; 
        if self.check(a): return a
        # TODO
        return a

    def merge(self, a): # O(nlogn) t | O(n) s
        if self.check(a): return a

        def merge(a, b): # TODO
            if len(a) is 1 and len(b) is 1:
                a, b = a[0], b[0]
                return [a, b] if a < b else [b, a]
            else: return self.merge(a) + self.merge(b)
        
        m = len(a) / 2
        l = self.merge(a[:m]); r = self.merge(a[m:])
        return merge(l, r)

    def quick(self, a): # O(nlogn) t | O(logn) s
        if self.check(a): return a
        p = a[len(a) / 2]
        l = e = g = []
        for i in a:
            if i < p: l.append(i)
            elif i > p: g.append(i)
            else: e.append(i)
        # l = [(i if i < p else _) for i in a] # confirm _
        return self.quick(l) + e + self.quick(g)



########################################
##  SEARCHING ALGO'S
########################################

class Searching:

    def __init__(self):
        pass
    
    def linear_search(self, a, x):
        for i in a:
            if x is i: return x # todo: all non-type() 'is' comparisons -> ==
        return None

    def binary_search(self, a, x):

        if len(a) is 0: return None

        a.sort() # or - sorted(a) # O(n log n) t 
        # TODO: NB: .sort() isn't a method in case 'a' was a string literal
        # & sorted(str) returns a sorted array/list of str's characters
        # so for strings, call "".join(sorted(str)) on a new string literal "" (list doesn't have .join() method)

        # * NB: sorting array before proceeding also affects indices (in-case actual array's item's index is required)

        def r_binary_search(a, x):
            l = len(a)
            if l is 0: return None
            m = math.floor(l / 2) # avoid float
            if x < a[m]: return r_binary_search(a[:m], x) # slice excludes endIndex
            elif x > a[m]: return r_binary_search(a[m+1:], x)
            # else - x == a[m] - best to check for this before other if-cases (imperfect way chosen, for memory)
            else: return a[m] # or return a bool instead of same x arg - index m decreasing recursively, as a's length decreases

        def r_binary_search(a, x, f, l):
            if len(a) is 0 or f > l: return None
            m = math.floor(f + (l - f) / 2) # better than (index-wise for edge-cases) - (f + l) / 2 - eg. (5 + 10) / 2 -> 15 / 2 -> 7.5
            # ! difference (l - f) halved (/ 2) is the mid-length + start-index 'f' - eg. 5 + (10 - 5) / 2 -> 5 + 5/2 -> 5 + 2.5 -> 7.5
            # * (NB: pemdas / bodmas - division always before addition)
            if x == a[m]: return m
            elif x < a[m]: return r_binary_search(a, x, f, m - 1)
            # else - x > a[m]
            else: return r_binary_search(a, x, m + 1, l)

        f, l = 0, len(a) - 1
        r_binary_search(a, 7); r_binary_search(a, 7, f, l)

        while f < l:
            m = math.floor(f + (l - f) / 2)
            if x == a[m]: return m
            elif x < a[m]: l = m - 1
            # else - x > a[m]
            else: f = m + 1
        
        return None



########################################
##  OTHER ALGO'S
########################################

# Data Structures (Arrays, Strings, Matrices, etc)

class DataStructures:

    def __init__(self): # O() t ; O() s
        pass # TODO
    

    # Arrays & Strings

    class Arrays:

        def __init__(self): # O() t ; O() s
            # TODO
            pass

        reverse = lambda a: a[::-1] # O(1) t ; O(1) s # todo: confirm reverse-slicing as O(1) t

        def reverse(self, a: list): # O(n/2) t ; O(1) s
            i, j = 0, len(a) - 1
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1; j -= 1
            return a
        
        # ! with math problems, always try solving them with math-algo's 1st, before considering array / string conversions
        def reverse_number(self, num): # O(1 ~ d) t [d = num's number of digits] ; O(1) s
            rnum = 0
            while num > 0:
                d = num % 10 # get last digit
                # remove last digit (as a 10th-divided decimal)
                num = num // 10 # * or: math.floor(num / 10)
                rnum = rnum * 10 + d # append last digit to reversed number (as a 10th-multiplied padded 0)

        def remove_element(self, a): # TODO
            pass

        #
        def remove_element(self, a):
            pass

        # 3rd-Party (Tutorial) - LC #
        def remove_element(self, a):
            pass

        def remove_elements(self, a): # TODO
            pass

        #
        def remove_elements(self, a):
            pass

        # 3rd-Party (Tutorial) - LC #
        def remove_elements(self, a):
            pass

        def majority_element(self, a): # TODO
            pass

        #
        def majority_element(self, a):
            pass

        # 3rd-Party (Tutorial) - LC #169
        def majority_element(self, a: List[int]) -> int: # O(n + m ~ 2n ~ n) t ; O(n) s
            m = {}

            # 1st pass: keep count of items in hash-map
            for n in a:
                if n in m: m[n] += 1
                else: m[n] = 1

            # 2nd pass: for each item in map, return key of count which is > n/2
            majority = math.floor(len(a) / 2.0)
            majority_element = nums[0]

            for k, v in map.items():
                if v > majority:
                    majority_element = k

            return majority_element
        
        def find_duplicates(self, a): # O(n) t ; O(1) s
            # can use a hashmap or extra array - O(n) s
            # can also remove each item and re-check if it still exists in same array
            for i, v in enumerate(a):
                del a[i] # todo: confirm O(1) t - deleting array-item by index
                if v in a: return True
            return False
        
        # 3rd-Party (Tutorial) - using absolute values (in-case deleting array-items not an option)
        '''
            find duplicates in 1D array in O(n) t where its integer values are smaller than length of array
            constraints: 
                - maximum number smaller than size of array
                (i.e. array's indices are also part of its values)
                - +ve & -ve values also considered repetitions
        '''
        def find_duplicates(self, a): # O(n) t ; O(1) s
            for n in a:
                an = abs(n) # get absolute index of n
                '''
                    if any integer > len(a), 
                    a[abs(n)] in that case would throw:
                    IndexError: list index out of range
                    so all integer-values in array 'a' must less than its size, as an input
                '''
                if a[an] >= 0: # if n's absolute, as an index with a[index] - +ve 
                    a[an] = -a[an] # turn a[index] -ve, if +ve
                else: # a[index] - -ve
                    print('Repitition found: %s' % str(an))
                    return an
                '''
                    a[an] - item at 'an' index is turned negative when positive
                    so on any next iteration where abs(n) gives same 'an' value
                    & same a[an] accessor is now -ve this time, then that 'n' 'absolute'd was a repetition
                '''
            return -1

        def min_jumps(self, a): # O() t ; O() s
            # TODO
            pass

        # ! WRONG - padding zeroes to end - infinite loop
        def move_zeroes_to_end(self, a): # O(n^2 ~ n) t ; O(1) s
            for i, v in enumerate(a):
                if v is 0:
                    # ! wrong - popping out from index will disrupt iterations
                    # * (next iteration will skip this index's replacement item)
                    a.pop(i) # O(n ~ 1) or: del a[i] - O(1)
                    # ! wrong - appending 0s also turns to an infinite loop
                    a.append(v) # ! also O(n ~ 1) t on worst-case
                    # ! cannot set on length-index (out of range exception) - in .py
                    # a[len(a)] = v # O(1) t on setting at index
            return a
            # ! use a while-loop (manual iteration-control) if the same input array must be edited
        
        # using a manual while loop (only iterate when necessary)
        def move_zeroes_to_end(self, a): # O(n/2 ~ n) t ; O(1) s
            i = c = 0
            while i < len(a):
                n = a[i]
                if n == 0:
                    if len(a) - i <= c: # ! should be '==' but added <= in case of length-subtraction errors - Test & confirm
                        break
                    c += 1
                    a.pop(i) # O(n~1)
                    a.append(0) # O(n~1)
                else: i += 1
            return a

        # 3rd-Party (Tutorial) - LC #283 - iterative swaps
        def move_zeroes_to_end(self, a: List[int]) -> None: # O(2n ~ n) t ; O(1) s
            i = 0
            for n in a:
                if not n is 0:
                    a[i] = n
                    i += 1
            for j in range(i, len(a)):
                a[j] = 0

        def move_zeroes(self, a): # TODO
            pass

        #
        def move_zeroes(self, a):
            pass

        # 3rd-Party (Tutorial) - LC #283 - using Iterative Swaps
        def move_zeroes(self, a: List[int]) -> None: # O(n) t ; O(1) s
            if len(a) <= 1: return a

            def swap(a: List[int], i: int, j: int):
                tmp = a[i]; a[i] = a[j]; a[j] = tmp

            non_zero_last_index = 0; runner = 0

            while runner < len(a):
                if a[runner] != 0:
                    swap(a, non_zero_last_index, runner)
                    non_zero_last_index += 1
                runner += 1

            return a

        '''
        Given an array of ints, return true if:
            - length >= 3
            - index i, such that:
                a[0] < a[1] < ... < a[i] &
                a[i] > a[i + 1] > ... > a[a.size - 1]
            - so a[i] is the 'apex' of the array
        
        Soln: Find if there's an increasing subarray followed by a decreasing subarray
        '''
        # * Using 2-pointer
        def valid_mountain(self, a): # O(n/2) ~ 1) t - 'fake' apex's can be found earlier ; O(1) s
            if len(a) < 3: return None

            i, j = 0, len(a) - 1
            apex = None

            while i < j:
                # ! could be '>=' on the constraint: a[?] <= a[i]
                if a[i + 1] > a[i]: i += 1
                else:
                    if apex is not None \
                        and apex is not i: return False
                    else: apex = i
                if a[j - 1] > a[j]: j -= 1
                else:
                    if apex is not None \
                        and apex is not j: return False
                    else: apex = j

            # * not required; apex will always be found
            # if apex is None: apex = i if a[i] > a[j] else j if a[j] > a[i] else (i, j)

            return True, apex, a[apex]

        def valid_mountain(self, a): # O(n) t ; O(1) s
            i = 1
            while i < len(a) and a[i] > a[i - 1]:
                i += 1
            if i is 1 or i is len(a):
                return False
            while i < len(a) and a[i] < a[i - 1]:
                i += 1
            return i is len(a)

        # 3rd-Party (Tutorial) - LC #941
        def valid_mountain(self, a: List[int]) -> (bool, int): # O(n) t ; O(1) s
            if len(a) < 3: return False
            i = 1

            while i < len(a) and a[i] > a[i - 1]:
                i += 1
            if i == 1 or i == len(a):
                return False
            while i < len(a) and a[i] < a[i - 1]:
                i += 1
            return i == len(a), a[i]

        '''
        Given a number n that reps amount of version
        & a function that accepts a number & returns whether it's a bad version or not
        find the 1st bad version of the array
        
        NB: if a version is bad, all succeeding versions are bad
        '''
        # 2-pointer
        def first_bad_version(self, a):
            pass # TODO

        #
        def first_bad_version(self, a):
            pass # TODO

        # 3rd-Party (Tutorial) - LC #2778 - 2-pointer
        def first_bad_version(self, num): # O(log n ~ n (why ~ n ?) t ; O(1) s

            is_bad_version = lambda n: random.rand([true, false])

            left, right = 1, num

            while left < right:
                mid = left + (right - left) // 2
                if not is_bad_version(mid):
                    left = mid + 1
                else: right = mid

            return left

        '''
        Find the maximum area between any 2 heights in a given container
        '''
        # 2-pointer
        def container_with_most_water(self, a): # O(n) t ; O(1) s # ! NO 'n/2' t because both pointers do not iterate simultaneously
            # (they iterate 1 after the other, so each item is dealt with singly (iteration-wise) - even though both extremes are dealt with together)


            i, j, max_area = 0, len(a) - 1, 0

            while i < j:
                shorter_height = min(a[i], a[j])
                area = shorter_height * (j - i)
                max_area = max(max_area, area)

                if a[i] < a[j]:
                    i += 1
                else: j -= 1

            return max_area

        # 3rd-Party (Tutorial) - LC #11
        def container_with_most_water(self, a): # O(n) t ; O(1) s
            i, j, max_area = 0, len(a) - 1, 0

            while i < j:
                max_area = max(
                    max_area,
                    min(a[i], a[j])
                    * (j - i)
                )
            if a[i] < a[j]:
                i += 1
            else: j -= 1

            return max_area

        '''
        Boats to Save People - trying to add people in safety boats
        Given an array 'people' of people's weight & an integer limit, 
        ith person has a weight people[i], & each boat can carry at most 'limit'
        
        Each boat carries at most 2 people at the same time, 
        given that their weight sum is at most limit
        
        return the minimum number of boats to carry every given person
        
        NB: it is guaranteed each person can be carried by a boat
        
        Constraints:
            - max no. of people a boat can carry is 2
            - each person has a weight <= limit
            - worst-case scenario is that 
            it'd take as many boats as there are people
        '''
        def boats_to_save_people(self, people, limit=2): # O( n(n/2) ~ n ) t ; O( n ~ n/? ~ 1 ) s
            boats, boat, backlog = 0, 0, []

            def save(p):
                if p <= limit - boat: # enough space
                    boat += p
                else: # not enough space
                    backlog.append(p) # O(n/?) s
                    return

                if boat is limit:
                    boats += 1
                    boat = 0

            for p in people:
                while backlog: # O(n/2) t
                    save(backlog.pop(0))
                save(p)

            return boats

        # sort array, add from lightest to heaviest person
        def boats_to_save_people(self, people, limit=7): # O(n log n + n ~ ?? ) t ; O( n ~ n/? ~ 1 ) s

            people = sorted(people) # O(n log n) t
            # return self.boats_to_save_people(people, limit)
            boats, boat, backlog = 0, 0, [] # * backlog still required in case

            def save(p):
                if limit - boat < p: # not enough space
                    backlog.append(p)
                    return
                else: # enough space
                    boat += p

                if boat is limit:
                    boats += 1
                    boat = 0

            for p in people: # O(n) t
                while backlog:
                    save(backlog.pop(0))
                save(p)

            return boats

        # 2-pointer - sort array, add the lightest & heaviest people
        def boats_to_save_people(self, people, limit=7): # O(n log n + n/2 ~ ?? ) t ; O( n ~ n/? ~ 1 ) s

            people = sorted(people) # O(n log n) t
            # return self.boats_to_save_people(people, limit)

            boat, boats, backlog, i, j = 0, 0, [], 0, len(people) - 1

            def save(p):
                available_space = limit - boat
                if p <= available_space:
                    boat += p
                else:
                    backlog.append(p); return

                boat = 0; boats += 1

            while i < j:

                while backlog: # * can also ensure backlog is always sorted (more time-expensive)
                    save(backlog.pop(0))

                # add lightest 1st, then heaviest
                # * can also add both of them together - will complicate limit with available-space
                save(people[i]); i += 1
                save(people[j]); j -= 1

            return boats

        # 2-pointer - sort array, add the lightest & heaviest people ; with no backlog
        '''
            sort list of people 1st

            use 2-pointers at start & end of people
            iterate with 2 pointers while left < right
            when left & right are equal, incremented boats returned out of loop

            if both weights of people at both left & right pointers are lower than or equal to limit:
                move left pointer right & right pointer left, & increment no. of boats required
            
            if both weights are bigger than the limit, 
                add the heavier person alone (move right pointer to the left)
                & increment the no. of boats required
            
            NB: the heavier person can be backlogged to be added with priority later
            but if that person will be added with priority later, best to add alone right now
            
            as right pointer moves to left, towards lighter people, 
                the current lightest person on the far left pointer can be added along
                then the left pointer can also be moved to the right
            
            NB: left-pointer (lightest person) has to wait 
                until right-pointer reaches a 'heavy' person, light enough, 
                for the lightest person to be added, while total weight < limit
            NB: beats the point of 'saving' people because more boats will be allocated to singly-people (or prioritizing the 'heavy/fat/wealthy')
                before the lightest people 'get on board'
            NB: so another algo can cater to this flaw; more people get saved earlier if lighter people are prioritized
            
            always increment no. of boats required as & whenever limit is reached
            
            Worst-case scenario:
                every person would need their own individual boat
        '''
        def boats_to_save_people(self, people, limit=7): # O(n log n + n/2 ~ ?? ) t ; O( n ~ n/? ~ 1 ) s

            people = sorted(people)
            boats, boat, i, j = 0, 0, 0, len(people) - 1

            def save(l, r):
                res = (False, False)

                if l + r <= limit:
                    boat += l + r
                    res = (True, True)
                else: # r (heavier person) alone cannot exceed limit
                    # ! constraint: each person has a weight <= limit
                    boat += r
                    res = (False, True)
                    '''
                        # ! in this situation, you can instead keep adding left only, until limit is reached
                        * so (True, False) returned instead, for only left-pointer to be moved to right
                    '''
                    ''' 
                        # ! Now, here's why this alternative is still a 'stupid' solution
                        
                        if left-pointer (lightest) is more prioritized than right-pointer (heaviest):
                            right-pointer will stay static for the remainder of the loop, for left-pointer to reach it
                            left-pointer moves towards heavier people, so they can never be added with heaviest person 
                                together to still be below the weight limit
                            - O(t) eventually falls back to O(n) & not O(n/(2 or ?) ~ n) t
                            - 1 person keeps being added at a time, with only 1 (left) pointer being iterated
                                
                                # ! - if a 3rd (or even more) pointer is used to pre-iterate before left-pointer, then multiple (~ > 2) lightest people can then be added at a goal
                                # ! then this will be the most optimized solution - except the 3rd-pointer flaws must be taken into consideration
                            
                        if right-pointer (heaviest) is more prioritized than left-pointer (lightest):
                            left-pointer will never stay static for the remainder of the loop, for right-pointer to reach it
                            right-pointer moves towards lighter people, so will always reach a light-enough person to be added 
                                together with the lightest person to now be below the weight limit
                            - O(t) should still be O(n/(2 or ?) ~ n) t
                            - 1 person only keeps being added at a time, until 2 people can be added together again
                            - as 2 people keep being added together (even with more 'heavy-people breaks' in-between)
                                more people get added to the boat at a much faster rate
                        
                        # ! but in reality, (when saving people and not regarding usage of 'pointers' to access them):
                            - fastest option is always to add the lightest people first, for saving maximum possible
                    '''

                if boat is limit:
                    boats += 1
                    boat = 0

                return res

            while i < j:
                res = save(people[i], people[j])
                if res[0]: i += 1
                if res[1]: j += 1

            return boats

        # 3rd-Party (Tutorial) - LC #881 - 2-pointer
        def boats_to_save_people(self, people: List[int], limit: int = 2) -> int: # O(n log n + n/2) t ; O(1) s
            people.sort()
            i, j, boats = 0, len(people) - 1, 0

            while i <= j:
                if i == j:
                    boats += 1
                    break
                if people[i] + people[j] <= limit:
                    i += 1

                j -= 1
                boats += 1

            return boats

        def first_and_last_position(self, a, n): # O(n/2) t ; O(1) s
            i, j = 0, len(a) - 1
            first = last = None

            while i < j:
                if a[i] is n:
                    first = i
                else: i += 1
                if a[j] is n:
                    last = j
                else: j -= 1

                # if first and last: # * not optimal
                # bool(0) (or any other 'falsy' value) is still False
                if first is not None \
                    and last is not None:
                    break

            return (first, last)

        # in a sorted array
        def first_and_last_position(self, a, n): # O(n/2) t ; O(1) s
            # a.sort() # * sort if not already sorted - O(n log n) t

            i, j = 0, len(a) - 1
            first = last = None

            while i < j:
                if a[i] is n:
                    first = i
                else: i += 1
                if a[j] is n:
                    last = j
                else: j -= 1

                # if first and last: # * not optimal
                # bool(0) (or any other 'falsy' value) is still False
                if first is not None \
                    and last is not None:
                    break

            return first, last

        # binary search on a sorted array
        '''
            ensure array is sorted 1st
            set 2 pointers at start & end of array
            
            getting 'middle' occurrence index:
            
            loop while left-pointer <= right-pointer
                - binary-search for target number between both pointers
                - get middle index, assign left/right to mid +/- 1 based on comparison b/n target & middle item
                - expand both indices out, until edge indices of target number's repetitions
                
        '''
        def first_and_last_position(self, a, n): # O(n/2) t (array already sorted) ; O(1) s
            # a.sort() # or: a = sorted(a) - ensure array sorted - O(n log n)
            f, l = 0, len(a) - 1
            first = last = None

            while f < l:
                m = f + (l - 1) // 2
                if n is a[m]: # n - target
                    '''
                    now, iterate both f & l back to their opposite directions,
                    until both edges of n's repetitions
                    for first & last indices
                    '''
                    f = l = m
                    while a[f] is n: f -= 1
                    while a[l] is n: l += 1
                    # ! re-add 1-step back again, to actually be at edge - indices
                    first, last = f + 1, l - 1
                    break
                elif n > a[m]: f = m + 1
                else: l = m - 1

            return first, last

        # binary search for both 1st & last occurrence
        '''
            ensure array is sorted 1st
            set 2 pointers at start & end of array
            
            getting 1st occurrence index:
            
            loop while left-pointer <= right-pointer:
                - binary-search for target number between both pointers
                - get middle-index, assign left/right to mid +/- 1 based on comparison b/n target & middle item
                - if target is found at middle-index, return middle-index if:
                    - (mid - 1 >= 0) && (nums[mid - 1] != target) || (mid == 0)
                    - else - assign right = mid - 1
            
            reset 2 pointers to start & end of array
            
            getting last occurrence index:
            
            loop while left <= right:
                - binary-search for target number between both pointers
                - get middle-index, assign left/right to mid +/- 1 based on comparison b/n target & middle item
                - if target is found at middle-index, return middle-index if:
                    - (mid + 1 < nums.size()) && (nums[mid + 1] != target) || (mid == nums.size() - 1)
                    - else - assign left = mid + 1
            
        '''
        def first_and_last_position(self, a, n): # O(2log n ~ log n) t (binary-search) ; O(1) s

            f, l = 0, len(a) - 1
            first = last = None

            while f <= l:
                m = f + (l - f) // 2
                if a[m] is n: # binary-search with only target equality-check
                    if m - 1 >= 0 and \
                        not a[m - 1] is n or \
                            m is 0:
                        first = m; break
                    else: l = m - 1 # unnecessary else with break in pre-condition
                elif a[m] < n: f = m + 1
                else: l = m - 1

            f, l = 0, len(a) - 1

            while f <= l:
                m = f + (l - f) // 2
                if a[m] is n: # not the typical binary-search (only target equality-check required)
                    if m + 1 < len(a) and \
                        not a[m + 1] is n or \
                            m is len(a) - 1:
                        last = m; break
                    else: f = m + 1
                elif a[m] < n: f = m + 1
                else: l = m - 1

            return first, last

        # 3rd-Party (Tutorial) - LC #34
        def first_and_last_position(self, nums, target): # O(log n) t (binary-search) ; O(1) s

            def get_left_position(nums, target):
                left, right = 0, len(a) - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    if (nums[mid] == target):
                        if mid - 1 >= 0 and \
                            nums[mid - 1] != target or \
                                mid == 0:
                            return mid
                        right = mid - 1
                    elif nums[mid] > target:
                        right = mid - 1
                    else: left = mid + 1

                return -1

            def get_right_position(nums, target):
                left, right = 0, len(a) - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    if (nums[mid] == target):
                        if mid + 1 < len(nums) and \
                            nums[mid + 1] != target or \
                                mid == len(nums) - 1:
                            return mid
                        left = mid + 1
                    elif nums[mid] > target:
                        right = mid - 1
                    else: left = mid + 1

                return -1

            left = get_left_position(nums, target)
            right = get_right_position(nums, target)

            return [left, right]


        # using a hashmap / extra array
        def contains_duplicates(self, a): # O(n) t ; O(n) s - whether hashmap / extra array
            m, a1 = {}, []
            for n in a:
                if n in m or n in a1:
                    return True
                m[n] = 1; a1.append(n)
            return False

        # updating input array
        def contains_duplicates(self, a): # O(n) t ; O(1) s
            for i, n in enumerate(a):
                del a[i]
                if n in a:
                    return True
            return False

        # sorting, then checking adjacent values
        def contains_duplicates(self, a):
            a.sort()
            for i, n in enumerate(a):
                # if n is a[i + 1]: # raises out-of-bounds error at i = len(a)
                if i is 0: continue # so instead, skip 1st iteration # ! but find out .py iteration through a list, still with more control over index
                if n is a[i - 1]:
                    return True
            return False

        # 3rd-Party (Tutorial) - LC #217
        def contains_duplicates(self, a): # O() t ; O() s
            pass

        # 3rd-Party (Tutorial) - LC #217
        def contains_duplicates(self, a: List[int]) -> bool: # O(n) t ; O(n) s
            if len(a) <= 1: return False
            m = {}
            for n in a:
                if n in m:
                    return True
                m[n] = True
            return False

        # using a hashmap / extra array
        def two_sum(self, a, t): # O(n) t ; O(1) s
            m, a1 = {}, [] # can choose between which data-structure to use (don't use both like in this case
            pairs = []
            for n in a:
                d = t - n
                if d in m or d in a1:
                    pairs.append((n, d))
                d[n] = 1; a1.append(n)
            return pairs

        # sort, then 2-pointer
        def two_sum(self, a, t): # O( n log n + (n/2 ~ n) ~ ?? n + n => 2n => n ) t ; O(1) s
            a.sort() # O(nlogn)
            i, j = 0, len(a) - 1
            pairs = []
            while i < j:
                s = a[i] + a[j]
                if s == t:
                    pairs.append(a[i], a[j])
                elif s < t: # move towards higher values
                    i += 1
                else: j -= 1 # move towards lower values

        # 3rd-Party (Tutorial) - LC #1
        def two_sum(self, a: List[int], t: int) -> List[int]: # O(n) t ; O(3n ~ n - only 1 map actually needed; extra 2 arrays only hold results) s
            m, ips, nps = {}, [], []
            for i in range(0, len(a)): # ranging through indices (0 -> length-1)
                d = t - a[i]
                if d in m: # return / append index-pairs
                    ips.append((m[d], i)) # append index-pair
                    nps.append((d, a[i])) # append num-pair
                else: m[a[i]] = i
            return ips, nps

        # using a base-pointer, then 2 pointers
        def three_sum(self, a): # O( n (n/2 ~ n) ~ n^2) t ; O(1) s
            i, j = 1, len(a) - 1
            pairs = []
            for n in a:
                while i < j:
                    s = n + a[i] + a[j]
                    if s == t: pairs.append((n, a[i], a[j]))
                    elif s < t: i += 1
                    else: j -= 1
            return pairs

        #
        def three_sum(self, a): # O() t ; O() s
            pass

        # 3rd-Party (Tutorial) - LC #
        def three_sum(self, a): # O() t ; O() s
            pass

        def four_sum(self, a): # TODO
            pass

        #
        def four_sum(self, a):
            pass

        # 3rd-Party (Tutorial) - LC #
        def four_sum(self, a):
            pass

        # finding out multiple intersections (repeating intersections included)
        def intersection_of_2_arrays(self, a1, a2): # O(n) t ; O(1) s
            intersections = []
            # ! always iterate through the shorter array
            # todo: so check for which is shorter 1st
            for i, n in enumerate(a1):
                if n in a2:
                    i2 = a2.index(n)
                    # ! in reality, always confirm cost-benefit of deleting any piece of data
                    del a1[i], a2[i2] # ! not-optimal, but required for newer (& repeating) intersections
                    # if n not in intersections: # * if pruning repeating intersections was required
                    intersections.append((n, i, i2))

            return intersections

        # if different array-lengths, iterate through the smaller array, check its items in the other
        def intersection_of_2_arrays(self, a1, a2): # O(n) t ; O(1) s
            intersections = []
            for n in a1 if len(a1) < len(a2) else a2: # loop through shorter array
                if n in a1 and n in a2 and (not n in intersections): # check both arrays (for compromise in previous line)
                    intersections.append(n) # * only append unique intersections this time
            return intersections

        def intersection_of_2_arrays(self, a1, a2): # O() t ; O() s
            pass # TODO

        # if same array-lengths, iterate through 1 array, check its items in the other
        def intersection_of_2_arrays(self, a1, a2): # O(n) t ; O(1) s
            ints = []
            for n in a1:
                if n in a2 and n not in ints: # ! ALSO DON'T GET TRICKED BY LANGUAGE SYNTAX
                    
                    # * 'in' keyword checks if data-structure contains a value
                    # TODO: so confirm O(t) of 'in' keyword in .py
                    # * - is it O(1) t by "time-perfected" syntax - constant-time by "keyword syntax"
                    # * or is it still O(n) t - "Linear Search" / O(log n) t - "Binary Search"
                    # * - by checking if the data-structure contains a certain value with an algo behind-the-scenes

                    # ! answers (G4G - Geeks for Geeks): 
                    # * O(n) t (Linear Search) in arrays - Binary Search not used, unless explicitly used
                    # * O(1) t in sets - Sets in Python are implemented using hash tables.
                    # The in operator for sets leverages the hash function to determine if an element exists, providing average case constant time complexity.
                    # * O(1) t in dictionaries / hashmaps / hashtables - Similar to sets, dictionaries in Python are also implemented using hash tables.
                    # The in operator checks if a key exists in the dictionary, providing average case constant time complexity.
                    # * O(m * n) t in strings - The time complexity is O(m * n), where n is the length of the string and m is the length of the substring being searched for.
                    # Strings in Python are arrays of characters. 
                    # When using the in operator to check if a substring exists within a string, Python performs a substring search, which can be quite complex.

                    
                    ints.append(n)

            return ints

        def intersection_of_2_arrays(self, a1, a2): # O() t ; O() s
            pass # TODO

        # if same array-lengths, iterate through 1 array, using its indices to access the other, in constant time
        def intersection_of_2_arrays(self, a1, a2): # O() t ; O() s
            pass # TODO

        def intersection_of_2_arrays(self, a1, a2): # O() t ; O() s
            pass # TODO

        # using a hashmap
        def intersection_of_2_arrays(self, a1, a2): # O(n) t ; O(n) s
            m, ints = {}, []
            for n in a1:
                if n not in m:
                    m[n] = 1
            for n in a2:
                if n in m:
                    if not n in ints:
                        ints.append(n)
            return ints

        def intersection_of_2_arrays(self, a1, a2): # O() t ; O() s
            pass # TODO

        # 3rd-Party (Tutorial) - LC #349
        def intersection_of_2_arrays(self, a1: List[int], a2: List[int]) -> List[int]: # O(2n + n/? (based on number of distinct elems added to map) ~ n) t ; O(n) s
            # ! another explanation
            # O( n1 + n2 + m ~ 2n1 + n2 or 2n2 + n1 (since length of m should be length of shorter array; which should've been iterated through 1st)
            # ~ 3n ~ n (if n = length of shorter array, with all distinct elements - so hashmap length == shorter array length) = n ) t ;
            # O( m + i ~ m (i - intersections only hold results) ~ n (length of shorter array == length of m) = n ) s

            # error-case if any of arrays is empty
            if not (len(a1) and len(a2)): return []

            # 1st pass: add items in a1 to hashmap
            m = {}
            for n in a1:
                if n not in m:
                    m[n] = 1

            # 2nd pass: for each item in a2, mark the ones that exist in the hashmap as 0
            num_ints = 0
            for n in a2:
                if n in m and m[n] == 1:
                    m[n] = 0
                    num_ints += 1

            # 3rd pass: iterate through hashmap, & if m[k, v]'s v = 0, then add it to intersections array
            ints = []
            for k, v in m.items(): # * confirm again: .iteritems()
                if v == 0:
                    ints.append(k)

            return ints

    
    class Strings:

        def __init__(self): # O() t ; O() s
            # TODO
            pass

        reverse = lambda s: s[::-1]

        def reverse(self, s):
            ''.join(list(s)[::-1])

        def reverse(self, s: str): # O(n + n/2 + n ~ n) t ; O(1) s
            s = list(s) # O(n ~ 1) t - convert str to list of characters
            i, j = 0, len(s) - 1
            while i < j: # O(n/2 ~ n) t
                # str doesn't support item assignment (string must be converted into a character-list 1st)
                s[i], s[j] = s[j], s[i]
                i += 1; j -= 1
            return ''.join(s) # O(n ~ 1) t

        def reverse(self, s): # TODO
            pass

        #
        def reverse(self, s):
            pass

        # 3rd-Party (Tutorial) - LC #344
        def reverse(self, s): # O(n/2 ~ n) t ; O(1) s

            def swap(s: List[str], front: int, end: int): # O(1) t & s
                tmp = s[front]; s[front] = s[end]; s[end] = tmp

            front = 0; end = len(s) - 1
            while front < end:
                swap(s, front, end) # todo: ensure swap worked with s by reference
                # * else return s = swap(..)
                front += 1; end -= 1

            return s

        def reverse_words(self, s): # O(3n ~ n) t ; O(1) s
            # ! s.split(' ').reverse().join(' ') # ! .js -> .py common mistake
            '''
            s.split('') - empty separator error
            s.split(' ') - splits on whitespaces ' ' - splits words
            # * list(s) - splits each character into a list
            [].reverse() - removes value completely (does not reverse)
            [][::-1] - reverses array
            [].join() - error! list objects don't have .join()
            # * ''.join([..]) - how to join lists into a string, with '' no whitespace
            ' '.join([..]) - how to join with ' ' whitescace
            ' - '.join([..]) - join with ' - '
            '''
            ' '.join(s.split(' ')[::-1])

        #
        def reverse_words(self, s): # O(3n ~ n) t ; O(1) s
            strs = s.split(' ') # O(n) t

            i, j = 0, strs.length - 1
            while i < j:
                strs[i], strs[j] = strs[j], strs[i]
                i += 1; j -= 1

            return ' '.join(strs) # O(n) t

        #
        def reverse_words(self, s):
            pass

        # 3rd-Party (Tutorial) - LC #557
        def reverse_words(self, s: str) -> str: # ! O(n(n/2) ~ n) t ; O(n / n~1 ? - argue between extra char-array being required for algo's usage or not) s

            def reverse(s: List[str], front: int, end: int):
                while front < end:
                    tmp = s[front]
                    s[front] = s[end]
                    s[end] = tmp
                    front += 1
                    end -= 1

            if len(s) <= 1: return s

            front, end, chars = 0, 0, list(s)

            # 2-pointer iteration outer & inner
            while end < len(s):
                # reverse when whitespace
                if chars[end].isspace():
                    reverse(chars, front, end - 1)
                    front = end + 1
                # handle last word, with no space after it
                elif end == len(s) - 1:
                    reverse(chars, front, end)
                end += 1

            return ''.join(chars)

        # 3rd-Party (Tutorial) - LC #557
        def reverse_words(self, s: str) -> str:
            pass # TODO

        # first unique character
        def first_non_repeating_char(self, s): # TODO
            pass

        #
        def first_non_repeating_char(self, s):
            pass

        # 3rd-Party (Tutorial) - LC #387
        def first_non_repeating_char(self, s):
            pass

        # first non-repeating character
        def first_unique_char(self, s): # TODO
            pass

        #
        def first_unique_char(self, s):
            pass

        # 3rd-Party (Tutorial) - LC #387
        def first_unique_char(self, s):
            if len(s) == 0: return -1
            if len(s) == 1: return s[0] # return 1st item
            m = {}
            for c in s:
                if c not in m:
                    m[c] = 1
                else: m[c] += 1
            for c in s:
                if m[c] == 1:
                    return c
            return None

        is_palindrome = lambda s: s == s[::-1] # self.reverse(s)

        def is_palindrome(self, s): # O(1) t ; O(1) s
            return s == s[::-1] # todo: confirm reverse-slicing as O(1) t

        def is_palindrome(self, s): # O(n/2) t ; O(1) s
            i, j = 0, len(s) - 1
            while i < j:
                if not s[i] == s[j]:
                    return False
            return True
        
        def is_anagram(self, s1, s2): # O(n) t ; O(1) s
            if len(s1) != len(s2): return False
            for c in s1:
                if not c in s2: return False
                del s2[s2.index(c)]  # * O(1) t ? - for .index() & del array-item
            return True

        # 3rd Party (Tutorial)
        def is_anagram(self, s1, s2): # O(2n log n) + O(n) t ~ O(n log n) t ; O(1) s
            s1, s2 = sorted(s1), sorted(s2) # O(n log n) * 2
            # return s1 == s2 # * can just end here, since both are sorted
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    return False
            return True

        # 3rd Party (Tutorial) - LC #242
        def is_anagram(self, s: str, t: str) -> bool: # O(2n + m ~ 3n ~ n) t ; O(n) s
            if not s and not t: return True
            if not s or not t: return False
            if len(s) != len(t): return False

            m = {}

            # 1st pass: add chars in s to map, & keep count
            for c in s:
                if c in m: m[c] += 1
                else: m[c] = 1

            # 2nd pass: reduce counts of chars in t found in map
            for c in t:
                if c not in m: return False
                m[c] -= 1

            # 3rd pass: check for all counts in hashmap not 0, then true
            for k, v in m.items():
                if v != 0: return False

            return True

        # remove from 1 string and compare
        def check_anagrams(self, s1, s2): # O(n) t ; O(1) s
            for s in s1:
                if s in s2:
                    del s2[s2.index(s)]
                else: return False
            return True

        # sort both and compare
        def check_anagrams(self, s1, s2): # O(2n log n) t ; O(1) s
            # s1.sort(); s2.sort() # ! string has not .sort method
            s1 = ''.join(sorted(s1))
            s2 = ''.join(sorted(s2))
            return s1 == s2 # 'is' compares var's reference id, not value itself

        def check_anagrams(self, s1, s2):
            pass

        # 3rd-Party (Tutorial) - LC #
        def check_anagrams(self, s1, s2):
            pass

        # ! wrong algo
        def longest_palindrome(self, s): # * only finds reflective pali-feature of substrings - will have breakages in-between
            i, j = 0, len(s) - 1
            l, maxL = 0, 0

            while i < j:
                if s[i] is s[j]:
                    l += 1
                else:
                    maxL = max(maxL, l) # * 2(l) - 'fake-length of 'non'-pali'
                    l = 0

            return maxL

        #
        def longest_palindrome(self, s):
            pass # TODO

        # ! IMPORTANT
        # TODO: 3rd-Party (Tutorial) - LC # ! ?
        def longest_palindrome(self, s):
            left, right, n = 0, 0, len(s)
            if n < 2: return s

            palindrome = [ [0] * n for _ in range(n) ]

            for i in range(1, n):
                for j in range(0, i):
                    isPalindrome = palindrome \
                        [j + 1][i - 1] or i - j <= 2

                    if isPalindrome and s[i] == s[j]:
                        palindrome[j][i] = True
                        if i - j > right - left:
                            left = j; right = i

            return s[left : right + 1]

        """
        Finds the longest common substring between two strings s1 and s2.
        For example, the longest common substring of "ABCDEF" and "ZBCDFG" is "BCDF".

        :param s: string to search through
        :return: longest common substring
        """
        def longest_common_substring(self, s1, s2):
            pass # TODO

        # s1 & s2 have the same length
        def longest_common_substring(self, s1, s2): # O(n) t ; O(1) s
            l = maxL = 0
            for i, c in enumerate(s1):
                if c is s2[i]:
                    l += 1
                else:
                    maxL = max(maxL, l)
                    l = 0
            return maxL

        #
        def longest_common_substring(self, s1, s2):
            pass # TODO

        # 3rd-Party (Tutorial) - LC # ?
        def longest_common_substring(self, s1, s2):
            pass # TODO

        # with a list or hashmap
        def longest_substring_without_repeating_characters(self, s): # O(n) t ; O(n) s
            m = [] # or {}
            max_length = 0

            def check(n):
                if n in m:
                    max_length = max(max_length, len(m))
                    m = []
                else: m.append(n) # or: m[n] = 1/true/ index - (injected from map method)

            map(check, s) # map check-function through list

            return max_length

        # sliding-window - 2-pointer (same direction) method
        '''
            using an empty map & 2 pointers, left & right, at start & end respectively
            map has key-value pair (character, position)
            loop with both pointers as long as both left & right are smaller than string length
                - if right-pointer item exists in map:
                    set left-pointer to maximum between the current left-pointer
                    and the value (index) of the item existing in the map (m[s[j]]), + 1
                
                NB: m[s[j]] has the last position (index) of current element s[j]
                by adding 1, & assigning the value to the left-pointer,
                it's moved to the next possible starting position (index)
                
                - after the if-check set m[s[j]] to right-pointer
                - check if current window has a larger length than previous one
                - move right-pointer to righ
        '''
        def longest_substring_without_repeating_characters(self, s): # O(n) t ; O(n) s
            m, i, j, n, max_length = {}, 0, 0, len(s), 0

            while i < n and j < n:
                if s[j] in m:
                    i = max(i, m[s[j]] + 1) # keep i at next starting index
                    # whether already-ahead of j, of 1 index after j

                # ! wrong implementations
                #     m[s[j]] = j - not necessary; stmt also required in else-case for setting new items' value (index) in map to current (lead) index
                # else: m[s[j]] = j - stmt also required in if-case for re-setting item's value (index) in map to current lead-index

                m[s[j]] = j

                max_length = max(max_length, j - i + 1)
                j += 1

            return max_length

        # * this time, moving with i as the lead-index, and j as the trailing-index
        def longest_substring_without_repeating_characters(self, s): # O(n) t ; O(n) s
            m, i, j, n, max_length = {}, 0, 0, len(s), 0

            while i < n and j < n:
                if s[i] in m:
                    j = max(j, m[s[i]] + 1)
                m[s[i]] = i
                max_length = max(max_length, i - j + 1)
                i += 1

            return max_length

        # 3rd-Party (Tutorial) - LC #3
        def longest_substring_without_repeating_characters(self, s): # O(n) t ; O(n) s
            m, i, j, n, max_length = {}, 0, 0, len(s), 0

            while i < n and j < n:
                if s[i] in m:
                    j = max(j, m[s[i]] + 1)
                m[s[i]] = i
                max_length = max(max_length, i - j + 1)
                i += 1

            return max_length


    # (Array) Lists & Tuples


    # Sets & Sequences


    # WeakMaps & WeakSets


    # HashMaps & HashTables

    class Hash:

        class HashMap:

            map = {} # same dict being used here; should be an array config'd into a custom dict/map

            def __init__(self, map={}):
                self.map = map
            
            def map(self):
                return self.map
            
            def size(self):
                return len(self.map.items())
            
            def print(self):
                print(self.map) # todo: Pattern-Program

            def check(self, key):
                return key in self.map

            def get(self, key): 
                return self.map[key] if self.check() else None

            def put(self, key, value): 
                self.map[key] = value
            
            def remove(self, key):
                return self.map.pop(key)
                # or - del self.map[key] 

        class HashTable:
            pass

        
        ''' # TODO: HashMap/Table solutions to problems are mostly sub-optimized placeholders, because they involve utilizing extra space (mostly O(n) s)
        because accessing hash-values by hash-keys is in constant time (O(1) t), using them doesn't add any extra time complexity (only space)

        Most-optimized algo solutions to all hashmap/table problems mostly exist and do not involve with hashmaps/tables, 
        but sometimes have to compensate with extra (but insignificant) time complexity, like sorting the data structure in question first, before executing them
        With these most-optimized algos, not requiring hashmaps/tables keeps them at O(1) constant space (or their own base-level space complexity)
        And sometimes required extra compensation (like sorting 1st) inc's their time complexities by some (but insignificant) time

        eg. the Two-Pointer algo can be used for the Two-Sum / Pairs with Sum problem, with constant O(1) space (without hashmaps/tables)
        but having to sort the array in question first (if it's not already sorted) moves time complexity from O(n) t, up to O(n log n + n)
        now with O(n log n + n), by BCR, we can ignore log n 's insignificant effect making ~ O(2n), and then by ignoring constants' effect
        we can end up with the same O(n) t (but only in best-case scenarios)

        - now with the 2-Pointer having ~ O(n) t & definite O(1) s, is arguably a better solution, than using HashMaps/Tables

        Check this out - https://docs.google.com/document/d/1KWwbliK1PYVXpt_njYhlCq8t373SC78eb_XJdECacTQ/edit?usp=sharing

        '''


        # Q - Given an array of integers, return all pairs that add up to a target
        # sometimes array may have only distinct (non-repeating) integers, or target may be 0 (so there'll be -ve integers)

        def pairs_with_sum(self, arr, target): # O(n) t ; O(n) s (dict)
            # todo: use Two-Pointer algo (sort arr 1st) to avoid dicts (O(1) s)
            if len(arr) < 2: return
            m, p = {}, [] # p = pairs with sum
            for n in arr:
                d = target - n
                if d in m: # or - if d in m
                    p.append((d, n)) # todo: or return (d, n) if two_sum() (finding only 1st pair)
                if n not in m: # only needed if arr doesn't have distinct elements
                    m[n] = 1 # or - if n not in m: m[n] = 1
            return p
            # todo: this time, we check for current i in m, and add current d to m
            # we could also check for current d in m, and add current i to m
            # because of target, i now will be d later, and d now will be i later

        def two_sum_indices(self, arr, target): # O(n) t ; O(n) s (dict)
            # todo: use Two-Pointer algo (sort arr 1st) to avoid dicts (O(1) s)
            if len(arr) < 2: return
            m = {}
            for i, n in enumerate(arr):
                d = target - n
                # return index of d (1st number of pair) and index i of current (2nd) number v
                if d in m: return (m[d], i) 
                if n not in m: # only needed if arr doesn't have distinct elements
                    m[n] = i
            return None
            # todo: this time, we check for current n in m, and add current d to m

        def two_sum_indices(nums, target): 
            # todo: use Two-Pointer algo (sort arr 1st) to avoid dicts (O(1) s)
            if len(nums) < 2: return
            m = {}
            for i, n in enumerate(nums):
                d = target - n
                if d in m: return [i, m[d]]
                if n not in m: # only needed if arr doesn't have distinct elements
                    m[n] = i
            return None
            # todo: this time, we check for current d in m, and add current n to m

        # 2-sum, with an array of only distinct elements (non-repeating integers)
        # same as above, but returning indices of elements, not elements themselves

        def two_sum(nums, target): 
            if len(nums) < 2: return
            d = {}
            for i, n in enumerate(nums):
                if (target - n) in d: return [i, d[target - n]]
                d[n] = i # no 'if n in d:' check required, if 'a' has only distinct elements
            return None

        def contains_duplicates(self, arr): # O(n) t ; O(n) s
            if len(arr) < 2: return
            m = {}
            for n in arr:
                if n in m: return True
                m[n] = 1
            return False
            ''' # todo: Other Options
            - sort array; if 2 consecutive elems are equal, return true
            - add all elems to a set; if set & array sizes are equal, return true
            '''
        
        # 3rd-Party (Tutorial) - LC #217
        def contains_duplicates(self, arr): # O(n) t ; O(n) s
            # defaultdict simplifies code and avoids the need for explicit initialization of counts for each character
            m = defaultdict(int)
            for n in arr:
                # in case n wasn't found in m, 0 would be returned, and not KeyError
                if m[n]: # but bool(m[n]) when default 0 is returned is still False, not True
                    return True
                m[n] = 1 # m[n] is initialized by 0 by default
            return False

        def majority_element(self, arr): # O(n + d ~ 2n ~ n) t ; O(n) s
            m = defaultdict(int)
            for n in arr: # O(n) t
                m[n] += 1 # m[n] is initialized by 0 by default, before being incremented
            max_n = max_c = 0 # max number & count
            for i, v in enumerate(m): # O(d) t
                if v > max_c:
                    max_n = i
                    max_c = v
            return (max_n, max_c) # return max number with its count

        ''' # todo: 3rd-Party - check if an element's count is greater than half the length of the array
        NOT Optimal, because an elem's count may be majority, but not more than array's half-length
        eg. [1, 2, 3, 4, 5, 1] - 1 is majority (count = 2), but 2 < 3 (6/2)
        '''
        def majority_element(self, arr): # O(n) t ; O(n) s
            m = {}
            for n in arr:
                m[n] = m.get(n, 0) + 1
            for n in arr:
                if m[n] > (len(arr)//2): # if count > half-length of array
                    return n

        # Q - Given an array of strings, group all anagrams together
        # anagrams are words which have the exact same letters (can be re-arranged to become the same word)
        
        def group_anagrams(self, arr): # O(n slogs + k) t ; O(n) s (last returned list of maps's array values isn't included in algo's exec)
            # k = number of unique words / anagram groups (can be treated as a constant term, if arr & its unique anagram groups are not too large)
            # s = length of longest string / average length of strings (longest string is a better assignment)
            
            ''' # todo: NB:
            last returned list of maps's array values may not be included in algo's exec
            but should be taken into consideration in real-world algo scenarios
            because in those cases, they're still in the system ("the algo never stops")
            '''

            m = {}
            for str in arr: # O(n) t

                # TODO: Find all the fastest &/ possible ways of sorting a string (in-place is best)

                key = ''.join(sorted(str)) # O(n log n) t quick sort | # todo: O(t) for ''.join() ?
                
                ''' # todo: .sort() a list method only (not for strings)
                # sorted(str) returns a sorted list of str's characters, so call ''.join(..) with a new string literal

                key = str
                key.sort() # O(s log s) t (quick sort in-place - key is now a "hashed value")
                '''
                
                if key in m: m[key].append(str) # or also check if str in m[key]
                else: m[key] = [str]
            
            return list(m.values()) # list of anagram groups # todo: O(k) t or O(?) NB: k = number of anagram groups
            # or [a for a in m.values()] # array of anagram groups # todo: compare O(t) with above
            # passing m's .values() to list() constructor might be inherently faster than looping through .values() & manually appending
        
        # 3rd-Party
        def group_anagrams(self, strs: List[str]) -> List[List[str]]:

            sort_str = lambda s: ''.join(sorted(s))
            m = {}

            for s in strs:
                key = sort_str(s)
                if key not in m: m[key] = []
                m[key].append(s) # this time, no need for else check, m[key] was init'd with [] instead
            
            return [a for a in m.values()]
    
        # TODO: TEST 4-SUM Qs

        # Q - Given 4 lists (arr of 4 lists), find 4 numbers (1 in each list) that add up to sum
        # sometimes array(s) may have only distinct (no repeating) integers, or target may be 0 (so there'll be -ve integers)
        # * in this case, find how many tuples there are such that, sum is 0
        
        def four_sum(self, arr: List[List[int]], target: int = 0) -> int: # 
            m, pairs = defaultdict(list), []
            [A, B, C, D] = arr # or - A, B, C, D = arr

            for x in A:
                for y in B:
                    s = x + y
                    m[s].append((x, y)) # m[s] = [] if s not in m
            
            for x in C:
                for y in D:
                    d = target - (x + y) # now, in case target != 0
                    # target - s (this sum's difference) should be the sum (if target == 0, -ve mirror of the sum) from previous loop
                   
                    # now d, should be in m
                    if d in m:
                        for p in m[d]: pairs.append((*p, x, y))
            
            return pairs
        
        # 3rd-Party - Count number of 4-group numbers that sum u pto 0 (target=0 by default)
        def four_sum_count(self, arr: List[List[int]]) -> int: # 
            m = {}; c = 0
            [A, B, C, D] = arr # or - A, B, C, D = arr

            # Because , target=0 this time ..
            # Check 1st 2 lists for all pairs & their sums
            # Check next 2 lists for all pairs with a -ve sum mirror of any sum from the 1st check

            for x in A: # or - for i in range(0, len(A)):
                for y in B:
                    s = x + y
                    if s not in m: m[s] = 0
                    m[s] += 1 # or use defaultdict(int)
                    ''' # todo: or save the pairs instead
                    if s not in m: m[s] = [] # or use defaultdict(list)
                    m[s].append((x, y))
                    '''
            
            for x in C:
                for y in D:
                    s = -(x + y) # s should be the -ve mirror of the sum from previous loop 
                    # so reverse its sign - just like `target - (x + y)` in previous Q (but target = 0 now)
                    
                    # now s, should be in m
                    if s in m: c += m[s] # not 1
                    # Not 1, because each increment of all s-finds should be multiplied by all increments of their mirror s counts (from the previous loop)
                    # permutations - if previous loop increment m[s] times, each match-pair here should match with all match-pairs (increments) there
                    
                    ''' # or - 
                    for p in m[s]: pairs.append((*p, x, y)) 
                    if m[s] was a list of tuples, each of a pair from the previous loop
                    '''

            return c # or pairs
        

        # TODO: Test more complex LRU Cache

        class LRU_Cache(HashMap):
            
            # HashMaps for fast lookups
            # Double-ended Queues for fast removals

            cache = {}
            keys = []
            
            def __init__(self, capacity):
                
                self.cache = {}
                super().__init__(map=self.cache) # todo: confirm if self.cache is passed in by reference
                # self.cache = self.map # {} # instead of assigning self.map to self.cache here
                # todo: YES - self.cache is passed by reference (so this class' obj has twin props self.map & self.cache)
                # so making changes to self.map affects self.cache (vice versa)
                
                self.keys = DataStructures.Queues.Queue()
                # for implementing LRU policy - double-ended (L/FIFO) key-placement
                # based on LRUsage
                
                self.capacity = capacity
            
            def print(self):
                print("LRU Cache:", '\n')
                self.keys.print()
                super().print()

            def check_capacity(self):
                # todo: sync checks between keys-queue length & cache-map size
                # if self.keys.len() == self.capacity:
                if self.size() == self.capacity:
                    return False
                elif self.size() > self.capacity:
                    print('Cache Overflow Error: Invalidate & Remove LRU items until capacity')
                else: return True # cache-map size / keys-queue length < capacity
            
            def get(self, key):
                # * don't self.check(key) before calling super.get() - parent meth already checks if key exists
                value = super().get(key)
                return value if value else -1
            
            def get_lru_item(self): # gets Least-Recently-Used key's value
                # * this time, self.check(key) before re-arranging it as lru key
                # already checking if key exists in super.get() - parent meth should be almost insignificant now
                key = self.get_lru_key()
                if self.check(key):
                    # todo: ensure that key == self.set_lru_key()'s return key always
                    return self.get(self.set_lru_key()) # todo: and that this return value is never None
                    # because key exists; get_lru_key() & set_lru_key() work in sync
                return -1
            
            def get_lru_key(self): # keys-queue's last item is least-recently-used
                return self.keys.last() # deque[-1] 
            
            def set_lru_key(self): # dequeueing last item in keys-queue, then enqueueing it to the beginning
                key = self.keys.dequeue_last() # deque.pop()
                self.keys.enqueue_first(key) # deque.appendleft()
                return key
            
            def get_item(self, key): # gets specific key's value
                if self.check(key): # if exists, move key to keys-queue's beginning, then get its cache-map value
                    self.keys.dequeue(value=key)
                    self.keys.enqueue_first(key)
                    return self.get(key)
                return -1

            def put_item(self, key, value):
                if not self.check(key):
                    if self.check_capacity(): # * if at capacity, invalidate LRU item 1st
                        # pop last item from keys deque & remove it from cache map
                        # todo: NB: This is the Least-Recently-Used key
                        last_key = self.keys.dequeue_last()
                        self.remove(last_key)
                    # now, put key-value in cache-map, then enqueue key at beginning
                    # * this will increment keys-queue's length & cache-map's size
                    super().put(key, value)
                    self.keys.enqueue_first(key) # * not .enqueue(key) (- queue's end), because key is now the Most-Recently-Used
                else: # then, dequeue this specific key from keys deque ..
                    # set the key-value in cache-map (parent class) ..
                    # then enqueue it back to the beginning
                    self.keys.dequeue(value=key)
                    super().put(key, value)
                    self.keys.enqueue_first(key)
                
                ''' # todo: OR: move last 2 calls from both condition-cases out of if-else check
                else: self.keys.dequeue(value=key)

                # now, put key-value in cache-map, then enqueue key at beginning
                super().put(key, value)
                self.keys.enqueue_first(key)
                '''

        # * Simpler Implementation
        class LRU_Cache_2:

            def __init__(self, capacity: int):
                self.capacity = capacity
                self.cache = dict()
                self.keys = deque()
            
            def print(self):
                print("LRU Cache - Simplified", '\n')
                print(self.keys)
                print(self.cache)
            
            def get(self, key: int) -> int:
                if key in self.cache:
                    value = self.cache[key]
                    self.keys.remove(key)
                    self.keys.appendleft(key)
                    return value
                return -1

            def put(self, key: int, value: int):
                if key not in self.cache:
                    if len(self.keys) == self.capacity:
                        oldest = self.keys.popleft()
                        del self.cache[oldest]
                else: self.keys.remove(key)

                # now, add key-value to cache map
                # then enqueue key to queue's beginning
                self.cache[key] = value
                self.keys.appendleft(key)


        # Q - Design & implement a data-structure for the Least-Recently-Used Cache

        def lru_cache(self, cache: 'LRU_Cache_2'): 
            complex = DataStructures.Hash.LRU_Cache()
            cache.print(); complex.print()
        
        # Q - Given a string S and sub-string T, find the minimum window in S which will contain all characters in sub-string T

        def minimum_window_substring(self, str, s):
            pass # TODO

        # TODO: 3rd-Party - Understand logic
        def minimum_window_substring(self, s1: str, s2: str) -> str:
            l1, l2 = len(s1), len(s2)
            if l1 < l2: return '' # no way for pattern s to exist in str
            
            m1, m2 = {}, {} # assigning 1 object is by reference

            for i in range(0, l1):
                if m2.get(s2[i]) is None:
                    m2[s2[i]] = 0
                m2[s2[i]] += 1
            
            count, left, start_i, min_l = 0, 0, -1, float('inf')

            for right in range(0, l1):

                if m1[s1[right]] is None:
                    m1[s1[right]] = 0
                m1[s1[right]] += 1

                if m2[s1[right]] is None:
                    m2[s1[right]] = 0

                if m1[s1[right]] <= m2[s1[right]]:
                    count += 1

                if count == l2:

                    while m1[s1[left]] > m2[s1[left]]:
                        m1[s1[left]] -= 1
                        left += 1
            
                    window_length = right - left + 1
                    if min_l > window_length:
                        min_l = window_length
                        start_i = left
            
            # outside for loop
            if start_i == -1: return ''
            return s1[start_i : start_i + min_l] # minimum substring window


    # Matrices

    class Matrix:

        def __init__(self): # O() t ; O() s
            # TODO
            pass

        def matrix_chain_multiplication(self, arr, i, j):
            if i == j: return 0

            min_ops = sys.maxsize
            for k in range(i, j):
                ops = self.matrix_chain_multiplication(arr, i, k) + \
                    self.matrix_chain_multiplication(arr, k + 1, j) + \
                        arr[i - 1] * arr[k] * arr[j]
                min_ops = min(ops, min_ops)
            return min_ops

        def top_down_matrix_chain_multiplication(self, arr, i, j, memo):
            if i == j: return 0

            if memo[i][j] >= 0: return memo[i][j]

            min_ops = sys.maxsize
            for k in range(i, j):
                ops = self.top_down_matrix_chain_multiplication(arr, i, k, memo) + \
                    self.top_down_matrix_chain_multiplication(arr, k + 1, j, memo) + \
                        arr[i - 1] * arr[k] * arr[j]
                min_ops = min(ops, min_ops)
            memo[i][j] = min_ops
            return memo[i][j]

        def bottom_up_matrix_chain_multiplication(self, arr, n, mat):
            
            for l in range(2, n):
                for i in range(1, n - l + 1):
                    j = i + l - 1
                    if j == n: continue
                    min_ops = sys.maxsize
                    for k in range(i, j):
                        min_ops = min(min_ops, (mat[i][k] + mat[k + 1][j] + \
                            arr[i - 1] * arr[k] * arr[j]))
                    mat[i][j] = min_ops
            return mat[1][n - 1]
        
        def test(self, test='mcm'):
            obj = DataStructures.Matrix()
            if test == 'mcm':
                arr = [4, 3, 2, 1, 5]; n = len(arr)
                print(obj.matrix_chain_multiplication(arr, 1, n - 1))
            elif test == 'td_mcm':
                arr = [4, 3, 2, 1, 5]; n = len(arr)
                memo = [[-1 for i in range(n)] for i in range(n)]
                print(obj.top_down_matrix_chain_multiplication(arr, 1, n - 1, memo))
            elif test == 'bu_mcm':
                arr = [4, 3, 2, 1, 5]; n = len(arr)
                mat = [[0 for i in range(n)] for i in range(n)]
                print(obj.bottom_up_matrix_chain_multiplication(arr, n, mat))
            else: pass


    # Linked Lists

    class LinkedList:

        class ListNode:

            def __init__(self, v=None, n=None):
                self.value = v; self.next = n

        # Singly-linked list
        class SListNode(ListNode):

            def __init__(self, v=None, n=None):
                super().__init__(v, n)

        # Doubly-linked list
        class DListNode(ListNode):

            def __init__(self, v, n=None, p=None): 
                super().__init__(v, n)
                self.prev = p
            
            def be_next_of(self, l):
                l.next = self
                return l
            
            def be_prev_of(self, r):
                r.prev = self
                return r
            
            @staticmethod
            def from_array(a): 
                pass # TODO
                # nodes = [ListNode(i) for i in a]
                # nodes.__reduce__(lambda(acc: ListNode, cur: ListNode): acc.be_next_of(cur))
            
            def for_each(self, cb, i):
                cb(self.value, i)
                if self.next is not None:
                    self.next.for_each(cb, i + 1)

        def __init__(self, h=None, t=None, l=0): 
            self.head: ListNode = h
            self.tail: ListNode = t
            self.length = l
        
        def create_list(self, arr):
            start = self.head
            tmp = start
            n = len(arr); i = 0
            while i < n:
                node = ListNode(arr[i])
                if i == 0:
                    start = node
                    tmp = start
                else:
                    tmp.next = node
                    node.prev = tmp
                    tmp = tmp.next
                i += 1
            self.head = start
            return self.head

        def print_list(self):
            node = self.head
            ll = ''
            while node:
                ll += (str(node.value) + ' ')
                node = node.next
            print(ll)
        
        def length(self):
            # required when there's no self.length prop being inc'd/dec'd whenever there's a change in the linked list
            node = self.head
            l = 1
            while node.next:
                node = node.next
                l += 1
            return l

        def traverse(self, backward=False, cb: Callable[[ListNode], None]=None):
            node = self.head if not backward else self.tail
            while node is not None:
                print(f"Working with node - {node.value}")
                cb(node)
                node = node.next if not backward and node.next else node.prev if node.prev else None
        
        def find(self, i):
            node = self.head
            c = 0
            while c < i: # previous node after loop end
                node = node.next
                c += 1
            return node
    
        def find_tail(self, i): # if no tail is set yet
            if self.tail is not None: return self.tail
            if not self.head: return None
            node = self.head
            while node.next:
                node = node.next
            self.tail = node
            return self.tail
        
        def insert(self, n: ListNode):
            if self.head is None:
                self.head = self.tail = n
            else: self.insertTail(n)
        
        def insert_at_index(self, v, i: int): # O(n ~ i) t
            node = ListNode(v)
            if i == 0: 
                self.insert_head(node) # O(1) t 
                return
            prev = self.find(i) # O(n ~ i) t
            # O(1) t
            next = prev.next
            prev.next = node
            node.prev = prev
            node.next = next
            next.prev = node

        def insert_at_index(self, i: int, v): # override
            if self.head is None or \
                i < 0 or i >= self.length: 
                return None
            node = ListNode(v)
            if i == 0: self.insert_head(node)
            elif i == self.length - 1: self.insert_tail(node)
            else:
                c = 0
                tmp = self.head
                while c < i:
                    tmp = tmp.next
                    c += 1
                next = tmp.next
                node.prev = tmp
                node.next = next
                tmp.next = node
                next.prev = node
        
        def insert_head(self, n: ListNode):
            n.next = self.head
            self.head = n
        
        '''
        faster than inserting an item to the beginning or end of an array - for i in range(500000): arr.insert(0, i)
        because array has to shift all the other items to the right, after each insertion of a new item to the beginning
        '''
        
        def insert_tail(self, n: ListNode):
            if type(n) is DataStructures.LinkedList.DListNode: 
                n.prev = self.tail
            self.tail.next = n
            self.tail = n
        
        def remove_at_index(self, i):
            if self.head is None: return
            prev = self.find(i-1)
            if prev and prev.next:
                node = prev.next
                next = node.next
                prev.next = next 
                next.prev = prev
                node.next = node.prev = None
        
        def remove_at_index(self, i: int): # override
            if self.head is None or \
                i < 0 or i >= self.length:
                return None
            if i == 0: self.remove_head()
            elif i == self.length - 1: self.remove_tail()
            else:
                c = 0
                node = self.head

                # Option 1 - only for doubly-linked
                
                while c < i:
                    node = node.next
                    c += 1
                prev = node.prev 
                next = node.next
                prev.next = next
                next.prev = prev

                # Option 2 - only for singly-linked
                
                while c < i-1: # would still work for i == 1; first iteration would fail, but node = self.head already
                    node = node.next
                    c += 1
                node.next = node.next.next
        
        def remove_value(self, v): # O(n) t
            # remove all nodes containing value v

            def remove_node(node):
                prev = node.prev # wouldn't work on a singly-linked (use self.find with an index - 1)
                next = node.next
                prev.next = next
                next.prev = prev
                node.next = node.prev = None
            
            if self.head is None: return
            tmp = self.head
            while tmp:
                if tmp.value == v:
                    remove_node(tmp)
                tmp = tmp.next
        
        def remove_head(self):
            if self.head is None: return
            n = self.head
            self.head = self.head.next # or n.next
            n.next = None; self.head.prev = None
        
        def remove_tail(self): # works for doubly-lls only
            if self.head is None: return
            if self.tail is None: self.tail = self.head
            self.tail = self.tail.prev
            self.tail.next = None
            # or
            n = self.tail
            # self.tail = n.prev # unnecessary if uncomment, not tail set if commented
            n = None
        
        def remove_nth_from_end(self, i: int) -> ListNode:
            # only works for doubly-linked lists
            node = self.tail
            while i > 0:
                node = node.prev
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

        def middle_node(self): # O(n/2 ~ n) t ; O(1) s
            slow = fast = self.head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(self): # O(n) t ; O(1) s
            node = self.head
            prev = next = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            self.head = prev # or self.tail
        
        def has_cycle(self):
            if self.head is None or self.head.next is None:
                return False
            slow = fast = self.head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                # if fast began from the next to start (slow) node, you check before iterating nodes
                if slow is fast or id(slow) == id(fast) or slow == fast: 
                # 3rd (slow == fast) check also works for referenced object equality comparison
                    return True
            return False
        
        def odd_evens(self): # O(n) t ; O(n) s (2 * n/2)
            # sort ll with odds 1st, then evens after
            if not self.head: return None
            lo = le = ListNode()
            lo_head = lo; le_head = le
            node = self.head
            while node:
                if node.value % 2 == 0:
                    le.value = node.value
                    le = le.next = ListNode()
                else:
                    lo.value = node.value
                    lo = lo.next = ListNode()
                node = node.next
            if not lo.value: lo = le_head
            else: lo.next = le_head
            if not le.value: le = None
            else: self.tail = le_tail = le
            # finding le's tail if set to None becomes difficult here
            # next option is to use a dummy head for the 2nd half (le - evens ll), 
            # so there's no need to create empty ListNodes at the end of each iteration
            
            # next implementation options below # test
            ll = DataStructures.LinkedList(h=lo_head)
            return ll
        
        def odd_evens(self): # todo: Test
            if not self.head: return None
            lo = le = ListNode()
            lo_dummy, le_dummy = lo, le
            node = self.head; i = 0
            while node:
                if node.value % 2 == 0:
                    le = le.next = ListNode(v=node.value)
                else:
                    lo = lo.next = ListNode(v=node.value)
                node = node.next
                i += 1

            # after loop, node == null)
            le.next = node # point last even node to null node
            self.tail = le # then set it to tail
            lo.next = le_dummy.next # connect odd lo and even le
            # find out if lo_dummy / le_dummy's states (being assigned le by obj reference) change whenever le.next or lo.next gets updated
            le_dummy = le_dummy.next = None # find out if this affects le's real head (lo.next) by obj reference
            
            ll = DataStructures.LinkedList(h=lo_dummy.next, t=le, l=i)
            return ll
        
        # Better option - creating only 1 extra ll for evens, as the main ll is being traversed (remove evens to be added to extra ll), then append evens to main ll after
        
        def odd_evens(self): # O(n) t; O(n/k or n-k ? ~ 1) s (k - num even numbers)
            if not self.head: return None
            le_dummy = le = ListNode()
            node = self.head; i = 0
            # easier using node.prev if doubly-linked
            prev = None # with singly-linked, loop alongside manual prev var
            while node:
                if node.value % 2 == 0:
                    if prev == None: # for 1st iteration only (optimize is necessary)
                        self.head = node.next
                    else: # should check: type(prev) is ListNode
                        prev.next = node.next
                    le = le.next = node # ListNode(v=node.value) is actually not required; can point directly to the node # todo: test

                else: pass # do nothing this time, if node.value is odd
                
                prev = node
                node = node.next

            # after loop, prev is the last node (node == null)
            le.next = node # point last even node to null node
            self.tail = le # then set it to tail
            prev.next = le_dummy.next # connect main ll and even le
            le_dummy = None # delete le dummy node
            return self.head # final odd-even sorted linked-list

        # Best option so far - only a few extra vars created, instead of an extra ll or 2 lls as the before options

        def odd_evens(self): # O(n) t ; O(1) s
            pass # TODO: 

        # 3rd-Party - Alt-logic # todo: test

        def odd_evens(self): # O(n) t ; O(1) s (only 3 additional vars are used)
            if not self.head: return None

            # this assumes 1st node always contains an odd number
            odd = self.head; 
            # this assumes 2nd node always contains an even number
            even = odd.next
            evenList = even

            while even and even.next:
                odd.next = even.next
                odd = odd.next

                even.next = odd.next
                even = even.next
            
            odd.next = evenList
            return self.head


        ''' # todo: Test
        ll = LinkedList()
        ll.head = ListNode(5)
        node = ListNode(1)
        ll.head.next = node
        node.next = ListNode(7)
        ll.insert_at_index(2, 2)
        ll.print_list()
        ll.remove_at_index(2)
        ll.print_list()
        '''


        # todo: Test next set of Alt (3rd-Party - Tutorials) Logic Samples


        def get(self, i: int) -> int:
            if i < 0 or i >= self.length: return -1
            node = self.head
            while i != 0:
                node = node.next
                i -= 1 # decrementing this time
            # when i reaches 0, node is found
            return node.value
        
        def addAtHead(self, v):
            node = ListNode(v)
            if self.head is None:
                self.head = self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.length += 1
        
        def addAtTail(self, v):
            node = ListNode(v)
            if self.head is None:
                self.head = self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            self.length += 1

        def addAtIndex(self, i: int, v):
            if self.head is None or \
                i < 0 or i > self.length: 
                return None
            elif i == 0: self.addAtHead(v)
            elif i == self.length: self.addAtTail(v)
            else:
                tmp = self.head
                while i-1 != 0:
                    tmp = tmp.next
                    i -= 1
                node = ListNode(v)
                node.next = tmp.next
                tmp.next.prev = node
                tmp.next = node
                node.prev = tmp
                self.length += 1
            # not outside else: because it's also inc'd in both addAt(Head/Tail)
        
        def deleteAtHead(self):
            if self.head is None: return None
            else:
                node = self.head.next
                if node: node.prev = None
                self.head = node
            self.length -= 1
        
        def deleteAtTail(self):
            if self.tail is None:
                if self.head is None: return None
                else: self.tail = self.head 
                # set new tail to be deleted later (or now .. if required)
            else:
                node = self.tail.prev # for doubly-linked only (else, loop to end of singly-linked-list)
                self.tail = node
            self.length -= 1
        
        def deleteAtIndex(self, i):
            if self.head is None or \
                i < 0 or i >= self.length: 
                return
            elif i == 0: self.deleteAtHead()
            elif i == self.length - 1: self.deleteAtTail()
            else:
                c = 0
                node = self.head

                # Option 1 - only for doubly-linked
                
                while c < i:
                    node = node.next
                    c += 1
                prev = node.prev 
                next = node.next
                prev.next = next
                next.prev = prev

                # Option 2 - only for singly-linked
                
                while c < i-1: # would still work for i == 1; first iteration would fail, but node = self.head already
                    node = node.next
                    c += 1
                node.next = node.next.next
        
        def deleteAtIndex(self, i: int): # override
            if i < 0 or i >= self.length: return
            elif i == 0: # manually deleting Head
                node = self.head.next
                if node: node.prev = None
                self.head = self.head.next # node
                self.length -= 1
                if self.length == 0:
                    self.tail = None
            elif i == self.length - 1:
                node = self.tail.prev
                if node: node.next = None
                self.tail = self.tail.prev # node
                self.length -= 1
                if self.length == 0:
                    self.head = None
            else:
                node = self.head
                while i - 1 != 0:
                    node = node.next
                    i -= 1
                node.next = node.next.next
                node.next.prev = node
                self.size -= 1

        def middleNode(self, head: ListNode) -> ListNode:
            # corner case: if head or head.next is null, return head
            if head is None or head.next is None:
                return head

            slow = head
            fast = head
            # step 2: move slow and fast pointers until fast.next or fast.next.next is null
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            
            # step 3:
            
            middle = head;                                                                                    
            # odd case
            # if fast.next is null, middle is slow
            if fast.next is None:
                middle = slow
            # even case
            # else fast.next.next is null, middle is slow.next
            else:
                middle = slow.next
            
            return middle


        def hasCycle(self, head: ListNode) -> bool:
            # corner case: if head or head.next == null, return false
            if head is None or head.next is None:
                return False
            
            #  run two pointers, slow (turtle) and fast (rabbit) while fast.next and fast.next.next is not null
            slow = head
            fast = head.next
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next

                # if there is a cycle, 2x speed fast (rabbit) will eventually catch up with 1x speed slow (turtle) pointer
                if slow == fast:
                    return True
                
            return False

        def insertAtLocation(self, v, i):
            tmp = self.head
            l = self.length()
            if l + 1 < i: return tmp
            node = ListNode(v)
            if i == 1:
                node.next = tmp
                tmp.prev = node
                self.head = node
                return self.head
            if i == l + 1:
                while tmp.next is not None:
                    tmp = tmp.next
                tmp.next = node
                node.prev = tmp
                return self.head
            j = 1
            while j < i - 1:
                tmp = tmp.next
                j += 1
            next = tmp.next
            node.next = next
            next.prev = node
            tmp.next = node
            node.prev = tmp
            return self.head
        
        def removeAtLocation(self, i):
            tmp = self.head
            l = self.length()
            if l < i: return tmp
            if i == 1:
                tmp = tmp.next
                self.head = tmp
                return self.head
            if l == i:
                while tmp.next and tmp.next.next:
                    tmp = tmp.next
                    tmp.next = None
                    return self.head
            j = 1
            while j < i - 1:
                tmp = tmp.next
                j += 1
            prev = tmp
            node = tmp.next
            next = node.next
            prev.next = next
            next.prev = prev
            node.next = node.prev = None
            return self.head
        
        def removeNthFromEnd(self, head: ListNode, i: int) -> ListNode:
            ans = ListNode(0)
            node = next = ans # todo: node & next would be set by reference on abstract objects (and primitive arrays, dicts, etc), but not the most basic primitive literals (like int 0)
            # updating next obj would also update node the same way (ans is an obj of abstract class ListNode)
            ans.next = head # like this, would update both node & next, being already assigned ans by reference
            # unless node / next var is assigned an entirely new value, they would both point to ans's value in memory
            for i in range(1, i + 1):
                node = node.next
            while node is not None:
                node = node.next
                next = next.next
            next.next = next.next.next
            return ans.next # exclude dummy head

        # works perfectly for singly-linked listnodes
        # reset node's value to next's value, then set node's .next to next's .next
        def deleteNode(self, node):
            if node is None or node.next is None: return
            nextNext = node.next.next
            node.value = node.next.value
            node.next = nextNext
        
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            if head is None or head.next is None: return head
            node = head
            while node.next is not None:
                if node.value == node.next.value:
                    node.next = node.next.next
                else: node = node.next
                # else statement this time, forces iteration to stay with current node until all in-line duplicates are removed
            return head
        
        def reverse(self, head: ListNode) -> ListNode: # override
            prev = None; node = head; next = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev # new head
        
        def reverse(self, head: ListNode) -> ListNode: # override
            node = None
            while head is not None:
                next = head.next
                head.next = node
                node = head
                head = next
            return node # new head


        # todo: End of set of Alt (3rd-Party) Logic Samples


    def reverse(self, l: LinkedList): 
        node = l.head
        next = l.head.next
        l.head = l.tail
        l.tail = l.head
        node.next = None
        while next:
            tmp = next.next
            next.next = node
            node.prev = next
            node = next
            next = tmp

    def merge(self, l1: LinkedList, l2: LinkedList) -> LinkedList: 
        
        # sorted - O(a + b ~ n) t (n - length of longer list) ; O(a + b ~ n) s (creating a newly merged linked-list)

        node, l1_node, l2_node = ListNode(0), l1.head, l2.head
        dummy = node; i = 0

        while l1_node and l2_node:
            if l1_node.value <= l2_node.value:
                node.next = l1_node
                l1_node = l1_node.next
            else:
                node.next = l2_node
                l2_node = l2_node.next
            node = node.next # crucial shift, or the merged list would stay at only 1 node iteration throughout loop
            i += 1
        if l1_node: # if-check is unnecessary (while check is enough)
            while l1_node:
                node.next = l1_node
                l1_node = l1_node.next
                node = node.next
                i += 1
        while l2_node:
            node.next = l2_node
            l2_node = l2_node.next
            node = node.next
            i += 1
        
        # now, construct a new linked list, remove dummy head, then return it
        ll = DataStructures.LinkedList(h=dummy, t=node.next, l=i)
        ll.remove_head()
        return ll

        # unsorted - O(sorting ll - ?) + O(a + b) t ; O(sorting ll - ?) + O(1) s
        
        # TODO
        
    def merge_k_lls(self, ks: List[LinkedList]) -> LinkedList:
        if len(ks) == 0: return None

        def find_min(arr):
            found = min(arr) # O(?) t
            # arr.remove(found) # removes, but doesn't return value
            min_val = arr.pop(arr.index(found)) # this pops it out, but has to find the index 1st
            # find out O(?) ts for both options

            return min_val
        
        def should_loop(nodes):
            for n in nodes:
                if n is not None: return True
            return False


        # sorted - O(kn) t ; O(n) s (n - longest ll's length)

        dummy = ListNode()
        ll = DataStructures.LinkedList(h=dummy)
        ll_node = ll.head
        nodes = [l.head for l in ks]
        min = ListNode(v=sys.maxsize)

        while should_loop(nodes):
            # finding min value before comparing - waste of t
            # arr = [n.value for n in nodes] 
            # min_value = find_min(arr)
            found_index = 0
            for i, n in enumerate(nodes):
                if n and n.value <= min.value:
                    min = n; found_index = i
            ll_node.next = min
            ll_node = ll_node.next
            min = min.next
            # replace min-value node in nodes, before resetting min node
            nodes[found_index] = min # nodes.replace()
            min = ListNode(v=sys.maxsize)
        ll_node.next = None
        ll.tail = ll_node
        # ll.head = ll.head.next
        ll.remove_head()
        return ll
        
        
        # unsorted - 
    
        # TODO
        

    def add(self, l1, l2): # O() t ; O() s
        pass # TODO
        
    def add_nums(self, l1, l2): # O() t ; O() s
        pass # TODO
        
    def add_2_nums(self, l1, l2): # O(n) t (n - length of longer list); O(n) s (creating a newly summed linked-list)

        # both are singly-linked lists, each having a number's digits in reverse order (123 = 3 -> 2 -> 1)
        # regular addition of 2 numbers with multiple digits is already done in reverse order, 
        # with n > base 10's extra digit carried over as a multiple of 10 (10, 100, 1000, ...) to the next 

        l1, l2, ls = l1.head, l2.head, ListNode()
        s = c = 0 # todo: s & c would be set by reference on abstract objects (and primitive arrays, dicts, etc), but not the most basic primitive literals (like int 0)
        ll = DataStructures.LinkedList(h=ls)
        while l1 or l2:
            s = int(l1.value if l1 and l1.value else 0) + \
                int(l2.value if l2 and l2.value else 0) + c
            if len(f"{s}") > 1:
                ls.value = int((f"{s}")[-1]) # or s % 10
                c = int((f"{s}")[::-1]) # or s / 10
            else:
                ls.value = s
                c = 0
            ls.next = ListNode()
            l1, l2, ls = l1.next, l2.next, ls.next
        if c > 0: ls.value = c
        else: ls = None # remove the last empty ls node
        return ll


    # todo: Test next set of Alt (3rd-Party - Tutorials) Logic Samples


    def merge(self, l1: LinkedList.ListNode, l2: LinkedList.ListNode) -> LinkedList.ListNode:
        node = ListNode(0); dummy = node
        while l1 and l2:
            if l1.value > l2.value:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next
        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next
        return dummy.next # exclude the dummy from list first, if required
        
    def mergeKlls(self, ks: List[LinkedList.ListNode]) -> LinkedList.ListNode:
        if len(ks) == 0: return None

        def merge2lls(l1, l2):
            node = ListNode(0)
            ans = node

            while l1 and l2:
                if l1.value > l2.value:
                    node.next = l2
                    l2 = l2.next
                else:
                    node.next = l1
                    l1 = l1.next
                node = node.next

            while l1:
                node.next = l1
                l1 = l1.next
                node = node.next

            while l2:
                node.next = l2
                l2 = l2.next
                node = node.next

            return ans.next
        
        i = 0; last = len(ks) - 1; j = last

        while last != 0:
            i = 0; j = last
            while j > i:
                ks[i] = merge2lls(ks[i], ks[j])
                i += 1; j -= 1; last = j
        return ks[0]
    
    def add2Nums(self, l1, l2): 
        ans = DataStructures.LinkedList.ListNode()
        node = ans
        s = c = 0 # todo: s & c would be set by reference on abstract objects (and primitive arrays, dicts, etc), but not the most basic primitive literals (like int 0)
        while l1 or l2:
            s = c
            if l1:
                s += l1.value
                l1 = l1.next
            if l2:
                s += l2.value
                l2 = l2.next
            c = int(s / 10)
            node.next = ListNode(s % 10)
            node = node.next
        if c > 0: node.next = ListNode(c)
        return ans.next # leave out dummy head


    # todo: End of set of Alt (3rd-Party) Logic Samples


    # Stacks

    class Stacks:

        class Stack:

            def __init__(self):
                self.stack = []
            
            def stack(self):
                return self.stack
            
            def push(self, v):
                self.stack.append(v)
            
            def top(self):
                if self.len() > 0:
                    return self.stack[-1] # return last item, without removing
                return None

            def pop(self):
                if self.len() > 0:
                    return self.stack.pop() # remove last item (LIFO) | Queue .pop(0) - 1st elem
                return None

            def len(self):
                return len(self.stack)

            def find_min(self): # O(n) t ; O(1) s
                # todo: O(1) t - if min/max is monitored on every push/pop
                if self.len() == 0: return None
                min_ = sys.max_size
                for _, v in enumerate(self.stack[::-1]): # iterate from behind for 'stack' (not required)
                    if v < min_: min_ = v
                return min_


        def __init__(self):
            self.stack = DataStructures.Stacks.Stack()
        
        # Other Methods

        def find_min(self): # O(n) t ; O(1) s
            if self.stack.len() == 0: return None
            min_ = sys.max_size
            for _, v in enumerate(self.stack.stack()[::-1]): # iterate from behind for 'stack' (not required)
                if v < min_: min_ = v
            return min_
        
        # Given a string that can contain (, ), {, }, [, and ], check if it is valid
        # (parentheses are arranged in standard order, with no overlaps)
        # Any open brackets must be closed by the same type of brackets
        # Open brackets must be closed in the correct order

        def valid_parenthesis(self, s):
            '''
            Check if string s has valid enclosing parentheses: () / {} / []
            your eg. " [ ... ( ... ' ${} ' ... ) ... ] " - if any parenthesis mixes up 'syntactical-order': not_valid
            actual eg. "[({})]" (no extra chars in string, except for the different types of parentheses)
            Better to use a stack here (instead of an array) so you can lifo-pop items to compare with string characters
            stack's i is 1st half-char of parenthesis, string's c is 2nd half-char
            '''

            def is_parenthesis(c1, c2): # check for all kinds of parentheses
                if (c1 == '(' and c2 == ')') \
                    or (c1 == '[' and c2 == ']') \
                    or (c1 == '{' and c2 == '}'):
                    return True
                return False

            # * Init new stack obj to use
            stack = DataStructures.Stacks.Stack()
            for c in s:
                if stack.len() != 0:
                    i = stack.top() # check top 1st, then pop if is_parenthesis()
                    if is_parenthesis(i, c):
                        stack.pop() # take out the last item
                        continue
                stack.push(c)

            return stack.len() == 0 # is_valid if all items in stack have been popped out
        
        # DFS - Pre/In/Post-Order Traversals (with Stack-Iteration, without recursion)
        def binary_tree_dfs(self, tree: 'DataStructures.Tree'): 
            if tree.root is None: return
            
            stack = DataStructures.Stacks.Stack()
            node = tree.root

            while node or stack.len() > 0: 

                # Pre-Order Traversal

                if node:
                    print(node.value)
                    stack.push(node)
                    node = node.left
                else:
                    node = stack.pop()
                    node = node.right
                
                # In-Order Traversal

                if node:
                    stack.push(node)
                    print(node.value)
                    node = node.left
                else:
                    node = stack.pop()
                    node = node.right
                
                # Post-Order Traversal - .right to .left

                if node:
                    print(node.value)
                    stack.push(node)
                    node = node.right
                else:
                    node = stack.pop()
                    node = node.left

                ''' # if N-ary Tree (3+ children)
                for c in node.children:
                    queue.enqueue(c)
                # todo: decide when to work with node.value during loop 
                # (for pre/in/post - orders)
                '''
        
        # todo: Alt 3rd-Party (Tutorial) Logic
        def binary_tree_dfs(self, root: 'DataStructures.Tree.TreeNode'): # O(n) t ; O(1~n) s (explanation of 1~n s in Tree Class's DFS - Stack Iteration algo)
            
            # DFS - Post-Order Traversal - 2-Stack-Iteration method (without 'recursion')
            
            '''
            While popping out & working with Stack 1's current iteration node,
            Push it to Stack 2, and its children to Stack 1, for next iterations

            After Stack 1's loop, pop out all nodes from Stack 2
            LIFO pop from Stack 2 logic is for DFS Post-Order Traversal
            ''' # TODO: Visualize entire algo with tree and 2 stacks to understand better
            # lifo popping out last item of s1, while appending n1's children from left to right ..
            # plus lifo popping out last item of s2 after s1's loop is what achieves DFS Post-Order

            ans = []
            if not root: return ans

            s1, s2 = [], []
            s1.append(root)

            while s1:
                n1 = s1[-1]
                s1.pop()
                s2.append(n1)
                if n1.left: s1.append(n1.left)
                if n1.right: s2.append(n1.right)
            
            while s2:
                n2 = s2[-1]
                s2.pop()
                ans.append(n2.value)
            
            return ans
        
        # TODO: 
        def binary_tree_bfs(self, root: 'DataStructures.Tree.TreeNode'):
            
            # BFS - Post-Order Traversal - Stack-Iteration method (without 'Queues', not 'recursion' like with DFS)
            
            ''' # By "BFS Post-Order Traversal" .. 
            # assume question is asking for "BFS Right-to-Left Level-Order Traversal"
            # and not "DFS Post-Order Traversal", because of the "Post-Order" term

            While popping out & working with Stack 1's current iteration node,
            Push it to Stack 2, and its children to Stack 1, for next iterations

            After Stack 1's loop, pop out all nodes from Stack 2
            LIFO pop from Stack 2 logic is for Post-Order Traversal
            ''' # TODO: Implement Left to Right BFS Level-Order Traversal with 2 Stacks (if the 2nd Stack is required)
            # TODO: If Possible, Ponder on Pre & In - Order Traversals, but with BFS (not DFS) this time

            # TODO
            pass


    # Queues

    class Queues:

        class Queue: # * Works as a Double-Ended Queue (can enqueue/dequeue from both beginning & end)

            def __init__(self):
                self.queue = [] # or deque()
            
            def queue(self):
                return self.queue
        
            def len(self):
                return len(self.queue)

            def print(self):
                print(f"Queue - {self.queue}")
            
            def first(self):
                if self.len() > 0:
                    return self.queue[0] # return 1st item, without removing
                return None
            
            def last(self):
                if self.len() > 0:
                    return self.queue[-1] # return last item, without removing | deque[-1] 
                return None
            
            def enqueue(self, v):
                self.queue.append(v) # insert item to end of queue | deque - .append(v)
            
            def dequeue(self):
                if self.len() > 0:
                    return self.queue.pop(0) # remove first item (FIFO) | deque .popleft()
                return None

            def find(self, index=-1):
                if index < self.len():
                    return self.queue[index] # return item item, without removing
                return None
            
            # * Only works well if items are unique (no repetitions)
            def find(self, value=None): # return index of v
                try: return self.queue.index(value) # deque - convert to list 1st, then .index()
                except: return -1 # returns ValueError if v isn't in queue
            

            # * Other Methods
            

            def dequeue(self, value=None):
                if value and self.len() > 0:
                    i = self.find(value=value)
                    if i > -1: # valid index (.find only returns valid indices, or -1 - for None/Errors)
                        # * deque - .remove(value) straight-away;
                        return self.queue.pop(i) # so out-of-bounds exception will never be called # todo: optimize
                        # self.dequeue_at(i) will also .find(index=) before dequeueing, so call .pop(i) directly
                return None
            
            def enqueue_first(self, v):
                self.queue.insert(0, v) # insert item to beginning of queue | deque - .appendleft(v)
            
            def dequeue_last(self):
                if self.len() > 0:
                    return self.queue.pop() # remove last item (Forced LIFO) | deque - .pop()
                return None
            
            def enqueue_at(self, i, v):
                if i < self.len():
                    self.queue.insert(i, v) # insert item to index of queue | deque - .appendleft(v)
                return False

            def dequeue_at(self, i):
                if self.find(index=i):
                    return self.queue.pop(i) # remove ith item | del self.queue[index] | deque - convert to list, delete at index, then convert back to deque
                return None


        def __init__(self):
            self.queue = DataStructures.Queues.Queue()
        
        # Other Methods

        # BFS - Level-Order Traversal (with Queue-Iteration)
        def binary_tree_bfs(self, tree: 'DataStructures.Tree'): 
            if tree.root is None: return
            
            queue = DataStructures.Queues.Queue()
            queue.enqueue(tree.root)

            while queue.len() > 0:
                node = queue.dequeue()
                print(node.value)
                
                # .left - side to .right - side

                if node.left: queue.enqueue(node.left)
                if node.right: queue.enqueue(node.right)
                ''' # if N-ary Tree (3+ children)
                for c in node.children:
                    queue.enqueue(c)
                '''

                # Reverse-order - .right - side to .left - side

                if node.right: queue.enqueue(node.right)
                if node.left: queue.enqueue(node.left)
                ''' # N-ary Tree
                for c in node.children[::-1]:
                    queue.enqueue(c)
                '''
        
        # todo: Alt 3rd-Party (Tutorial) Logic
        def binary_tree_bfs(self, root: 'DataStructures.Tree.TreeNode') -> List[List[int]]:
            ans = []
            if root is None: return ans

            q = deque([root])

            while q:
                tmp = []

                # todo: this time, first work with all current-level items in queue
                for i in range(0, len(q)):
                    node = q.popleft()

                    # work with n.value, before / after appending children
                    tmp.append(node.value) # in this case, add to tmp array, to be added in bulk to ans array after this loop

                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    # enqueue all the next level items, while working with this current level

                if len(tmp) > 0:
                    ans.append(tmp[:]) # append the tmp (current tree level / height) array of current level's items
                    tmp.clear()
            
            return ans
        
        # BFS - ZigZag Level-Order Traversal (with Queue-Iteration)
        # left to right in 1 layer, then right to left in next layer
        def binary_tree_zigzag_bfs(self, tree: 'DataStructures.Tree'): 
            
            # enqueue left to right, then right to left
            # or enqueue in 1 direction, then dequeue first item, then last item

            if tree.root is None: return None

            ans, reverse = [], False
            queue = DataStructures.Queues.Queue()
            queue.enqueue(tree.root)

            while queue.len() > 0:
                tmp = []
                
                # todo: this time, firstly working with all current-level items in queue, makes zig-zag traversal easier
                # reverse direction after each level's iteration

                for i in range(0, queue.len()):
                    node = queue.dequeue() # remove 1st fifo item
                    tmp.append(node.value)

                    ''' # longer checks required, to check if .left / .right exists, before enqueueing
                    queue.enqueue(node.left if not reverse else node.right)
                    queue.enqueue(node.right if not reverse else node.left)
                    '''

                    if reverse:
                        if node.left: queue.enqueue(node.left)
                        if node.right: queue.enqueue(node.right)
                    else: # this time, enqueue from right to left
                        if node.right: queue.enqueue(node.right)
                        if node.left: queue.enqueue(node.left)
                    
                    # todo: or, enqueue in 1 direction, but dequeue from (fifo) start / (lifo) end, based on reverse bool
                    # wouldn't be exact zig-zag; in reverse-order lifo dequeues with left->right enqueues would have many mini-zags (with 1 zig in non-reverse order - vice versa)
                
                if len(tmp) > 0:
                    ans.append(tmp[:])
                    tmp.clear()
                    reverse = not reverse
            
            return ans
        
        # todo: Alt 3rd-Party (Tutorial) Logic
        def binary_tree_zigzag_bfs(self, root: 'DataStructures.Tree.TreeNode') -> List[List[int]]: 
            ans = []
            if not root: return ans

            zigzag = False
            q = deque()
            q.append(root)

            while q:
                tmp = []
                for _ in range(len(q)):

                    '''
                    in this case, in non-reverse order, fifo pop, enqueue to end, from left to right
                    in reverse order, lifo pop, enqueue to start, from right to left
                    '''

                    if zigzag:
                        node = q.pop()
                        tmp.append(node.value)
                        if node.right: q.appendleft(node.right)
                        if node.left: q.appendleft(node.left)
                    else:
                        node = q.popleft()
                        tmp.append(node.value)
                        if node.left: q.append(node.left)
                        if node.right: q.append(node.right)
                
                if len(tmp) > 0:
                    ans.append(tmp)
                    zigzag = not zigzag
            
            return ans


    # Heaps (max & min)
    

    # Binary Heaps


    # Priority Queues


    # Trees

    class Tree: # Acyclic Undirected Graph - a tree if connected, and a forest if not connected
            
        class TreeNode:

            def __init__(self, v=None, l=None, r=None, c=[], p=None):
                self.value = v
                self.left = l
                self.right = r
                self.parent = p # for bi-directed tree-nodes
                self.children = c # for more than 2 children
                self.depth = None # length of the path from the tree root-node to this node
        
            def add_child(self, n: 'DataStructures.Tree.TreeNode'): # * using a Forward Reference for the current class as an argument's data type
                # using a string containing the class name as a type hint, when defining methods that take or return instances of the same class
                
                self.children.append(n)
            
            def add_left(self, n):
                self.left = n
                n.parent = self # todo
            
            def add_right(self, n):
                self.right = n
            
            def add_parent(self, n):
                n.add_child(self)
                self.parent = n
    
            def print(self, level=0):
                print("  " * level, self.value)
                # self.print_tree(self.left, level = level + 1)
                # self.print_tree(self.right, level = level + 1)
                # or
                for child in self.children:
                    self.print_tree(child, level = level + 1)
        
        def __init__(self, n: TreeNode):
            self.root = n
            self.height = 1 # length of the longest path from the root to a leaf node
            # todo: depth - height (less the 1st root node) from root node to any given node
        
        def set_root(self, n):
            n.left = self.root.left
            n.right = self.root.right
            n.children = self.root.children
            self.root = n
            # * don't increment height - self.height += 1 
        
        def add_root(self, n): # add new root on top of old
            n.add_child(self.root)
            # todo: set old root to n's left or right child
            # if using BST child class, .left if old_root.value < n.value else .right
            self.root = n
            self.height += 1
        
        def print(self):
            self.print_tree(self.root)
    
        def print_tree(self, root, level=0):
            print("  " * level, root.value)
            for child in root.children:
                self.print_tree(child, level = level + 1)

        def print_tree(self, root, indent=''):
            # Print the current noode's value
            print(indent + str(root.value))

            # Recursively print each child with appropriate indentation
            for i, child in enumerate(root.children):
                if i < len(root.children) - 1:
                    print(indent + '├── ', end='')
                else:
                    print(indent + '└── ', end='')
                self.print_tree(child, indent = indent + '│   ')
        
        def print_tree(self, root, indent='', last=True):
            print(indent, end='')
            if last:
                print('└── ', end='')
                indent += '    '
            else:
                print('├── ', end='')
                indent += '│   '

            print(root.value)

            # Recursively print each child with appropriate indentation
            child_count = len(root.children)
            for i, child in enumerate(root.children):
                self.print_tree(child, indent=indent, last = i == child_count - 1)


        '''
            breadth - first search
            code (value) - first (binary) search
            depth - first search
        ''' 


        # BFS / Level-Order Traversal
        def bfs(self, root): #  # O(n) t ; O(1 ~ n) s

            '''
            O(n) s argument due to Queue usage
            but O(1) t to both enqueue & dequeue, so queue's length is increased & decreased constantly
            if Binary Tree, queue's enqueued 2x, dequeued once, making O(n/2) s ~ O(n) s (removing constant term 1/2)
            if N-ary Tree, queue's enqueued n-ary times (avg number of children per node), dequeued once, making (n / n-ary) s ~ O(n) s
            but by algo's end, queue is emptied, making O(1) s
            # todo: keep researching on this argument
            '''

            if root is None or type(root) is not DataStructures.Tree.TreeNode:
                return
            
            '''
            BFS always traverses horizontally (whether from left/right first), layer by layer
            '''

            # BFS  - Queue - Iteration
            # * uses queue in while loop

            queue = deque() # DoubleQueue ('Deque')
            queue.append(root) # or = deque([root])

            while queue: # No pre/post/in - order in BFS

                node = queue.popleft() # queue - fifo, so pop oldest item (no .popright())
                print(node.value)

                # BFS "Straight" order - .left to .right
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                for child in node.children:
                    queue.append(child)
        
                # NB: BFS "Reverse" - order - .right to .left
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
                for child in node.children[::-1]:
                    queue.append(child)
        
        # todo: binary-search through BSTs only
        def cfs(self, root=None, cb: function=None): # O(log n) t ; O(1) s
            if root is None or cb is None: return None

            # TODO: implement .is_BST() validation
            # if not DataStructures.Tree.is_BST(root): return None

            # Option 1 - Recursion

            while root is not None and root.value is not None:
                res = cb(root)
                if res == 'l': self.cfs(root.left, cb) # todo: or root = root.left (iteration method)
                elif res == 'r': self.cfs(root.right, cb) # todo: or root = root.right (iteration method)
                else: return res # or root / root.value
            
            # Option 2 - Iteration

            res = cb(root) # todo: cb() should return node or node.value being searched
            # or 'l' or 'r' for traversal only (direct search in next method option)
            while root and root.value != res:
                if res == 'l': root = root.left
                elif res == 'r': root = root.right
                res = cb(root)
            return res
        
        def cfs(self, root=None, v: int=None):
            if root is None or v is None: return None

            def iteration(root, v):
                while root and root.value != v:
                    if root.value > v: root = root.left
                    else: root = root.right
                return root
            
            def recursion(root, v):
                if root.value == v: return root
                elif root.value > v: return recursion(root.left, v)
                else: return recursion(root.right, v)
            
            print(iteration(root, v))
            print(recursion(root, v))
        
        def dfs(self, root, order='pre-order'):
            if root is None: return

            if order == 'pre-order': print(root.value)
            self.dfs(root.left)
            if order == 'in-order': print(root.value)
            self.dfs(root.right)
            if order == 'post-order': print(root.value)

            ''' # in this case, consider ways of working with root.value around/within loop
            for child in root.children:
                self.dfs(child)
            ''' # TODO: Also check different dfs scenarios in override below 
        
        def dfs(self, root): # O(n) t ; O(1) s
            # * uses recursion
            if root is None or type(root) is not DataStructures.Tree.TreeNode:
                return
            
            '''

            DFS always traverses from top-bottom nodes (whether from left/right first)
            but works with each tree/sub-tree (triangular node-family, with 1 parent) in a specific order (pre/in/post)
            Visualize traversals here: https://tree-visualizer.netlify.app/
            
            Pre/In/Post-Orders always transcend through all trees/sub-trees
            whether outermost tree, or in-between, or innermost sub-trees

            eg. for the entire tree (no matter the size):
            Post-order left-before-right:
            For the outermost tree / triangular node-family (surrounding the entire tree):

            (Top) Root node will always be traversed through first
            (Bottom) left-most node will always be worked with (or used) first
            aside all other DFS post-order traversals and node usages in-between (with inner sub-trees)
            (Bottom) right-most node will be worked with next
            aside all other DFS post-order traversals and node usages in-between (with inner sub-trees)
            (Top) Root node will always be worked with (or used) last
            (despite it being always traversed through first)

            # TODO: Try out this logic for other scenarios:
            (tree size/height/depth) / (pre/in-orders) / (right-before-left) / (other sub-trees)

            '''

            # DFS pre-order - Recursive traversal
            print(root.value)
            self.dfs(root.left)
            self.dfs(root.right)
            for child in root.children:
                self.dfs(child)

            # DFS post-order - Recursive traversal
            self.dfs(root.left)
            self.dfs(root.right)
            for child in root.children:
                self.dfs(child)
            print(root.value)

            # DFS in-order - Recursive traversal
            self.dfs(root.left)
            print(root.value)
            self.dfs(root.right)
            # consider in-order with root.children

            # todo: NB: DFS "Reverse" pre/post/in - order too - .right before .left or reverse .children

            # TODO: test these extra options

            # Traverse all children
            for child in root.children:
                self.dfs(child)
            print(root.value)

            # Traverse all children, except last child
            for i in range(len(root.children) - 1):
                self.dfs(root.children[i])
            print(root.value)
            
            # Traverse last child only
            if root.children:
                self.dfs(root.children[-1])
            print(root.value)


            # Stack - Iteration Tree-Traversals (all .left to .right, except post-order)
            
            # O(n) t ; O(h ~ 1) s (h - max height)
            
            # Stack takes in nodes until max-height h, and pops them out alongside algo; doesn't maintain all nodes for algo's exec
            # List (despite n - total) is only used to record traversed values to be returned, not within algo's actual complexity
            # could do away with List by just printing out node.value()s


            # DFS pre-order - Stack - Iteration - O(1 ~ n) s

            '''
            O(n) s argument due to Stack usage
            but O(1) t to push & O(1 ~ n) t to pop, so stack's length is increased & decreased constantly
            if Binary Tree, stack's pushed into 2x, popped once, making O(n/2) s ~ O(n) s (removing constant term 1/2)
            if N-ary Tree, stack's pushed into n-ary times (avg number of children per node), popped once, making (n / n-ary) s ~ O(n) s
            but by algo's end, stack is emptied, making O(1) s
            # todo: keep researching on this argument
            '''

            stack, node = [], root

            while node or len(stack) > 0:
                if node:
                    print(node.value)
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    node = node.right

            # DFS in-order - Stack - Iteration
            stack, node = [], root

            while node or len(stack) > 0:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    print(node.value)
                    node = node.right

            # DFS post-order - Stack - Iteration - .right to .left
            stack, node = [], root

            while node or len(stack) > 0:
                if node:
                    print(node.value)
                    stack.append(node)
                    node = node.right
                else:
                    node = stack.pop()
                    node = node.left
            

        # Iterator Traversals

        class DFS_Iterator_Traversal:

            def __init__(self, root: 'DataStructures.Tree.TreeNode'):
                self.node = root
                self.stack = []
            
            def has_next(self): self.node or len(self.stack) > 0

            def next(self):
                while self.has_next():
                    if self.node:
                        self.stack.append(self.node)
                        self.node = self.node.left
                    else:
                        self.node = self.stack.pop()
                        res = self.node.value
                        self.node = self.node.right
                        return res
                return sys.maxsize
            
            def test(self):
                it = DataStructures.Tree.Iterator()
                print(it.next())
                print(it.next())
                print(it.has_next())
                print(it.next())
                print(it.next())
                print(it.has_next())


        def diameter(self): # O() t ; O() s
            # TODO
            pass

        def max_depth_or_height(self): # O() t ; O() s
            # TODO
            pass

        @staticmethod
        def is_BST(self): # O() t ; O() s
            # TODO
            pass

        def lowest_common_ancestor(self): # O() t ; O() s
            # TODO
            pass

        def unique_paths(self): # O() t ; O() s
            # TODO
            pass

        # TODO: Test

        def tests(self):
            root = DataStructures.Tree.TreeNode(4)
            root.left = DataStructures.Tree.TreeNode(5)
            root.right = DataStructures.Tree.TreeNode(6)
            root.left.left = DataStructures.Tree.TreeNode(7)
            root.print()
            # 
            self.print_tree(root)


    # Binary (Search) Trees

    class BTree(Tree): # only 2 (.left & .right) children
        
        def __init__(self, n=None):
            super().__init__(n)
        
        def is_symmetric(self): # O(~ n) t (check may complete early) ; O(1) s
            
            # TODO: New concept - O(log n) s (for a balanced tre)e / O(n) s (due to recursive calls)
            # since we can't tell if tree is "passive" or not

            if self.root is None: return
            root = self.root
            if not (root.left and root.right):
                return True # only self.root node
            if not root.left \
                or not root.right \
                or root.left.value != root.right.value:
                return False
            
            is_symmetric = True
            
            ''' # todo: Recursion-wise
                Best to keep the base-case checks on the current args' state
                then recurse to next state

                instead of checking base-case on the next args' state (recursive call)
            '''
            def check(n1, n2):
                ''' # todo: double & single - based checks
                    Best to check double case 1st [(not) (x and y)]
                    then check both single cases [(not) x or (not) y]
                '''
                if not (n1 and n2): return True
                if not n1 \
                    or not n2 \
                    or n1.value != n2.value: 
                    return False
                
                is_symmetric = True # won't have to reset is_symmetric to True, if it already was
                # also won't have to return a boolean since "global" is_symmetric is the final return value
                
                # if construct pre-empting recursion before reaching base-case
                if not check(n1.left, n2.right) \
                    or not check(n1.right, n2.left):
                    return False
                
                return True

            is_symmetric = check(root.left, root.right)
            
            def check2(n1, n2):
                if not (n1 and n2): 
                    is_symmetric = True # won't have to reset is_symmetric to True, if it already was
                    return
                if not n1 \
                    or not n2 \
                    or n1.value != n2.value: 
                    is_symmetric = False
                    return
                
                is_symmetric = True # won't have to reset is_symmetric to True, if it already was
                # no need for if-check pre-empt because above base-case checks are enough
                
                check2(n1.left, n2.right)
                check2(n1.right, n2.left)

            check2(root.left, root.right)

            # todo: Alt / 3rd-Party (Tutorial) Logic
            def check3(n1, n2):
                if n1 is None and n2 is None:
                    return True
                if n1 is None or n2 is None:
                    return False
                
                return (n1.value == n2.value) \
                    and check3(n1.right, n2.left) \
                    and check3(n1.left, n2.right)
                
            is_symmetric = check3(root, root)

            return is_symmetric
        
        def maximum_depth_of_value(self, v): # O(n) t ; O(h) s (height of tree, due to recursive calls with new argument variables d)
            if self.root is None: return None

            depth = 0 # 0 for root height, 1 for root's child's height
            
            # pass in depth, because it'll be incremented 1st on the root's child's recursive call
            def dfs_depth_1(node, d): 
                if node is None: return -1 # no depth (value v not found)
                if node.value == v:
                    # todo: Option 1 - if return value is required
                    # return all recursive calls too
                    return d # so incremented d's current value is returned to base/1st call
                
                    # todo: Option 2 - in case return value isn't required, 
                    # NB: also can't update d-2-depth directly because (int) depth isn't passed by reference
                    # depth = d # increment "global" depth var
                    # return # then just return
                
                # todo: can't return both simult, so would have to check 1st recursive calls' value before 2nd
                # unnecessary, so Option 2 - better
                # * could return both together if boolean return values (with and/or conditions)
                return dfs_depth_1(node.left, d + 1)
                return dfs_depth_1(node.right, d + 1)

            # in case return value isn't required, increment depth var inside recursive function
            depth = dfs_depth_1(self.root, depth)

            depth = 0

            def dfs_depth_2(node, d):
                if node is None: return
                if node.value == v:
                    depth = d
                    return
                dfs_depth_2(node.left, d + 1)
                dfs_depth_2(node.right, d + 1)
            
            dfs_depth_2(self.root, depth)

            return depth

        def maximum_depth(self): # O(n) t ; O(1) s (no tree-height space, h required, due to recursive calls with new argument variables d)
            # unlike the previous method .maximum_depth_of_value(...)

            d = -1 # can start at -1, so root's depth is 0
            if self.root is None: return d

            # -1 is returned, if self.root is None
            def dfs_depth(node):
                if node is None: return
                d = d + 1 # d is incremented directly here (so O(1) space - no recursive variable is created ; only node - object passed in by reference)
                dfs_depth(node.left)
                dfs_depth(node.right)

            dfs_depth(self.root)
            return d

        # 3rd-Party (Tutorial) Logic - Self-method recursion
        def maximum_depth(self, node):
            if node is None: return 0
            if node.left is None \
                and node.right is None:
                return 1
            
            left = self.maximum_depth(node.left)
            right = self.maximum_depth(node.right)

            return max(left, right) + 1 # + 1 for the current node

        # Find if a root to any sub-node path exists where sum of path's node values equals target
        def path_sum(self, target):
            if self.root is None: return None

            found = False

            def dfs_path_sum(node, s):
                if node is None: return None
                s += node.value # increment s before check & recursive calls
                if s == target:
                    found = True
                    return node
                dfs_path_sum(node.left, s)
                dfs_path_sum(node.right, s)
                
                return None

            tail = dfs_path_sum(self.root, 0) # or return boolean found
            return DataStructures.LinkedList(self.root, tail) if tail else None
        
        # 3rd-Party (Tutorial) Logic
        # This time, root to any leaf-node
        def path_to_leafsum(self, target): # O(n) t ; O(n) s (recursive calls with args' new memory)
            if self.root is None: return None

            def is_leaf(node):
                return not (node.left and node.right)

            def has_sum(node, t, s):
                if node is None: return False
                s += node.value
                if s == t and is_leaf(node):
                    return True
                
                return (
                    has_sum(node.left, t, s) or \
                    has_sum(node.right, t, s)
                )
            
            return has_sum(self.root, target, 0)
        
        # TODO: Visualize logic before understanding
        def lowest_common_ancestor(self, node1, node2): # O(n) t ; O(1) s (no extra vars created in recursion; only 2 target node vars)
            if self.root is None: return None
            
            def lca(node, n1, n2):
                if node is None: return None
                if node.value == n1.value \
                    or node.value == n2.value:
                    return node

                # Divide
                left = lca(node.left, n1, n2)
                right = lca(node.right, n1, n2)

                # Conquer
                if not (left and right): return None
                if left and right: return node # lca - recursive returns eventually meet at lca node
                return left if left else right
                # todo: since valid left & right nodes keep getting returned, after 'Divide'
                # their returns will eventually meet at the lca node
                
                ''' # TODO: Compare with main .java file LCA
                // Conquer
                if (left == null && right == null)
                    return null;
                if (left != null && right != null)
                    return root;
                if (left != null) return left;
                if (right != null) return right;

                return null;

                3rd-Party pseudo
                if !left -> return right
                return left
                '''
            
            return lca(self.root, node1, node2)

        def kth_smallest_elem(self, kth): # O(n^2) t ; O(log n) s (in a balanced tree) / O(n) s (due to recursion)
            if self.root is None: return None

            def kth_smallest(node, k):
                # if node is None: return None
                count_nodes = lambda n: 0 if n is None else \
                    1 + count_nodes(n.left) + count_nodes(n.right)

                count = count_nodes(node.left)
                if count + 1 == k: return node
                elif count + 1 > k:
                    return kth_smallest(node.left, k)
                elif count + 1 < k: 
                    return kth_smallest(node.right, k - 1 - count)
                
                return -1

            return kth_smallest(self.root, kth)
        
        def serialize(self): # O(n) t ; O(n) s (recursion)
            if self.root is None: return 'X#'

            def serialize(node):
                if node is None: return 'X#'
                left = serialize(node.left)
                right = serialize(node.right)
                return str(node.value) + '#' + left + right
                
            return serialize(self.root)

        def deserialize(self, data): # O(n) t ; O(n) s (recursion)
            
            def deserialize():
                value = next(data)
                if value == 'X': return None
                node = DataStructures.Tree.TreeNode(int(value))
                node.left = deserialize()
                node.right = deserialize()
                return node
            
            data = iter(data.split('#'))
            return deserialize()
        
        # TODO: Visualize logic before understanding
        def maximum_path_sum(self):
            if self.root is None: return None

            ans = float('inf')

            def max_path_sum(node):
                if node is None: return 0

                left = max_path_sum(node.left)
                right = max_path_sum(node.right)

                max_side = max(
                    node.value,
                    node.value + max(left, right)
                )
                max_top = max(
                    max_side,
                    node.value + left + right
                )

                ans = max(ans, max_top)
                return max_side

            max_path_sum(self.root)
            # ans is updated within recursive function
            return ans
        
    class BST(Tree): # .left.value <= .value <= .right.value (vice versa)
        
        def __init__(self, n=None):
            super().__init__(n)
        
        def add_root(self, n): # add new root on top of old
            if not self.root:
                self.root = n
                return

            # todo: decide on whether to .insert(n.value) if n.value == self.root.value
            # or whether to go straight ahead and add it as a new root, like when > self.root.value
            if n.value <= self.root.value: self.insert(n.value)
            else: # n.value > self.root.value (new max value in BST): so can insert at BST new root
                n.add_child(self.root)
                # set old root to n's LEFT child because n.value > self.root.value
                n.left = self.root
                self.root.parent = n # set parent to new root, if bi-directional node
                self.root = n
            
            # increment tree-height
            self.height += 1
        
        def find(self, v):
            return self.cfs( # todo: Remember, cfs (code-1st / binary searches) only work on Binary Search Trees
                self.root, 
                cb=lambda root: None if not (root and root.value) \
                    else root if root.value == v \
                    else 'l' if root.value > v \
                    else 'r' # BST left children less values, right children greater values
            )
        
        def insert(self, v):
            node = DataStructures.BST.TreeNode(v)
            if not self.root: # if no root, insert node as root
                self.root = node
                return

            def cb(root):
                if not root: return None

                if root.value == v:
                    print(f"Node with value '{v}' already exists")
                    return root # or - root.value ; not the newly un-added node
                elif not root.left and not root.right: # if root is a leaf-node
                    # add a check for root.children .length
                    node.parent = root # set parent before or after add leaf-node
                    if v < root.value: root.left = node
                    else: root.right = node # v == root.value - already checked
                    
                    print(f"Done with inserting Node({v})")
                    return self.root # not the newly added node
                
                else: # check traverse left/right
                    if root.value > v: return 'l'
                    else: return 'r' # root.value == v - already checked
                    
            return self.cfs(self.root, cb=cb)
        
        # 3rd-Party (Tutorial) Logic
        def insert(self, v):
            if v == self.value:
                print(f"Node({v}) already exists")
            elif v < self.value:
                if self.left: self.left.insert(v)
                else: self.left = DataStructures.BST.TreeNode(v)
            else: # v > self.value:
                if self.right: self.right.insert(v)
                else: self.right = DataStructures.BST.TreeNode(v)

        def remove(self, v):
            if not self.root: return None
            node = None

            def cb(root):
                if not root: return None

                if not root.left and not root.right: # if root is a leaf-node and has value v
                    # add a check for root.children .length
                    if root.value == v:
                        print(f"Leaf Node with value '{v}' exists. Removing ..")
                        node = root; root = None
                    return node # else: node == None
                elif root.value == v:
                    print(f"Node with value '{v}' exists. Removing ..")
                    # todo: also do this with 1-directional tree nodes (no .parent)
                    # remove current node
                    # if 1 child-node, connect its parent to its child 
                    # if 2 children-node, connect its right-child's side's minimum value node in-between its parent and right child itself
                    # by 'minimum' traverse through all left child nodes, from the current node's right child, until left-leaf-node
                    # left-leaf-node will always be higher than current node's value (hence its left child's), keeping the BST binary
                    # todo: NB: All nodes to the right of any node, have greater values than that node's value
                    node = root; parent = root.parent
                    if not root.left: # only root.right child-node
                        if parent.left == root: parent.left = root.right
                        elif parent.right == root: parent.right = root.right
                        # might not need to check for parent.right, but should be explicitly done anyway
                    elif not root.right: # only root.left child-node
                        if parent.left == root: parent.left = root.left
                        elif parent.right == root: parent.right = root.left
                    else: # both root .left & .right children-nodes
                        loop_node = root.right
                        while loop_node and loop_node.left:
                            loop_node = loop_node.left
                        loop_node.left = root.left
                        loop_node.right = root.right
                        if parent.left == root: parent.left = loop_node
                        elif parent.right == root: parent.right = loop_node
                    
                    # when done, delete root and return it as node
                    root = None
                    return node
                else: # check traverse left/right
                    if root.value > v: return 'l'
                    else: return 'r' # root.value == v - already checked
                    
            return self.cfs(self.root, cb=cb)


    # todo: Test next set of Alt (3rd-Party - Tutorials) Logic Samples

    
    def find(self, root: 'DataStructures.BST.TreeNode', v):
        if root is None: return None
        node = root
        if node.value == v: return node
        if node.value < v:
            return self.find(node.right, v)
        return self.find(node.left, v)

    def insert(self, root: 'DataStructures.BST.TreeNode', node: 'DataStructures.BST.TreeNode'):
        if root is None:
            root = node
            return
        if root.value < node.value:
            if root.right is None: root.right = node
            else: self.insert(root.right, node)
        else:
            if root.left is None: root.left = node
            else: self.insert(root.left, node)
    
    def remove(self, root: 'DataStructures.BST.TreeNode', v):
        if root is None: return root
        node = root

        def minTreeValue(node):
            while node.left is not None:
                node = node.left
            return node

        if v < node.value:
            node.left = self.remove(node.left, v)
        elif v > node.value:
            node.right = self.remove(node.right, v)
        else:
            if node.left is None:
                tmp = node.right
                node = None
                return tmp
            elif node.right is None:
                tmp = node.left
                node = None
                return tmp
            tmp = minTreeValue(node.right)
            node.value = tmp.value
            node.right = self.remove(node.right, tmp.value)
        
        return node
    
    def tests(self):
        tree = DataStructures.BST.TreeNode(5)
        self.insert(tree, DataStructures.BST.TreeNode(4))
        self.insert(tree, DataStructures.BST.TreeNode(3))
        self.insert(tree, DataStructures.BST.TreeNode(2))
        node = self.find(tree, 3)
        self.remove(tree, node)
        tree.print()


    # todo: End of set of Alt (3rd-Party) Logic Samples


    # Tries
    

    # Graphs

    class Graph:

        def __init__(self): # O() t ; O() s
            # TODO
            pass


        # Cyclic or Non-Acyclic Graph - has at least 1 cycle

        # Acyclic Graph - has NO cycles

        # Directed Acyclic Graph (DAG) - has no directed 'cycles'

        # Acyclic Undirected Graph - a tree if connected, and a forest if not connected


        class DirectedGraph: # All edges are 1/uni-directional (point in 1 specific direction)
            # * Same as class DirectedGraphWithAdjacencyMatrix
        
            def __init__(self, num_nodes):
                self.num_nodes = num_nodes + 1
                self.graph = [ # Graph is setup as an Adjacency Matrix (not Adj List)
                    [0 for x in range(self.num_nodes)] 
                    for y in range(self.num_nodes)
                ]
            
            def get_root(self): return self.graph[0][0]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) \
                    and (v2 >= 0 and v2 <= self.num_nodes)

            def insert_edge(self, v1, v2):
                if self.within_bounds(v1, v2): self.graph[v1][v2] = 1
            
            def print(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            print(f"{i} -> {j}")
            
            def test(self):
                g = DataStructures.Graph.DirectedGraph(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()

        class UndirectedGraph: # All edges are bi-directional (do not point in any 1 specific direction)
            # * Same as class UndirectedGraphWithAdjacencyMatrix
        
            def __init__(self, num_nodes):
                self.num_nodes = num_nodes + 1
                self.graph = [ # Graph is setup as an Adjacency Matrix (not Adj List)
                    [0 for x in range(self.num_nodes)]
                    for y in range(self.num_nodes)
                ]
            
            def get_root(self): return self.graph[0][0]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) \
                    and (v2 >= 0 and v2 <= self.num_nodes)

            def insert_edge(self, v1, v2):
                if self.within_bounds(v1, v2):
                    self.graph[v1][v2] = 1
                    self.graph[v2][v1] = 1 # Undirected / Bi-directional edges (both directions)
            
            def print(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            print(f"{i} -> {j}")
            
            def test(self):
                g = DataStructures.Graph.UndirectedGraph(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()
        
        
        '''

        Traversal Actions: Visit node; Check node; Push to stack; Pop from stack (also a visit);

        
        Traversal Option Opinions:
        

        # TODO: Fix
        - BFS: # O(n + e) t (n = nodes, e = edges) ; O(~n) s (queue only nodes with 2+ unchecked neighbors in & out)
        
        pick (visit) root node as start node
        check node 1st (if not already checked), push to queue if it has 2+ unchecked neighbors (except previous node), move to next neighbor (bfs - all, cfs - custom value check, dfs - first), repeat
        repeat until current node has 0 neighbors or 1 already/previously checked neighbor node, pop latest (lifo) node from queue (also already checked, before pushed to queue)
        after pop latest node (already checked) from queue, start again (with current node as start node)

        
        - 3rd-Party BFS (tutorial): # O(n + e) t (n = nodes, e = edges) ; O(n) s (queue all nodes in & out)

        Traversing graph horizontally, layer by layer

        pick (visit) root node as start node
        mark current node as visited and enqueue it (add to queue)
        while queue is not empty, dequeue 1st (fifo) node from queue (this time, already visited, but not checked), check current node and mark as checked
        for all unvisited (also unchecked, but unvisited is better) neighbors (in the next layer) of current node, mark them as visited and enqueue them into queue
        repeat while loop until queue is empty

        NB: this time, only mark current node as visited before enqueueing it to queue, and only check current node after dequeueing it from queue
        if you enqueued all unchecked (not unvisited) neighbors unto queue, you'd end up enqueueing duplicate (already visited) nodes into queue (more space complexity)
        if you had duplicates in queue (after enqueueing unchecked but already visited nodes only), you'd check them after dequeueing the latest duplicate, and skip the other duplicates because they'd already be checked by then.


        - DFS: # O(n + e) t (n = nodes, e = edges) ; O(~n) s (stack only nodes with 2+ unchecked neighbors back & forth)
        
        pick (visit) root node as start node
        check node 1st (if not already checked), push to stack if it has 2+ unchecked neighbors (except previous node), move to next neighbor (bfs - all, cfs - custom value check, dfs - first), repeat
        repeat until current node has 0 neighbors or 1 already checked neighbor node (which will lead to a cycle if it wasn't the previously checked node), pop latest (lifo) node from stack (also already checked, before pushed to stack)
        after pop latest node (already checked) from stack, start again (with current node as start node)

        
        - 3rd-Party DFS (tutorial): # O(n + e) t (n = nodes, e = edges) ; O(n) s (stack all nodes back & forth)
        
        Traversing graph vertically, path by path

        pick (visit) root node as start node
        mark current node as visited and push to stack
        while stack is not empty, pop latest (lifo) node from stack (this time, already visited, but not checked), check current node and mark as checked
        for all unvisited (also unchecked, but unvisited is better) neighbors of current node, mark them as visited and push to stack
        repeat while loop until stack is empty

        NB: this time, only mark current node as visited before pushing it to stack, and only check current node after popping it from stack
        if you pushed all unchecked (not unvisited) neighbors unto stack, you'd end up pushing duplicate (already visited) nodes onto stack (more space complexity)
        if you had duplicates in stack (after pushing unchecked but already visited nodes only), you'd check them after popping the latest duplicate, and skip the other duplicates because they'd already be checked by then.


        '''

        def bfs(self, graph: 'DirectedGraphWithAdjacencyList'): # O(n + e) t (n = nodes, e = edges) ; O(n) s (stack all nodes back & forth)
            root = graph.get_root()
            visited = set()
            checked = set()
            queue = deque()
            queue.append(root)

            # Option 1: with visited only
            
            visited.add(node)
            
            while len(queue) > 0:
                node = queue.popleft() # deque: .popleft() 1st item (.pop() last item ; .pop(0) error - takes no argument)
                # if queue = [], .pop(0) 1st item
                print(node, end=' ')
                for n in self.graph[node]:
                    if n not in visited: # consider whether to check for n not None (in case graph has null-value items)
                        # before adding to visited set or queue
                        visited.add(n)
                        queue.append(n)

            # Option 2: with checked only

            while len(queue) > 0:
                node = queue.popleft() # deque: .popleft() 1st item (.pop() last item ; .pop(0) error - takes no argument)
                # if queue = [], .pop(0) 1st item
                if node and node not in checked:
                    print(node, end=' ')
                    checked.add(node)
                for n in self.graph[node]:
                    if n not in checked:
                        queue.append(n)

            # Option 3: with visited & checked

            visited.add(node)
            
            while len(queue) > 0:
                node = queue.popleft() # deque: .popleft() 1st item (.pop() last item ; .pop(0) error - takes no argument)
                # if queue = [], .pop(0) 1st item
                if node not in checked:
                    print(node, end=' ')
                    checked.add(node)
                for n in self.graph[node]:
                    if n not in visited: # or checked: (but visited is better)
                        visited.add(n)
                        queue.append(n)


        def cfs(self, graph): 
            pass


        def dfs(self, graph: 'DirectedGraphWithAdjacencyList'): # O(n + e) t (n = nodes, e = edges) ; O(n) s (stack all nodes back & forth)
            root = graph.get_root()
            visited = set()
            checked = set()
            stack = []
            stack.append(root)

            # Option 1: with visited only

            visited.add(node)

            while len(stack) > 0:
                node = stack.pop() # .pop() last item (.pop(0) index 0 (1st) item)
                print(node, end=' ')
                for n in self.graph[node]:
                    if n not in visited:
                        visited.add(n)
                        stack.append(n)

            # Option 2: with checked only

            while len(stack) > 0:
                node = stack.pop() # .pop() last item (.pop(0) index 0 (1st) item)
                if node not in checked:
                    print(node, end=' ')
                    checked.add(node)
                for n in self.graph[node]:
                    if n not in checked:
                        stack.append(n)

            # Option 3: with visited & checked

            visited.add(node)

            while len(stack) > 0:
                node = stack.pop() # .pop() last item (.pop(0) index 0 (1st) item)
                if node not in checked:
                    print(node, end=' ')
                    checked.add(node)
                for n in self.graph[node]:
                    if n not in visited: # or checked: (but visited is better)
                        visited.add(n)
                        stack.append(n)
        
        def dijkstra(self, graph, node): # O(e log n) t (n = nodes, e = edges) ; 
            pass
        
        def tests(self):
            dgl = DataStructures.Graph.DirectedGraphWithAdjacencyList()
            dgm = DataStructures.Graph.DirectedGraphWithAdjacencyMatrix()
            ugl = DataStructures.Graph.UndirectedGraphWithAdjacencyList()
            ugm = DataStructures.Graph.UndirectedGraphWithAdjacencyMatrix()
            for gl in [dgl, dgm, ugl, ugm]:
                gl.insert_edge(2, 1); gl.insert_edge(2, 5); gl.insert_edge(5, 6)
                gl.insert_edge(5, 8); gl.insert_edge(6, 9); gl.insert_edge(5, 6)
                self.bfs(gl); self.cfs(gl); self.dfs(gl)
        
        class DirectedGraphWithAdjacencyList:

            def __init__(self):
                self.graph = defaultdict(list) # Graph is setup as an Adjacency List (dict of lists)
            
            def get_root(self): return self.graph[self.graph.keys()[0]]
            
            def insert_edge(self, v1, v2):
                self.graph[v1].append(v2) # self.graph[v1] = [.., v2] (add v2 node to 1 of v1 node's neighbors)
            
            def print(self):
                for node in self.graph:
                    for v in self.graph[node]:
                        print(node, ' -> ', v)
            
            def test(self):
                g = DataStructures.Graph.DirectedGraphWithAdjacencyList()
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()

        class DirectedGraphWithAdjacencyMatrix:

            def __init__(self, num_nodes):
                self.num_nodes = num_nodes + 1
                self.graph = [
                    [0 for x in range(self.num_nodes)]
                    for y in range(self.num_nodes)
                ]
            
            def get_root(self): return self.graph[0][0]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) \
                    and (v2 >= 0 and v2 <= self.num_nodes)
            
            def insert_edge(self, v1, v2):
                if self.within_bounds(v1, v2): self.graph[v1][v2] = 1
            
            def print(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            print(i, '->', j)
            
            def test(self):
                g = DataStructures.Graph.DirectedGraphWithAdjacencyMatrix()
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()
        
        class UndirectedGraphWithAdjacencyList:

            def __init__(self):
                self.graph = defaultdict(list) # Graph is setup as an Adjacency List (dict of lists)
            
            def get_root(self): return self.graph[self.graph.keys()[0]]
            
            def insert_edge(self, v1, v2):
                self.graph[v1].append(v2)
                self.graph[v2].append(v1)
            
            def print(self):
                for node in self.graph:
                    for v in self.graph[node]:
                        print(node, ' -> ', v)
            
            def test(self):
                g = DataStructures.Graph.UndirectedGraphWithAdjacencyList()
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()

        class UndirectedGraphWithAdjacencyMatrix:

            def __init__(self, num_nodes): 
                self.num_nodes = num_nodes + 1
                self.graph = [
                    [0 for x in range(self.num_nodes)]
                    for y in range(self.num_nodes)
                ]
            
            def get_root(self): return self.graph[0][0]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) \
                    and (v2 >= 0 and v2 <= self.num_nodes)
            
            def insert_edge(self, v1, v2):
                if self.within_bounds(v1, v2):
                    self.graph[v1][v2] = 1
                    self.graph[v2][v1] = 1
            
            def print(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            print(i, ' -> ', j)
            
            def test(self):
                g = DataStructures.Graph.UndirectedGraphWithAdjacencyMatrix(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()

        class DirectedWeightedGraphWithAdjacencyList: # All edges are assigned a weight/cost value (to calculate costs from node to node)

            def __init__(self):
                self.graph = defaultdict(list)
            
            def get_root(self): return self.graph[self.graph.keys()[0]]
            
            def insert_edge(self, v1, c, v2): # c for cost of v1 to v2
                self.graph[v1].append((c, v2))
            
            def print(self):
                for node in self.graph:
                    for v in self.graph[node]:
                        print(node, ' -(', v[0], ')> ', v[1])
            
            def test(self):
                g = DataStructures.Graph.DirectedWeightedGraphWithAdjacencyList()
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()

        class DirectedWeightedGraphWithAdjacencyMatrix:

            def __init__(self, num_nodes):
                self.num_nodes = num_nodes + 1
                self.graph = [
                    [0 for x in range(self.num_nodes)]
                    for y in range(self.num_nodes)
                ]
            
            def get_root(self): return self.graph[0][0]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) \
                    and (v2 >= 0 and v2 <= self.num_nodes)
            
            def insert_edge(self, v1, c, v2):
                if self.within_bounds(v1, v2):
                    self.graph[v1][v2] = (c, 1)
                    self.graph[v2][v1] = (c, 1)
            
            def print(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            c = self.graph[i][j][0]
                            print(i, ' -(', c, ')> ', j)
            
            def test(self):
                g = DataStructures.Graph.DirectedWeightedGraphWithAdjacencyMatrix(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()

        class UndirectedWeightedGraphWithAdjacencyList:

            def __init__(self):
                self.graph = defaultdict(list)
            
            def get_root(self): return self.graph[self.graph.keys()[0]]
            
            def insert_edge(self, v1, c, v2):
                self.graph[v1].append((c, v2))
                self.graph[v2].append((c, v1))
            
            def print(self):
                for node in self.graph:
                    for v in self.graph[node]:
                        print(node, ' -(', v[0], ')> ', v[1])
            
            def test(self):
                g = DataStructures.Graph.UndirectedWeightedGraphWithAdjacencyList()
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()

        class UndirectedWeightedGraphWithAdjacencyMatrix:

            def __init__(self, num_nodes):
                self.num_nodes = num_nodes + 1
                self.graph = [
                    [0 for x in range(self.num_nodes)]
                    for y in range(self.num_nodes)
                ]
            
            def get_root(self): return self.graph[0][0]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) \
                    and (v2 >= 0 and v2 <= self.num_nodes)
            
            def insert_edge(self, v1, c, v2):
                if self.within_bounds(v1, v2):
                    self.graph[v1][v2] = (c, 1)
                    self.graph[v2][v1] = (c, 1)
            
            def print(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            c = self.graph[i][j][0]
                            print(i, ' -(', c, ')> ', j)
            
            def test(self):
                g = DataStructures.Graph.UndirectedWeightedGraphWithAdjacencyMatrix(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print()
        
        class ShortestPathAlgorithms:

            def __init__(self): # O() t ; O() s
                # TODO
                pass


            class Dijkstra:

                def __init__(self, adj_mat, start_vertex):
                    self.mat = adj_mat
                    self.start = start_vertex
                    self.v = len(adj_mat)
                    self.visited = [False for _ in range(len(adj_mat))]
                    self.distances = [float('inf') for _ in range(len(adj_mat))]
                    self.distances[start_vertex] = 0
                
                def get_min_vertex(self):
                    # vertex with the lowest distance
                    min_vertex_value = sys.maxsize
                    min_vertex_index = 0

                    for i in range(self.v):
                        if not self.visited[i] and self.distances[i] < min_vertex_value:
                            min_vertex_value = self.distances[i]
                            min_vertex_index = i
                    
                    return min_vertex_index
                
                def calculate(self):

                    for vertex in range(self.v):
                        actual_vertex = self.get_min_vertex()
                        print(f"Considering vertex {actual_vertex}")
                        self.visited[actual_vertex] = True

                        for other_vertex in range(self.v):
                            if self.mat[actual_vertex][other_vertex] > 0:
                                if self.distances[actual_vertex] + self.mat[actual_vertex][other_vertex] < \
                                    self.distances[other_vertex]:
                                    self.distances[other_vertex] = self.distances[actual_vertex] + self.mat[actual_vertex][other_vertex]

                def print_distance(self):
                    print(self.distances)
            
                def test(self): 
                    m = [
                        [0, 7, 5, 2, 0, 0],
                        [0, 7, 5, 2, 0, 0],
                        [0, 7, 5, 2, 0, 0],
                        [0, 7, 5, 2, 0, 0],
                        [0, 7, 5, 2, 0, 0],
                        [0, 7, 5, 2, 0, 0]
                    ]
                    algo = DataStructures.Graph.ShortestPathAlgorithms.Dijkstra(m, 0)
                    algo.calculate()
                    algo.print_distance()
                
                # TODO: Understand 'network_delay_time' fully & Test completely

                def network_delay_time(self, times: List[List[int]], n: int, k: int, \
                    graph: 'DataStructures.Graph.DirectedWeightedGraphWithAdjacencyList') -> int: # k - start node

                    # node u to v, with cost c
                    for u, v, c in times:
                        graph.insert_edge(u, c, v)
                    
                    min_heap = [(0, k)]
                    visited = set()
                    distances = { i: float('inf') for i in range(1, n + 1) }
                    distances[k] = 0

                    while min_heap and len(min_heap) > 0:
                        d, u = heapq.heappop(min_heap)
                        if u in visited: continue
                        visited.add(u)
                        # check if all nodes have been visited
                        if len(visited) == n: return d
                        # now check remaining nodes
                        for distance, node in graph[u]:
                            if d + distance < distances[node] and \
                                node not in visited:
                                distances[node] = d + distance
                                heapq.heappush(min_heap, (distances[node], node))
                    
                    return -1
                
                def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int: # k - start node
                    graph = defaultdict(list) # working with a directed weighted graph with adjacency list

                    # node u to v, with cost c
                    for u, v, c in times:
                        graph[u].append((c, v))
                    
                    min_heap = [(0, k)]
                    visited = set()
                    distances = { i: float('inf') for i in range(1, n + 1) }
                    distances[k] = 0

                    while min_heap and len(min_heap) > 0:
                        d, u = heapq.heappop(min_heap)
                        if u in visited: continue
                        visited.add(u)
                        # check if all nodes have been visited
                        if len(visited) == n: return d
                        # now check remaining nodes
                        for distance, node in graph[u]:
                            if d + distance < distances[node] and \
                                node not in visited:
                                distances[node] = d + distance
                                heapq.heappush(min_heap, (distances[node], node))
                    
                    return -1

            class BellmanFord: 
                pass


    # Bits


    # Blobs


    ''' # TODO: Note other data-structure combos of Prefixes & Suffixes
    Prefixes - Array, Map, Hash, Table, Weak, Linked, Tree, Graph, Skip, Binary, Priority, Double (Queue) / Deque, Binary-Search (Tree), Red-Black (Tree), Trie, B+ (Tree), Bloom (Filter), Segment (Tree), Disjoint (Set),  ...
    Suffixes - Array, Map, Table, Set, List, LinkedList, Stack, Queue, Deque, Heap, Tree, Graph, (Tree) Forest, (Bloom) Filter,  ...
    '''

    def func(self): # O() t ; O() s
        pass # TODO


########################################
##  PROBLEM-SOLVING ALGO'S
########################################


class DynamicProgramming: # ! Not Enough DP work

    '''

        Dynamic Programming Algorithms

        Technique for solving problems, that depends on dividing a problem into sub-problems
        and results gotten from sub-problems are saved into state, to be used later, for future sub-problems

        - about storing the results of these sub-problems into memory so they need to be recalculated repeatedly
        - ?
        
        Attributes:

        - Optimization over Recursion & other problem-solving techniques
            - BackTracking, Divide & Conquer, Greedy Algo techniques
        - ?

        - State Machine
            - Memorize & Memoize repeated solution states
                - at each sub-problem step
            - so time isn't wasted trying to recalculate things
                - already in state
            - basically trading memory for speed
                - using extra space for holding state
                    - to speed up algo's calculations
                        - perhaps sometimes, mathematically (by formulae)
            - ?
        
        - Memoization
            - Caching state data at different steps
        
        Identification:

        - problem can be broken down / divided into smaller sub-problems
        - problem is recursive
        - a lot of repeated states in solution
        - demands for Optimal Solution
        - & Optimal solution of sub-problems
            - can be used to form
            - the Optimal Solution of the Original Problem
        - repetitive sub-problems
        - memoized sub-problems
        - recursive solution
        - ?

        - Tips:
            - Do you have something you can cache ?
            - Saving maximum Time-Complexity (& perhaps Space-Complexity too)
                - enables cost minimization, & gain (or revenue) maximization
                    - can increase bottom-line / salary gains
            - ?
        
        - Examples:
            - Fibonacci Sequence Problem
            - ?

        Approach:

        - Structured as a Tree / Graph
            - with a root node, parent nodes, children nodes, and leaf nodes

        - Top-Down
            - DFS Traversal, with Recursion

            - or (not really): BFS Traversal, with Recursion (if possible - TODO: confirm) /(before) Queued-While-loops
                - while saving state data
                    - for each step / node at each depth
            - From top / root node to bottom / deepest depth
            - state data is saved at each node
                - so if any future node / child node
                    - of past nodes / a parent node
                    - (which are connected to the child node)
                    - required state data from any connected past / parent node
                        - that saved state data helps child node
                            - skip unnecessary re-calculation
            
            - Combination of Recursion & Memoization
                - Recursively solving sub-problems (mostly DFS)
                - while memorizing (saving) results in memory (state data)
                - so overlapping sub-problems do not have to be re-solved
                - Memoization helps speed up algo
            
            - eg. Recursive Fibonacci Series: f(n) = f(n-1) + f(n-2)
                - Recursion (with DFS - or can be BFS too)
                    - since we're still calculating from the top to bottom
                        - f(n)
                        - hence, Top-Down Approach
                    - even though values still come from base-cases 1st
                        - leaf node scenarios
                            - f(n - largest difference)
                            - or 1st number-function in sequence
                - saves previous number-functions' results
                - for summing them up for future number-functions
                - BUT, still Top-Down Approach, since the root node
                    - function f(n) is called 1st,
                        - before next parents f(n-1) & f(n-2)
                        - and so on .. 
                        - until base functions with base cases
                            - summing up all their returns values
                            - until returning values back to 
                            - Top (1st) function call
        
        - Bottom-Up
            - BFS Traversal, with Queued-While-loops
            - or (not really): BFS Traversal (from the bottom), with Queued-While-loops /(before) Recursion (if possible - TODO: confirm)
                - while saving state data
                    - for each step / node at each depth
            - From bottom / leaf node depth to top / root node
            - state data is saved at each node
                - so if any future node / parent node
                    - of past nodes / child nodes
                    - (which are connected to the parent node)
                    - required state data from any connected past / child node
                        - that saved state data helps parent node
                            - skip unnecessary re-calculation
            
            - Simply an Iterative Approach with BFS Traversal (Queued-While Loops)
                - instead of Top-Down's combination of Recursion & Memoization
            
            - or 'maybe' DFS Traversal with Recursion too
                - or perhaps that's also the Top-Down approach, 
                    - due to recursion calculating for the top node
                        - even though values come from the bottom - leaf nodes
                - but ACTUALLY, it can't be 'both' for 'both'
                    - DFS Traversal with Recursion CANNOT be seen as both top-down & bottom-up
                    - (ONLY Top-Down)
                        - depending on which nodes (whether root / leaf nodes) are worked on 1st
                            - 'worked on 1st' meaning, which nodes have their initial raw-inputs 1st
                                - to be able to be 'worked on 1st'
                        - or: also depending on which order from which you look at the data-structure at hand
                            - whether a list, or a tree; data-structure can be seen from the opposite-direction
                                - eg. fibonacci functions being a list
                                    - can be seen as a tree, with the 1st 2 functions as leaf - child nodes
                                        - this is actually the Bottom-Up Approach
                                            - with Iterative or Queued-While-loops
            
            - BFS Traversal with Iterative / Queued-While-loops can also ONLY be seen as Bottom-Up ONLY
            - (NOT both approaches)
                - for the same reasons as for with DFS with Recursion
                - with BFS Iterative Traversals:
                    - whether nodes are seen as a list (from 1st / leaf - child nodes) to end (final / root node)
                        - if seen as a tree:
                            - the leaf-child nodes (with 'deepest' depth)
                                - can be pushed into a Queue
                                    - for Iterative While-loops
                                        - WHILE the Queue is NOT empty
                            - of the entire tree can be converted into a list of nodes
                                - with the 'deepest' depth (leaf) - child nodes
                                    - being appending into the list 1st
                                        - THEN in that order:
                                            - from deepest depths
                                                - up until root parent node
                    - with nodes now seen as a list (or as Queued child-nodes):
                        - Iterative Traversals on them will work on children nodes 1st
                            - before calculating parent nodes after
                - Iterative BFS Traversals can ONLY be Bottom-Up
                    - because they can only calculate parent nodes, from child nodes 1st
                    - hence, they can NEVER be Top-Down
                - NB: For Top-Down Approach, with DFS Recursion
                    - root node functions are called 1st (with their children) recursively
                        - before their calculated return values, 
                            - are collated in a Bottom-Up-wise fashion
                            - as collated returned values,
                                - until root node function's return value
            
            - eg. Iterative Fibonacci Series: regular iteration, 
                - starting from 1st 2 leaf - child nodes
                - code: n = 7 (or some length); a[0] = 0; a[1] = 1 - (bottom-)
                    - Iterate: from i=2 to i=n -> 
                        a[i] = a[i - 1] + a[i - 2]
                    - return: a[n] - (-up approach) - as last fibo-number (this time)
                
                - NB: for 'Queued-While-loops', previous 2 child nodes can be queued
                    - then new sums can always be queued and re-calc'd
                        - whenever queue-length = 2
            
            - eg. Iterative Fibonacci Series: Queued-While-loops
                - starting from 1st 2 leaf - child nodes
                    - then popping, peeking, & pushing
                        - for the next iteration
                - code: n = 7 (or some length); a = [0, 1]; q = [a[0], a[1]] - (bottom-) - with a queue this time
                    - While: len(array 'a') < n + 1 ->
                        num = q.pop(out 1st item) + q.peek(2nd item)
                        a.append(num) - add number to fibo-sequence
                        q.push(num) - push number as new 2nd item in Queue
                    - return: a - (-up approach) - as entire fibo-sequence (this time)
        
        - Memoization
            
            - Top-Down Approach:
                - can store each sub-problem's data in an external table, for re-use
                - can also rely on recursive function-call's return-value collation
                    - which is already auto, so wouldn't need to store return values
                    - but any extra values in recursion, 
                        - still required in recursive calculations
                            - can be stored in external tables
                                - or other data-structures

            - Bottom-Up Approach:
                - can store each sub-problem's data in an external table, for re-use
                - can also rely on iterative calculations, 
                    - using values from previous iterations / previous list/queue - items
                    - can also store extra data in external tables / other data-structures
                        - to be used in future iterations
        
        Example:

        - Check out both Fibonacci Series examples
            - Top-Down - Recursion
            - Bottom-Up - Iterative / Queued-While-loops

        Comparisons:

        - vs BackTracking
            - Both DP & BTrack work with Tree Data-Structure
                - but DP works with trees, in terms of:
                    - nodes as input-values of sub-problems
                        - in the entire problem space
                - whilst BTrack works with trees, in terms of:
                    - nodes as paths / options of strategy
                        - in the entire problem space
                
                - hence, DP will always work with ALL nodes
                    - in order to find optimal solution
                - BUT, BTrack will only work with SOME (or ALL) nodes
                    - when finding the optimal solution
                
                - HOWEVER, since much of the nodes in the DP's tree
                    - contain memoized values from previous children nodes
                        - DP can ignore working with such nodes
                            - since it can just take out their already
                                - calculated value from state data / memory
                - so both DP & BTrack can also be likened
                    - to still be working with 
                        - only some nodes, 
                            - of the entire problem space
            
            - ?
        
        - vs Divide & Conquer
            - DP can be seen as D&C + Memoization
                - ?

            - D&C divides the problem into sub-problems
                - solved to construct the solution
                - of the Original Problem
                    - by combining results of sub-problems' solutions
            - BUT, D&C sub-problems are NON-OVERLAPPING sub-problems
                - i.e. they're independent from each other
                    - & do not depend on state data from each other
            
            - eg. D&C's Merge Sort:
                - array is divided into 2 halves, recursively
                    - with being independent from each other
                    - they never repeat at any point of recursion
                    - they never depend on each other, for any reason
            
            - DP sub-problems are OVERLAPPING
                - they depend on each other's state data
            
            - eg. Fibonacci Sequence:
                - each number is the sum of 2 previous numbers in the sequence
                - if 2 previous number-functions have already been pre-calculated
                    - and saved to state data
                - the next number-function does not need to re-calculate them
                    - it can just use their pre-calculated values
                        - already saved to state data

            - ?
        
        - vs Greedy
            - both DP & Greedy are used to find optimal solution
            
            - BUT Greedy approaches don't guarantee Optimality
                - they have to be tested with multiple, & different test cases
                - to confirm if they actually provide an optimal solution
            - BUT DP approaches guarantee Optimal Solutions
                - using Principle of Optimality
                - ensuring final solution is most-optimal in all different test cases
            
            - Greedy approaches choose whichever 'BEST' option at the moment
                - and then solve future sub-problems arising
                    - after the previous 'best' choice was made
                    - no matter the cost to the final 'sub-optimal' solution
                        - or any future steps / sub-problems
            - DP approaches choose at each step
                - but choices always depend on future final solution
                    - as well as solutions at all steps / sub-problems
                - since each step's result is saved to state data
                    - to be used in future steps / sub-problems
                    - for the sake of the final optimal solution
            
            - Greedy approaches are much easier since there are mostly 'no risks'
                - to worry about (bring about more risks anyway)
            - DP approaches are more difficult to implement
                - since 'all risks' / 'optimality' of solutions
                - of each sub-problem matters, at each step
            
            - Greedy eg. - Coin-change problem
                - ?
            - DP eg. - Fibonacci / ? problem
                - ?
            
            - ?
        
        - vs Recursion
            - DP is an 'Optimization' over Recursion
            - same DP problems can also be solved with Recursion
                - but if problems have overlapping (related) sub-problems
                - where they depend on state data from each other
                - Recursive solution, without saving state data for later
                    - will take more time, recalculating
                        - same sub-problems repeatedly
            - ?
        

    '''

    def __init__(self): # O() t ; O() s
        pass # TODO


    # ! standard

    
    def meth(self): # O() t ; O() s
        pass # TODO
    

    # Top-Down Approach - Recursion
    def fibonacci(self, n): # O() t ; O() s
        
        def recurse(n):
            if n == 0: return 1
            elif n == 1: return 2
            else: return recurse(n - 1) + recurse(n - 2)
        
        return recurse(n)

    # Bottom-Up Approach - Iterative for-loop
    def fibonacci(self, n): # O() t ; O() s
        
        a = [1, 2]
        for i in range(2, n + 1):
            a[i] = a[i - 1] + a[i - 2]
        
        return a[n] # or: a, for the entire fibo-sequence

    # Bottom-Up Approach - Queued while-loop
    def fibonacci(self, n): # O() t ; O() s
        
        a = [1, 2]
        q = [a[0], a[1]]

        while len(a) < n + 1: # while fibo-series is not at total length, n
            # now, pop, then peek, then push
            # * can also use an actual queue() data-structure
            num = q.pop(0) + q[1] # pop out 1st item, then .peek( 2nd item by index )
            a.append(num) # append fibo-number
            q.append(num) # push fibo-number into queue, for next iteration
        
        return a # entire fibo-sequence, or last item - a[n]

    # 3rd-Party (Tutorial) - REGULAR recursion - Top-Down
    def fibonacci(self, n): # O(2^n) t ; O(1) s
        # O(2^n) t - recursive calls - default time-complexity
        # O(1) s - no space required

        calcs = 0

        def recurse(n):
            calcs += 1 # can run this recursive function ..
            # & compare number of 'calculations' made (WAY slower than below)
            if n < 2: return n
            return recurse(n - 1) + recurse(n - 2)
        
        return recurse(n)

    # ! 3rd-Party (Tutorial) - DP (DFS) recursion, with Caching - Top-Down (BEST & FASTEST Option)
    # BEST & FASTEST Option - since it avoids unnecessary recursive re-calculations
    # plus fibo-numbers will never repeat, since lower ones add up to higher ones
    
    def fibonacci(self, n): # O(n) t ; O(n) s

        # O(n) t - recursive calls, BUT with caching - to remove unnecessary re-calculations
        # algo ends up only recursing through only unique n values
        # O(n) s - extra hashmap or hashtable - used as a cache data-structure
        
        cache = {}
        calcs = 0

        def recurse(n):
            calcs += 1 # can run this recursive function ..
            # & compare number of 'calculations' made (WAY faster than above)
            if n in cache: return cache[n]
            else:
                # ! 'calcs += 1' doesn't have to be placed here ..
                # * because above base-case still prevents below recursive calls
                if n < 2: return n
                else:
                    cache[n] = recurse(n - 1) + recurse(n - 2)
                    return cache[n] # return cached-number, after storing
                # so it's still accessible in future recursive calls
        
        return recurse(n)
    
    # 3rd-Party (Tutorial) - DP (BFS) iterative, without Caching - Bottom-Up (ALSO BEST & FASTEST Option)
    # using same resulting array to save previous calculations
    def fibonacci(self, n): # O() t ; O() s

        a = [0, 1]

        for i in range(2, n + 1):
            a.append(a[i - 1] + a[i - 2])
        
        return a


    '''

        TODO: ?

    '''
    

    def bitmasking(self): # O() t ; O() s
        pass # TODO

    def digit_dp(self): # O() t ; O() s
        pass # TODO

    def sum_over_subsets(self): # O() t ; O() s
        pass # TODO

    
    '''

        Unique Paths - LeetCode #62

        .

    '''
    
    def unique_paths(self): # O() t ; O() s
        pass # TODO
    
    def unique_paths(self): # O() t ; O() s
        pass # TODO
    
    def unique_paths(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #62
    def unique_paths(self, m: int, n: int) -> int: # O() t ; O() s
        
        dp = [ \
            [ \
                0 for x in range(m) for y in range(n)
            ]
        ]

        for i in range(m):
            dp[0][i] = 1
        
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = \
                dp[i - 1][j] \
                + \
                dp[i][j - 1]
        
        return dp[-1][-1]


    '''

        Climbing Stairs

    '''
    
    def climbing_stairs(self): # O() t ; O() s
        pass # TODO
    
    def climbing_stairs(self): # O() t ; O() s
        pass # TODO
    
    def climbing_stairs(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #70
    def climbing_stairs(self, n: int) -> int: # O() t ; O() s
        
        if n == 1: return 1

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


    '''

        House Robber

    '''
    
    def house_robber(self): # O() t ; O() s
        pass # TODO
    
    def house_robber(self): # O() t ; O() s
        pass # TODO
    
    def house_robber(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #198
    def house_robber(self, nums: List[int]) -> int: # O() t ; O() s
        
        n = len(nums)
        if n == 0: return 0

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(n):
            dp[i] = nums[0] if i == 0 else ( \
                max(nums[0], nums[1]) \
                if i == 1 else \
                max( \
                    dp[i - 1], \
                    dp[i - 2] + nums[i] \
                )
            )
        
        return dp[n - 1] # last item


    '''

        Coin Change

    '''
    
    def coin_change(self): # O() t ; O() s
        pass # TODO
    
    def coin_change(self): # O() t ; O() s
        pass # TODO
    
    def coin_change(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #322
    def coin_change(self, coins: List[int], amount: int) -> int: # O() t ; O() s
        
        if amount <= 0: return 0

        if min(coins) > amount: return -1

        INT_MAX = 1 << 32
        dp = [INT_MAX] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min( \
                        (dp[i - coin] + 1), \
                        dp[i] \
                    )
        
        return dp[amount] if dp[amount] != INT_MAX else -1
    
    # TODO: 3rd-Party (Tutorial) - Using Recursion (NOT DP, in this case) - LC #322
    def min_coins_recursion___NO_DP(self, coins, n, total): # O(n ^ a) t ; O(a) s ; a - target amount

        if total == 0: return 0

        res = sys.maxsize

        for i in range(n):

            if coins[i] <= total:

                sub_res = self.min_coins(coins, n, total - coins[i])

                if sub_res != sys.maxsize and sub_res + 1 < res:

                    res = sub_res + 1
        
        return res
    
    # TODO: 3rd-Party (Tutorial) - Using DP (NOT Recursion, in this case) - LC #322
    def min_coins_top_down_recursion(self, coins, n, total, table): # O(na) t ; O(a) s ; a - target amount

        if total == 0: return 0
        if total in table.keys(): return table[total]

        res = sys.maxsize

        for i in range(n):
            if coins[i] <= total:
                sub_res = self.min_coins_top_down( \
                    coins, n, total - coins[i], table \
                )
                if sub_res != sys.maxsize and sub_res + 1 < res:
                    res = sub_res + 1
        
        table[total] = res
        return res
    
    # TODO: 3rd-Party (Tutorial) - Using DP (NOT Recursion, in this case) - LC #322
    def min_coins_bottom_up_iteration(self, coins, n, total, table): # O(na) t ; O(a) s ; a - target amount

        table = [sys.maxsize for k in range(total + 1)]
        table[0] = 0

        for i in range(1, total + 1):
            for j in range(n):
                if coins[j] <= 1:
                    sub_res = table[i - coins[j]]
                    if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                        table[i] = sub_res + 1
        
        return table[total]


    '''

        Best Time to Buy & Sell Stock

    '''
    
    def best_time_to_buy_sell_stock(self): # O() t ; O() s
        pass # TODO
    
    def best_time_to_buy_sell_stock(self): # O() t ; O() s
        pass # TODO
    
    def best_time_to_buy_sell_stock(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #121
    def best_time_to_buy_sell_stock(self, prices: List[int]) -> int: # O() t ; O() s
        
        buy_price = float('inf')
        profit = 0

        for i, price in enumerate(prices):
            if buy_price > price:
                buy_price = price
            else:
                profit = max(profit, price - buy_price)
        
        return profit
    
    # TODO: 3rd-Party (Tutorial) - LC #121
    def max_profit(self, prices: List[int]) -> int: # O() t ; O() s
        
        buy_price = float('inf')
        profit = 0

        for i, price in enumerate(prices):
            if buy_price > price:
                buy_price = price
            else:
                profit = max(profit, price - buy_price)

        return profit


    '''

        Word Search

    '''
    
    def word_search(self): # O() t ; O() s
        pass # TODO
    
    def word_search(self): # O() t ; O() s
        pass # TODO
    
    def word_search(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #79
    def word_search(self, board, word, x, y, cur): # O() t ; O() s


        def exist(self, board: List[List[str]], word: str) -> bool:
            
            if len(word) == 0: return True

            n = len(board)

            for i in range(n):

                m = len(board[i])

                for j in range(m):

                    if word[0] == board[i][j] and \
                        self.word_search(board, word, i, j, ''):
                        
                        return True
            
            return False


        dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

        if x < 0 or \
            x >= len(board) or \
                y < 0 or \
                    y >= len(board[x]) or \
                        board[x][y] == ' ':
            
            return False
        
        cur += board[x][y]

        if len(cur) > len(word):
            return False
        if cur[len(cur) - 1] != word[len(cur) - 1]:
            return False
        if cur == word:
            return True
        
        temp = board[x][y]
        board[x][y] = ' '

        for i in range(4):
            if self.word_search(
                board, \
                word, \
                x + dx[i], \
                y + dy[i], \
                cur
            ):
                return True
        
        board[x][y] = temp

        return False
    

    '''

        Longest Palindromic Substring

    '''
    
    def longest_palindromic_substring(self): # O() t ; O() s
        pass # TODO
    
    def longest_palindromic_substring(self): # O() t ; O() s
        pass # TODO
    
    def longest_palindromic_substring(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #5
    def longest_palindromic_substring(self, s: str) -> str: # O() t ; O() s
        
        n = len(s)

        if n < 2: return s

        left = right = 0
        palindrome = [[0] * n for _ in range(n)]

        for j in range(1, n):
            for i in range(0, j):
                
                inner_is_palindrome = palindrome[i + 1][j - 1] \
                or j - i <= 2

                if s[i] == s[j] and inner_is_palindrome:

                    palindrome[i][j] = True

                    if j - i > right - left:
                        left, right = i, j
        
        return s[left : right + 1]


    '''

        Trapping Rain Water

    '''
    
    def trapping_rain_water(self): # O() t ; O() s
        pass # TODO
    
    def trapping_rain_water(self): # O() t ; O() s
        pass # TODO
    
    def trapping_rain_water(self): # O() t ; O() s
        pass # TODO
    
    # TODO: 3rd-Party (Tutorial) - LC #42
    def trapping_rain_water(self, height: List[int]) -> int: # O() t ; O() s
        
        n = len(height)
        if n == 0: return 0

        # * do not chain-assign a reference value (list)
        left, right = [0] * n, [0] * n

        ans = 0
        left[0] = height[0]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        right[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        
        for i in range(0, n):
            ans += min(left[i], right[i]) - height[i]
        
        return ans


    '''

        Staircase

    '''
    
    def staircase(self): # O() t ; O() s
        pass # TODO
    
    def staircase(self): # O() t ; O() s
        pass # TODO
    
    def staircase(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - LC #?
    def staircase(self, n, k): # O() t ; O() s
        
        if n == 0: return 1
        if n < 0: return 0

        ans = 0

        for i in range(1, k + 1):
            ans += self.staircase(n - i, k)
        
        return ans
    
    # 3rd-Party (Tutorial) - LC #?
    def ways(self, n, k): # O(3 ^ n) t ; O(n) s
        
        if n == 0: return 1
        if n < 0: return 0

        ans = 0

        for i in range(1, k + 1):
            ans += self.ways(n - i, k)
        
        return ans
    
    # 3rd-Party (Tutorial) - LC #?
    def ways_top_down_recursion(self, n, k, dp): # O(n) t ; O(n) s

        if n == 0:
            # return 1 # for soln's sake, don't just return '1' base-value
            dp[n] = 1; return dp[n] # return '1' base-value as list's indexed value
        
        if n < 0: return 0

        if not dp[n] == -1:
            return dp[n]

        dp[n] = 0

        for i in range(1, k + 1):
            dp[n] += self.ways_top_down_recursion(n - i, k, dp)
        
        return dp[n]
    
    # 3rd-Party (Tutorial) - LC #?
    def ways_bottom_up_iteration(self, n, k): # O(n) t ; O(n) s

        dp = [0] * (n + 1)
        dp[0] = 1

        for step in range(1, n + 1):

            dp[step] = 0

            for j in range(1, k + 1):

                if step - j >= 0:
                    dp[step] += dp[step - j]
        
        return dp[n]
    

    '''

        Knapsack

    '''
    
    def knapsack(self): # O() t ; O() s
        pass # TODO
    
    def knapsack(self): # O() t ; O() s
        pass # TODO
    
    def knapsack(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - LC #?
    def knapsack(self, weight, price, n, capacity, values): # O(2 ^ n) t ; O(n) s
        
        if n == 0 or capacity == 0:
            values[n - 1][capacity - 1] = 0
            return 0
        
        if values[n - 1][capacity - 1] != -1:
            return values[n - 1][capacity - 1]

        incl = excl = 0

        if weight[n - 1] <= capacity:
            incl = \
                price[n - 1] + \
                    self.knapsack( \
                        weight, price, n - 1, capacity - weight[n - 1], values \
                    )
        
        excl = self.knapsack( \
            weight, price, n - 1, capacity, values \
        )

        values[n - 1][capacity - 1] = max(incl, excl)

        return values[n - 1][capacity - 1]
    
    # 3rd-Party (Tutorial) - LC #?
    def get_max_profit__recursion(self, weight, price, n, capacity, values): # O(2 ^ n) t ; O(n) s
        
        pass # TODO
    
    # 3rd-Party (Tutorial) - LC #?
    def get_max_profit__top_down_memoization(self, weight, price, n, capacity, values): # O(nw) t ; O(nw) s
        
        if n == 0 or capacity == 0:
            values[n - 1][capacity - 1] = 0
            return 0
        
        if values[n - 1][capacity - 1] != -1:
            return values[n - 1][capacity - 1]

        incl = excl = 0

        if weight[n - 1] <= capacity:
            incl = \
                price[n - 1] + \
                    self.get_max_profit( \
                        weight, price, n - 1, capacity - weight[n - 1], values \
                    )
        
        excl = self.get_max_profit( \
            weight, price, n - 1, capacity, values \
        )

        values[n - 1][capacity - 1] = max(incl, excl)

        return values[n - 1][capacity - 1]

    # 3rd-Party (Tutorial) - LC #?
    def get_max_profit__bottom_up_iteration(self, weight, price, n, capacity): # O(nw) t ; O(nw) s

        values = [[0 for i in range(capacity + 1)] for i in range(n + 1)]

        for i in range(n + 1):
            for j in range(capacity + 1):

                if i == 0 or j == 0:

                    values[i][j] = 0

                else:

                    incl = excl = 0

                    if weight[i - 1] <= j:

                        incl = price[i - 1] + values[i - 1][j - weight[i - 1]]

                    excl = values[i - 1][j]
                    values[i][j] = max(incl, excl)
        
        return values[n][capacity]


    '''

        Longest Decreasing Subsequence

    '''
    
    def longest_decreasing_subsequence(self): # O() t ; O() s
        pass # TODO
    
    def longest_decreasing_subsequence(self): # O() t ; O() s
        pass # TODO
    
    def longest_decreasing_subsequence(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - LC #?
    def longest_decreasing_subsequence(self, nums, i, prev): # O(2 ^ n) t ; O(n) s
        
        if i == len(nums): return 0

        incl = 0

        if nums[i] < prev:
            
            incl = 1 + self.longest_decreasing_subsequence(nums, i + 1, nums[i])
        
        excl = self.longest_decreasing_subsequence(nums, i + 1, prev)

        return max(incl, excl)
    
    # 3rd-Party (Tutorial) - LC #?
    def get_lds_top_down_memoization(self, nums, prev_i, curr, dp): # O(n ^ 2) t ; O(n ^ 2) s
        
        if curr == len(nums): return 0

        if dp[prev_i][curr] > 0:
            return dp[prev_i][curr]
        
        incl = 0

        if prev_i < 0 or nums[curr] < nums[prev_i]:

            incl = 1 + self.get_lds_top_down_memoization( \
                nums, curr, curr + 1, dp \
            )

        excl = self.get_lds_top_down_memoization( \
            nums, prev_i, curr + 1, dp \
        )

        dp[prev_i + 1][curr] = max(incl, excl)

        return dp[prev_i + 1][curr]
    
    # 3rd-Party (Tutorial) - LC #?
    def get_lds_bottom_up_iteration(self, nums): # O(n ^ 2) t ; O(n) s
        
        if len(nums) == 0: return 0

        max_lds = [1] * len(nums)
        max_so_far = 1

        for j in range(1, len(nums)):
            for i in range(j):

                if nums[j] < nums[i]:

                    max_lds[i] = max(max_lds[j], max_lds[i] + 1)
                
                max_so_far = max(max_so_far, max_lds[j])
        
        return max_so_far


    '''

        Levenshtein

    '''
    
    def levenshtein(self): # O() t ; O() s
        pass # TODO
    
    def levenshtein(self): # O() t ; O() s
        pass # TODO
    
    def levenshtein(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - LC #?
    def levenshtein(self, str1, str2, m, n): # O(3 ^ m) t ; O(mn) s
        
        if m == 0 or n == 0:
            return max(m, n)
        
        ch1 = 1 + self.levenshtein(str1, str2, m, n - 1)
        ch2 = 1 + self.levenshtein(str1, str2, m - 1, n)

        if str1[m - 1] == str2[n - 1]:
            k = 0
        else: k = 1

        ch3 = k + self.levenshtein(str1, str2, m - 1, n - 1)

        return min(ch1, ch2, ch3)
    
    # 3rd-Party (Tutorial) - LC #?
    def get_edit_distance__top_down_memoization(self, str1, str2, m, n, dp): # O(mn) t ; O(mn) s
        
        if m == 0 or n == 0: return max(m, n)

        if dp[m - 1][n - 1] >= 0:
            return dp[m - 1][n - 1]
        
        ch1 = 1 + self.get_edit_distance__top_down_memoization( \
            str1, str2, m, n - 1, dp \
        )
        ch2 = 1 + self.get_edit_distance__top_down_memoization( \
            str1, str2, m - 1, n, dp \
        )

        if str1[m - 1] == str2[n - 1]:
            k = 0
        else: k = 1

        ch3 = k + self.get_edit_distance__top_down_memoization( \
            str1, str2, m - 1, n - 1, dp \
        )

        dp[m - 1][n - 1] = min(ch1, ch2, ch3)

        return dp[m - 1][n - 1]
    
    # 3rd-Party (Tutorial) - LC #?
    def get_edit_distance__bottom_up_iteration(self, str1, str2, m, n): # O(mn) t ; O(mn) s
        
        l_dist = [[0 for i in range(n + 1)] for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):

                if i == 0: l_dist[i][j] = j
                elif j == 0: l_dist[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    l_dist[i][j] = l_dist[i - 1][j - 1]
                else:
                    l_dist[i][j] = \
                        min( \
                            l_dist[i - 1][j], \
                            l_dist[i - 1][j - 1], \
                            l_dist[i][j - 1] + 1 \
                        )
        
        return l_dist[m][n]


    '''

        Rod Cutting

    '''
    
    def rod_cutting(self): # O() t ; O() s
        pass # TODO
    
    def rod_cutting(self): # O() t ; O() s
        pass # TODO
    
    def rod_cutting(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - LC #?
    def rod_cutting(self, price, n): # O(2 ^ (n - 1)) t ; O(n ~ 1) s
        
        if n == 0: return 0

        max_revenue = -sys.maxsize

        for i in range(1, n + 1):

            max_revenue = max( \
                max_revenue, price[i - 1] + self.rod_cutting(price, n - i) \
            )
        
        return max_revenue
    
    # 3rd-Party (Tutorial) - LC #?
    def rod_cut_top_down_memoization(self, price, n, memo): # O(n ^ 2) t ; O(n) s
        
        if n == 0: return 0

        if memo[n - 1] > 0:
            return memo[n - 1]

        max_revenue = -sys.maxsize

        for i in range(1, n + 1):

            max_revenue = max( \
                max_revenue, \
                price[i - 1] + \
                self.rod_cut_top_down_memoization( \
                    price, n - i, memo \
                )
            )
        
        memo[n - 1] = max_revenue

        return memo[n - 1]

    
    # 3rd-Party (Tutorial) - LC #?
    def rod_cut_bottom_up_iteration(self, price, n): # O(n ^ 2) t ; O(n) s
        
        revenues = [0] * (n + 1)

        max_revenue = -sys.maxsize

        for i in range(1, n + 1):
            for j in range(1, i + 1):

                max_revenue = max( \
                    max_revenue, \
                    price[j - 1] + revenues[i - j] \
                )
            
            revenues[i] = max_revenue
        
        return revenues[n]


    '''

        Matrix Chain - Multiplication

    '''
    
    def matrix_chain_multiplication(self): # O() t ; O() s
        pass # TODO
    
    def matrix_chain_multiplication(self): # O() t ; O() s
        pass # TODO
    
    def matrix_chain_multiplication(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - LC #?
    def matrix_chain_multiplication(self, seq, i, j): # O(2 ^ n) t ; O(n) s
        
        if i == j: return 0

        min_ops = sys.maxsize

        for k in range(i, j):

            ops = \
                self.matrix_chain_multiplication( \
                    seq, i, k \
                ) + \
                self.matrix_chain_multiplication( \
                    seq, k + 1, j \
                ) + \
                seq[i - 1] * \
                seq[k] * \
                seq[j]
            
            min_ops = min(ops, min_ops)
        
        return min_ops
        
    # 3rd-Party (Tutorial) - LC #?
    def mcm_top_down_memoization(self, seq, i, j, memo): # O(n ^ 3) t ; O(n ^ 2) s
        
        if i == j: return 0

        if memo[i][j] >= 0:
            return memo[i][j]

        min_ops = sys.maxsize

        for k in range(i, j):

            ops = \
                self.mcm_top_down_memoization( \
                    seq, i, k, memo \
                ) + \
                self.mcm_top_down_memoization( \
                    seq, k + 1, j, memo \
                ) + \
                seq[i - 1] * \
                seq[k] * \
                seq[j]
            
            min_ops = min(ops, min_ops)
        
        memo[i][j] = min_ops

        return memo[i][j]
    
    # 3rd-Party (Tutorial) - LC #?
    def mcm_bottom_up_iteration(self, seq, n): # O(n ^ 3) t ; O(n ^ 2) s
        
        arr = [[0 for i in range(n)] for i in range(n)]
        # arr[i][j] = 0

        for len in range(2, n):
            for i in range(1, n - len + 1):

                j = i + len - 1

                if j == n: continue

                min_ops = sys.maxsize

                for k in range(i, j):

                    min_ops = min( \
                        min_ops, \
                        ( \
                            arr[i][k] + \
                            arr[k + 1][j] + \
                            seq[i - 1] * \
                            seq[k] * \
                            seq[j] \
                        )
                    )
                
                arr[i][j] = min_ops
        
        return arr[1][n - 1]
    
    
    # ! easy


    def coin_change(self): # O() t ; O() s
        pass # TODO

    def subset_sum(self): # O() t ; O() s
        pass # TODO

    def cutting_a_rod(self): # O() t ; O() s
        pass # TODO
    
    def painting_fence(self): # O() t ; O() s
        pass # TODO

    def longest_common_subsequence(self, a): # O() t ; O() s
        pass # TODO

    def longest_increasing_subsequence(self, a): # O() t ; O() s
        pass # TODO

    def min_cost_path(self): # O() t ; O() s
        pass # TODO

    def longest_common_substring(self, a): # O() t ; O() s
        pass # TODO

    def edit_distance(self): # O() t ; O() s
        pass # TODO

    def convex_hull(self): # O() t ; O() s
        pass # TODO
    
    def unique_paths(self): # O() t ; O() s
        pass # TODO

    
    # ! medium


    def knapsack(self): # O() t ; O() s
        pass # TODO

    def zero_or_one_knapsack(self): # O() t ; O() s
        pass # TODO

    def fractional_knapsack(self): # O() t ; O() s
        pass # TODO

    def unbounded_knapsack(self): # O() t ; O() s
        pass # TODO

    def edd_dropping_puzzle(self): # O() t ; O() s
        pass # TODO
    
    def word_break(self): # O() t ; O() s
        pass # TODO

    def vertex_cover(self, a): # O() t ; O() s
        pass # TODO

    def tile_stacking(self, a): # O() t ; O() s
        pass # TODO

    def box_stacking(self): # O() t ; O() s
        pass # TODO

    def partition(self, a): # O() t ; O() s
        pass # TODO

    def travelling_salesman(self): # O() t ; O() s
        pass # TODO

    def longest_palindromic_subsequence(self, a): # O() t ; O() s
        pass # TODO

    def longest_common_increasing_subsequence(self, a): # O() t ; O() s
        pass # TODO

    def distinct_subset_sums(self, a): # O() t ; O() s
        pass # TODO

    def weighted_job_scheduling(self): # O() t ; O() s
        pass # TODO
    
    def count_derangements(self): # O() t ; O() s
        pass # TODO
    
    def min_insertions_to_palindrome(self): # O() t ; O() s
        pass # TODO
    
    def adjacent_balls(self): # O() t ; O() s
        pass # TODO

    
    # ! hard

    
    def palindrome_partitioning(self, s): # O() t ; O() s
        pass # TODO
    
    def word_wrap(self): # O() t ; O() s
        pass # TODO
    
    def painters_partition(self): # O() t ; O() s
        pass # TODO
    
    def bridge_and_torch(self): # O() t ; O() s
        pass # TODO
    
    def matrix_chain_mult(self): # O() t ; O() s
        pass # TODO
    
    def max_sum_rect(self): # O() t ; O() s
        pass # TODO
    
    def max_profit(self): # O() t ; O() s
        pass # TODO
    
    def min_cost(self): # O() t ; O() s
        pass # TODO
    
    def arithmethic_progression(self): # O() t ; O() s
        pass # TODO
    
    def dp_on_trees(self): # O() t ; O() s
        pass # TODO
    
    def max_height(self): # O() t ; O() s
        pass # TODO
    
    def longest_repeating_substr(self): # O() t ; O() s
        pass # TODO


class DivideAndConquer: # ! Not Enough D&C work

    '''

        Divide & Conquer Algorithms

        - dividing problems into sub-problems to be solved recursively, then the result is combined
        
        Identification:

            - if problem may generate 2+ sub-problems of the 'same' kind that:
                - can be solved recursively
                - can be combined back for global result
        
        - eg. Merge & Quick Sorts, Binary Search

        Approach:

            - divide problem into 'a' sub-problems of size 'n/b'
                - a >= 1, b > 1
            - conquer by solving each sub-problem recursively
                - until it becomes really small / almost constant
            - combine the solution of sub-problems into an overall solution
                - ** this is optional
        
        Recurrence:

            - T(n) = a T(n/b) + work done to split problem & combine / merge all the sub-problems back
                - T - time to solve a problem
                - Time to solve entire problem = no. of sub-problems * Time to solve each sub-problem
                    + work done to split problem into sub-problems + work done to combine/merge all sub-problems
        
    '''

    def __init__(self): # O() t ; O() s
        pass # TODO

    
    # ! standard


    def merge_sort(self, a): # O(2 log n * n ~ n log n) t ; O(n) s

        def sort(a, b): # O(1) t ; O(1) s
            # * only 1 if-check before returning value
            # 1 check doesn't run if the other check passes
            if a <= b: return [a, b]
            else: return [b, a]
            '''
            # ! even if there's only 1 return case,
            there are 2 forced checks to be passed, for both items
            
            return [
                a if a <= b else b,
                b if b <= a else a
            ]
            '''

        def merge(a): # O(n log n) t ; O(n) s

            # O(1) t - base-case or O(log n * (n1 + n2) ~ log n * n - "average of both" - hacky opinion
            #   - rather n = total size of initial input array, so n is each sub-array's maximum-case scenario = n log n) t ;

            # O(n1 + n2 (left & right extra arrays) + s (resulting merged array)
            #   ~ n - "average of both" - hacky opinion
            #   - rather - same opinion as above (n1 & n2 are subset-lengths of n)
            #   ~ 1 - constant-space because even though a1 & a2 are extra arrays being used,
            #   - they are still returned values from the recursive calls = O(1) s ?

            # ! argument - but a1 & a2 can be argued to being used for merging, after dividing & conquering
            #   - & merging is part of the algo itself (as a "merge-sort")
            #   - so even if a1 & a2 are resulting arrays of recursive calls,
            #   - they can still be argued to be additions of space-complexity,
            #   - even though they're not "extra" space (- by your own terms) = n ) s

            # ! TODO: argue again

            if len(a) == 2:
                return sort(a[0], a[1])
            else:
                l = len(a) / 2

                # ! avoid adding sorted sub-arrays
                # * (will end up with merged but unsorted batches of sub-arrays)
                # return merge(a[:l]) + merge(a[l:])

                a1, a2 = merge(a[:l]), merge(a[l:])
                s = []

                while len(a1) and len(a2): # ! argument: both are iterated through simult,
                    # * so the time taken due to both of them should still be based on their "average lengths" - for all D&C merge-sort "hacky opinions"

                    ''' # ! argument: compare both cases in highest-level terms
                        less code: assign a.pop(0) in both cases to a value to append after if-else-check
                        more code; less space: no extra variable used (but could've been gc'd after its usage)
                    '''

                    if a1[0] <= a2[0]: # ! argument: but both arrays are popped from in different logic-lines (if-case) so
                        # * and this loop doesn't end until both are empty, so both arrays' lengths are exhausted before loop ends
                        # ! so O(t) is still O(n1 + n2) t - but still summarised to ~ O(n) t - where n = total size / length of initial input array
                        # * so n is each sub-array's maximum-case scenario

                        s.append(a1.pop(0))
                    else: s.append(a2.pop(0))

                    # * compare .pop()ing 1st elem with using an indexed loop
                    # * is .pop(0) on 1st item still O(1) t, even if it was O(n) t "in theory" (because of 1st item) - even if "stupid"
                    # * i.e. is .pop() based on iterating until found index - in O(n) t ;
                    # * or is it based on straight access of elem by index - in O(1) t constant time

                # ! wrong O(t) here - * total complexity - O(2 log n + n ~ log n + n) t ; O(n) s
                # ! even if the "merging while-loop" is implemented after "recursive calls" to "merge"
                # * don't forget that it's still exec'd on every "merge" since it's still a part of the "merge" function,
                # * so "merging while-loop" O(n) t shouldn't be added, but multiplied

                # ! so total complexity - O(2 log n * n ~ n log n) t ; O(n) s

                return s

        if len(a) == 2: return sort(a[0], a[1])
        if len(a) < 2: return a

        return merge(a)

    # 3rd-Party (Tutorial) - LC #?
    def merge_sort(self, a, l = None, u = None): # O(2 log n * n ~ n log n) t ; O(n) s

        def merge(a, l, m, u): # O(n) t ; O(n) s

            # O(n1 + n2 + (n1 + n2) + n1 + n2 ~ 3n1 + 3n2 ~ n1 + n2 - removing constants
            #   ~ n - "average of both" - hacky opinion
            #   - rather n = total size of initial input array, so n is each sub-array's maximum-case scenario = n ) t ;

            # O(n1 + n2 (left & right extra arrays) ~ n - "average of both" - hacky opinion
            #   - rather - same opinion as above (n1 & n2 are subset-lengths of n) = n ) s

            # ! argument: over here, left & right array are actually used as "extra" space in the "merge" section of the algo
            #   - and not used to return values of any recursive call in the algo (like the above "merge_sort()" option)
            # ! so O(1) s cannot be argued at all in this case

            n1 = m - l + 1
            n2 = u - m

            # temp left & right sub-arrays
            left = [0] * n1
            right = [0] * n2

            # copying data
            for x in range(n1): # O(n1)
                left[x] = a[l + x]

            for y in range(n2): # O(n2)
                right[y] = a[m + 1 + y]

            # merging data into array
            i, j, k = 0, 0, l

            while i < n1 and j < n2: # O(n1 + n2 ~ n - "average of both" - hacky opinion - rather n = total size of initial input array, so n is each sub-array's maximum-case scenario)
                if left[i] < right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1

            while i < n1: # O(n1)
                a[k] = left[i]
                i += 1; k += 1

            while j < n2: # O(n2)
                a[k] = right[j]
                j += 1; k += 1


        if not l or not u: # then start merge-sort all over
            l, u = len(a), len(a) - 1

        m = 0

        if l < u:
            m = (l + (u - 1)) // 2

            self.merge_sort(a, l, m) # O(log n) t - recursion with halved data ; O(1) s
            self.merge_sort(a, m + 1, u)
            merge(a, l, m, u) # O(n) t ; O(n) s when called

            # ! wrong O(t) here - * total complexity - O(2 log n + n ~ log n + n) t ; O(n) s
            # ! even if "merge" is called after "recursive calls" to "merge_sort"
            # * don't forget that it's still called on every "merge_sort",
            # * so "merge" O(n) t shouldn't be added, but multiplied

            # ! so total complexity - O(2 log n * n ~ n log n) t ; O(n) s

        return a # even if array is worked on by reference


    def quick_sort(self, a): # O( n/2 * 2 log n ~ n log n ) t ; O(1) s

        # ! all 'a' parameters are passed by reference,
        # * so input array 'a' will always be updated

        def swap(a, i, j): # O(1) t ; O(1) s
            tmp = a[j]; a[i] = a[j]; a[j] = tmp

        def sort(a): # O(1) t ; O(1) s
            if len(a) == 3:
                if a[0] > a[1]:
                    swap(a, 0, 1)
                if a[1] > a[2]:
                    swap(a, 1, 2)
            elif len(a) == 2:
                if a[0] > a[1]:
                    swap(a, 0, 1)
            return a

        # ! based on logarithmic recursive calls from merge-sort
        # * test pre-logic of adding while-loop O(t), before multiplying it by recursive calls

        def quick(a): # O( n/2 * 2 log n ~ n log n ) t ; O(1) s

            # ! wrong still - O( n/2 + 2 log n * n/2 ~ n + n log n ) t ;
            # * adding while-loop O(t) before still doesn't reduce o expected O(nlogn) t
            # * so best to regard the while-loop as being in the recursive function entirely,
            # * and not just being exec'd before recursive calls
            # ! so O(t) - O( n/2 * 2 log n ~ n log n ) t
            # O(1) s

            if len(a) <= 3:
                return sort(a) # O(1) t ; O(1) s
            else:
                f, l = 0, len(a) - 1
                m = math.floor(f + (l - f) / 2)

                # ! now, try using 2-pointer to find discrepancy-pairs, then swap
                
                while f < l: # ! TODO: "MAYBE wrong" termination-predicate ! visualize loop 1st
                    # O(n/2 ~ n) t ; O(1) s
                    
                    if a[f] > a[m] \
                        and a[l] < a[m]: # left > pivot & right < pivot - discrepancy-pair
                        swap(a, f, l)
                        f += 1; l -= 1
                    if a[f] < a[m]: # increment if no discrepancy
                        f += 1
                    if a[l] > a[m]: # decrement if no discrepancy
                        j -= 1

                # ! now, return the array-concatenation of both "quick" recursive-calls
                return quick(a[:m]) + quick(a[m:]) # O(2 log n ~ log n) t ; O(1) s

        return quick(a)

    def quick_sort(self, a): # O( n/2 * 2 log n ~ n log n ) t ; O(1) s

        # ! all 'a' parameters are passed by reference,
        # * so input array 'a' will always be updated

        def swap(a, i, j): # O(1) t ; O(1) s
            tmp = a[j]; a[i] = a[j]; a[j] = tmp

        def sort(a): # O(1) t ; O(1) s
            if len(a) == 3:
                if a[0] > a[1]:
                    swap(a, 0, 1)
                if a[1] > a[2]:
                    swap(a, 1, 2)
            elif len(a) == 2:
                if a[0] > a[1]:
                    swap(a, 0, 1)

        def quick(a): # O( n/2 * 2 log n ~ n log n ) t ; O(1) s
            if len(a) <= 3:
                sort(a)
            else:
                f, l = 0, len(a) - 1
                m = math.floor(f + (l - f) / 2)

                # ! now, try using 2-pointer to find discrepancy-pairs, then swap
                
                while f < l: # ! TODO: "MAYBE wrong" termination-predicate ! visualize loop 1st
                    
                    if a[f] > a[m] \
                        and a[l] < a[m]: # left > pivot & right < pivot - discrepancy-pair
                        swap(a, f, l)
                        f += 1; l -= 1
                    elif a[f] < a[m]:
                        f += 1
                    elif a[l] > a[m]:
                        j -= 1

                # ! now, make both "quick" recursive-calls
                quick(a[:m]); quick(a[m:])

        quick(a) # ! all method calls work with 'a' array by reference
        return a

    # 3rd-Party (Tutorial) - LC #?
    def quick_sort(self, a, l = None, u = None): # O(n * 2 log n ~ n log n) t ; O(1) s
        # ! argument: O(n^2) t still chosen by others - due to partition's while-loops argument
        # ! O(n) s also chosen due to the recursive-calls taking more stack memory

        def partition(a, l, u):
            # O( n/2 * ( (n/? ~ 1) + (n/? ~ 1) ~ (2n/? ~ n ~ 1) ) ~ n^2 or n ? = n (chosen) ) t ;
            # ~ O(n) t
            # O(1) s

            p, left, right = a[l], l, u

            while left < right: # O(n/2 * (2n/? ~ n / 1) ~ n^2 or n ? = n (chosen) ) t

                # ! argument: O(n^2) t still chosen by others - find out exactly why
                # * O(2n/? ~ n / 1) t - still chosen as constant time due to:
                #   pivot 'p' limit checks in both inner while-loops
                # * O(n/2) t - the outer while-loop's base-check

                while a[left] <= p \
                    and left < len(a) - 1: # O(n/? ~ n / 1) t
                    left += 1

                while a[right] > p \
                    and right > 0: # O(n/? ~ n / 1) t
                    right -= 1

                if left < right:
                    # now, swap
                    tmp = a[left]
                    a[left] = a[right]
                    a[right] = tmp

            # swap right with pivot
            tmp = a[l]
            a[l] = a[right]
            a[right] = tmp

            return right


        if not l or not u: # * then start quick-sort all over
            l, u = 0, len(a) - 1

        if l < u:
            i = partition(a, l, u) # O( n/2 * ( (n/? ~ 1) + (n/? ~ 1) ~ (2n/? ~ n ~ 1) ) ~ n^2 or n ? = n (chosen) ) t ; O(1) s
            self.quick_sort(a, l, i - 1) # O(log n) t ; O(1) s
            self.quick_sort(a, i + 1, u)

        return a


    ''' # * Median of Medians
        find median, m of an unsorted array such that:
        half of its elems < m ; & other half > m
        
        No need to sort 1st, before calc'ing middle-index - O(n log n)
        can use the Quick-Sort algo's process to find median mid-way
        
        idea 1:
        
        choose pivot element, rearrange elems based on left < m < right
        after each rearrangement, keep switching pivots:
        until difference in left & right elems' lengths <= 1, 
        then m is now median; or if difference in lengths == 1,
        m or its adjacent elem (in the longer side) is median
        
        idea 2:
        
        choose middle index as median inde, m, x & 1st pivot from start
        then keep rearranging & switch pivots back from median index
        until all left < m < right elems; with lengths-difference <= 1
        then the element at m is median, or its adjacent elem in the longer side
    '''
    def median_of_medians(self, a): # O() t ; O() s

        f, l = 0, len(a) - 1
        m = math.floor(f + (l - f) / 2) # function-scope median index

        def swap(a, i, j): # O(1) t ; O(1) s
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

        def median(a, f, l): # O() t ; O() s

            supposed_median = a[m]
            supposed_median_index = m
            
            while f < l: # ! TODO: "MAYBE wrong" termination-predicate ! visualize loop 1st
                
                left = a[f]
                right = a[l]

                # check for swap
                if left > supposed_median \
                    and right < supposed_median:
                    swap(a, f, l)
                    f += 1; l -= 1
                if left < supposed_median:
                    f += 1
                if right > supposed_median:
                    l -= 1

            # todo: base-case & recursive-case calls
            if supposed_median == a[m]:
                return supposed_median, m

            # ! TODO: Test this theory - recursive calls with the entire array
            # * for swapping to span across all elements around the middle-element (new supposed_median)
            # return median(a, 0, len(a) - 1) # ! base-case will return median if supposed_median ends up as middle element a[m]

            # ! wrong - will mix up sub-array sort-orders
            # TODO: Test
            elif supposed_median < a[m]:
                return median(a, m + 1, len(a) - 1)
            else: return median(a, 0, m - 1)

        return median(a, f, l)

    # * subset all medians & sub-medians & find subset's median
    def median_of_medians(self, a):

        pass

    # 3rd-Party (Tutorial) - LC #?
    def median_of_medians(self, a): # O(  ) t ; O() s

        def find_pivot(a, low, high): # O(  ) t ; O() s

            if high - low + 1 <= 9:
                sorted(a)
                return a[ int( len(a) / 2 ) ]

            medians = [0] * int(math.ceil( # O(n or ?) s
                (high - low + 1) / 5
            ))

            median_index = 0

            while high >= low: # O() t ; O() s

                tmp = [0] * min(5, (high - low + 1)) # O(n or ?) s

                for i in range(0, len(tmp)):
                    if low <= high:
                        tmp[i] = a[low]
                        low += 1

                sorted(tmp) # O(n log n) - quick-sort

                medians[median_index] = \
                    tmp[ int( len(tmp) / 2 ) ]

                median_index += 1

            return find_pivot(medians, 0, len(medians) - 1)

        def partition(a, low, high): # O( n/2 * (n1 + n2 ~ n or 1) ~ n^2 or n or 1) t ; O(1) s

            pivot = find_pivot(a, low, high) # * O(t/s) deliberately excluded here

            while low < high:

                while a[low] < pivot: low += 1
                while a[high] > pivot: high -= 1

                if a[low] == a[high]: low += 1

                # swap
                elif low < high:
                    tmp = a[low]
                    a[low] = a[high]
                    a[high] = tmp

            return high

        def median(a, k, low, high): # O(1) t ; O(1) s

            m = partition(a, low, high) # * O(t/s) deliberately excluded here

            length = m - low + 1

            if length == k:
                return a[m]
            elif length > k:
                return median(a, k, low, m - 1)
            else:
                return median(a, k - length, m + 1, high)


        # * - ?
        median = median(a, a / 2 + 1, 0, len(a) - 1)
        # todo: find out bodmas/pemdas on - a / 2 + 1

        return median


    def pow(self, x, n): # O() t ; O() s
        pass # TODO

    def closest_pair(self): # O() t ; O() s
        pass # TODO

    def karatsuba_mult(self): # O() t ; O() s
        pass # TODO

    def strassens_matrix_mult(self): # O() t ; O() s
        pass # TODO

    def max_subarray_sum(self): # O() t ; O() s
        pass # TODO

    def longest_common_prefix(self): # O() t ; O() s
        pass # TODO

    def convex_hull(self): # O() t ; O() s
        pass # TODO

    def quick_hull(self): # O() t ; O() s
        pass # TODO

    # binary search based

    def peak_elem(self, a): # O() t ; O() s
        pass # TODO

    def majority_elem(self): # O() t ; O() s
        pass # TODO

    def kth_elem(self): # O() t ; O() s
        pass # TODO

    def num_zeroes(self): # O() t ; O() s
        pass # TODO

    def rotation_count(self): # O() t ; O() s
        pass # TODO

    def unbounded_binary_search(self): # O() t ; O() s
        pass # TODO

    def median_of_sorted_arrays(self): # O() t ; O() s
        pass # TODO

    def painters_partition(self): # O() t ; O() s
        pass # TODO

    
    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! easy

    
    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! medium

    
    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! hard

    
    def meth(self): # O() t ; O() s
        pass # TODO


    def square_root(self): # O() t ; O() s
        pass # TODO

    def max_min_of_array(self): # O() t ; O() s
        pass # TODO

    def elem_frequency(self): # O() t ; O() s
        pass # TODO

    def tiling(self): # O() t ; O() s
        pass # TODO

    def inversion_count_using_merge_sort(self): # O() t ; O() s
        pass # TODO

    def skyline(self): # O() t ; O() s
        pass # TODO

    def search_2d_matrix(self): # O() t ; O() s
        pass # TODO

    def alloc_min_pages(self): # O() t ; O() s
        pass # TODO

    
    def meth(self): # O() t ; O() s
        pass # TODO


class Greedy: # ! Not Enough Greedy work

    '''

        Greedy Algorithms

        - opt for local / immediate / next best option, without planning for the next / future options / effects

        - make the locally-optimal choice that seems best atm, hoping to lead to a globally-optimal solution

        attributes:
            - easy to think of, with easy complexity analysis
            - hard to confirm / prove if optimal / correct
            - solutions might also be correct, but still not optimal
            - ?

        identification:
            - if a problem's sub-problem sets are very independent of each other
            - ?

        approach:
            - hit and trial to prove if solution is correct
            - can also go with mathematical definition
            - always look for next-best choice locally
                - if choice doesn't fit into solution, don't choose it
            - keep building the global solution

        notes:
            - most problems that can't be solved with greedy algo's:
                - can sometimes be solved with "Dynamic Programming", with certainty
                - eg. 'Fractional Knapsack' - best solved with greedy algo
                    - but '0/1 Knapsack' cannot be solved correctly with greedy algo's
                    - unless a "Dynamic Programming" algo is used as the solution

            - NB: Dynamic Programming (DP) is based on exhaustive search & using memoization
                for all solutions of sub-problems leveraged already

    '''

    def __init__(self): # O() t ; O() s
        pass # TODO

    
    # ! standard


    def load_balancing(self): # O() t ; O() s
        pass # TODO

    def coin_change(self): # O() t ; O() s
        pass # TODO

    '''
        
        Given a set of items, and a knapsack (or bag) with a max weight of items that it can hold
        each item with its weight should be picked out of the set to give you the most profit 
        
        Greedy algo well suited for fractional knapsack, but not 0/1 knapsack
        
        - 0/1 knapsack requires only 1 item with full-weight of knapsack bag be picked, or not at all
        - fractional knapsack allows picking of multiple items with weights that can sum up to knapsack total weight
        or
        - 0/1 knapsack requires all items of the same kind (eg. flowers) from source be picked at once, to fill up knapsack weight
        - whilst fractional knapsack allows picking of some of the items of the same kind (eg. flowers) from source to be picked up
        
        Greedy algo not suited for 0/1 knapsack since it only has 1 chance to select most-optimal solution
            - going with the 1st-best option might not be the most-optimal
            - this is why 0/1 knapsack is best solved with Dynamic Programming
        
    '''

    def knapsack(self): # O() t ; O() s
        pass # TODO


    # sort source 1st, then pick from lowest, until knapsack is full
    def fractional_knapsack(self, a, limit=20): # O(n log n + n) t ; O(n ~ 1) s

        source = list(a.items()) # convert input array into list of tuples
        # O(n) s ignored, because source is only re-holding input array

        source.sort(key = lambda i: i[1]) # O(n log n) t - sort by each item's 2nd item (value - "weight")

        knapsack = [] # O(n ~ 1) s - only holds the returning result, not required for the algo's further execution
        # ! on this level of problem-solving, always keep track of everything used
        # ! whether algo / new algo or data-structure / new data-structure
        # ! also know when & where each new algo / data-structure is used,
        # ! & how it affects the old algo / old data-structure

        # ! optimize all algo's, data-structure, & extra variable usage
        # ! whenever & wherever necessary - minimum input to maximum output is the ultimate goal

        # ! no extra variable, in this case is used to keep count of the sum
        # ! to be compared with the limit
        # ! instead, the 'limit's importance is considered to know whether it can be altered
        # ! if it can be altered (wouldn't be required in future) ??
        # ! then it is decremented instead, on every new value 'v' (item weight)
        # ! when limit gets to 0, then loop breaks

        # ! also know when for / while / do-while loops are necessary
        # ! & when innate indices / multiple indices / or extra (outer) indices are also necessary

        for k, v in source: # O(n) t
            if v - limit > 0: break
            else: limit -= v
            knapsack.append((k, v))

        return knapsack

    #
    def fractional_knapsack(self, a, b): # O() t ; O() s
        pass

    #
    def fractional_knapsack(self): # O() t ; O() s
        pass

    # 3rd-Party (Tutorial) - LC #?
    def fractional_knapsack(self, a, b): # O() t ; O() s

        class Item:

            def __init__(self, wt, val, ind):
                self.wt = wt
                self.val = val
                self.ind = ind
                self.cost = val // wt

            def __lt__(self, other):
                return self.cost < other.cost

        def get_max_value(wt, val, capacity): # O(n log n + n) t ; O(1) s

            items = [0] * len(wt) # used to re-hold the same input arrays

            for i in range(0, len(wt)): # ! disregarding O(t/s) here
                items[i] = Item(wt[i], val[i], i) # re-holding the same input arrays, as an 'Item' object

            items.sort(reverse=True) # O(n log n) t
            total_val = 0

            for item in items: # O(n) t
                cur_wt = int(item.wt)
                cur_val = int(item.val)

                if capacity - cur_wt >= 0:
                    capacity -= cur_wt
                    total_val += cur_val
                else:
                    fraction = capacity / cur_wt
                    total_val += cur_val * fraction
                    # capacity = int(capacity - (cur_wt * fraction))
                    break

            return total_val


        # * Test

        wt = [10, 40, 20, 30]
        val = [60, 40, 100, 120]
        capacity = 50

        max_val = get_max_value(wt, val, capacity)

        print("The maximum profit possible: ", max_val)

        return max_val


    def zero_or_one_knapsack(self): # O() t ; O() s
        pass # TODO


    '''
        
        Interview Scheduling Maximization
        
        Given a set of intervals, 
        find a set of non-overlapping or non-conflicting intervals of maximum size
        i.e. choose as many intervals as possible that don't conflict with each other
        
        approach:
            - sort intervals by their finish times
            - choose the earliest finish time interval
            - make sure interval should not conflict with the previous one
        
        - by choosing the earliest finish-time interval, more can be included
        
    '''

    # by 'conflict' intervals (sub-arrays with 2 items only) shouldn't ACTUALLY overlap with each other
    # not overlap in any 2 intervals' ranges
    def interval_scheduling(self, a: List[List[int]]) -> List[List[int]]: # O() t ; O() s

        # any sub-array's edge-number shouldn't be between another's edge-numbers (edge-numbers - interval)
        def funny_trick(a=a): # O() t ; O() s

            m = {}
            
            for i, n in enumerate(a):
                for k, v in m.items():
                    found = False
                    # ! in the case sub-arrays don't have sorted intervals
                    # * n.sort()
                    for x in n: # * even if n is a sub-array of 2 items (edge-numbers) only
                        if x >= k and x <= v: # ! intersections can also land on edges' equalities, in this case
                            # * otherwise: x > k and x < v
                            found = True
                            del a[i]
                            break
                    if not found:
                        m[n[0]] = n[1] # * n is sub-array of 2 numbers only (interval)

            return a

    # by 'conflict' adjacent intervals (sub-arrays with 2 items only) shouldn't ACTUALLY overlap with each other
    # not overlap in any 2 adjacent intervals' ranges
    def interval_scheduling(self, a: List[List[int]]) -> List[List[int]]: # O() t ; O() s

        # don't store arrays' digits as key-values in a map; just delete on intersections in adjacent arrays
        def funny_trick(a=a): # O() t ; O() s

            def compare(a, b):
                for n in a:
                    # b.sort() - if unsorted sub-arrays
                    if n >= b[0] and n <= b[1]:
                        return True
                return False

            for i in range(1, len(a)):
                curr, prev = a[i], a[i - 1]
                if compare(curr, prev):
                    del a[i]

            return a

    # * by 'conflict' lists shouldn't have any similar number
    def interval_scheduling(self, a: List[List[int]]) -> List[List[int]]: # O() t ; O() s

        # store arrays' digits as a key string in a map, then delete on duplicates
        def funny_trick(a=a): # O(nm ~ n^2 (on all unique arrays) ~ n (on many duplicate array-digits)) t ; O(n) s

            to_str = lambda a: ''.join(map(lambda n: f"{n}", a))

            m = {} # O(n) s

            for i, n in enumerate(a): # O(n) t
                for k, _ in m.items(): # O(m) t
                    found = False
                    for x in n: # O(n1) t ; n1 - average sub-array length - but 2 if sub-arrays are intervals of 2 edge-numbers only
                        if f"{x}" in k:
                            found = True
                            del a[i]
                            break
                    if not found:
                        m[to_str(n)] = 1

            return a


    # * by 'conflict' adjacent lists shouldn't have any similar number
    def interval_scheduling(self, a: List[List[int]]) -> List[List[int]]: # O() t ; O() s

        # don't store arrays' digits as a key string in a map; just delete on duplicates in adjacent arrays
        def funny_trick(a=a): # O() t ; O() s

            # Brute-force - O(ab ~ a or b - best to loop through shorter) t used here (sub-arrays with very few digits)
            # + only will only be iterating through 1 sub-array to check if exists in other,
            # with 'in' keyword # ! confirm: .py 'in' keyword - O(1) t or O(n)
            # * more optimized to use a hashmap - O(n) t, or sort / delete on duplicates, but unnecessary
            def compare(a, b): # = lambda a, b:
                for n in a if len(a) <= len(b) else b:
                    if n in a and n in b:
                        return True
                return False

            '''
            # iterating with next item - less-optimal - requires extra check for array out-of-bounds exception, on last iteration
            for i, n in enumerate(a):
                next = a[i + 1]
                if compare(n, next):
                    del a[i]

                if i + 2 == len(a): break # ! break out of loop at next to last index
                # to avoid array out-of-bounds exception on the next iteration
            '''

            # iterating with previous item - better - avoids array out-of-bounds exception, on last iteration
            for i in range(1, len(a)):
                curr = a[i]; prev = a[i - 1]
                if compare(curr, prev):
                    del a[i] # this time, delete the current item (as the "next" item duplicate)

            return a

    # * by 'conflict' lists shouldn't be equal
    def interval_scheduling(self, a: List[List[int]]) -> List[List[int]]: # O() t ; O() s

        def funny_trick(a=a): # O(n) t ; O(n~1) s - reversed array not really considered as added space 'complexity' (but is still added space)
            ra = a[::-1]
            for i, v in enumerate(a):
                if not i == ra.index(v): # ! confirm .py 'in' syntax O(n / 1) t ?
                    # if there's a new index, from the back (reversed array)
                    # then there's a duplicate value in array

                    # * so delete from both arrays
                    del a[i], ra[len(a) - 1 - i]
                    # for reversed, reverse the index too, to remove the exact mirror-item

            del ra # be sure to remove the reversed array
            return a # new array with no repeating elements
        
        # ! reverse-array is used in this case, because the hack of removing an item to check if it still exists isn't possible
        # ! because removing an item to put it back in (if it doesn't repeat) is 'stupid'


    # * by 'conflict' adjacent lists shouldn't be equal
    def interval_scheduling(self, a: List[List[int]]) -> List[List[int]]: # O() t ; O() s

        def funny_trick(a=a): # O(n) t ; O(1) s
            for i, v in enumerate(a):
                if v == a[i + 1]:
                    del a[i]
            return a


    #
    def interval_scheduling(self): # O() t ; O() s
        pass


    #
    def interval_scheduling(self): # O() t ; O() s
        pass


    # 3rd-Party (Tutorial) - sorting intervals-matrix by 'last-finish-time' - last edge of all intervals
    def interval_scheduling(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log n + n) t ; O(1) s (optimal_intervals array only holds result)
        
        intervals.sort(key = lambda i: i[1]) # O(n log n) t
        
        last_finish_time = float('-inf')

        optimal_intervals = [] # O(n) s - but ignored since it only holds result
        # intersecting intervals can also be deleted from input-array instead

        for interval in intervals: # O(n) t

            start = interval[0]

            if start > last_finish_time:

                end = interval[1]
                optimal_intervals.append(interval)
                last_finish_time = end
            # else: delete intervals[index] of this iteration, on intersection
            # then return updated input-array

        return optimal_intervals


    '''
    
        Huffman Coding / Variable-Length Coding
        
        Data Compression algorithm based on character-frequency of text-string data, in files mostly
        
        - using Priority Queues & Merkle-Tree Algorithm
        - eg. full-solution: https://github.com/Amo-Addai/api-feature-development/tree/main/compression/huffman-encode-decode/python
        - 
    
    '''


    def huffman_coding(self): # O() t ; O() s
        pass # TODO


    def huffman_coding(self): # O() t ; O() s
        pass # TODO


    def huffman_coding(self): # O() t ; O() s
        pass # TODO


    # TODO: 3rd-Party (Tutorial) - using a Priority-Queue & Merkle-Tree
    def huffman_coding(self, data: str): # O(n + n log n + n log k ~ n log k) t ; O(n + k ~ k) s ; k = total number of nodes

        # ! O( .. ~ n log k) t - ignoring non-dominant terms when analyzing logarithmic complexities in asymptotic rate
        # * O(n log k) t is larger than both O(n) t & O(n log n) t
        # ! O(n + k ~ k) s - ignoring non-dominant term O(n) s
        # * since k (number of nodes used for algo) > n (only number of string characters)

        class HuffmanNode:

            def __init__(self, freq, data, left, right):
                self.freq, self.data, self.left, self.right \
                    = freq, data, left, right

        def encode(str: str):

            mapping = {}

            for c in str:
                if not c in mapping: mapping[c] = 1
                else: mapping[c] += 1

            root = generate_tree(mapping)
            set_binary_code(root, '')

            print(' char | huffman code ')
            for char in mapping:
                print(
                    ' %-4r | %12s ' % \
                    (char, char_binary_mapping[char])
                )
            
            s = ''
            for c in str: s += char_binary_mapping[c]

            return s

        def generate_tree(mapping):

            keyset = mapping.keys()

            priority_queue = [] # ! deque() - Dequeue (Double-ended Queue) much better for implementation

            for c in keyset:
                node = HuffmanNode(mapping[c], c, None, None)

                # add to priority-queue
                priority_queue.append(node)

                # then sort priority-queue based on frequency
                priority_queue = sorted(
                    priority_queue,
                    key = lambda x: x.freq
                )

            while len(priority_queue) > 1:
                first = priority_queue.pop(0)
                second = priority_queue.pop(0)
                merge_node = HuffmanNode(
                    first.freq + second.freq,
                    '-', first, second
                )
                priority_queue.append(merge_node)
                priority_queue = sorted(
                    priority_queue,
                    key = lambda x: x.freq
                )
            
            return priority_queue
        
        def set_binary_code(node, s):

            if not node is None:

                if node.left is None and node.right is None:
                    char_binary_mapping[node.data] = encoded_str

                # left
                encoded_str += '0'
                set_binary_code(node.left, encoded_str)
                encoded_str = encoded_str[::-1]
                
                # right
                encoded_str += '1'
                set_binary_code(node.right, encoded_str)
                encoded_str = encoded_str[::-1]
        

        def decode(str: str):
            # TODO:
            pass


        encoded_str = ''

        # store resulting binary-code mapping for each character
        char_binary_mapping = {}

        code = encode(data)
        print(code)
        str1 = decode(code)
        print(str1)

        return code, str1


    '''
    
        Dijkstra's Algorithm
        
        Find the shortest path for each vertex from a given source vertex

        - 
    
    '''
    
    
    def dijkstra_algo(self): # O() t ; O() s
        pass # TODO
    
    
    def dijkstra_algo(self): # O() t ; O() s
        pass # TODO
    
    
    def dijkstra_algo(self): # O() t ; O() s
        pass # TODO
    

    # TODO: 3rd-Party (Tutorial) - using an Adjacency Matrix Graph
    def dijkstra_algo(self, mat): # O(n(n-1) ~ n^2) t ; O(n) s
        
        v = len(mat)
        visited = [False for i in range(v)]
        distance = [0 for i in range(v)]

        for i in range(1, v):
            distance[i] = float('inf')

        for i in range(v - 1):

            min_vertex = find_min_vertex(distance, visited)
            visited[min_vertex] = True

            for j in range(v):

                if mat[min_vertex][j] != 0 and \
                    not visited[j]:

                    new_distance = distance[min_vertex] + mat[min_vertex][j]
                    
                    if new_distance < distance[j]:
                        distance[j] = new_distance
        
        for i in range(v):
            print(i, ' ', distance[i])

        
        def find_min_vertex(distance, visited):
            
            min_vertex = -1

            for i in range(len(distance)):
                if (min_vertex == -1 or \
                    distance[min_vertex] > distance[i]) and \
                        not visited[i]:
                        min_vertex = i # ! confirm double-tab delimeter
            
            return min_vertex
    
    
    '''
    
        Maximum Non-Overlapping Segments
        
        Given a number of segments,
        find the maximum number of these segments that do not overlap with each other

        - similar to: Activity Selection Problem
            - where to choose the max non-overlapping tasks
    
    '''
    
    
    def max_non_overlapping_segments(self): # O() t ; O() s
        pass # TODO
    
    
    def max_non_overlapping_segments(self): # O() t ; O() s
        pass # TODO
    
    
    def max_non_overlapping_segments(self): # O() t ; O() s
        pass # TODO
    

    # 3rd-Party (Tutorial) - 
    def max_non_overlapping_segments(self, a, b): # O(n) t ; O() s
        pass # TODO
    
    
    '''
    
        Tie Ropes
        
        - 
    
    '''
    
    
    def tie_ropes(self): # O() t ; O() s
        pass # TODO
    
    
    def tie_ropes(self): # O() t ; O() s
        pass # TODO
    
    
    def tie_ropes(self): # O() t ; O() s
        pass # TODO
    

    # 3rd-Party (Tutorial) - 
    def tie_ropes(self): # O() t ; O() s
        pass # TODO
    

    '''
        # TODO: 
    '''

    
    def independent_sets(self): # O() t ; O() s
        pass # TODO

    def activity_selection(self): # O() t ; O() s
        pass # TODO

    def job_sequencing(self): # O() t ; O() s
        pass # TODO

    def huffman_coding(self): # O() t ; O() s
        pass # TODO

    def huffman_decoding(self): # O() t ; O() s
        pass # TODO

    def water_connection(self): # O() t ; O() s
        pass # TODO

    def egyptian_fraction(self): # O() t ; O() s
        pass # TODO

    def police_thieves(self): # O() t ; O() s
        pass # TODO

    def fitting_shelves(self): # O() t ; O() s
        pass # TODO

    def mice_to_holes(self): # O() t ; O() s
        pass # TODO

    
    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! easy


    def split_into_max_composite_nums(self, n): # O() t ; O() s
        pass # TODO

    def buy_max_stocks(self): # O() t ; O() s
        pass # TODO

    def min_max_amount(self): # O() t ; O() s
        pass # TODO

    def max_equal_sum(self): # O() t ; O() s
        pass # TODO

    def cuboid_to_cubes(self): # O() t ; O() s
        pass # TODO

    def max_custs_to_satisfy(self): # O() t ; O() s
        pass # TODO

    def min_rotations_to_unlock(self): # O() t ; O() s
        pass # TODO

    def min_rooms_for_events(self): # O() t ; O() s
        pass # TODO

    def min_cost_to_reduce_size(self): # O() t ; O() s
        pass # TODO

    def min_cost_to_acquire_coins(self): # O() t ; O() s
        pass # TODO

    def min_increment_by_ops(self): # O() t ; O() s
        pass # TODO

    def min_number_of_notes(self): # O() t ; O() s
        pass # TODO

    def smallest_subset_with_greatest_sum(self): # O() t ; O() s
        pass # TODO

    
    # ! medium


    def max_trains_for_stoppage(self): # O() t ; O() s
        pass # TODO

    def min_fibonacci_terms(self): # O() t ; O() s
        pass # TODO

    def divide_with_min_sum_diff(self): # O() t ; O() s
        pass # TODO

    def min_num_squares(self): # O() t ; O() s
        pass # TODO

    def min_diff_between_groups(self): # O() t ; O() s
        pass # TODO

    def min_num_platforms(self): # O() t ; O() s
        pass # TODO

    def min_vertices_to_traverse_matrix(self): # O() t ; O() s
        pass # TODO

    def largest_palindromic_num(self): # O() t ; O() s
        pass # TODO

    def smallest_num_given_digits_num_sum(self): # O() t ; O() s
        pass # TODO

    def lexi_largest_subsequence(self): # O() t ; O() s
        pass # TODO

    
    # ! hard


    def max_elems_made_equal(self): # O() t ; O() s
        pass # TODO

    def min_cash_flow(self): # O() t ; O() s
        pass # TODO

    def min_cost_to_cut_board(self): # O() t ; O() s
        pass # TODO

    def min_cost_to_process_tasks(self): # O() t ; O() s
        pass # TODO

    def min_time_to_finish_jobs(self): # O() t ; O() s
        pass # TODO

    def minimize_max_diff(self, a): # O() t ; O() s
        pass # TODO

    def min_edges_to_reverse(self, a): # O() t ; O() s
        pass # TODO

    def largest_cube(self): # O() t ; O() s
        pass # TODO

    def rearrange_str_chars(self): 

        # so no 2 adjacent chars are equal
        # so all equal chars become d distance away
        pass


class BackTracking: # ! Not Enough BTrack work

    '''

        BackTracking Algorithms

        Technique to solve a problem recursively, by making series of choices;
        and if any choice fails, it gets abandoned, for another one to be tried

        - trying out a possible solution, and "backtracking" when not optimal, 
        to try out other possible solutions, until the most-optimal solution is found

        - some extended form of recursion, but with some special properties

        - for problems where taking decisions back are necessary
            - change decisions at runtime, & take step(s) back for re-decisions
        
        Attributes:

        - useful for game dev programming
            - and game theory strategies
        
        Identification:

        - problem gives set of choices to be made
        - & set of constraints to follow
        - also consists of decision-making calls (Recursive)
            - with given choices & constraints
        
        - Difference b/n BackTracking & Recursion:
            - Recursion:
                - keep moving forward with solving a problem (recursively)
                - sub-problem after sub-problem, being solved recursively, at each stage
                - until the problem is fully-solved (at the base-case scenario)
            - BackTracking:
                - keep moving forward with solving a problem (recursively)
                - until current choice / option fails
                - then backtrack to starting / mid - (base) - point
                - then try another choice / option, & continue solving recursively
                - until that also fails, then loop recursion + backtracking
                - until problem is finally solved
        
        Approach:

        - Choices
            - Matrix / Tree/Graph - Depth-First Search Traversal
            - can be treated as DFS traversal of a tree
            - if a path is blocked, traversal backtracks until start/mid-point
            - then changes direction to traverse another node's path
        - Each Step of Choice
            - each step (node) has multiple choices (children)
            - (same decision-space at each step)
            - DFS traverse through by choosing 1 node's path
                - if a wrong choice was made:
                    - go back then make the next possible choice

        - DFS Traversal Options
            - Recursion - with Pre / Post / In - Order Traversals
            - ?
            - NB: BFS Traversals: not required for BackTracking
                - Queued While-Loop
                - ?
            - ?
        
        - Constraints
            - prevent traversal through certain paths / choice options
            - or at base-case / final destination
                - where the path reaches the end of the traversal
                    - with no other possible path
                    - whether this was a valid path or not
                - if path was valid:
                    - then the answer has been found
                    - or 1 of the answers have been found
                        - (& probably appended to a list of answers)
                - if path was not valid:
                    - then traversal will 'BackTrack'
                        - to the closest mid-point node
                        - to continue traversal to the next best option node

        - Example:
            - Matrix of 0s & 1s:
                - find the path of 0s, 
                - from a starting point (eg. 1 vertex)
                - to an ending point (eg. another vertex - at the opposite corner)
            - DFS Traversal from starting 0, based on 0-direction, till ending 0
                - Constraint: can only move in Cross-Directions (up, down, left, right)
                    - cannot move diagonally
                - if traversal reaches a 0 with more spots to move to
                    - i.e. that 0 is not at an ending vertex (ending point)
                    - but all spots to move to, have 1s,
                        - then base-case scenario (in recursion, for DFS Traversal),
                        - but not a successful path
                    - so Recursive DFS Traversal will 'BackTrack' to nearest 0 - midpoint
                    - (by recursively calling the '0' paths only)
                    - (whether left -> right / right -> left)
                    - (but still with Pre / Post / In - Order Traversal chosen)
                        - Recursive DFS Traversal will 'BackTrack' to nearest 0 - midpoint
                        - which has other 0 paths to traverse (DFS with Recursion)
                    
                    - if base case of all 0s do not land on an ending vertex point
                        - then there is no valid path (return False)
                    - if base case (whether 1st, or can also find multiple, then save all valid paths)
                        - then there is 1+ valid paths (return True / list of valid paths)
        
        Tips:

        - most problems involve a list / array / string data-structure
            - most of the inputs (lists/arrays/strings) can be backtracked through, 
                - whilst forming a Tree data-structure of results
        - most solutions involve a loop with recursive iterations
            - loop through base input array, 
                - with each item as the pivot,
                    - while recursing with entire input array each time
            - NB: without saving results to state, using a state-machine
                - like with Dynamic Programming
        

    '''

    def __init__(self): # O() t ; O() s
        pass # TODO

    
    # ! standard


    '''

        Subsets

        Given a set of distinct integers, nums,
        return all possible subsets (the power set)

        Constraints:
        - solution set must not contain duplicate subsets
        - must include both:
            - empty list as a subset - []
            - and the entire input array, 
                - also as a subset - [ ... ]
    
    '''
    
    # BackTrack with a Recursive Tree Structure of subset permutations
    def subsets(self, a): # O() t ; O() s
        
        # * 1st, set up Tree with root node value as the empty array []

        sub_set = []

        tree = DataStructures.Tree(
            r = DataStructures.Tree.TreeNode(
                v = sub_set, # value
                c = [] # children
            ) # root
        )

        root = tree.root

        def recurse(a, sub_set, node): # O() t ; O() s

            # ! Recursive base-case is handled just before recursing
            # * to prevent array-out-of-bounds error on recursion
            
            ''' # ! ALL DONE RECURSIVELY, to fill up the tree
             * for each item in list, 
                append to subset
                then append subset to node's children
             * then recurse, 
                without 1st item in array
                with that current subset
                & with that current child-node
            '''

            for i, n in enumerate(a):
                
                sub_set.append(n)

                # ! still wrong, because sub_set has to be confirmed to not already be in the tree
                # todo: so DFS search 'tree' to ensure that it doesn't already contain 'sub_set'
                exists = False
                # ! Tree.dfs() doesn't have a callback argument, so create one
                tree.dfs(root, sub_set, cb = lambda value: exists = value is not None)
                # if not exists: then set node_to_append, & .append(to node.children)

                node_to_append = DataStructures.Tree.TreeNode(
                    v = sub_set,
                    c = []
                )
                node.children.append(
                    node_to_append
                )

                # ! now, recurse on this iteration
                # ! skipping the current n's index

                # ! but make sure this recursion's sub-array has length > 1
                if len(a) > 1: # ! so recursion's BASE-CASE is actually handled here
                    
                    # * or you can a.pop(0) and then pass in 'a'

                    # * then base case of len(a) == 0: return
                    # could be at beginning of function

                    recurse(a[i + 1:], sub_set.copy(), node_to_append)

                    # ! pass in a copy of subset instead, 
                    # * so that this specific subset can be worked with after

                # ! and also pop out last appended item in subset
                # before next iteration, which will only need to work with next array item
                sub_set.pop()


        recurse(a, sub_set, root)

        # ! print out Tree
        # tree.print() # or: find a way to print(tree object)

        # ! now, tree contains all possible subsets, in all its nodes
        # TODO: TEST & Confirm

        res = []

        # use Breadth-First Search to list out all of the tree's nodes
        # ! Tree.bfs() doesn't have a callback argument, so create one
        tree.bfs(root, cb: lambda value: res.append(value))
        # ! or implement BFS search manually

        # * NB: BFS is better since children nodes are appended laterally
        # * so getting same / similar length subsets with BFS is faster & cleaner

        return res

    
    # BackTrack with a Recursion, without a Tree, 
    # but straight to a list of subset permutations
    def subsets(self, a): # O() t ; O() s
        
        res = [] # O(ignore) s - only holding result
        subset = [] # O( ?? ) s - ?
        # ! will keep appending number permutations, for each subset addition
        # * unless perhaps, you delete the current subset, after recursion

        def recurse_WRONG(a, subset): # O() t ; O() s
            if len(a) == 0: return

            for n in a:
                subset.append(n)
                if subset not in res: # check if subset doesn't already exist 1st
                    res.append(subset)
                a.pop(0)

                recurse(a, subset.copy())
                # ! pass in a copy of subset instead, 
                # * so that this subset can be deleted after

                del subset # ! delete it after recusive usage
                # * to remove all subsets when they become unnecessary

                '''
                    passing subset (as a list) be reference will affect original subset
                    but its only original use was to be appended to 'res', so no issue really
                    
                    # ! so it's still best to pass in a copy instead, and delete right after
                    else, there would be residual subset lists being affected and not being used any more
                '''

                # ! SUB-SET DOESN'T ACTUALLY HAVE TO BE DELETED, OR LEFT ALONE
                # ! INSTEAD, IT MUST POP OUT THE LAST APPENDED ITEM, 
                # ! SO IT DOESN'T INCLUDE IT IN THE NEXT ITERATION
        
        # ! CORRECT recursion
        def recurse(a, subset): # O() t ; O() s
            if len(a) == 0: return

            for n in a:
                subset.append(n)

                if subset not in res: # check if subset doesn't already exist 1st
                    res.append(subset)

                a.pop(0) # * still pop out 1st item in array, before recursing
                recurse(a, subset.copy()) # * remember to still pass in a copy of subset instead
                subset.pop() # * and also pop out last appended item in subset
                # before next iteration, which will only need to work with next array item


        recurse(a, subset)

        return res

    
    def subsets(self, a): # O() t ; O() s
        pass # TODO

    
    def subsets(self, a): # O() t ; O() s
        pass # TODO


    # TODO: TEST: 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix
    def subsets(self, a): # O() t ; O() s

        ans = []
        
        def recurse(nums, ans, curr, index):
            if index >= len(nums): return

            ans.append(curr)

            for i in range(index, len(nums)):

                if not nums[i] in curr:

                    curr.append(nums[i])
                    recurse(nums, ans, curr, i)
                    curr.pop()
        
        recurse(a, ans, [], 0)

        return ans

    
    # 3rd-Party (Tutorial) - LC #78 - 
    def subsets(self, nums: List[int]) -> List[int]: # O() t ; O() s
        
        ans = []; curr = []

        def recurse(nums, ans, curr, index):

            if index > len(nums): return
            
            ans.append(curr[:]) # append as a copy

            for i in range(index, len(nums)):

                if nums[i] not in curr:

                    curr.append(nums[i])
                    recurse(nums, ans, curr, i)
                    curr.pop()
        
        recurse(nums, ans, curr, 0)

        return ans


    '''
    
        Subset Sum

        -

    '''


    def subset_sum(self, a): # O() t ; O() s
        pass # TODO


    def subset_sum(self, a): # O() t ; O() s
        pass # TODO


    # 3rd-Party (Tutorial) - 
    def subset_sum(self, a): # O() t ; O() s
        pass # TODO


    '''

        Combination Sum

        Given a set of +ve candidate numbers (without duplicates),
        & a target number,
        Find all unique Combinations of candidates,
        where the candidate numbers sum up to the target number

        - The same repeated number may be chosen from candidates
        for an unlimited number of times

        - Constraints:
            - solution set must not contain duplicate combinations
            - ?
    
    '''
    

    # TODO: TEST: BackTrack with a Recursive Tree Structure of subset permutations
    def combination_sum(self, a, target = 7): # O() t ; O() s
        
        tree = DataStructures.Tree(
            r = DataStructures.Tree.TreeNode(
                v = None,
                l = None,
                r = None,
                c = []
                # ! this time, only working with .left & .right children nodes
                # * subsets in same depth-path not entirely related to each other, 
                # like with 'subsets' problem-solution with Tree Data-Structure
            )
        )

        root = tree.root
        subset = []

        # TODO: TEST
        def recurse(a, node, subset): # O() t ; O() s

            for n in a:

                if n == target:

                    # ! WRONG code - don't reset subset
                    # * which may already have numbers with sum < target
                    # subset = [n]
                    value = [n] # better

                    # ! NB: if preferred, can prevent duplication combinations, with .dfs search
                    exists = False
                    # ! Tree.dfs() doesn't have a callback argument, so create one
                    tree.dfs(root, value, cb: lambda value: exists = value is not None)
                    # if not exists: # then set to node.value

                    node.value = value # ! NOT 'subset'
                    # * instead, set node's value to a new array

                    # ! now, just return
                    # * because any other addition is > target
                    return

                    # ! NO NEED to remove 'n' from subset then continuing on to next iteration
                    # ! because a new 'value' list was created in place of 'subset'

                    # * can end recursion here as a base-case 
                    # and not have to recurse again with node's children
                    # plus that would even cause an infinite recursion issue, with this same 'n' later

                    # ! since duplicates are also not allowed, a faster addition would've been to
                    # * also remove this 'n' from 'a', but would have to use the global 'a' input array 1st
                    # ! with a recursive index this time
                
                elif n < target:

                    subset.append(n) # add number

                    subset_sum = sum(subset) # O(s) t
                    
                    if subset_sum > target:

                        # ! WRONG
                        # end recursion if subset's sum exceeds target
                        # ! return # good base-case for backtracking from failed paths

                        # * why return ? when in this case, both other cases will not continue on to next iteration ?

                        # elif subset_sum < target: will recurse with same node & subset's copy
                        # so next recursion can re-work with this same 'n'

                        # else: if subset_sum == target: will set node.value
                        # then recurse with both node .left & .right child nodes

                        # ! INSTEAD, pop out this n 'lifo'wise, then continue on to next iteration
                        subset.pop(); continue
                    
                    elif subset_sum < target: # also an 'elif' check, before equality-check
                        # so recursion can happen, with this current node's .value prop
                        # before dealing with node's children (.left & .right)

                        recurse(a, node, subset.copy()) # ! remember to pass in a copy, 
                        # * to avoid updates by reference

                    else: # if subset_sum == target: # check sum

                        # ! NB: if preferred, can prevent duplication combinations, with .dfs search
                        exists = False
                        # ! Tree.dfs() doesn't have a callback argument, so create one
                        tree.dfs(root, value, cb: lambda value: exists = value is not None)
                        # if not exists: # then set to node.value

                        node.value = subset # ! 'subset' this time
                        # now, can deal with node's children (.left & .right)

                        # ! but, use subset without current n again (like in 'subset > target' check)
                        # because any other recursion's appending will exceed > target
                        subset.pop() # * so pop out current iteration's n again

                        if not node.left:
                            recurse(a, node.left, subset.copy())
                        
                        if not node.right:
                            recurse(a, node.right, subset.copy())

                # else: pass # ! NO n > target check necessary
                # ! continue on to next iteration, with same subset


        recurse(a, root, subset)

        # ! print out tree
        # tree.print() # or: print(tree)

        res = []

        # ! BFS Traverse tree for all nodes' values
        tree.bfs(root, cb = lambda value: res.append(value) if value is not None else print('None Value Found (check if root)'))

        return res
    

    # TODO: TEST BackTrack with a Recursion, without a Tree, 
    # but straight to a list of subset permutations
    def combination_sum(self, a, target): # O() t ; O() s
        
        res = []
        subset = []

        def recurse(a, subset):

            for n in a:

                if n == target:

                    value = [n]
                    if value not in res:
                        res.append(value)
                    
                    return
                
                elif n < target:

                    subset.append(n)

                    subset_sum = sum(subset)

                    if subset_sum > target:

                        subset.pop()
                        continue

                    elif subset_sum < target:

                        recurse(a, subset.copy())
                    
                    else: # if subset_sum == target:

                        if subset not in res:
                            res.append(subset)
                        
                        subset.pop()

                        recurse(a, subset.copy())
        

        recurse(a, subset)

        return res

    
    def combination_sum(self, a, target): # O() t ; O() s
        pass # TODO
    
    
    def combination_sum(self, a, target): # O() t ; O() s
        pass # TODO
    
    
    # 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix
    def combination_sum(self, a, target): # O() t ; O() s

        res, curr = [], []
        
        def recurse(a, res, curr, target, index, subset_sum):
            if subset_sum == target:
                res.append(curr)
            elif subset_sum < target:
                for i in range(index, len(a)):
                    curr.append(a[i])
                    recurse( \
                        a, res, curr, \
                        target, i, \
                        subset_sum + a[i] \
                    )
                    curr.pop()
            return
        
        recurse(a, res, curr, target, 0, 0)

        return res
    

    # 3rd-Party (Tutorial) - LC #39 - 
    def combination_sum(self, a: List[int], target: int) -> List[List[int]]: # O() t ; O() s
        
        ans, cur = [], []

        def recurse(candidates, ans, cur, target, index, sum):
            if sum == target:
                ans.append(cur[:])
            elif sum < target:
                n = len(candidates)
                for i in range(index, n):
                    cur.append(candidates[i])
                    recurse(candidates, ans, cur, target, i, sum + candidates[i])
                    cur.pop()
            return
        
        recurse(a, ans, cur, target, 0, 0)

        return ans


    '''

        Letter Combinations of a Phone Number

        Given a string containing digits from 2-9 inclusive, 
        find all possible letter combinations 
        that the number could represent

        NB: in a 'feature phone', each digit (from 2-9 inclusive) in keyboard
        correspond to a set of letters (eg. 2 - abc, 3 - def, .. , 7 - pqrs, 9 - wxyz)

        - Constraints:
            - can only take 1 letter from each digit's set / string of letters
            - ?
        
        - Examples:
            - input: '23' ( 2 - abc & 3 - def )
            - approach: can brute-force through all possible letter combinations
                - but with only 1 letter from both numbers' string
            - output: [ 'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf' ]

        - Approach:
            - Steps:
                - create a map b/n digits & corresponding letters
                - set up digit-to-letters mapping, m
                - call recursive backtracking function with params:
                    - ans, m, digits, '', 0
                    - where:
                        '' - current combination string
                        0 - current index, in the digits string
                    - recursive steps:
                        - check if index < length of digits string
                        - check if combination string sum is equal to digits size
                            - add the current combination to the answer
                                & return from current recursive call
                        - after both checks:
                            - find corresponding string for current digit @ param index
                                - digit[index], eg. called curString
                                - curDigit = digits[index]; curString = m[curDigit]
                            - loop over curString:
                                - recursively call backtracking function
                                    - but add 1 to index
                                    - also add current character of curString to combination
                                - backtrack(ans, m, digits, combo + curString[i], index + 1)
                            - ?
    
    '''

    digit_letters_map = {
        2: 'abc', 3: 'def',
        4: 'ghi', 5: 'jkl', 6: 'mno',
        7: 'pqrs', 8: 'tuv', 9: 'wxyz'
    }
    
    # can only pick 1 letter from each digit's string
    def letter_combinations_of_phone_number(self, s): # O() t ; O() s

        if not s or len(s) == 0: return []

        res, combo = [], ''

        def recurse(s, combo):
        
            for d in s:

                try: d = int(d)
                except: d = None

                if not d or \
                    d in [0,1] or \
                        d > 9: # * d (digit) will never > 9
                    return # error - case (not base-case)

                cs = self.digit_letters_map[d]

                for c in cs: # ! TODO: confirm: this section works properly

                    # * now, recursively combine c with every 1 character, in every other digit

                    combo += c

                    if len(combo) > 1: # bad (or unnecessary 'perfection'-check)
                        # * find a way to combine letters from 2+ strings, before appending to result
                        res.append(combo)
                    
                    recurse(s[1:], combo)
                
                    # ! remove the current iteration's character (c)
                    # * to prevent repetitions in 1 digit's letters
                    # * can only pick 1 letter from each digit's string
                    combo = combo[ : len(combo) - 1 ]
        
        recurse(s, combo)

        return res

    
    # can also pick multiple letter from each digit's string
    def letter_combinations_of_phone_number(self, s): # O() t ; O() s
        pass # TODO
    
    # 
    def letter_combinations_of_phone_number(self, s): # O() t ; O() s
        pass # TODO
    
    # 
    def letter_combinations_of_phone_number(self, s): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix
    def letter_combinations_of_phone_number(self, s): # O() t ; O() s

        if len(s) == 0: return []
        
        ans = []
        combo = ''
        m = self.digit_letters_map


        def recurse(ans, m, digits, combo, index):

            if index > len(digits): return

            if len(combo) == len(digits):

                ans.append(combo)
                return
            
            curDigit = digits[index]
            curString = m[curDigit]

            for i in range(len(curString)):

                recurse( \
                    ans, \
                    m, \
                    digits, \
                    combo + curString[i], \
                    index + 1 \
                )

        recurse(ans, m, s, combo, 0)

        return ans
    
    # 3rd-Party (Tutorial) - LC #17 - 
    def letter_combinations_of_phone_number(self, digits): # O() t ; O() s
        
        ans = []

        if len(digits) == 0: return ans

        m = self.digit_letters_map

        def backtrack(ans, m, digits, combination, index):

            if index > len(digits): return

            if len(combination) == len(digits):
                ans.append(combination[:])
                return
            
            curDigit = digits[index]
            curString = m[curDigit]

            for i in range(len(curString)):

                backtrack( \
                    ans, \
                    m, \
                    digits, \
                    combination + curString[i], \
                    index + 1 \
                )
        
        backtrack(ans, m, digits, '', 0)

        return ans


    '''

        Palindrome Partitioning

        Given a string s, partition s such that 
        every substring of each partition is a palindrome
        return all possible palindrome partitioning of s

        - Example:
            - s = 'aab'
            - output: [ [ 'aa', 'b' ], [ 'a', 'a', 'b' ] ]
        
        - Approach:
            - 
    
    '''
    
    # adding palindrome-partitions to result array
    def palindrome_partitioning(self, s): # O() t ; O() s

        if len(s) == 0: return []
        elif len(s) == 1: return s

        sub_str = ''
        partition = []
        res = []
        
        is_palindrome = lambda s: s == s[::-1] # O(n ~ 1) t
        
        def recurse(s, sub_str, partition, res):

            if len(s) == 0: return

            for c in s:

                sub_str += c

                if is_palindrome(sub_str):
                    partition.append(sub_str)

                recurse(s[1:], sub_str, partition, res)

                sub_str = sub_str[ : len(sub_str) - 1 ]

            # ! TODO: Confirm: append partition to res after entire iteration of current 's'
            res.append(partition)

        recurse(s, sub_str, partition, res)

        return res

    
    # forming palindrome-partitions into a tree, then traversing back into a result array
    def palindrome_partitioning(self, s): # O() t ; O() s
        pass # TODO
    
    def palindrome_partitioning(self, s): # O() t ; O() s
        pass # TODO
    
    def palindrome_partitioning(self, s): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix
    def palindrome_partitioning(self, s): # O() t ; O() s

        is_palindrome = lambda s: s == s[::-1]
        
        def dfs(s, tmp, ans):
            if len(s) == 0 and len(tmp) > 0:
                ans.append([tmp])
                return
            
            for i in range(1, len(s)):
                segment = s[:i] # s.substring(0, i) - i inclusive / exclusive
                if is_palindrome(segment):
                    tmp.append(segment)
                    dfs(s[i:]) # s.substring(i) - i inclusive / exclusive
                    tmp.pop(len(tmp) - 1) # pop out last item
                    # or just: tmp.pop()
        
        tmp, ans, = [], []

        dfs(s, tmp, ans)

        return ans
    
    # 3rd-Party (Tutorial) - LC #131 - using DFS Approach (on string data-structure ; not tree/graph)
    def palindrome_partitioning(self, s): # O() t ; O() s
        
        res, tmp = [], []

        def is_pali(s):
            
            i, j = 0, len(s) - 1

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        def dfs(s):

            if len(s) == 0 and len(tmp) > 0:
                res.append(tmp[:])
                return
            
            n = len(s) + 1

            for i in range(1, n):
                seg = s[:i]
                if is_pali(seg):
                    tmp.append(seg)
                    dfs(s[i:])
                    tmp.pop()

        dfs(s)

        return res


    '''

        Rat in a Maze

        Given a maze (as a 2D-Array / matrix / graph), with some blocked paths / obstacles / dead-ends,
        a rat starts from the top-left corner, & has to reach the bottom-right corner,
        
        - matrix can have 0s (for blocked paths) & 1s (for valid paths)
            - 
        
        - Approach:
            
            - Choices:
                - decision-space: 
                    - can only either go in x-direction (left / right) 
                    - or in y-direction (up / down)
                    -
            
            - Recursion:
                - Go in either x / y direction
                - if cannot go in either direction:
                    - discard / go back in opposite direction
                    - to previous cell in maze
                - 
        
        - Constraints:
            - can only move in cells having value '1'
            - cell (row / col value) must be within the maze
                (bounds of the matrix / 2D-Array)
            - 

        - Goal:
            - 
    
    '''
    
    def rat_in_maze(self): # O() t ; O() s
        pass # TODO
    
    def rat_in_maze(self): # O() t ; O() s
        pass # TODO
    
    def rat_in_maze(self): # O() t ; O() s
        pass # TODO
    
    def rat_in_maze(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix (wrong) - # TODO: Confirm why wrong
    def rat_in_maze(self, mat): # O() t ; O() s

        # 1st, create empty matrix, for holding rat's path in maze
        board = [[] for _ in range(0, len(mat))] # O(n ^ 2 or n * m) s ; 
        # but only holds resulting path, so is not being considered here

        def recursion(maze, x, y, board):

            if x == n - 1 and \
                y == n - 1 and \
                    maze[x][y] == 1:
                    board[x][y] = 1
                    return True
            
            if recursion(maze, x + 1, y, board):
                return True # can go in x-direction

            if recursion(maze, x, y + 1, board):
                return True # can go in y-direction
            
            # backtrack move (cannot go in either direction)
            board[x][y] = 0
            return False
        
        recursion(mat, 0, 0, board)

        return board
    
    # 3rd-Party (Tutorial) - 
    def rat_in_maze(self, maze: List[List[int]]): # O( 2 ^ ( n ^ 2) ) t ; O(n ^ 2) s

        def is_safe(maze, x, y, n):

            if 0 <= x < n and \
                0 <= y < n and \
                    maze[x][y] == 1:
                    return True
            
            return False
        
        def solve_maze(maze, x, y, soln, n):

            # base-case
            if x == n - 1 and \
                y == n - 1 and \
                    maze[x][y] == 1:
                    soln[x][y]= 1
                    return True

            if is_safe(maze, x, y, n):

                soln[x][y] = 1

                # x - dir, x is rows, downwards
                if solve_maze(maze, x + 1, y, soln, n):
                    return True
                
                # y - dir, y is cols, horizontally
                if solve_maze(maze, x, y + 1, soln, n):
                    return True
                
                # backtrack
                maze[x][y] = 0

            return False
        
        soln = [ \
            [ \
                0 for j in range(len(maze[0])) \
            ] \
            for i in range(len(maze)) \
        ]

        n = len(maze)
        
        if solve_maze(maze, 0, 0, soln, n):
            for i in soln:
                for j in i:
                    print( \
                        str(j), \
                         ' ', \
                         end = ' ' \
                    )
                print(' ')


    def rat_in_a_maze(self): # O() t ; O() s
        pass # TODO


    '''

        N-Queens (Chess Problem with Queen pieces)

        Given a Chess board of nxn (n^2) size and n Queens,
        put the n Queens on the board, (n size of board == n number of Queens)
        in a way that they cannot attack each other
        (based on the Queen piece's possible moves - Complete Compass)

        - given a matrix (representing the chess board) filled with 0s,
            - place n number of 1s (Queens) in a non-attacking way

        - Approach:

            - Choices:
                - each Queen can move:
                    - horizontally in-row
                    - vertically in-col
                    - diagonally too, across cells
                - can only choose a cell to place a Queen where:
                    - its moves cannot intersect with another's
            
            - Recursion:
                - if choices do not work out:
                    - discard or undo current move
                    (backtracking to previous step)

        - Constraints:
            - ensure no move intersections
                - check if each cell is safe 1st

        - Goal:
            - end recursion when columns are exhausted
        
        - Hint:
            - The Knight can move to the cells, that The Queen cannot
        
    '''
    
    def n_queens(self): # O() t ; O() s
        pass # TODO
    
    def n_queens(self): # O() t ; O() s
        pass # TODO
    
    def n_queens(self): # O() t ; O() s
        pass # TODO
    
    def n_queens(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix
    def n_queens(self, board): # O() t ; O() s
        
        def is_safe(board, row, col, size):

            # loop through left-sided columns
            for c in range(col, len(board[0])):
                if board[row][c] == 1:
                    return False
            
            # loop through upper-left rows & cols (diagonally)
            # for:
            if board[r][c] == 1: return False

            # loop through lower-left rows & cols (diagonally)
            # for:
            if board[r][c] == 1: return False
        
            return True
        
        def save_the_queen(board, col):

            cols_size = len(board[0]) - 1

            if col > cols_size:
                return True
            
            for r in range(0, len(board)):
        
                if is_safe(board, r, col, cols_size):

                    # make move
                    board[r][col] = 1

                    if save_the_queen(board, col + 1):
                        return True
                
                    # BackTrack move
                    board[r][col] = 0

            return False
        
        res = None # todo: should pass into recursive function
        # * to be set (triggered) to True, once & for all, on success
        # ! should be False by default
        # todo: & adjust recursive function save_the_queen; to trigger 'res'

        save_the_queen(board, 0)

        return res

    
    # 3rd-Party (Tutorial) - 
    def n_queens(self, board): # O(n!) t ; O(n) s

        # O(t) - for each col, traversing through n rows, & n depth of recursive calls
        # so base complexity n ^ n time
        # however, recursive calls only happen for remaning n-queens only
        # i.e. after placing 1st queen, there are n - 1 options to place the others
        # so recursive part: n * T(n - 1) time
        # and considering the is_safe() call runs for n times for n cols
        # so is_safe part: n & 2 time
        # so total: T(n) = O(n ^ 2) + n * T(n - 1)
        # T(n) = O(n ^ 2) ( O( (n - 2)! ) ) ~~ O(n!) t
        # * so: O(n!) t

        # O(s) - 'n' recursive calls at a time, on the call-stack
        # so there will be linear space-complexity
        # * can assume n x n board requires n ^ 2 space
        # but that's not actually part of the algo
        # only auxillary space algo consumes is considered
        # * so not included in the already linear space being used
        # * so: O(n) s

        def is_safe(board, row, col, size):

            # no queen horizontally
            for i in range(col):

                if board[row][i] == 1:
                    return False
            
            # upper-half
            for i, j in zip( \
                range(row, -1, -1), \
                range(col, -1, -1) \
            ):
                if board[i][j] == 1:
                    return False
            
            # lower-half
            for i, j in zip( \
                range(row, size, 1), \
                range(col, -1, -1) \
            ):
                if board[i][j] == 1:
                    return False
            
            # else, this is the right cell to place a queen
            return True
        
        def save_queens(board, col, size):

            if col >= size: return True

            for i in range(size):

                if is_safe(board, i, col, size):

                    board[i][col] = 1

                    if save_queens(board, col + 1, size):
                        return True
                    
                    # backtrack
                    board[i][col] = 0
            
            return False

        #  
        size = len(board)
        res = save_queens(board, 0, size)

        if not res: print('No Solution')
        else:
            for i in board:
                for j in i:
                    print(str(j), ' ', end=' ')
                print(' ')
        
        return res

    def n_queen(self): # O() t ; O() s
        pass # TODO


    '''

        Knight's Tour

        Given a n x n chess board, and a Knight, with its 'jumping' moves,
        (a knight's moves go beyond the queen's moves - vertically, horizontally, & diagonally)
        make the knight visit every single cell on the board, with all its movements

        - Approach:

            - Choices:
                - knight has maximum 8 possible moves
                    - nearest cells to the knight that the queen cannot access
                    - the knight accesses those cells by 'jumping' to them
                - movement coordinates:
                    - (i + 2, j + 1)    or    (i + 1, j + 2)
                    - (i - 1, j + 2)    or    (i - 2, j + 1)
                    - (i - 2, j - 1)    or    (i - 1, j - 2)
                    - (i + 1, j - 2)    or    (i + 2, j - 1)
            
            - Recursion:
                - checking if solution was found
                    - at any move choice made
                - if no choice is left to move forward:
                    - discard the current move
            
            - BackTracking:
                - the 'discarding' sub-step above
                    - where we eject out decision
                        - for the current cell

        - Constraints:
            - knight can move to a cell only once
                - cannot move to an already visited cell
            - knight cannot move outside the chess board
                - cannot go ahead of the last (n - 1) column
                - cannot go ahead of the last (n - 1) row
            - moveIsValid if:
                - row, col < N & value of cell = 0

        - Goal:
            - to find the path / tour
                - that knight takes to visit
                    - each cell exactly once
        
    '''
    
    def knights_tour(self): # O() t ; O() s
        pass # TODO
    
    def knights_tour(self): # O() t ; O() s
        pass # TODO
    
    def knights_tour(self): # O() t ; O() s
        pass # TODO
    
    def knights_tour(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix
    def knights_tour(self, board): # O() t ; O() s

        size = len(board)

        # paths a Knight can take
        x_path = [2,1, -1,-2, -2,-1, 1,2]
        y_path = [1,2, 2,1, -1,-2, -2,-1]

        def move_is_valid(board, row, col): return True # TODO
        
        def recurse(board, row, col, step):

            # last step check
            if step == n**2: return True # TODO

            for i in range(size):

                r = row + x_path[i]
                c = col + y_path[i]

                if move_is_valid(board, r, c):

                    step += 1
                    board[r][c] = step

                    if recurse(board, r, c, step + 1):
                        return True
                    
                    # backtrack move
                    step -= 1
                    board[r][c] = 0
            
            return False
        
        # ! TODO: should set 'res' as a 'callback' argument in recursive function
        res = recurse(board, 0, 0, 1)

        return res
    
    # 3rd-Party (Tutorial) - 
    def knights_tour(self, board): # O( 8 ^ (n ^ 2) ) t ; O(n ^ 2) s

        # O(t) - max 8 choices (knight moves) can be made, with board as matrix of n x n size
        # * so: O( 8 ^ (n ^ 2) ) t

        # O(s) - recursive function can be called for n rows & n cols at a time
        # so call-stack may have n^2 recursive calls at a time
        # * so: O(n ^ 2) s

        size = len(board)
        x_path = [2,1, -1,-2, -2,-1, 1,2]
        y_path = [1,2, 2,1, -1,-2, -2,-1]

        def move_is_valid(board, row, col):

            if 0 <= row < size and \
                0 <= col < size and \
                    board[row][col] == -1:
                    return True
            
            return False
        
        def recurse(board, row, col, step):

            # last step check
            if step == n**2: return True

            for i in range(size):

                r = row + x_path[i]
                c = col + x_path[i]

                if move_is_valid(board, r, c):

                    board[r][c] = step

                    if recurse(board, r, c, step + 1):
                        return True
                    
                    board[r][c] = -1
            
            return False
        
        board[0][0] = 0
        step = 1
        size = len(board)

        if recurse(board, 0, 0, 0):
            for i in range(size):
                for j in range(size):
                    print(board[i][j], ' ', end=' ')
                print(' ')
        else: print('solution does not exist')


    def knights_tour(self): # O() t ; O() s
        pass # TODO


    '''

        Boggle 'Word Search'

        Given a matrix (or board) of characters,
        (with each cell containing 1 character)
        and a dictionary / set of words (or not),
        find all words that can be formed,
        from the characters in the matrix or board

        - either from data-structure of words,
            - or all possible words in general
        - either by sequence of adjacent characters / cells,
            - or randomly - accessed cells
        - either cells cannot be revisited, regardless of the words found 1st
            - or cells can be revisited,
                - so all expected / possible words can also be found
                - if all their characters exist in the matrix or not
                - regardless of intersections between words' characters
            - NB: if cells cannot be revisited:
                - some characters might be 'taken' by words found first
            - or, perhaps:
                - cells can only be revisted,
                    - after a given word has been found
                    - so revisited cells are reset (from '1' to '0')
                        - when any given word is found
                - this way, any 1 given word cannot be found
                    - by revisiting cells
                        - in case, multiple instances of a character is required
                        - eg. 'book' required 2 'o's, if they both exist in matrix
                - after finding any 1 given word
                    - all cells reset (from '1' to '0')
                    - so the next word can be found
                        - with NO already visited cells
        - default constraint-option chosen:
            - sequence of adjacent cells
            - only words from data-structure of words
            - cells can only be visited once, regardless of the words found 1st
        
        - Approach:

            - with Default Chosen Option:
                - words from data-structure / bag of words
                - words by sequence of adjacent characters / cells

            - Choices:
                - in order to look for words, with default chosen option
                    - can move in all eight directions of any given cell
                    (sequence of adjacent cell chosen option)
                - can move to:
                    - (i, j + 1)        or    (i, j - 1)       or
                    - (i + 1, j - 1)    or    (i + 1, j + 1)   or
                    - (i - 1, j + 1)    or    (i + 1, j)       or
                    - (i - 1, j)        or    (i - 1, j - 1)
            
            - Context:
                - matrix initially filled up with 0s
                - cells updated to 1s when visited
                    - matrix keeps track of visited cells with 1s
                - so a cell can only be visited when:
                    - it's in context (in range of the matrix)
                    - & when its value is 0 (not already been visited)
            
            - Recursion:
                - about checking if a word will be found
                    - with the character choice that was made
                        - in the given recursion
                - in the case when a roadblock is reached
                    - no choice left to move to
                        - but still, no word found at the roadblock
                    - at a corner or any blocked cell in the matrix
                        - cannot move to any other unvisited cell
                        - also cannot move outside the matrix
                    - then current move has to be discarded
                        - and BackTracking is required
                        - going back previous moves
                            - until can move to another cell choice again
                - TODO: Find the entire algo' in the tutorial

        - Constraints:
            - can form only words from data-structure of words
            - movement through sequence of adjacent cells only
                - i.e. only in all 8 directions of a given cell
                - 2 vertically, horizontally, & diagonally
            - cannot revisit already visited cells / characters
            - cannot go outside of the matrix
                - cannot go ahead of last / n - 1 column
                - cannot go ahead of last / n - 1 row

        - Goal:
            - to find either words in a given list
                - or any other data-structure
            - or: to find all possible words
            - so find all words present in the boggle (or given matrix)
                - by trying every possible combination
        
    '''
    
    def boggle_word_search(self): # O() t ; O() s
        pass # TODO
    
    def boggle_word_search(self): # O() t ; O() s
        pass # TODO
    
    def boggle_word_search(self): # O() t ; O() s
        pass # TODO
    
    def boggle_word_search(self): # O() t ; O() s
        pass # TODO
    
    # 3rd-Party (Tutorial) - pseudocode-algo # TODO: Test & Fix
    def boggle_word_search(self, boggle, word_map): # O() t ; O() s

        M, N = len(boggle), len(boggle[0])
        visited = [[0 for i in range(0, N)] for i in range(0, M)]
        
        def cell_is_valid(row, col, visited):

            return \
                row is not None and col >= 0 and \
                row < M and col < N and \
                visited[row][col] == 0
        
        def word_is_valid(word):
            return word in word_map
        
        def recurse(boggle, visited, row, col, word):

            for i in range(0, M):
                for j in range(0, N):

                    # mark cell as visited
                    visited[i][j] = 1

                    # include letter of cell
                    word = word + boggle[i][j]

                    # check if word is valid
                    if word_is_valid(word):
                        print('Valid: ', word)
                        return True

                    # iterate through choices, & update row - column

                    if cell_is_valid(row, col, visited):
                        recurse(boggle, visited, row, col, word)
                    
            # mark cell as unvisited
            visited[row][col] = 0

            return False
    
        # ! TODO: MUST exec recursive function in iteration
        # for all cells in matrix
        # * for i in range(M): for j in range(N):
        res = recurse(boggle, visited, 0, 0, '')
        # recurse( will already be printing found words )

        return res
    
    # 3rd-Party (Tutorial) - 
    def boggle_word_search(self, boggle, my_dict): # O(8 ^ (mn)) t ; O(mn) s

        # O(t) - maximum 8 choices to make at each cell 
        # & m x n size of matrix (boggle) of words
        # * so: O(8 ^ (mn)) t

        # O(s) - m x n maximum number of recursive calls
        # happening on the call stack at a point in time
        # * so: O(mn) s

        m = len(boggle)
        n = len(boggle[0])

        def is_valid(row, col, visited):

            if 0 <= row < m and \
                0 <= col < n and \
                visited[row][col] == 0:
                return True
            
            return False
        
        def find_words(boggle, visited, i, j, word):

            word = ''.join( \
                [word, boggle[i][j]] \
            )

            visited[i][j] = 1

            if word in my_dict:
                print(word)

            for row in range(i - 1, i + 2):
                for col in range(j - 1, j + 2):

                    if is_valid(row, col, visited):

                        find_words(boggle, visited, row, col, word)
            
            visited[i][j] = 0
            # * in this case, not returning bool result
            # just printing found / valid words
        
        visited = [ \
            [0 for j in range(n)] \
            for i in range(m) \
        ]

        for i in range(m):
            for j in range(n):
                find_words(boggle, visited, 0, 0, '')


    # * Others


    def m_coloring(self): # O() t ; O() s
        pass # TODO

    def hamiltonian(self): # O() t ; O() s
        pass # TODO

    def sudoku(self): # O() t ; O() s
        pass # TODO

    def magnet_puzzle(self): # O() t ; O() s
        pass # TODO

    def remove_invalid_parenthesis(self): # O() t ; O() s
        pass # TODO

    def generate_gray_codes(self): # O() t ; O() s
        pass # TODO

    def string_permutations(self): # O() t ; O() s
        pass # TODO

    
    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! easy


    def print_subsets(self): # O() t ; O() s
        pass # TODO

    def is_sum_str(self): # O() t ; O() s
        pass # TODO

    def possible_paths(self): # O() t ; O() s
        pass # TODO

    def bitmasking_distinct_subsets(self): # O() t ; O() s
        pass # TODO

    def path_from_source(self): # O() t ; O() s
        pass # TODO

    def print_paths_from_source(self): # O() t ; O() s
        pass # TODO

    def print_strings_using_spaces(self): # O() t ; O() s
        pass # TODO

    
    # ! medium


    def tug_of_war(self): # O() t ; O() s
        pass # TODO

    def eight_queens(self): # O() t ; O() s
        pass # TODO

    def combinational_sum(self): # O() t ; O() s
        pass # TODO

    def warnsdorff_for_knights_tour(self): # O() t ; O() s
        pass # TODO

    def paths_in_maze(self): # O() t ; O() s
        pass # TODO

    def max_num_by_k_swaps(self): # O() t ; O() s
        pass # TODO

    
    # ! hard


    def power_set(self): # O() t ; O() s
        pass # TODO

    def word_break(self): # O() t ; O() s
        pass # TODO

    def set_to_k_subsets(self): # O() t ; O() s
        pass # TODO

    def longest_route_in_matrix(self): # O() t ; O() s
        pass # TODO

    def shortest_safe_route(self): # O() t ; O() s
        pass # TODO

    def print_n_queen_solns(self, a): # O() t ; O() s
        pass # TODO

    def longest_common_subsequence(self, a): # O() t ; O() s
        pass # TODO


class Iteration:

    '''
        
        Iteration

        -

    '''

    def __init__(self): # O() t ; O() s
        pass # TODO

    
    # ! standard


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! easy


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! medium


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! hard


    def meth(self): # O() t ; O() s
        pass # TODO


class Recursion:

    '''
        
        Recursion

        -

    '''

    def __init__(self): # O() t ; O() s
        pass # TODO

    
    # ! standard


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! easy


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! medium


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! hard


    def meth(self): # O() t ; O() s
        pass # TODO


class Mathematical: # ! Not Enough Math work

    '''
        
        Math Problems

        # ! NB:

        All Math Problems can be solved with mathematical formulae
        # * most of the time, bringing solutions' speed from linear to constant time-complexities
        # ! O(n) t ~ O(1) t | with already O(1) s

        "Calculations speed up number - algorithms"
        
    '''

    def __init__(self): # O() t ; O() s
        pass # TODO

    
    # ! standard


    '''

        Missing Number Problem

        Given an unsorted array of n distinct numbers, from 0 -> n
        - find the missing number
        - NB: easier solution if array is sorted
    
    '''

    # find multiple missing numbers; already sorted array - can sort 1st, if array not already sorted
    def missing_number(self, a): # O(nd ~ n) t ; O(1 - 'ans' only holding result) s

        ans = [] # in case of multiple missing numbers
        
        # ! use for i in range(1, len(a)): for starting loop from index i
        # * to work with both a[i] & a[i - 1]
        for i, n in enumerate(a):
            # ! breaking at end of loop to prevent out-of-bounds exception
            if i == len(a) - 1: break
            # ! should've started loop from index 1, not 0; instead of checking this on every iteration
            d = a[i + 1] - n # already sorted, a[i + 1] > a[i]
            if d > 1: # using 'd', in case d also > 2 (so there might be more missing numbers)
                for _ in range(1, d): # O(d ~ 1) t - only iterate from 1 (0-exclusive) to d-1 (d-exclusive), 
                    # for the number of times numbers were actually missing # ! (visualize calculation)
                    n += 1 # just increment n, since it'll iterate to next
                    ans.append(n) # append all missing numbers
        
        return ans

    # find multiple missing numbers; unsorted array - using a hashmap
    def missing_number(self, a): # O(2n ~ n) t ; O(n) s

        # self.missing_number(sorted(a)) # ! can sort 1st: return above 
        # O( n log n + n ~ n log n (2nd term 'n' being non-dominant term) ) t ; O(1) s
        # ! (n) faster than (n log n) faster than (2n) in t
        # ! so (2n ~ n) is still faster than (n log n + n ~ n log n), whether both BigO's are simplified or not
        # todo: confirm: (2n) is still faster than (n log n + n), whilst (n) is still faster than (n log n)
        # * either way, the sorting option has O(1) s ; whilst the hashmap option has O(n) s
        
        ans = []
        m = {}

        for n in a:
            m[n] = 1 # no need to check if already exists, due to all distinct numbers

        for n in a:

            '''
            # not using 'd', in case differences are always 1 (only 1 step of each missing number)
            if not n == 0 and n - 1 not in m:
                ans.append(n-1)
            '''
            
            if not n > 0: # assuming there are only distinct +ve integers
                while n - 1 not in m: # keep appending lesser (decremented) numbers which aren't in m (or the input array)
                    n -= 1
                    ans.append(n)

        return ans

    # find only 1 missing number; already sorted array
    def missing_number(self, a): # O(n) t ; O(1) s
        
        for i, n in enumerate(a):
            if i == 0: continue # ! should just start loop from index 1, instead of checking this on every iteration
            d = n - a[i - 1]
            if d > 1: return a[i - 1] + 1 # 1st (& only, in this case) missing number

        return -1

    # find only 1 missing number; unsorted array
    def missing_number(self, a): # O(2n ~ n) t ; O(n) s

        m = {}

        for n in a:
            m[n] = 1
        
        for n in a:
            if not n == 0 and n - 1 not in m:
                return n - 1 # ! assuming there's only 1 missing number
                # ! otherwise, the remaining 'decremented n's not in m will be left out
                # * and even in such a case, the best answer should be the 1st missing number
                # ! not the last missing number < n in this iteration case
        
        '''
        # ! in 2nd loop, you can also just loop from 0 to n, to find all possible missing numbers too
        for x in range(0, n): # ! only if given 'n' the maximum number of the array
            if not x in m:
                return x / ans.append(x)
        '''

        return -1
    
    # find multiple missing numbers, given the maximum number too
    def missing_number(self, a, max): # O(n) t ; O(1) s

        # * can add all a's numbers to a hashmap, then loop from 0 to max, checking each in hashmap
        # ! no need to sort a in any scenario (would be 'dumb' addition to solution - unnecessary)

        ans = []

        # ! best method is to just iterate from 0 to max, checking if all numbers exist in same input array
        for x in range(0, max + 1): # max + 1, so max is inclusive
            # * the 'max' number removes the need for sorting the array
            if not x in a:
                ans.append(x) # or return x as 1st (or only) missing number

        return ans

    # 3rd-Party (Custom) - Mathematical Approach - Gauss Formula - Linear ~ Constant (in only 'some' special cases) Time
    '''
        Gauss Formula  # ! NB: All summation math-solutions match with summation '∑' Math-formulae

        (i=0 -> N) ∑ i = n * (n + 1) / 2
        
        - summation of i=0 till N ; with i = ...
        
        " summation of numbers from 0 up to n, is equal to ... 
        n multiplied by n toss 1 over 2 (n * (n + 1)/2) "

        where n = length of array of numbers from i=0 till N

        Approach to Solution:

        # ! only works where there's only 1 missing number

        - find the intended sum up to N (array-length) using Gauss Formula
            - find the actual reduced sum of the input array,
            - then calc the difference with the intended sum
            - difference is the missing number

    '''
    def missing_number(self, a): # O(n ~ 1) t ; O(1) s
        
        gauss = lambda n: n * (n + 1) / 2

        intended_sum = gauss(len(a))

        current_sum = 0 # ! or: sum(a) # O(n ~ 1) t - for .py optimum-speed sake
        for n in a: # O(n) t
            current_sum += n
        
        return intended_sum - current_sum # ! only 1 expected missing number
    
    # 3rd-Party (Tutorial) - Gauss Formula
    def missing_number(self, nums: List[int]) -> int: # O(n ~ 1) t ; O(1) s
        
        current_sum = sum(nums) # O(n ~ 1) t - for .py optimum-speed sake

        n = len(nums)
        intended_sum = n * (n + 1) / 2

        return int(intended_sum - current_sum)


    '''

        Count Primes Problem

        Count number of prime numbers less than a given non-negative number

        NB: prime number - greater than 1 & can only be divided by 1 & itself - only 2 common multiples (1 & itself)
        # ! 1 may not be regarded as a prime number (in this Math-Algo's case)
        # ! 2 is a prime number, as the smallest even counting number
        # ! 0 is not a prime number; if divisible by 1 & 0 (= 0), then also divisible by all other numbers (= 0)

        Options:

        - find 'lcm's of 1 & 2, & all odd numbers less than n 
        - (only 'Common Multiples' not actually 'Lowest'; 'lcm's just used as a jargon in this case)
            - can skip finding lcms of 1 & 2, since they're already obvious
            - therefore, from 3 to largest prime number less than n
            - primes are those of lcms with 2 numbers (can confirm 1 & itself)
            # ! - how (formulae) to find LCMs programmatically
        - 

        Mathematical Approach:

        Sieve of Eratosthenes - Algorithm

        - define a boolean array of size n & set all elements to True
            - then set 1st & 2nd elements to False
            - representing 0 & 1, which are not prime numbers
            # * - 1 is disregarded as a prime-number in this case
        - loop from index 2 to square root of N
        - if current index has Prime number (True in boolean array):
            - set all multiples of index i up to N to False, in the boolean array
        
        - now return the total number of 'True's in the boolean array
    
    '''

    # 
    def count_primes(self): # O() t ; O() s
        pass # TODO

    # 
    def count_primes(self): # O() t ; O() s
        pass # TODO

    # 3rd-Party (Tutorial) - Sieve of Eratosthenes Algo
    def count_primes(self, n: int) -> int: # O(n/2 * ~n/2 ~ n) t ; O(1) s
        
        if n < 2: return 0 # 0 & 1 are not prime-numbers

        isPrime = [True] * n # assume all numbers < n are prime for now
        isPrime[0] = isPrime[1] = False # but base-case - 0 & 1 are not prime

        for i in range(2, math.ceil(math.sqrt(n))): # loop from 2 till square-root of n
            # * square-root of n is the mid-point at which, 1-half of all potential multiples have been found

            if isPrime[i]: # if number in this index is assumed to be a prime-number
                # then make all its multiples non-prime
                # * by default 

                # range(i * i, n, i) - step-method for finding all multiples of n
                for multiples_of_i in range(i * i, n, i):
                    isPrime[multiples_of_i] = False
                    # ! todo: find out how this 'removes' all non-prime numbers
                    # * Square-of 'already-set' prime-number i till n, in i steps (i^2 + i + i + .. + i < n)
                    ''' # ! 'already-set' prime-numbers is achieved by starting loop from 2, to square-root of n
                    step-method from 'square-of i till n, in i steps' will help remove 
                    as many multiples as possible, below n, which are all non-prime numbers
                    ''' # ! this step method is done for each iteration i which has not already been set as non-prime
        
        return sum(isPrime) # * int(True) = 1 | int(False) = 0
        # * sum(of array of booleans is sum of number of 'True's)
    
    # 3rd-Party (Tutorial) - Sieve of Eratosthenes Algo - no comments
    def count_primes(self, n): # O(n/2 * ~n/2 ~ n) t ; O(1) s

        if n < 2: return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if isPrime[i]:
                for mults_i in range(i * i, n, i):
                    isPrime[mults_i] = False
        
        return sum(isPrime)


    '''

        Single Number Problem

        Given a non-empty array of integers, every element appears twice (2x), except for 1
            - find that 1 exception (that appears only once)
        
        Options:
            - sort all elems, find the 1 that isn't adjacent to itself
                - O(n log n + n~1 ~ n) t | O(1) s
            - stupid: store all elems in hashmap, incrementing values of repetitions to 2
                - loop again & find 1 with value 1
                - O(2n ~ n) t | O(n) s
            - better: store elems in hashmap, delete as repetitions are found
                - find the last 1 standing in hashmap
                - O(n) t | O(n ~ 1) s (maybe ~ constant-space since repetitions are deleted from hashmap, until 1 item, finally 'deleted' after being found & used)
    
        Mathematical Approach:
        
        2 * UniqueSum - Sum = Answer

        (2 * UniqueSum) - Sum = Same Answer - by BODMAS / PEMDAS - multiplication before subtraction

        UniqueSum = sum of all unique numbers (non-repeating)
        Sum = sum of all numbers

        - unique elems is all present numbers, without their repetitions
        - including the 1 single-number being searched
            - get all unique elems by converting array into a set (in .py)
        
        # ! this formula only works if repeating numbers only appear twice (2x)
        # * they must all appear the same number of times (which is > 1)
        - for the formula to be: # ! n * UniqueSum - Sum = Answer
            - where n = number of times each repeating number appears
        - the '2' represents the repeating numbers appearing twice
            - so the regular sum = (2 * unique-sum) + the single-number - can solve algebraic'ly

    '''

    # ! NB: in the case of multiple non-repetitions, you can always append them all into a resulting array
    # * for each case here, dealing with only 1 non-repeating number

    # sort 1st, then find non-repeating number
    def single_number(self, a): # O(n log n + n ~ n log n) t ; O(1) s
        
        a.sort() # O(n log n) t

        # for i, n in enumerate(a):
        # using a while-loop instead, for jumping index'ing
        i = 0
        while i < len(a):
            # if last item or item != next item
            if i == len(a) - 1 or \
                not a[i] == a[i + 1]:
                return a[i]
            else: i += 2
            # since we're only expecting 1 non-repeating number in these cases
            # * will never need to increment index by 1 (when a non-repeating number is found)
        
        return -1

    # stupid: store all elems in hashmap, increment repetitions
    def single_number(self, a): # O(2n ~ n) t ; O(n) s
        
        m = {}

        for n in a:
            if n in m: m[n] += 1
            else: m[n] = 1
        
        for k, v in m.items():
            if v == 1: return k
        
        return -1

    # better: store elems in hashmap, delete repetitions
    def single_number(self, a): # O(n) t ; O(n ~ 1) s
        
        m = {}

        for n in a:
            if n in m: del m[n]
            else: m[n] = 1
        
        print(len(m)) # confirm length of map is 1, else there are multiple non-repetitions

        return list(m.keys())[0] # return 1st (only, if 1 non-repetition) key-value -> list item

    # Math Approach - 2 * UniqueSum - Sum = Ans
    def single_number(self, a): # O(3(n ~ 1) ~ n ~ 1) t ; O(n ~ 1 ~ back to n - by opinion) s
        # O(n) s - usage of set is still used in formula, alongside the input array, 
        # * so can also be considered a part of the algo
        
        unique = set(a) # O(n ~ 1) t | O(n) s
        
        return 2 * sum(unique) - sum(a) # O(n~1 + n~1 ~ 2(n~1) ~ n~1) t

    # 3rd-Party (Tutorial) - 
    def single_number(self, nums): # O(n ~ 1) t ; O(n ~ 1 ~ back to n - by opinion) s
        return 2 * sum(set(nums)) - sum(nums)


    '''

        Robot Return to Origin Problem

        Imagine a robot standing at position (0, 0) in a 2D grid
        Given a string of its moves, find its final location

        - eg. UD - UP, DOWN

        NB: movements
        U - up - increase in y-axis
        D - down - decrease in y-axis
        R - right - increase in x-axis
        L - left - decrease in x-axis

        "Robot Return to Origin" means judge if moves are circular
            - i.e. robot returned to its original position (0, 0)
    
    '''

    def robot_moves_from_origin(self, moves: str, pos: tuple[int] = (0, 0)) -> tuple[int]:
        # O(n or s - length of string) t ; O(1) s
        
        for c in moves:
            if c == 'U': pos[1] += 1
            elif c == 'D': pos[1] -= 1
            if c == 'R': pos[0] += 1
            elif c == 'L': pos[0] -= 1
        
        return pos

    # 'Judge-Circle' - check if moves are circular
    '''
        confirm if robot moves in a 'circle'ish motion, to land at same position
        'circular' motion eg. - u r d l
        'circular'ish motion eg. - u d r l
    '''
    def robot_return_to_origin(self, moves: str): # O(n) t ; O(1) s
        return self.robot_moves_from_origin(moves) == (0, 0)

    # 3rd-Party (Tutorial) - 'Judge-Circle' alt problem-name
    def robot_return_to_origin(self, moves: str): # O(n) t ; O(1) s
        
        x = y = 0

        for move in moves:
            if move == 'U': y += 1
            elif move == 'R': x += 1
            elif move == 'D': y -= 1
            elif move == 'L': x -= 1
        
        return x == 0 and y == 0 # or: (x, y) == (0, 0)

    # 3rd-Party (Tutorial) - 'Judge-Circle' actual problem
    def judge_circle(self, moves: str):

        # ! confirm order of characters in string as 'circular'
        # u r d l / u l d r - in this order, with any starting position
        # * can have multiple repetitions, but must have same-multiples of opposite direction, 
        # while in consistent order
        
        pass # TODO


    '''

        Add Binary Problem - Base 2 numbers addition

        Given 2 binary strings, return their sum

        NB: Binary (Base 2) numbers are numbers represented only by 0 & 1
        Decimal (Base 10) numbers are constructed by digits based in columns that are multiples of 10

        eg. 1996 = (1 * 1000) + (9 * 100) + (9 * 10) + (6 * 1)

        NB: now converting Base 2 numbers back to Decimal (Base 10) numbers

        digit * 2^(n - digit's index-position from right - starting from 0)

        eg. 1011 = 1 * (2^3) + 0 * (2^2) + 1 * (2^1) + 1 * (2^0)
                 = 1*8 + 0*4 + 1*2 + 1*1
                 = 11
    
    '''

    # Using carry-over addition, with base 2
    # While-looping until all digits removed, from both numbers
    def add_binary(self, a, b): # O(a or b ~ n - longest number) t ; O(1 - ignoring resulting array of base-2 digits) s

        sum = ans = c = 0
        
        while a > 0 or b > 0:
            
            ax, bx = a % 10, b % 10 # take out last digits

            a, b = a // 10, b // 10 # & remove last digits
            # or: a //= 10; b //= 10

            '''
            would've have summed up c + ax + bx
            then taken out last digit of sum as ans
            then will carry-over remaining number
            (without the last digit, & not replaced by 0, i.e. ans //= 10)
            '''

            # but instead, ensuring for Base - 2 numbers

            # * in this 'manual' case 0 <= s <= 3
            s = c + ax + bx
            
            c = 0
            if s == 2 or s == 0:
                ans = 0 # ans is always 0 on 0 & 2 (base-2)
                if s == 2: c = 1 # on 2, carry 1
            else: # s == 1 or 3
                ans = 1 # ans is always 1 on 1 & 3 (above base-2)
                if s == 3: c = 1 # on 3, ans = 1, carry = 1

            sum = sum * 10 + ans

        return sum


    # Using carry-over addition, with base 2
    # Using Iterators (instead of while-looping until all digits removed)
    def add_binary(self): # O() t ; O() s
        
        # TODO - find similar algo in next solution
        pass

    # 3rd-Party (Tutorial) - Base-2 addition, with Carry-Overs
    # Using Iterators (instead of while-looping until all digits removed)
    def add_binary(self, a, b): # O(n) t ; O(1) s
        
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
        
            result.append(
                str(
                    total % 2
                )
            )

            carry = total // 2
        
        return ''.join(reversed(result)) # O(2r ~ 1 ; r = result's digit-length)
    
    # 3rd-Party (Tutorial - 2) - same as above
    def add_binary(self, a, b): # O(n) t ; O(1) s

        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        # will iterate both pointers from right -> left of both numbers

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        
        return ''.join(reversed(result))

    
    def meth(self): # O() t ; O() s
        pass # TODO


    # ! easy


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! medium


    def meth(self): # O() t ; O() s
        pass # TODO

    
    # ! hard


    def meth(self): # O() t ; O() s
        pass # TODO


class Geometric:

    def __init__(self): # O() t ; O() s
        pass # TODO


class PatternSearching:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Bitwise:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Randomized:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Compression:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Encryption:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Hashing:

    def __init__(self): # O() t ; O() s
        pass # TODO


class BranchAndBound:

    def __init__(self): # O() t ; O() s
        pass # TODO


class MachineLearning:

    def __init__(self): # O() t ; O() s
        pass # TODO


class DeepLearning:

    def __init__(self): # O() t ; O() s
        pass # TODO


class NaturalLanguageProcessing:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Genetic:

    def __init__(self): # O() t ; O() s
        pass # TODO


class MultiThreading:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Games:

    def __init__(self): # O() t ; O() s
        pass # TODO


class Quant:

    def __init__(self): # O() t ; O() s
        pass # TODO


class SystemDesign:

    def __init__(self): # O() t ; O() s
        pass # TODO




########################################
#  Cracking Coding Interview Qs
########################################

# Arrays & Strings

def number_swapper(a, b): # in-place
    a = a+b; b = a-b; a = a-b # simple
    # or
    a = a-b; b = a+b; a = b-a # complex

def word_frequencies(book, words): # O(bw) time; O(w) / O(m) space
    map, f = {}, 0
    s = book.split(' ').lower() # remove all symbols (. , ' etc)
    for w in words:
        # str func to find all occurrences of x in s = f
        # or
        w = w.lower()
        for x in s:
            if x == w:
                f = f + 1
        map[w] = f

def word_frequencies(book, words): # O(b) + O(w) time; O(b) / O(m) space
    map = {}
    for s in book.split(' ').lower(): # remove all symbols (. , ' etc)
        if s in map: map[s] = map[s] + 1
        else: map[s] = 0
    for w in words:
        print('{} : {}'.format(w, map[w]))

def factorial_zeros(n):
    def calc_fact(n):
        if n is 1: return n * 1
        return calc_fact(n * (n-1))
    # TODO

def smallest_diff(a1, a2):
    
    a1.sort(); a2.sort() # O(a log a)
    # figure out space complexity here
    a, b, d = 0, 0, sys.maxsize # Python 3.5 | sys.maxint in Python 2.7
    while (a < len(a1) and b < len(a2)):
        if (d < abs(a1[a] - a2[b])):
            d = abs(a1[a] - a2[b])
            if (d is 0): return d
        if (a1[a] < a2[b]): a = a + 1
        else: b = b + 1

def sub_sort(a): # Learn - maybe O(n) 
    if len(a) is 0: return -1
    elif len(a) is 1: return (0, 0)

    f, l = 0, len(a) - 1
    ff, ll = None, None
    min, max = None, None
    while f < l:
        if ff is None and a[f] <= a[f+1]: f = f + 1
        else: 
            if ff is None: min = ff = f = f + 1
            else:
                if min < a[f]: min = a[f]
                f = f + 1

        if ll is None and a[l-1] <= a[l]: l = l - 1
        else: 
            if ll is None: max = ll = l = l - 1
            else:
                if max > a[l]: max = a[l]
                l = l - 1
    
    i = j = False
    while not (i and j):
        f = f - 1; l = l + 1
        if min >= a[f]:
            ff = f + 1 if (min > a[f]) else f
            i = True
        if max <= a[l]:
            ll = l - 1 if (max < a[l]) else l
            j = True
            
    return (ff, ll)

def contiguous_sequence(a): 
    sum, max_sum, s = 0, []
    for i in a:
        sum = sum + i
        if sum < 0: 
            sum = 0
            s = []
        else: s.append(i)
        if max_sum < sum: max_sum = sum
    return max_sum, s

def pattern_matching(p, v):
    if len(p) is 0: return len(v) is 0

    d, i, j, i1, j1, ptn = {}, 0, 0, '', ''
    while j < len(v):
        j1 = v[j]
        if i1 is '':
            i1 = p[i]
        # elif i1 == j1:
        # if i1 in d:
        #     if d[i1] is not ptn: return False
        # else: 
        #     d[i1] = ptn
        #     i1 = j1
        
        # if i1 is not None:
        else:
            ptn += j1

        j = j + 1
    return True

def sum_swap(a1, a2): 
    # Looking for a and b, such that ..
    # s1 - a + b = s2 - b + a  | s1 - s2 = 2(a - b) ~ a - b
    d = abs(sum(a1) - sum(a2)) # O(a1 + a2)
    if d > 0: # d != -ve (absolute value)
        # O(a1 * a2)
        for x in a1:
            for y in a2:
                # option 1 # todo: working option only
                s1 = sum(a1) - x + y # swap y into x, for a1
                s2 = sum(a2) - y + x # swap x into y, for a2
                if s1 == s2: return (x, y)
                # option 2 (not sure about this option, because this new d should be compared to old d)
                d = abs(x-y)
                if d == 0: return (x, y)
                # todo: perhaps, option 2 should be if (old) d == abs(x-y)
        # O(a1 + a2)
        dt = {}
        for y in a2: dt[y] = y
        for x in a1:
            if (x-d) in dt: return (x, x-d)
    else: # d == 0, therefore s1 == s2 already, therefore any 2 same number occurrences in both a1 & a2 can be returned
        for x in a1:
            for y in a2:
                d = abs(x-y) # OR: if x == y
                if d == 0: return (x, y) # therefore x == y, and if they're both swapped, s1 == s2 still (since the old d == 0)
    return None # so complete the solution (unless both arrays have all distinct values)

def pairs_with_sum(a, s): 
    if len(a) < 2: return

    # Option 1 - O(2n) t | O(d) s # todo: not O(d + p) s (pairs array not 'part' of algo's implementation; only value to be returned)

    p, d = [], {}
    for i in a:
        if i not in d: d[i] = 1
    for i in a:
        if (s-i) in d: p.append((i, s-i))

    # Option 2 - O(n) t | O(d) s
    
    for i in a: # using 1 loop
        if (s-i) in d: p.append((i, s-i))
        if i not in d: # only needed if a doesn't have distinct elements
            d[i] = i

    # Option 3 - Two-Pointer technique (with a sorted arr)
    # O(nlogn + n) t | O(1) s

    a.sort() # O(n log n) (quick) sort 1st if not already sorted
    i, j = 0, len(a) - 1

    while(i < j):
       
        # If we find a pair
        if (a[i] + a[j] == s): p.append((a[i], a[j]))
 
        # If sum of elements at current
        # pointers is less than target sum s,
        # we move towards higher values (left-pointer (i)'s next item to the right)
        # by incrementing i += 1
        elif(a[i] + a[j] < s): i += 1
 
        # If sum of elements at current
        # pointers is more than target sum s,
        # we move towards lower values (right-pointer (j)'s next item to the left)
        # by decrementing j -= 1
        else: j -= 1
    
    return p

# 2-sum, with an array of only distinct elements (non-repeating integers)
# same as above, but returning indices of elements, not elements themselves

def two_sum(nums, target): 
    if len(nums) < 2: return
    d = {}
    for i, n in enumerate(nums):
        if (target - n) in d: return [i, d[target - n]]
        d[n] = i # no 'if n in d:' check required, if 'a' has only distinct elements
    return None

# TODO
def lru_cache(): # O() t ; O() s
    # TODO
    pass


# Matrices


# HashMaps & HashTables


# Linked Lists


# Trees


# Graphs



########################################
#  LEETCODE
########################################


# https://leetcode.com/problems/add-two-numbers/description/

class ListNode:

    def __init__(self, v=None, n=None):
        self.value = v; self.next = n


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: # todo: optimize
    ls = ListNode(); sa = []; c = 0
    s = l1.value + l2.value
    d = f"{s}"[-1:]
    c = int(f"{s}"[::-1])
    sa.append(d)
    ls.value = d
    while (l1.next is not None) or (l2.next is not None):
        if l1.next is not None: 
            l1 = l1.next
            c += l1.value
        if l2.next is not None: 
            l2 = l2.next
            c += l2.value
        s = c
        d = f"{s}"[-1:]
        c = int(f"{s}"[::-1])
        sa.append(d)
        ls.next = ListNode(v=d)
    return ls # or return s

    # or

    # both are singly-linked lists, each having a number's digits in reverse order (123 = 3 -> 2 -> 1)
    # regular addition of 2 numbers with multiple digits is already done in reverse order, 
    # with n > base 10's extra digit carried over as a multiple of 10 (10, 100, 1000, ...) to the next 

    l1, l2, ls = l1.head, l2.head, ListNode()
    s = c = 0; ll = DataStructures.LinkedList(h=ls)
    while l1 or l2:
        s = int(l1.value if l1 and l1.value else 0) + \
            int(l2.value if l2 and l2.value else 0) + c
        if len(f"{s}") > 1:
            ls.value = int((f"{s}")[-1]) # or s % 10
            c = int((f"{s}")[::-1]) # or s / 10
        else:
            ls.value = s
            c = 0
        ls.next = ListNode()
        l1, l2, ls = l1.next, l2.next, ls.next
    if c > 0: ls.value = c
    else: ls = None # remove the last empty ls node
    return ll

    # or
    
    ans = ListNode(); node = ans
    s = c = 0
    while l1 or l2:
        s = c
        if l1:
            s += l1.value
            l1 = l1.next
        if l2:
            s += l2.value
            l2 = l2.next
        c = int(s / 10)
        node.next = ListNode(s % 10)
        node = node.next
    if c > 0: node.next = ListNode(c)
    return ans.next # leave out dummy head






# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
def lengthOfLongestSubstring(self, s: str) -> int: # todo: optimize
    if len(s) < 1: return 0
    elif len(s) == 1: return 1
    d = {}; l = 0; li = 0
    for i, c in enumerate(list(s)):
        if c in d: 
            li = i
            if li - d[c] > l: l = li - d[c]
        d[c] = i
    if l == 0: l = len(s)
    elif (len(s) - li) > l: l = len(s) - li
    return l


# https://leetcode.com/problems/string-compression-ii/?envType=daily-question&envId=2023-12-28
def getLengthOfOptimalCompression(self, s: str, k: int) -> int: # todo
    cs = ''
    while len(s) > 0:
        t = 0; si = 0
        cs += s[0]
        if len(s) >= 2 and s[0] == s[1]:
            t = 2
            for i, c in enumerate(s[2:]):
                if s[0] == c: t += 1
                else: 
                    si = i + 2
                    break
            cs += f"{t}"
        else: si += 1
        s = s[si:]
    return len(cs)


########################################
#  CODESIGNAL
########################################


# Given 2 sorted arrays, find the number of elements in common.
# Both arrays have the same length, and all distinct elements

def common_elems(arr1, arr2): # Brute-force algo [O(n^2)]
    nums = []
    for a1 in arr1:
        for a2 in arr2:
            if a1 is a2:
                nums.append(a1)
    print(nums)
    return len(nums)

def common_elems(arr1, arr2): # More optimized algo [time - O(n log n)] [space - should be O(n)]
    nums, low, high, mid = [], 0, len(arr2) - 1, None
    for a1 in arr1: # TODO now find a1 in arr2, using binary search
        while low <= high:
            mid = (low + high) / 2
            if arr2[mid] < a1: low = mid + 1
            elif arr2[mid] > a1: high = mid - 1
            else: # arr2[mid] == a1
                nums.append(a1)
                break

    print(nums)
    return len(nums)

def common_elems(arr1, arr2): # More optimized algo [time - O(2n) ~ O(n)] [space - should be O(n)]
    nums, d2 = [], {}
    for a2 in arr2:
        d2[a2] = a2
    
    for a1 in arr1:
        if a1 in d2:
            nums.append(a1)

    print(nums)
    return len(nums)

def common_elems(arr1, arr2): # Most optimized algo [time - O(n)] [space - should be O(1)]
    nums = [] # getting rid of nums, will put this algo at O(1) space complexity
    for a1 in arr1: # now find a1 in arr2, using linear search, but this time ..
        # with the search picking up where the last one left off (since both arrays are already sorted ..)
        # so runtime will be linear
        for j, a2 in enumerate(arr2):
            if a1 is a2:
                nums.append(a1)
            elif a1 > a2: # remove a2 from arr2
                arr2 = arr2[j+1:]
            elif a1 < a2: break # stop searching arr2, because it's sorted ..

    print(nums)
    return len(nums)


# 2-sum, with an array of only distinct elements (non-repeating integers)
# same as above, but returning indices of elements, not elements themselves

def two_sum(nums, target):
    if len(nums) < 2: return
    d = {}
    for i, n in enumerate(nums):
        if (target - n) in d: return [i, d[target - n]]
        d[n] = i # no 'if n in d:' check required, if 'a' has only distinct elements
    return None



# Given an array a that contains only numbers in the range from 1 to a.length, 
# find the first duplicate number for which the second occurrence has the minimal index.

def first_duplicate(a):
    arr = [] # USING AN ARRAY GETS EXEC TIME LIMIT EXCEEDED ..
    arr = set() # SETS ARE FASTER IN IMPLEMENTATION THAN ARRAYS ...
    for x in a:
        if x in arr:
            return x
        else:
            arr.append(x) # FOR arr = []
            arr.add(x) # FOR arr = set()
    return -1


# 

def sum_of_two(a,b,v):
    b = set(b)
    return any(v - x in b for x in a)


# 

def sum_in_range(nums, queries):
    totalSum, sumSoFar, prefixSum = 0, 0, [0]
    
    # DOESN'T PASS ALL TESTS ..
    # for x in queries:
    #     totalSum += sum(nums[x[0] : x[1]+1])
    
    for num in nums:
        sumSoFar += num
        prefixSum.append(sumSoFar)
        
    for query in queries:
        start = query[0]
        end = query[1] + 1
        totalSum += prefixSum[end] - prefixSum[start]
        
    return totalSum % ((10**9) + 7)


# You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. 
# Calculate how many distinct ways you can climb to the top of the staircase.

def climbing_stairs(n):
    if n == 1 or n == 2:
        return n
        
    prevPrev, prev, curr = 1, 2, 0
    
    for step in range(3, n+1):
        # Calculate no. of ways to reach current step
        curr = prevPrev + prev
        # Update pointers for next step
        prevPrev = prev
        prev = curr
    return curr



# You have a block with the dimensions 4 × n. Find the number of different ways you can fill this block with 
# smaller blocks that have the dimensions 1 × 2. You are allowed to rotate the smaller blocks.

# THIS METHOD EXCEEDS EXEC TIME LIMIT ...

def filling_blocks(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 5
    else:
        row = filling_blocks_0011(n-1)
        ccr = filling_blocks_0011(n-2)
        crc = filling_blocks_0110(n-2)
        cccc = filling_blocks(n-2)
        return row + ccr + crc + cccc


def filling_blocks_0110(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return filling_blocks(n) + filling_blocks_0110(n-2)
    

def filling_blocks_0011(n):
    if n == 0: return 1
    else: return filling_blocks(n) + filling_blocks_0011(n-1)


# TODO: TREES

# Given a binary tree of integers t, return its node values in the following format:

def traverse_tree(t):
    if t is None: return []
    arr, a, n = [], [t], None
    
    while len(a) > 0:
        arr.append(a[0].value)
        n = a.pop(0)
        if n.left is not None: a.append(n.left)
        if n.right is not None: a.append(n.right)
    
    return arr


# Return an array in which the first element is the largest value in the row with depth 0, 
# the second element is the largest value in the row with depth 1, the third element is the largest element in the row with depth 2, etc.

def largest_values_in_tree_rows(t):
    res = []; helper(res, t, 0)
    return res
    

def helper(res, root, d):
    if not root: return
    if d == len(res): res.append(root.value)
    else: res[d] = max(res[d], root.value)
    
    helper(res, root.left, d+1)
    helper(res, root.right, d+1)
    

# We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

def digit_tree_sum(t):
    return tree_paths_sum(t, 0)


def tree_paths_sum(t, v):
    if t is None: return 0
    v = (v*10) + t.value
    if t.left is None and t.right is None: return v
    return (tree_paths_sum(t.left, v) + tree_paths_sum(t.right, v))



########################################
##  EXTRA Qs
########################################

def wave_array(arr): # O(nlogn + (n/2)) t
    arr.sort() # O(n log n)
    for i in range(1, len(arr), 2): # O(n / 2)
        arr[i], arr[i-1] = arr[i-1], arr[i]

def count_like_dislike (A, P):
    c = 0; A = list(A); P = list(P) # these 2 castings might be O(A + P) t
    while len(A) > 0 or len(P) > 0: # O(n) t , if n is same length for both A and P
        if A.pop(0) == P.pop(0): c += 1 
        # todo: find out differences in time/space complexities and memory usage between indexing and pop() within python lists
    return c

def occupied_desks(arr):
  K = arr[0]
  occupied_desks = arr[1:]
  ways = 0
  for i in range(1, K+1):
    if i not in occupied_desks:
      if i + 1 <= K and i + 1 not in occupied_desks:
        ways += 1
      if i + 2 <= K and i + 2 not in occupied_desks:
        ways += 1
  return ways

def algebra(str):
    # __define-ocg__
    parts = str.split()

    # Get the index of the x character
    x_index = parts.index('x')

    # Get the numbers and the operator
    num1 = int(parts[0]) if x_index != 0 else None
    num2 = int(parts[2]) if x_index != 2 else None
    result = int(parts[4])

    # Determine the missing digit
    if parts[1] == '+':
        if x_index == 0:
            return result - num2
        elif x_index == 2:
            return result - num1
        else:
            return num1 + num2
    elif parts[1] == '-':
        if x_index == 0:
            return result + num2
        elif x_index == 2:
            return num1 - result
        else:
            return num1 - num2
    elif parts[1] == '*':
        if x_index == 0:
            return result // num2
        elif x_index == 2:
            return result // num1
        else:
            return num1 * num2
    elif parts[1] == '/':
        if x_index == 0:
            return result * num2
        elif x_index == 2:
            return num1 // result
        else:
            return num1 // num2

def gas_stations(strArr):
    # __define-ocg__
    N = int(strArr[0])
    gas_stations = [list(map(int, station.split(':'))) for station in strArr[1:]]

    # Check starting from each gas station
    for i in range(N):
        tank = 0
        for j in range(N):
            station = gas_stations[(i + j) % N]
            tank += station[0] - station[1]
            if tank < 0:
                break
        else:
            return i + 1

    return "impossible"




########################################
##  TEST CASES
########################################

if __name__ == "__main__":
    print("Hello, World!")

