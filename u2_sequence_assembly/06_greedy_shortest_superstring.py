
# coding: utf-8

# # Day 6 (9/19) in-class notebook
# 
# The objectives of this notebook are to practice
# 
# * the concept of read overlap and merging
# * finding solutions to the shortest superstring task
# * implementing graph data structures
# * defining Python classes
# * using inheritance with Python classes

# ## The shortest superstring problem

# ### PROBLEM 1: Finding the maximum overlap length of two strings (reads) (1 POINT)
# 
# A key component of most algorithms for addressing the shortest superstring problem is determining the length of the longest exact overlap between two strings.  In particular, for two strings, $left$ and $right$, we need to compute $overlap\_length(left, right)$, which is defined as the length of the longest **suffix** of $left$ that is a **prefix** of $right$.  Define a function that computes this value.  You may find the [endswith](https://docs.python.org/3/library/stdtypes.html#str.endswith) or [startswith](https://docs.python.org/3/library/stdtypes.html#str.startswith) methods of Python string objects helpful.  You do not need to implement the most efficient algorithm possible (a simple polynomial-time algorithm will suffice).

# In[1]:


# def overlap_length_fail(left, right):
#     """Returns the length of the longest suffix of left that is a prefix of right"""
#     #
#     # YOUR CODE HERE
#     overlap_list = []
#     overlap_len = 0
# #    print("{} | {}".format(left_reverse, right))
#     for i, c in enumerate(left):
# #        print(len(right))
#         if(i > len(right)-1): 
#             break
# #        print(i, right[i], c)
#         if right[i] == c:
#             overlap_len += 1
#             overlap_list.append(c)
# #            print("Len: {} | Str: {}".format(overlap_len, ''.join(overlap_list)))
#         else: break
#     return overlap_len
#     #
# #print("Overlap Len: ",overlap_length_fail("apple","app"))
# #print("Overlap Len: ",overlap_length_fail("hidrea","aeroplane"))


# def overlap_length(left, right):
#     """Returns the length of the longest suffix of left that is a prefix of right"""
#     #
#     # YOUR CODE HERE
#     overlap = ''
#     shorter_string_len = len(left) if left < right else len(right)
# #    print(shorter_string_len)
#     for i in range(shorter_string_len):
#         if left[-i-1:] == right[:i+1]:
#             overlap = left[-i-1:]
# #        #print(i)
# #        print(left[-1-i:])
# #        print(right[:i+1])
# #            #overlap = right[:i]
# #        #print(overlap)
#     return len(overlap)
# # tests for overlap_length
# #overlap_length("ATGC", "GCAT")


# In[2]:


def overlap_length(left, right):
    """Returns the length of the longest suffix of left that is a prefix of right"""
    #
    # YOUR CODE HERE
    overlap = ''
    shorter_string_len = len(left) if left < right else len(right)
    for i in range(shorter_string_len):
        if left[-i-1:] == right[:i+1]:
            overlap = left[-i-1:]
    return len(overlap)


# In[3]:


# tests for overlap_length
assert overlap_length("ATGC", "GCAT") == 2
assert overlap_length("AGCA", "AGCA") == 4
assert overlap_length("AGAG", "GAGT") == 3
assert overlap_length("GAGT", "AGAG") == 0
assert overlap_length("ATGC", "CA") == 1
assert overlap_length("CA", "ATCG") == 1
assert overlap_length("", "") == 0
print("SUCCESS: overlap_length passed all tests!")


# ### PROBLEM 2: Merging ordered reads (1 POINT)
# One way to think about constructing a superstring for a set of strings (reads) is to note that any given superstring imposes an ordering on the input strings, namely, the order in which those strings appear as substrings within the superstring.  With the assumption that no input string is a substring of any other input string, for any fixed ordering of of the input strings, there is a unique shortest superstring that imposes that ordering.  That superstring may be constructed by simply merging strings from left to right in the ordering, using the maximum possible overlap between adjacent strings.  Write a function below that computes the shortest superstring for a given ordered list of strings (reads).  You will likely need your `overlap_length` function from above.

