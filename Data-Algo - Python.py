# Given 2 sorted arrays, find the number of elements in common.
# Both arrays have the same length, and all distinct elements

def commonElems(arr1, arr2): # Brute-force algo [O(n^2)]
    nums = []
    for a1 in arr1:
        for a2 in arr2:
            if a1 is a2:
                nums.append(a1)
    print(nums)
    return len(nums)

def commonElems(arr1, arr2): # More optimized algo [time - O(n log n)] [space - should be O(n)]
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

def commonElems(arr1, arr2): # More optimized algo [time - O(2n) ~ O(n)] [space - should be O(n)]
    nums, d2 = [], {}
    for a2 in arr2:
        d2[a2] = a2
    
    for a1 in arr1:
        if a1 in d2:
            nums.append(a1)

    print(nums)
    return len(nums)

def commonElems(arr1, arr2): # Most optimized algo [time - O(n)] [space - should be O(1)]
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

def twoSum(nums, target):
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

def firstDuplicate(a):
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

def sumOfTwo(a,b,v):
    b = set(b)
    return any(v - x in b for x in a)


# 

def sumInRange(nums, queries):
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

def climbingStairs(n):
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

def fillingBlocks(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 5
    else:
        row = fillingBlocks0011(n-1)
        ccr = fillingBlocks0011(n-2)
        crc = fillingBlocks0110(n-2)
        cccc = fillingBlocks(n-2)
        return row + ccr + crc + cccc


def fillingBlocks0110(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return fillingBlocks(n) + fillingBlocks0110(n-2)
    

def fillingBlocks0011(n):
    if n == 0: return 1
    else: return fillingBlocks(n) + fillingBlocks0011(n-1)



# TREE TRAVERSAL ALGO'S

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# Given a binary tree of integers t, return its node values in the following format:

def traverseTree(t):
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

def largestValuesInTreeRows(t):
    res = []; helper(res, t, 0)
    return res
    

def helper(res, root, d):
    if not root: return
    if d == len(res): res.append(root.value)
    else: res[d] = max(res[d], root.value)
    
    helper(res, root.left, d+1)
    helper(res, root.right, d+1)
    

# We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

def digitTreeSum(t):
    return treePathsSum(t, 0)


def treePathsSum(t, v):
    if t is None: return 0
    v = (v*10) + t.value
    if t.left is None and t.right is None: return v
    return (treePathsSum(t.left, v) + treePathsSum(t.right, v))






########################################
#  OTHER ALGO'S
########################################










