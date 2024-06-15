import sys
import math
from typing import List, Callable
from collections import deque, defaultdict
import heapq

import numpy as np
import pandas as pd

# TODO: NB: Algo, Correctness, Speed / Execution Time, Uniqueness

'''

..

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
            m = (f + l) / 2
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
            if x is i: return x
        return None

    def binary_search(self, a, x):
        a.sort() # or - sorted(a) # O(n log n) t
        if len(a) is 0: return None

        def r_binary_search(a, x):
            if len(a) is 0: return None
            m = len(a) / 2 # better math.floor(len(a) / 2)
            if x < a[m]: return r_binary_search(a[:m-1], x)
            elif x > a[m]: return r_binary_search(a[m+1:], x)
            else: return m

        def r_binary_search(a, x, f, l):
            if len(a) is 0 or f > l: return None
            m = (f + l) / 2 # better - math.floor(f + (l - f) / 2) (NB: pemdas / bodmas)
            if x < a[m]: return r_binary_search(a, x, f, m - 1)
            elif x > a[m]: return r_binary_search(a, x, m + 1, l)
            else: return m

        f, l = 0, len(a) - 1
        r_binary_search(a, 7); r_binary_search(a, 7, f, l)

        while f < l:
            m = (f + l) / 2 # better - math.floor(f + (l - f) / 2) (NB: pemdas / bodmas)
            if x < a[m]: l = m - 1
            elif x > a[m]: f = m + 1
            else: return m
        return None



########################################
##  OTHER ALGO'S
########################################

# Data Structures (Arrays, Strings, Matrices, etc)

class DataStructures:

    def __init__(self): pass
    
    # Arrays & Strings

    def reverse(self, a: list): pass

    def longest_common_substring(self, s): pass

    def min_jumps(self, a): pass

    # (Array) Lists & Tuples

    # Sets & Sequences

    # HashMaps & HashTables

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

        # 3rd-Party - Alt-logic # test

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
            node = next = ans
            ans.next = head
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


    # todo: End of set of Alt (3rd-Party) Logic Samples


    # Stacks & Queues

    # Heaps (max & min)
    
    # Binary Heaps & Priority Queues

    # Trees

    class Tree(): # Acyclic Undirected Graph - a tree if connected, and a forest if not connected
            
        class TreeNode():

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
            code (value) - first search
            depth - first search
        ''' 


        def bfs(self, root): #  # O(n) t ; O(1) s
            # * uses queue in while loop
            if root is None or type(root) is not DataStructures.Tree.TreeNode:
                return
            
            '''
            BFS always traverses horizontally (whether from left/right first), layer by layer
            '''

            # BFS - Queue-Loop traversal

            queue = deque()
            queue.append(root)

            while queue: # No pre/post/in - order in BFS

                node = queue.popleft() # queue - fifo, so pop oldest item (no .popright())
                print(node.value)

                # BFS "Straight" order - .left to .right
                queue.append(node.left)
                queue.append(node.right)
                for child in node.children:
                    queue.append(child)
        
                # NB: BFS "Reverse" - order - .right to .left
                queue.append(node.right)
                queue.append(node.left)
                for child in node.children[::-1]:
                    queue.append(child)
        
        def cfs(self, root=None, cb=None): # O(log n) t : O(1) s
            if root is None or cb is None: return None

            while root is not None and root.value is not None:
                res = cb(root)
                if res == 'l': self.cfs(root.left, cb)
                elif res == 'r': self.cfs(root.right, cb)
                else: return res # or root / root.value
        
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


            # Stack-Loop Tree-Traversals (all .left to .right, except post-order)
            
            # O(n) t ; O(h ~ 1) s (h - max height)
            
            # Stack takes in nodes until max-height h, and pops them out alongside algo; doesn't maintain all nodes for algo's exec
            # List (despite n - total) is only used to record traversed values to be returned, not within algo's actual complexity
            # could do away with List by just printing out node.value()s


            # DFS pre-order - Stack-Loop traversal
            stack, node = [], root

            while node or len(stack) > 0:
                if node:
                    print(node.value)
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    node = node.right

            # DFS in-order - Stack-Loop traversal
            stack = [], node = None

            while node or len(stack) > 0:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    print(node.value)
                    node = node.right

            # DFS post-order - Stack-Loop traversal - .right to .left
            stack = [], node = None

            while node or len(stack) > 0:
                if node:
                    print(node.value)
                    stack.append(node)
                    node = node.right
                else:
                    node = stack.pop()
                    node = node.left
            

            # Iterator Traversals

            class Iterator:

                def __init__(self, root):
                    self.node = root
                    self.stack = []
                
                def has_next(self): self.node or len(self.stack) > 0

                def next(self):
                    while self.has_next():
                        if self.node:
                            stack.append(self.node)
                            self.node = self.node.left
                        else:
                            self.node = self.stack.pop()
                            res = self.node.value
                            self.node = self.node.right
                            return res
                    return sys.maxsize
                
                def test(self):
                    it = Iterator()
                    print(it.next())
                    print(it.next())
                    print(it.has_next())
                    print(it.next())
                    print(it.next())
                    print(it.has_next())


        def diameter(self): pass

        def max_depth_or_height(self): pass

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
            return self.cfs(
                self.root, 
                cb=lambda root: None if not (root and root.value) \
                    else root if root.value == v \
                    else 'l' if root.value < v \
                    else 'r'
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
                    return self.root # not the newly added node
                else: # check traverse left/right
                    if root.value < v: return 'l'
                    else: return 'r' # root.value == v - already checked
                    
            return self.cfs(self.root, cb=cb)
        
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
                        loop_node = root.right; leaf_left = None
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
                    if root.value < v: return 'l'
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
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)

            # Option 2: with checked only

            while len(queue) > 0:
                node = queue.popleft() # deque: .popleft() 1st item (.pop() last item ; .pop(0) error - takes no argument)
                # if queue = [], .pop(0) 1st item
                if node not in checked:
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
    # O(2n) t | O(d+p) s
    p, d = [], {}
    for i in a:
        if i not in d: d[i] = i
    for i in a:
        if (s-i) in d: p.append((i, s-i))

    # O(n) t | O(d+p) s
    for i in a: # combining 2 loops into 1
        if (s-i) in d: p.append((i, s-i))
        if i not in d: # needed if a doesn't have distinct elements
            d[i] = i

    # two-pointer technique (sorted arr)
    # O(nlogn + n) t | O(1) s

    a.sort() # O(nlogn) (quick) sort
    i, j = 0, len(a) - 1

    while(i < j):
       
        # If we find a pair
        if (a[i] + a[j] == s): p.append((a[i], a[j]))
 
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by incrementing i += 1
        elif(a[i] + a[j] < s): i += 1
 
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by decrementing j -= 1
        else: j -= 1
    
    return p

# same as above, but returning indices of elements, not elements themselves

def two_sum(nums, target): 
    if len(nums) < 2: return
    d = {}
    for i, n in enumerate(nums):
        if (target - n) in d: return [i, d[target - n]]
        d[n] = i

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


#

def two_sum(nums, target): # returning indices of elements, not elements themselves
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
##  EXTRA TESTS
########################################

def wave_array(arr): #nlogn + (n/2)
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

