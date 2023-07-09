'''
LEARN

for - iter, k/v, ..
..

'''

########################################
##  SEARCHING ALGO'S
########################################

def linear_search(a, x):
    for i in a:
        if x is i: return x
    return None

def binary_search(a, x):
    # a.sort()
    if len(a) is 0: return None

    def r_binary_search(a, x):
        if len(a) is 0: return None
        m = len(a) / 2
        if x < a[m]: return r_binary_search(a[:m-1], x)
        elif x > a[m]: return r_binary_search(a[m+1:], x)
        else: return m

    def r_binary_search(a, x, f, l):
        if len(a) is 0 or f > l: return None
        m = (f + l) / 2 # better: f + (l - f) / 2 (NB: pemdas / bodmas)
        if x < a[m]: return r_binary_search(a, x, f, m - 1)
        elif x > a[m]: return r_binary_search(a, x, m + 1, l)
        else: return m

    f, l = 0, len(a) - 1
    r_binary_search(a, 7); r_binary_search(a, 7, f, l)

    while f < l:
        m = (f + l) / 2 # better: f + (l - f) / 2 (NB: pemdas / bodmas)
        if x < a[m]: l = m - 1
        elif x > a[m]: f = m + 1
        else: return m
    return None


########################################
##  SORTING ALGO'S (ascending)
########################################

def check(a): # O(1) t ;
    return len(a) in [0, 1]
    
def swap(a, b): # O(1) t ; by ref
    t, a, b = a, b, t
    # (a, b) = (b, a) # faster, but () by value
    return a, b

def compare(a, b): # O(1) t ; generic
    return a < b

# regular

def insertion(a): # O(n^2) t ; O(1) s
    if check(a): return a
    for i in range(1, len(a)):
        j = i
        while j > 0 and (a[j] < a[j-1]):
            swap(a[j-1], a[j])
            j = j - 1
        # or
        for j in range(i, 0, -1):
            if a[j] < a[j-1]: swap(a[j-1], a[j])
            else: break # 1-lvl?
    return a

def selection(a): # O(n^2) t ; O(1) s
    if check(a): return a
    for i, x in enumerate(a):
        l = i
        for j in range(i + 1, len(a)):
            if a[j] < x: l = j
        if x is not a[l]: swap(a[i], a[l]) # x is a[i]
    return a

def shell(a): # O(n^2) t ; 
    if check(a): return a
    m = len(a) / 2
    while m > 0:
        for i in range(0, m): insertion(a[i : m]) # ensure call by ref
        m = m / 2        
    return a

# bad

def bubble(a): # O(n^2) t ; O(1) s
    if check(a): return a
    sorting = True
    while sorting: # fastest loop
        for i in range(0, len(a) - 1):
            if a[i] > a[i+1]: 
                swap(a[i], a[i+1])
                sorting = False
    # or
    for i in range(1, len(a)):
        sorted = True
        for j in range(0, len(a) - 1):
            if a[j] > a[j+1]: 
                swap(a[j], a[j+1])
                sorted = False
        if sorted: break
    # or
    for i in range(0, len(a)): # or len(a) - 1/i - both optimizations
        sorted = True
        for j in range(1, len(a)):
            if a[j] < a[j-1]:
                swap(a[j-1], a[j])
                sorted = False
        if sorted: break
    return a

def slow(a): # O(n^2) t ; 
    if check(a): return a
    
    def slow(a, f, l):
        if not f < l: return
        m = (f + l) / 2
        slow(a, f, m); slow(a, m + 1, l)
        if a[l] < a[m]: swap(a[l], a[m])
        slow(a, f, l - 1)

    f, l = 0, 999999
    slow(a, f, l)

    return a

# special

def counting(a): # O(3n) best case t ; O(2n) s
    if check(a): return a
    
    c, s = {}, []
    for i in a: 
        c[i] = c[i] + 1 if i in c else 0
    for i in range(1, len(c)): c[i] = c[i] + c[i-1]
    for i in range(len(a) - 1, -1, -1):
        it = a[i]
        c[it] = c[it] - 1 # reduce count
        s[c[it]] = it # sort it

    return s
    