# In[4]:


def overlap_left_end_index(left, right):
    """Returns the length of the longest suffix of left that is a prefix of right"""
    #
    # YOUR CODE HERE
    overlap = ''
    left_end_index = None
    if not left or not right:
        return left_end_index
    shorter_string_len = len(left) if left < right else len(right)
    for i in range(shorter_string_len):
        if left[-i-1:] == right[:i+1]:
            overlap = left[-i-1:]
            left_end_index = -i-1
    return left_end_index
# if 'a':
#     print("True")

def merge_two_strings(left, right):
    left_end_index = overlap_left_end_index(left,right)
    merged_string = ''.join([left[:left_end_index],right])
    return merged_string

#print(merge_two_strings('dan ng', ' ngong'))

def merge_ordered_reads(reads):
    """Returns the shortest superstring resulting from merging 
    the elements of reads, an ordered list of strings"""
    #
    # YOUR CODE HERE
    superstring = ''
    for read in reads:
        superstring = ''.join(merge_two_strings(superstring,read))
    return superstring
    
    #


# In[5]:


# tests for merge_ordered_reads
assert merge_ordered_reads(["AGAG", "GAGT"]) == "AGAGT"
assert merge_ordered_reads(["AGAG"]) == "AGAG"
assert merge_ordered_reads(["AGAG", "GAGT", "AGTC"]) == "AGAGTC"
assert merge_ordered_reads(["AGAG", "CGAG", "TCGA"]) == "AGAGCGAGTCGA"
assert merge_ordered_reads([]) == ""
print("SUCCESS: merge_ordered_reads passed all tests!")


# ### PROBLEM 3: Brute-force shortest superstring algorithm (1 POINT)
# Continuing with the reasoning from the previous problem, note that a shortest superstring for a set of (unordered) strings corresponds to some ordering of the strings.  So if we try every possible ordering of the strings and compute the shortest superstring for each ordering (using the `merge_ordered_reads` function above), we could find a solution to the shortest superstring problem.  Write a function `shortest_superstring` below, which implements this "brute-force" strategy for solving the shortest superstring problem given a set of input strings (reads).
# 
# You will likely find the [`permutations`](https://docs.python.org/3/library/itertools.html#itertools.permutations) function from the [`itertools`](https://docs.python.org/3/library/itertools.html) module in the Python standard library of use.  This function returns an iterator over all possible orderings (permutations) of the sequence given to it as input.
# 
# In the case that there are multiple shortest superstrings, your function should return the superstring that is lexicographically smallest (i.e., first in alphabetical order).

# In[6]:


import itertools
import math


def shortest_superstring(reads):
    """Returns the shortest superstring of reads, a list of strings.
    In the case of multiple shortest superstrings, the lexicographically smallest is returned.
    Assumes that no string in the input is a substring of another input string.
    """
    #
    permutations = itertools.permutations(reads)
    shortest_superstring = merge_ordered_reads(reads)
    shortest_length = len(shortest_superstring)
    for p in permutations:
#        print(p)
#        print(shortest_superstring)
        superstring = merge_ordered_reads(p)
#        print(superstring)
        if len(superstring) < shortest_length:
            shortest_superstring = superstring
            shortest_length = len(superstring)
        elif len(superstring) == shortest_length and superstring < shortest_superstring:
            shortest_superstring = superstring
    return shortest_superstring
    
    #


# In[7]:


# tests for shortest_superstring
assert shortest_superstring(['AGAT', 'CAGA', 'ATAT']) == "CAGATAT"
assert shortest_superstring(['GACC', 'ATCC', 'TACC']) == "ATCCGACCTACC"
assert shortest_superstring(['TGA', 'GAC', 'ATGC']) == "ATGCTGAC"
assert shortest_superstring(['TGA']) == "TGA"
assert shortest_superstring(['TGA', 'CTG']) == "CTGA"
print("SUCCESS: shortest_superstring passed all tests!")


