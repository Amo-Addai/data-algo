import sys
import numpy as np
import pandas as pd
import keras
import tensorflow as t

'''
LEARN

for - iter, k/v, ..
..

'''

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

    def insertion(self, a): # O(n^2) t ; O(1) s
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

    def selection(self, a): # O(n^2) t ; O(1) s
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

    def bubble(self, a): # O(n^2) t ; O(1) s
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

    def counting(self, a): # O(3n) best case t ; O(2n) s
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

    def merge(self, a): # O(nlogn) t ; O(n) s
        if self.check(a): return a

        def merge(a, b): # TODO
            if len(a) is 1 and len(b) is 1:
                a, b = a[0], b[0]
                return [a, b] if a < b else [b, a]
            else: return self.merge(a) + self.merge(b)
        
        m = len(a) / 2
        l = self.merge(a[:m]); r = self.merge(a[m:])
        return merge(l, r)

    def quick(self, a): # O(nlogn) t ; O(logn) s
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
##  OTHER ALGO'S
########################################


class DataStructures:

    def __init__(self): pass
    
    # Arrays & Strings

    def reverse(self, a: list): pass

    def longest_common_substring(self, s): pass

    def min_jumps(self, a): pass

    # Sets & Sequences

    # HashMaps & Dictionaries

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
            obj = Matrix()
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

            def __init__(self, v, n=None, p=None): 
                self.v = v; self.n = n; self.p = p
            
            def be_next_of(self, l):
                l.n = self
                return l
            
            def be_prev_of(self, r):
                r.p = self
                return r
            
            @staticmethod
            def from_array(a): 
                pass # TODO
                # nodes = [ListNode(i) for i in a]
                # nodes.__reduce__(lambda(acc: ListNode, cur: ListNode): acc.be_next_of(cur))
            
            def for_each(self, cb, i):
                cb(self.v, i)
                if self.n is not None:
                    self.n.for_each(cb, i + 1)


        def __init__(self, l: ListNode): 
            self.r = l


    def reverse(self, l: LinkedList): pass

    def merge(self, l1, l2): 
        
        # sorted 
        pass
        # unsorted
        

    def add(self, l1, l2): pass
        
    def add_nums(self, a, b): pass

    # Stacks & Queues

    # Heaps (max & min)

    # Trees

    # Binary (Search) Trees

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
                g = Graph(5)
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
                g = Graph(5)
                g.insert_edge(1, 2)
                g.insert_edge(2, 3)
                g.insert_edge(4, 5)
                g.print_graph()
        
        # 
        
        
        class DijkstrasAlgorithm:

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
                algo = DijkstrasAlgorithm(m, 0)
                algo.calculate()
                algo.print_distance()


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
    # O(2n) t ; O(d+p) s
    p, d = [], {}
    for i in a:
        if i not in d: d[i] = i
    for i in a:
        if (s-i) in d: p.append((i, s-i))

    # O(n) t ; O(d+p) s
    for i in a: # combining 2 loops into 1
        if (s-i) in d: p.append((i, s-i))
        if i not in d: # needed if a doesn't have distinct elements
            d[i] = i

    # two-pointer technique (sorted arr)
    # O(nlogn + n) t ; O(1) s

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


# Linked Lists


# Trees


# Graphs



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



# LINKED LIST TRAVERSAL ALGO'S


# Singly-linked list (interface already defined)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ls = ListNode(); sa = []; c = 0
    s = l1.val + l2.val
    d = f"{s}"[-1:]
    c = int(f"{s}"[:-1])
    sa.append(d)
    ls.val = d
    while (l1.next is not None) or (l2.next is not None):
        if l1.next is not None: 
            l1 = l1.next
            c += l1.val
        if l2.next is not None: 
            l2 = l2.next
            c += l2.val
        s = c
        d = f"{s}"[-1:]
        c = int(f"{s}"[:-1])
        sa.append(d)
        ls.next = ListNode(val=d)
    return ls # or return s



# TREE TRAVERSAL ALGO'S


# Binary tree (interface already defined)
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

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
##  TEST CASES
########################################

if __name__ == "__main__":
    print("Hello, World!")