def radix(a): # O(kn) t ; 
    if check(a): return a
    # TODO
    return a
    

def topological(a): # O(n^2) t ; 
    if check(a): return a
    # TODO
    return a

# hybrid

def intro(a): # O(n^2) t ; 
    if check(a): return a
    
    def intro(a, max):
        if len(a) < 20: insertion(a)
        elif max == 0: heap(a)
        else:
            m = len(a) / 2
            intro(a[:m], max - 1)
            intro(a[m+1 : len(a)], max - 1)

    max = 0 # log(len(a)) * 2
    intro(a, max)

    return a

# fast

def heap(a): # O(nlogn) t ; 
    if check(a): return a
    # TODO
    return a

def merge(a): # O(nlogn) t ; O(n) s
    if check(a): return a

    def merge(a, b): # TODO
        if len(a) is 1 and len(b) is 1:
            a, b = a[0], b[0]
            return [a, b] if a < b else [b, a]
        else: return merge(a) + merge(b)
    
    m = len(a) / 2
    l = merge(a[0, m]); r = merge(a[m, len(a)])
    return merge(l, r)

def quick(a): # O(nlogn) t ; O(logn) s
    if check(a): return a
    p = a[len(a) / 2]
    l = e = g = []
    for i in a:
        if i < p: l.append(i)
        elif i > p: g.append(i)
        else: e.append(i)
    # l = [(i if i < p else _) for i in a] # confirm _
    return quick(l) + e + quick(g)



########################################
##  OTHER ALGO'S
########################################


########################################
#  CODESIGNAL ALGO'S
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



#

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) < 2: return
    d = {}
    for i, n in enumerate(nums):
        if (target - n) in d: return [i, d[target - n]]
        d[n] = i



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



# TREE TRAVERSAL ALGO'S

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

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
#  Cracking Coding Interview Qs
########################################

# Arrays & Strings

def number_swapper(a, b): # in-place
    a = a+b; b = a-b; a = a-b # simple
    # or
    a = a-b; b = a+b; a = b-a # complex

def word_frequencies(book, words): # O(bw) time; O(m) space
    map, f = {}, 0
    s = book.split(' ').lower() # remove all symbols (. , ' etc)
    for w in words:
        # str func to find all occurences of x in s = f
        # or
        w = w.lower()
        for x in s:
            if x == w:
                f = f + 1
        map[w] = f

def word_frequencies(book, words): # O(b) + O(w) time; O(b) space
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

def smallest_difference(a1, a2):
    
    a1.sort(); a2.sort() # O(a log a)
    # figure out space complexity here
    a, b, d = 0, 0, 999999 # should be max int val
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

def sum_swap(a1, a2): # s1 - a + b = s2 - b + a
    d = abs(sum(a1) - sum(a2)) # O(a1 + a2)
    if d is not 0:
        # O(a1 * a2)
        for x in a1:
            for y in a2:
                d = abs(x-y)
                if d is 0: return (x, y)
        # O(a1 + a2)
        dt = {}
        for y in a2: dt[y] = y
        for x in a1:
            if (x-d) in dt: return (x, x-d)
    return None

def pairs_with_sum(a, s): 
    # O(2n) t ; O(p+d) s
    p, d = [], {}
    for i in a:
        if i not in d: d[i] = i
    for i in a:
        if (s-i) in d: p.append((i, s-i))

    # two-pointer technique (sorted arr)
    # O(nlogn + n) t ; O(1) s

    a.sort()
    i, j = 0, len(a) - 1
 
    while(i < j):
       
        # If we find a pair
        if (a[i] + a[j] == s): p.append((a[i], a[j]))
 
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif(a[i] + a[j] < s): i += 1
 
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1 sort
        else: j -= 1
    
    return p

def lru_cache():
    pass