# ### Thinking about the brute-force shortest superstring algorithm
# Assuming you have written it correctly, the above function solves the shortest superstring problem.  Is the algorithm implemented by this function efficient?  In the cell below, write down your thoughts regarding the computational complexity of this algorithm.

# *YOUR THOUGHTS HERE REGARDING THE COMPUTATIONAL COMPLEXITY OF THE ALGORITHM YOU IMPLEMENTED ABOVE*
# It's awful. It is n!, which is something that needs to be avoided at all costs, even with ever-increasing processing power

# ### Experimenting with your shortest superstring algorithm
# If you have time, experiment with running your brute-force shortest superstring algorithm on various inputs.  For example,
# 
# 1. Experiment with inputs of random DNA strings (I've provided some code for you below to generate such strings).  How short can the shortest superstring be given random inputs, relative to the the trival superstring, which simply concatenates the input strings?  Perhaps try with many random inputs and plot the distribution of the shortest superstring length, say with the [hist](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html) function of Pyplot.
# 
# 2. Experiment with (very small sets) of strings generated by your shotgun sequencing simulator in the Day 4 notebook.  Does the shortest superstring reconstruct the full DNA sequence?  

# In[8]:


# Some functions that you may find of use in experimenting with random inputs of DNA strings
import random
DNA_BASES = "ACGT"

def random_dna_string(length):
    """Returns a random DNA string of the given length"""
    return ''.join([random.choice(DNA_BASES) for i in range(length)])

def random_dna_strings(length, num_strings):
    """Returns a list of num_strings random DNA strings of the given length"""
    return [random_dna_string(length) for i in range(num_strings)]


# *YOUR EXPERIMENTS HERE*
# Did not have time.

# ## Implementing graphs as Python classes
# Many sequence assembly algorithms are formulated in terms of *graphs*.  In this section of the notebook, we will define a Python class that implements a graph data structure.

# ### A base class for directed graphs
# 
# There are many possible ways to implement a graph data structure and each has its own strengths and weaknesses in terms of memory usage and efficiency of various graph operations.  Algorithms that use graphs do not necessarily need to know how those graphs are implemented, and therefore it is helpful to separate the *interface* of a graph object from its underlying *implementation*.  Classes are a great way to provide such abstractions.
# 
# Below I have provided a *base* class for a directed graph, which specifies the interface that a general directed graph object should have.  This is an *abstract base class*, which is only meant to provide an interface and some default method definitions.  It is not meant to be instantiated directly.  Note that the key methods of `had_edge` and `add_edge` are not implemented.
# 
# With this direct graph class, we simply refer to each vertex by an integer index (0 to `num_vertices - 1`), and an edge *from* vertex `i` *to* vertex `j` is represented by the tuple `(i, j)`.
# 
# Study the class definition below to understand the inferface and the default implementations.

# In[9]:


class DirectedGraph:
    """Abstract base class for a directed graph.

    A functional directed graph class can be obtained by inheriting from 
    this class and overriding the methods has_edge and add_edge.  All other
    methods have default implementations, which may not be the most efficient.
    These other methods should also be overriden as appropriate to improve
    efficiency.
    """
    def __init__(self, num_vertices):
        """Constructs a directed graph with num_vertices vertices and zero edges"""
        self._num_vertices = num_vertices
    
    def has_edge(self, i, j):
        """Returns True if the graph contains the directed edge (i, j), False otherwise."""
        raise NotImplementedError
        
    def add_edge(self, i, j):
        """Adds the directed edge (i, j) to the graph."""
        raise NotImplementedError
        
    def out_edges(self, i):
        """Returns a list of directed edges outgoing from vertex i."""
        return [(i, j) for j in range(self._num_vertices) if self.has_edge(i, j)]
    
    def in_edges(self, j):
        """Returns a list of directed edges incoming to vertex j."""
        return [(i, j) for i in range(self._num_vertices) if self.has_edge(i, j)]
    
    def outdegree(self, i):
        """Returns the outdegree of vertex i."""
        return len(self.out_edges(i))
    
    def indegree(self, i):
        """Returns the indegree of vertex i."""
        return len(self.in_edges(i))
    
    def degree(self, i):
        """Returns the degree of vertex i."""
        return self.indegree(i) + self.outdegree(i)
        
    def add_edges(self, edges):
        """Adds all edges from a list to the graph."""
        for i, j in edges:
            self.add_edge(i, j)
            
    def num_vertices(self):
        """Returns the number of vertices in the graph."""
        return self._num_vertices

    def num_edges(self):
        """Returns the number of edges in the graph."""
        return len(tuple(self.edges()))
    
    def edges(self):
        """Returns an iterator over the edges of the graph."""
        for i in range(self._num_vertices):
            for edge in self.out_edges(i):
                yield edge
    
    def __str__(self):
        """Returns a string representation of the graph, so that it may be printed."""
        return "DirectedGraph with %d vertices and %d edge(s):\n%s" % (self.num_vertices(),
                                                                       self.num_edges(),
                                                                       sorted(self.edges()))


# ### A trival functional DirectedGraph class
# As an example of how to construct a fully-functional class that provides the DirectedGraph interface, below is a class that simply stores its edges in a set.  This results in relatively inefficient graph operations.  Examine the implementation below and how it *inherits* functionality from the base class `DirectedGraph`.

# In[10]:


class TrivialSetDirectedGraph(DirectedGraph):
    def __init__(self, num_vertices):
        # call the parent class's constructor
        super().__init__(num_vertices)
        # start with an empty set of edges
        self._edges = set()
    
    def has_edge(self, i, j):
        return (i, j) in self._edges
        
    def add_edge(self, i, j):
        self._edges.add((i, j))


# In[11]:


# An example of using TrivalSetDirectedGraph
my_graph = TrivialSetDirectedGraph(4)
print(my_graph)
my_graph.add_edge(3, 0)
print(my_graph)
my_graph.add_edges([(0, 2), (2, 3), (3, 1)])
print(my_graph)
print("Outdegree of vertex 3 =", my_graph.outdegree(3))
print("Graph has edge (2, 3):", my_graph.has_edge(2, 3))
print("Graph has edge (3, 2):", my_graph.has_edge(3, 2))


# ### PROBLEM 4: Adjacency list implementation of a directed graph (4 POINTS)
# A more efficent and common implementation strategy for graphs is to use *adjacency lists*.  In an adjacency list data structure, for each vertex, a list of vertices to which that vertex is connected by an edge is maintained.  For directed graphs, two lists per vertex can be used, one for all vertices that are adjacent via an *outgoing* edge and one for all vertices that are adjacent via an *incoming* edge.
# 
# With this implementation strategy, define the `AdjacencyListDirectedGraph` class below.  You will need to provide concrete definitions for the methods `add_edge` and `has_edge`.  You also need to override the constructor `__init__`, and methods `out_edges`, `in_edges`, `indegree`, and `outdegree` to make them more efficient with this implementation.

# In[26]:


class AdjacencyListDirectedGraph(DirectedGraph):
    def __init__(self, num_vertices):
        #
        # YOUR CODE HERE
        self._num_vertices = num_vertices
        self._edges = set()
        
        #
    
    def add_edge(self, i, j):
        #
        # YOUR CODE HERE
        self._edges.add((i,j))
        #
    
    def has_edge(self, i, j):
        #
        # YOUR CODE HERE
        return (i,j) in self._edges
        #
        
    def out_edges(self, i):
        #
        # YOUR CODE HERE
        return [(i,j) for j in range(self.num_vertices()) if self.has_edge(i,j)]
            
        #
        
    def in_edges(self, j):
        #
        # YOUR CODE HERE
        return [(i,j) for i in range(self.num_vertices()) if self.has_edge(i,j)]
        #
    
    def indegree(self, i):
        #
        # YOUR CODE HERE
        return len(self.in_edges(i))
        #
        
    def outdegree(self, i):
        #
        # YOUR CODE HERE
        return len(self.out_edges(i))
        #
        
    def degree(self, i):
        """Returns the degree of vertex i."""
        return self.indegree(i) + self.outdegree(i)
        
    def add_edges(self, edges):
        """Adds all edges from a list to the graph."""
        for i, j in edges:
            self.add_edge(i, j)
            
    def num_vertices(self):
        """Returns the number of vertices in the graph."""
        return self._num_vertices

    def num_edges(self):
        """Returns the number of edges in the graph."""
        return len(tuple(self.edges()))
    
    def edges(self):
        """Returns an iterator over the edges of the graph."""
        for i in range(self._num_vertices):
            for edge in self.out_edges(i):
                yield edge
                
    
    def __str__(self):
        """Returns a string representation of the graph, so that it may be printed."""
        nv = self.num_vertices()
        ne = self.num_edges()
        e = sorted(self.edges())
        return "DirectedGraph with %d vertices and %d edge(s):\n%s" % (nv, ne, e)


# In[27]:


# test for AdjacencyListDirectedGraph constructor
assert AdjacencyListDirectedGraph.__init__ != DirectedGraph.__init__, "__init__ not overridden"
test_graph = AdjacencyListDirectedGraph(10)
assert str(test_graph) == "DirectedGraph with 10 vertices and 0 edge(s):\n[]"
print("SUCCESS: AdjacencyListDirectedGraph constructor passed all tests!")


# In[28]:


# test for AdjacencyListDirectedGraph add_edge and has_edge
test_graph = AdjacencyListDirectedGraph(10)
test_graph.add_edge(3, 5)
assert test_graph.has_edge(3, 5)
test_graph.add_edge(2, 3)
assert test_graph.has_edge(2, 3)
assert not test_graph.has_edge(3, 2)
assert sorted(test_graph.edges()) == [(2, 3), (3, 5)]
print("SUCCESS: AdjacencyListDirectedGraph add_edge and has_edge passed all tests!")


# In[29]:


# test for AdjacencyListDirectedGraph out_edges and in_edges
assert AdjacencyListDirectedGraph.out_edges != DirectedGraph.out_edges, "out_edges not overridden"
assert AdjacencyListDirectedGraph.in_edges != DirectedGraph.in_edges, "in_edges not overridden"
test_graph = AdjacencyListDirectedGraph(10)
test_graph.add_edges([(2, 3), (2, 4), (4, 0)])
assert test_graph.out_edges(2) == [(2, 3), (2, 4)]
assert test_graph.out_edges(0) == []
assert test_graph.in_edges(0) == [(4, 0)]
assert test_graph.in_edges(2) == []
print("SUCCESS: AdjacencyListDirectedGraph out_edges and in_edges passed all tests!")


# In[30]:


# test for AdjacencyListDirectedGraph outdegree and indegree
assert AdjacencyListDirectedGraph.outdegree != DirectedGraph.outdegree, "outdegree not overridden"
assert AdjacencyListDirectedGraph.indegree != DirectedGraph.indegree, "indegree not overridden"
test_graph = AdjacencyListDirectedGraph(10)
test_graph.add_edges([(2, 3), (2, 4), (4, 0)])
assert test_graph.outdegree(2) == 2
assert test_graph.outdegree(0) == 0
assert test_graph.indegree(0) == 1
assert test_graph.indegree(2) == 0
print("SUCCESS: AdjacencyListDirectedGraph outdegree and indegree passed all tests!")


# In[ ]:




