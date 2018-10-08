
# coding: utf-8

# # Day 7 (9/21) in-class notebook
# 
# The objectives of this notebook are to practice
# 
# * checking if a graph is Eulerian
# * finding a cycle in a graph
# * using multiple inheritance in Python

# In this notebook we will work with graph data structures.  Included with this notebook is a graph module (graph.py), which contains the abstract base class `DirectedGraph` and trivial set implementation, `TrivialSetDirectedGraph`, from the Day 6 notebook.  We will use these graph interfaces and implementations throughout.

# In[1]:


import graph


# ### PROBLEM 1: Check if a graph is Eulerian (3 POINTS)
# First, write a function that takes as input a directed graph (i.e., an object that "is a" DirectedGraph), and returns whether the graph is Eulerian or not.  The function should assume that the graph is connected (i.e., there exists a path between every pair of vertices).

# In[2]:


def is_eulerian(g):
    """Returns True if DirectedGraph g is Eulerian.  Assumes that g is connected."""
    #
    # YOUR CODE HERE
    for i in range(g.num_vertices()):
        if g.indegree(i) != g.outdegree(i):
            return False
    else:
        return True
    #


# In[3]:


# test for is_eulerian g1
g1 = graph.TrivialSetDirectedGraph(4)
g1.add_edges([(0, 1), (1, 2), (1, 3), (2, 0), (2, 1), (3, 2)])
assert is_eulerian(g1)
print("SUCCESS: is_eulerian g1 test passed!")


# In[4]:


# test for is_eulerian g2 and g3
g2 = graph.TrivialSetDirectedGraph(4)
g2.add_edges([(0, 1), (1, 2), (1, 3), (2, 0), (3, 2)])
assert not is_eulerian(g2)
g3 = graph.TrivialSetDirectedGraph(4)
g3.add_edges([(0, 1), (1, 2), (1, 3), (2, 1), (3, 2)])
assert not is_eulerian(g3)
print("SUCCESS: is_eulerian g2 & g3 tests passed!")


# In[5]:


# test for is_eulerian g4 and g5
g4 = graph.TrivialSetDirectedGraph(2)
g4.add_edges([(0, 0), (0, 1), (1, 1), (1, 0)])
g5 = graph.TrivialSetDirectedGraph(1)
g5.add_edges([(0, 0)])
assert is_eulerian(g4)
assert is_eulerian(g5)
print("SUCCESS: is_eulerian g4 & g5 tests passed!")


# ### PROBLEM 2: Finding a cycle in an Eulerian graph (3 POINTS)
# Next, write a function that takes as input a Eulerian directed graph and a designated start vertex, and returns a cycle in the graph that starts and ends at the designated vertex and does use any edge more than once.  Note that this does **not** need to be an Eulerian cycle (which would traverse all edges).  Essentially, this function is tracing out the first cycle that would be found during the Eulerian cycle algorithm dicussed in the online lecture.
# 
# I encourage you to use the simple algorithm described in lecture, which is simply to traverse unused edges until you return to the start vertex.  You may find it useful to use a `set` object to keep track of edges that you have already used.

# In[29]:


a = [1]
b = [1,2,3,1]
curr_vertex = 1
print(a[:])
print(a)
print(a[0])
print(a[:1])
print(a[1:])
print("\n\n")
c = a[:a.index(1)]
print(c)
c.extend(b)
print(c)
c.extend(a[a.index(1)+1:])
print(c)


# In[39]:


from collections import deque
def find_cycle_in_eulerian_graph(g, start_vertex):
    """Returns a cycle in the Eulerian graph starting at the given vertex.
    The cycle is returned as a list of vertices with the same start and end vertex.
    Assumes that g is Eulerian."""
    #
    # YOUR CODE HERE
    path = [start_vertex]
    untraversed_edges = [edge for edge in g.edges()]
    vertices_with_more_outedges = deque([start_vertex])
    while vertices_with_more_outedges:
        curr_vertex = vertices_with_more_outedges.pop()
        out_edges = [out_edge for out_edge in g.out_edges(curr_vertex) if out_edge in untraversed_edges]
        curr_path = [curr_vertex]
        while out_edges:
            if len(out_edges) > 1:
                vertices_with_more_outedges.append(curr_vertex)
            traverse = out_edges[0]
            untraversed_edges.remove(traverse)
            #print("Traversing {} from {}".format(traverse,curr_vertex))
            curr_vertex = traverse[1]
            curr_path.append(curr_vertex)
            out_edges = [out_edge for out_edge in g.out_edges(curr_vertex) if out_edge in untraversed_edges]
            #print("Stop at {0} | {0}'s out edges {1} | curr_path {2}".format(curr_vertex, g.out_edges(curr_vertex), curr_path))
        new_path = path[:path.index(curr_vertex)]
        new_path.extend(curr_path)
        new_path.extend(path[path.index(curr_vertex)+1:])
        path = new_path
    print(path)
    return path
        
            
    
    
    
    
    
    
