import sys
import math
from collections import deque, defaultdict
from typing import List, Callable

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
                c = int((f"{s}")[:-1]) # or s / 10
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

    # Binary (Search) Trees

    class Tree():

        def __init__(self, x):
            self.value = x
            self.left = None
            self.right = None
            self.children = [] # for more than 2 children
        
        def add_child(self, t):
            self.children.append(t)
    
    def print_tree(self, tree, level=0):
        print("  " * level, tree.value)
        for child in tree.children:
            self.print_tree(child, level + 1)

    def print_tree_2(self, tree, indent=''):
        # Print the current noode's value
        print(indent + str(tree.value))

        # Recursively print each child with appropriate indentation
        for i, child in enumerate(tree.children):
            if i < len(tree.children) - 1:
                print(indent + '├── ', end='')
            else:
                print(indent + '└── ', end='')
            self.print_tree_2(child, indent + '│   ')
    
    def print_tree_3(self, tree, indent='', last=True):
        print(indent, end='')
        if last:
            print('└── ', end='')
            indent += '    '
        else:
            print('├── ', end='')
            indent += '│   '

        print(tree.value)

        # Recursively print each child with appropriate indentation
        child_count = len(tree.children)
        for i, child in enumerate(tree.children):
            self.print_tree_3(child, indent, i == child_count - 1)
    
    
    def dfs(self, tree):
        if tree is None or type(tree) is not DataStructures.Tree: return

        # DFS pre-order
        print(tree.value)
        self.dfs(tree.left)
        self.dfs(tree.right)
        for child in tree.children:
            self.dfs(child)

        # DFS post-order
        self.dfs(tree.left)
        self.dfs(tree.right)
        for child in tree.children:
            self.dfs(child)
        print(tree.value)

        # DFS in-order
        self.dfs(tree.left)
        print(tree.value)
        self.dfs(tree.right)
        ''' # TODO: test this option
        for child in tree.children:
            self.dfs(child)
            print(tree.value)
        '''
        # Traverse all children, except last child
        for i in range(len(tree.children) - 1):
            self.dfs(tree.children[i])
            print(tree.value)
        # Traverse last child
        if tree.children:
            self.dfs(tree.children[-1])
        print(tree.value)

    def bfs(self, tree):
        if tree is None or type(tree) is not DataStructures.Tree: return

        queue = deque()
        queue.append(tree)

        while queue:
            node = queue.popleft()
            print(node.value)
            queue.append(node.left)
            queue.append(node.right)
            for child in node.children:
                queue.append(child)
    
    def diameter(self): pass

    def max_depth_or_height(self): pass

    def is_BST(self): pass

    def lowest_common_ancestor(self): pass

    def unique_paths(self): pass

    # Tries
    
    # Graphs

    class Graph:

        def __init__(self): pass

        class DirectedGraph:
        
            def __init__(self, num_nodes):
                self.num_nodes = num_nodes + 1
                self.graph = [[0 for x in range(self.num_nodes)] for y in range(self.num_nodes)]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) and (v2 >= 0 and v2 <= self.num_nodes)

            def insert_edge(self, v1, v2):
                if self.within_bounds(v1, v2): self.graph[v1][v2] = 1
            
            def print_graph(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            print(f"{i} -> {j}")
            
            def test(self):
                g = DataStructures.Graph(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print_graph()

        class UndirectedGraph:
        
            def __init__(self, num_nodes):
                self.num_nodes = num_nodes + 1
                self.graph = [[0 for x in range(self.num_nodes)] for y in range(self.num_nodes)]
            
            def within_bounds(self, v1, v2):
                return (v1 >= 0 and v1 <= self.num_nodes) and (v2 >= 0 and v2 <= self.num_nodes)

            def insert_edge(self, v1, v2):
                if self.within_bounds(v1, v2):
                    self.graph[v1][v2] = 1
                    self.graph[v2][v1] = 1
            
            def print_graph(self):
                for i in range(self.num_nodes):
                    for j in range(len(self.graph[i])):
                        if self.graph[i][j] is not None:
                            print(f"{i} -> {j}")
            
            def test(self):
                g = DataStructures.Graph(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print_graph()

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

            class BellmanFord: 
                pass


    # Bits

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
#  LeetCode
########################################


# https://leetcode.com/problems/add-two-numbers/description/

class ListNode:

    def __init__(self, v=None, n=None):
        self.value = v; self.next = n


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: # todo: optimize
    ls = ListNode(); sa = []; c = 0
    s = l1.value + l2.value
    d = f"{s}"[-1:]
    c = int(f"{s}"[:-1])
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
        c = int(f"{s}"[:-1])
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
            c = int((f"{s}")[:-1]) # or s / 10
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
#  CodeSignal
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

