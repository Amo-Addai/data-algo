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
# TODO:

Test all files' Algo's - Correctness, Speed / Execution Time, Uniqueness
Re-assess all algos' Big Omega (Best-Case / Lower-Bound) & Big Theta (Average-Case / Tight-Bound) - Time & Space Complexities
Compare all cases with stated Big O (Worst-Case / Upper-Bound) - Time & Space Complexities alike

# TODO: To-Use


Hidden (Forgetful) Keys:

BCR & Visualizations - for all problems with all possible solutions
Base-Cases & Error-Cases - for everything, & wrong inputs
Brute-force methods - for all more-optimal solutions
HashMap & "Same / Extra" Array methods - for all more-optimal solutions
"Extra" / "Other" Data-Structure methods - for all more-optimal solutions
While / For / Foreach / .ForEach / .Map loops - for all requiring solutions


Data-Structures:

Done - arrays/strings (sorting/searching), lists/tuples, matrices, hash/weak-maps/tables/sets, linked-lists, stacks/queues, trees/b(s)ts, graphs,  …  
# todo - sets/seqs/vectors, dicts/maps/objs, tree-maps/sets, tries, max/min heaps, bi-heaps/p-queues, bits, blobs,  …  


Algorithm Mechanics & Facts:


Mechanic - DataStructure(s), Language-Syntax, Variations, Constraints, Question Constraints, Helpers, Laws & Facts, Combos


- same data-structure (eg. array - when only values required; not indices too) - language-syntax (eg. x 'in' arr over dict), 

- hashmap/hashtable - when indices (as map-values) also required, 

- variables - storing specific data (instead of extra data-structures), eg. min/max values, any trailing/leading data, 1/2/3 - pointers, 

Iterations: 1 / 2 / .. / n - pointers

- 1-pointer - arrays/strings/linkedlists/matrices?/.. , hashmap/table?, .. 

- 2-pointer - arrays/strings/linkedlists/matrices?/.. , binary/? search, inward/outward iteration, same-time/1-after-other/slow-faster/1-or-n-step(s)-ahead iteration, 
pointer-calculations (eg. middle-index), integer-math laws, int < target, (non-)repeating ints, sorting 'almost always' required (ints/strings/..), 

Searches: 

- Linear Search - arrays/strings/linkedlists/.. , 

- Binary Search - arrays/trees/.. , 2/? pointers, 

Others: 

- Sliding-window - arrays/strings/matrices?/.. , ranges/sub-arrays/.. , ..




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

    def __init__(self): pass
    

    # Arrays & Strings

    class Arrays:

        def __init__(self): pass

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

        def min_jumps(self, a): pass

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
                if n in a2 and n not in ints:
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

        def __init__(self): pass

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

        def __init__(self): pass

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
        

    def add(self, l1, l2): pass
        
    def add_nums(self, l1, l2): pass
        
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
        
        def __init__(self, n):
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


        def diameter(self): pass

        def max_depth_or_height(self): pass

        @staticmethod
        def is_BST(self): pass

        def lowest_common_ancestor(self): pass

        def unique_paths(self): pass

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

        def __init__(self): pass


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

            def __init__(self): pass


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

    def func(self): pass


class DynamicProgramming:

    def __init__(self): pass

    # advanced

    def bitmasking(self): pass

    def digit_dp(self): pass

    def sum_over_subsets(self): pass

    # easy

    def coin_change(self): pass

    def subset_sum(self): pass

    def cutting_a_rod(self): pass
    
    def painting_fence(self): pass

    def longest_common_subsequence(self, a): pass

    def longest_increasing_subsequence(self, a): pass

    def min_cost_path(self): pass

    def longest_common_substring(self, a): pass

    def edit_distance(self): pass

    def convex_hull(self): pass
    
    def unique_paths(self): pass

    # medium

    def knapsack(self): pass

    def fractional_knapsack(self): pass

    def unbounded_knapsack(self): pass

    def edd_dropping_puzzle(self): pass
    
    def word_break(self): pass

    def vertex_cover(self, a): pass

    def tile_stacking(self, a): pass

    def box_stacking(self): pass

    def partition(self, a): pass

    def travelling_salesman(self): pass

    def longest_palindromic_subsequence(self, a): pass

    def longest_common_increasing_subsequence(self, a): pass

    def distinct_subset_sums(self, a): pass

    def weighted_job_scheduling(self): pass
    
    def count_derangements(self): pass
    
    def min_insertions_to_palindrome(self): pass
    
    def adjacent_balls(self): pass

    # hard
    
    def palindrome_partitioning(self): pass
    
    def word_wrap(self): pass
    
    def painters_partition(self): pass
    
    def bridge_and_torch(self): pass
    
    def matrix_chain_mult(self): pass
    
    def max_sum_rect(self): pass
    
    def max_profit(self): pass
    
    def min_cost(self): pass
    
    def arithmethic_progression(self): pass
    
    def dp_on_trees(self): pass
    
    def max_height(self): pass
    
    def longest_repeating_substr(self): pass


class DivideAndConquer:

    '''
        # TODO:
        
    '''

    def __init__(self): pass

    # standard

    def pow(self, x, n): pass

    def closest_pair(self): pass

    def karatsuba_mult(self): pass

    def strassens_matrix_mult(self): pass

    def max_subarray_sum(self): pass

    def longest_common_prefix(self): pass

    def convex_hull(self): pass

    def quick_hull(self): pass

    # binary search based

    def peak_elem(self, a): pass

    def majority_elem(self): pass

    def kth_elem(self): pass

    def num_zeroes(self): pass

    def rotation_count(self): pass

    def unbounded_binary_search(self): pass

    def median_of_sorted_arrays(self): pass

    def painters_partition(self): pass

    # easy

    # medium

    # hard

    def square_root(self): pass

    def max_min_of_array(self): pass

    def elem_frequency(self): pass

    def tiling(self): pass

    def inversion_count_using_merge_sort(self): pass

    def skyline(self): pass

    def search_2d_matrix(self): pass

    def alloc_min_pages(self): pass


class Greedy:

    def __init__(self): pass

    # standard

    def activity_selection(self): pass

    def job_sequencing(self): pass

    def huffman_coding(self): pass

    def huffman_decoding(self): pass

    def water_connection(self): pass

    def egyptian_fraction(self): pass

    def police_thieves(self): pass

    def fitting_shelves(self): pass

    def mice_to_holes(self): pass

    # easy

    def split_into_max_composite_nums(self, n): pass

    def buy_max_stocks(self): pass

    def min_max_amount(self): pass

    def max_equal_sum(self): pass

    def cuboid_to_cubes(self): pass

    def max_custs_to_satisfy(self): pass

    def min_rotations_to_unlock(self): pass

    def min_rooms_for_events(self): pass

    def min_cost_to_reduce_size(self): pass

    def min_cost_to_acquire_coins(self): pass

    def min_increment_by_ops(self): pass

    def min_number_of_notes(self): pass

    def smallest_subset_with_greatest_sum(self): pass

    # medium

    def max_trains_for_stoppage(self): pass

    def min_fibonacci_terms(self): pass

    def divide_with_min_sum_diff(self): pass

    def min_num_squares(self): pass

    def min_diff_between_groups(self): pass

    def min_num_platforms(self): pass

    def min_vertices_to_traverse_matrix(self): pass

    def largest_palindromic_num(self): pass

    def smallest_num_given_digits_num_sum(self): pass

    def lexi_largest_subsequence(self): pass

    # hard

    def max_elems_made_equal(self): pass

    def min_cash_flow(self): pass

    def min_cost_to_cut_board(self): pass

    def min_cost_to_process_tasks(self): pass

    def min_time_to_finish_jobs(self): pass

    def minimize_max_diff(self, a): pass

    def min_edges_to_reverse(self, a): pass

    def largest_cube(self): pass

    def rearrange_str_chars(self): 

        # so no 2 adjacent chars are equal
        # so all equal chars become d distance away
        pass


class BackTracking:

    def __init__(self): pass

    # standard

    def knights_tour(self): pass

    def rat_in_a_maze(self): pass

    def n_queen(self): pass

    def subset_sum(self): pass

    def m_coloring(self): pass

    def hamiltonian(self): pass

    def sudoku(self): pass

    def magnet_puzzle(self): pass

    def remove_invalid_parenthesis(self): pass

    def generate_gray_codes(self): pass

    def string_permutations(self): pass

    # easy

    def print_subsets(self): pass

    def is_sum_str(self): pass

    def possible_paths(self): pass

    def bitmasking_distinct_subsets(self): pass

    def path_from_source(self): pass

    def print_paths_from_source(self): pass

    def print_strings_using_spaces(self): pass

    # medium

    def tug_of_war(self): pass

    def eight_queens(self): pass

    def combinational_sum(self): pass

    def warnsdorff_for_knights_tour(self): pass

    def paths_in_maze(self): pass

    def max_num_by_k_swaps(self): pass

    # hard

    def power_set(self): pass

    def word_break(self): pass

    def set_to_k_subsets(self): pass

    def longest_route_in_matrix(self): pass

    def shortest_safe_route(self): pass

    def print_n_queen_solns(self, a): pass

    def longest_common_subsequence(self, a): pass


class SystemDesign:

    def __init__(self): pass


class Mathematical:

    def __init__(self): pass


class Geometric:

    def __init__(self): pass


class PatternSearching:

    def __init__(self): pass


class Recursion:

    def __init__(self): pass


class Bitwise:

    def __init__(self): pass


class Randomized:

    def __init__(self): pass


class Hashing:

    def __init__(self): pass


class Compression:

    def __init__(self): pass


class Encryption:

    def __init__(self): pass


class BranchAndBound:

    def __init__(self): pass


class MachineLearning:

    def __init__(self): pass


class DeepLearning:

    def __init__(self): pass


class NaturalLanguageProcessing:

    def __init__(self): pass


class Genetic:

    def __init__(self): pass


class MultiThreading:

    def __init__(self): pass


class Games:

    def __init__(self): pass


class Quant:

    def __init__(self): pass



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
def lru_cache(): pass


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