#     def get_a_cycle(untraversed_edges, start_vertex):
#         path = []
#         while out_edges:
#             untraversed_edges = [edge for edge in g.edges()]
#             if len(out_edges) > 1:
#                 vertices_with_more_outedges.append([curr_vertex])
#             traverse = out_edges[0]
#             print("Traversing {} from {}".format(traverse,curr_vertex))
#             path.append(traverse)
#             curr_vertex = traverse[1]
#             out_edges = [out_edge for out_edge in g.out_edges(curr_vertex) if out_edge not in path]
#             print("Stop at {0} | {0}'s out edges {1} | path so far {2}".format(curr_vertex, g.out_edges(curr_vertex), path))
#         return path
#     path = []
#     untraversed_edges = [edge for edge in g.edges()]
#     vertices_with_more_outedges = deque([start_vertex])
#     print(vertices_with_more_outedges)
#     while vertices_with_more_outedges:
#         curr_vertex = vertices_with_more_outedges[0]
#         out_edges = [out_edge for out_edge in g.out_edges(curr_vertex) if out_edge not in path]
        
#         return path
#     #

g1 = graph.TrivialSetDirectedGraph(4)
g1.add_edges([(0, 1), (1, 2), (1, 3), (2, 0), (2, 1), (3, 2)])
find_cycle_in_eulerian_graph(g1,0)


# In[40]:


# test for find_cycle_in_eulerian_graph g1
def is_cycle(g, path, vertex):
    """Returns True if path is a cycle in g that starts and ends with vertex."""
    # check for cyclical path with given start/end vertex
    if len(path) < 2 or path[0] != vertex or path[-1] != vertex:
        return False
    # check for distinct edges
    path_edges = set(zip(path[:-1], path[1:]))    
    if len(path_edges) != len(path) - 1:
        return False
    # check for existence of edges
    for i, j in path_edges:
        if not g.has_edge(i, j):
            return False
    return True

g1 = graph.TrivialSetDirectedGraph(4)
g1.add_edges([(0, 1), (1, 2), (1, 3), (2, 0), (2, 1), (3, 2)])
assert is_cycle(g1, find_cycle_in_eulerian_graph(g1, 0), 0)
assert is_cycle(g1, find_cycle_in_eulerian_graph(g1, 3), 3)
print("SUCCESS: find_cycle_in_eulerian_graph g1 test passed!")


# In[41]:


# test for find_cycle_in_eulerian_graph g4
g4 = graph.TrivialSetDirectedGraph(2)
g4.add_edges([(0, 0), (0, 1), (1, 1), (1, 0)])
assert is_cycle(g4, find_cycle_in_eulerian_graph(g4, 0), 0)
assert is_cycle(g4, find_cycle_in_eulerian_graph(g4, 1), 1)
print("SUCCESS: find_cycle_in_eulerian_graph g4 test passed!")


# In[42]:


# test for find_cycle_in_eulerian_graph g6
g6 = graph.TrivialSetDirectedGraph(4)
g6.add_edges([(0, 1), (0, 2), (0, 3),
              (1, 0), (1, 2), (1, 3),
              (2, 0), (2, 1), (2, 3),
              (3, 0), (3, 1), (3, 2)])
assert is_cycle(g6, find_cycle_in_eulerian_graph(g6, 3), 3)
assert is_cycle(g6, find_cycle_in_eulerian_graph(g6, 0), 0)
print("SUCCESS: find_cycle_in_eulerian_graph g6 test passed!")


# ## Adding edge weights and vertex labels to graphs via "mixin" classes
# In the Day 6 notebook, we saw how we could implement a graph data structure via Python classes and use inheritance to provide multiple alternative implementations.  Here, we will see how to easily add other features to graphs with "mixin" classes.  For example, we may want to allow edges to have weights and for vertices to have labels (e.g., read strings for overlap graphs).

# Below is a "mixin" class `VertexLabeledDirectedGraph`, which allows you to "mix in" the feature of vertices having labels, with any particular implementation of a directed graph.  This eliminates the need to make vertex labeled versions of every possible graph implementation ahead of time.  Take a look at how `VertexLabeledDirectedGraph` is implemented.

# In[43]:


class VertexLabeledDirectedGraph(graph.DirectedGraph):
    """A mixin class that allows for vertices in a directed graph to have labels."""
    
    def __init__(self, num_vertices):
        # call the next constructor in Python's Method Resolution Order
        super().__init__(num_vertices)
        self._vertex_labels = [None] * num_vertices

    def set_vertex_label(self, i, label):
        """Adds a label to vertex i."""
        self._vertex_labels[i] = label
       
    def vertex_label(self, i):
        """Returns the label of vertex i or None if it is not assigned a label"""
        return self._vertex_labels[i]


# Below is how we would use this "mix in" class to add vertex labels to the trivial set implementation of directed graphs.

# In[44]:


# To "mix", simply inherit from multiple classes!
class VertexLabeledTSDirectedGraph(graph.TrivialSetDirectedGraph, VertexLabeledDirectedGraph):
    pass


# And below is an example of how this new mixed class could be used.

# In[45]:


g = VertexLabeledTSDirectedGraph(3)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.set_vertex_label(0, "the first vertex")
g.set_vertex_label(2, "the third vertex")
print(g)
print("The label of vertex 0 is", repr(g.vertex_label(0)))
print("The label of vertex 1 is", repr(g.vertex_label(1)))
print("The label of vertex 1 is", repr(g.vertex_label(2)))


# ### PROBLEM 3: Adding functionality for edge weights via a "mixin" class (3 POINTS)
# Now try your hand at defining another mixin class that allows for DirectedGraphs to have edge weights.  Consider using a `dict` to store the weights of edges and take note of the [`get`](https://docs.python.org/3/library/stdtypes.html#dict.get) method of `dict` objects. 

# In[57]:


a = set()
print(a)
a.add(1)
print(a)
b = dict()
print(b)
b["a"] = "hi"
print(b)
i = 2
j = 3
weight = 7
b[(i,j)] = weight
print(b)


# In[61]:


class EdgeWeightedDirectedGraph(graph.DirectedGraph):
    """A mixin class that allows for edges in a directed graph to have weights."""
    
    def __init__(self, num_vertices):
        #
        # YOUR CODE HERE
        super().__init__(num_vertices)
        self._edges = set()
        self._edge_weights = dict()
        #

    def add_weighted_edge(self, i, j, weight):
        """Adds an edge to the graph with the given weight."""        
        #
        # YOUR CODE HERE
        self._edges.add((i,j))
        self._edge_weights[(i,j)] = weight
        
        #
       
    def edge_weight(self, i, j):
        """Returns the weight of edge (i, j) or None if it is not assigned a weight"""
        #
        # YOUR CODE HERE
        return self._edge_weights.get((i,j))


# We can then use your class to add edge weight functionality to the trivial set implementation:

# In[62]:


class EdgeWeightedTSDirectedGraph(graph.TrivialSetDirectedGraph, EdgeWeightedDirectedGraph):
    pass


# Below is some example code that should run using the `EdgeWeightedTSDirectedGraph` class above.

# In[63]:


g = EdgeWeightedTSDirectedGraph(10)
g.add_weighted_edge(2, 4, 11)
g.add_weighted_edge(6, 1, 9)
g.add_edge(1, 2) # add unweighted edge
print(g)
print("Weight of edge (2, 4):", g.edge_weight(2, 4))
print("Weight of edge (6, 1):", g.edge_weight(6, 1))
print("Weight of edge (1, 2):", g.edge_weight(1, 2))


# In[64]:


# tests for EdgeWeightedTSDirectedGraph constructor
assert EdgeWeightedTSDirectedGraph.__init__ != graph.DirectedGraph.__init__, "__init__ not overridden"
test_graph = EdgeWeightedTSDirectedGraph(10)
assert str(test_graph) == "DirectedGraph with 10 vertices and 0 edge(s):\n[]"
print("SUCCESS: EdgeWeightedTSDirectedGraph constructor passed all tests!")


# In[65]:


# test for EdgeWeightedTSDirectedGraph add_weighted_edge
test_graph = EdgeWeightedTSDirectedGraph(10)
test_graph.add_weighted_edge(3, 5, 42)
assert test_graph.has_edge(3, 5)
test_graph.add_weighted_edge(2, 3, 43)
assert test_graph.has_edge(2, 3)
#
# AUTOGRADER TEST - DO NOT REMOVE
#
print("SUCCESS: EdgeWeightedTSDirectedGraph add_weighted_edge passed all tests!")


# In[66]:


# test for EdgeWeightedTSDirectedGraph edge_weight
test_graph = EdgeWeightedTSDirectedGraph(10)
test_graph.add_weighted_edge(3, 5, 42)
assert test_graph.edge_weight(3, 5) == 42
test_graph.add_weighted_edge(2, 3, 43)
assert test_graph.edge_weight(2, 3) == 43
test_graph.add_edge(1, 2) # We should be able to add an edge without a weight
assert test_graph.edge_weight(1, 2) is None
#
# AUTOGRADER TEST - DO NOT REMOVE
#
print("SUCCESS: EdgeWeightedTSDirectedGraph add_weighted_edge passed all tests!")


# In[ ]:




