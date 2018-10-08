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

class TrivialSetDirectedGraph(DirectedGraph):
    """A trivial implementation of a Directed Graph that simply stores edges in a set.
    Not meant for serious use.
    """
    
    def __init__(self, num_vertices):
        # call the next constructor in Python's Method Resolution Order
        super().__init__(num_vertices)
        # start with an empty set of edges
        self._edges = set()
    
    def has_edge(self, i, j):
        return (i, j) in self._edges
        
    def add_edge(self, i, j):
        self._edges.add((i, j))




# class FullyConnectedWeightedGraph:
#
#     def __init__(self, list_of_vertices, weight_function):
#         self.vertex_LUT = dict()
#         self._vertices = list_of_vertices
#         self._num_vertices = len(self._vertices)
#         for i, vertex in enumerate(list_of_vertices):
#             self.vertex_LUT[vertex] = i
#         self.weights = [[None]*self.num_vertices()]*self.num_vertices()
#         self.set_weights(weight_function)
#
#     def set_weights(self, weight_function):
#         return
#
#     def num_vertices(self):
#         return self._num_vertices
#
#     def has_vertex(self, vertex):
#         return vertex in self._vertices
#
#     def get_vertex_value(self, index):
#         return self._vertices[index]
#
#     def get_vertex_index(self, vertex_value):
#         return self.vertex_LUT[vertex_value]
#
#     def set_weights(self, weight_function):
#         for i in range(self.num_vertices()):
#             for j in range(i + 1, self.num_vertices()):
#                 self.add_edge(i, j, weight_function(self.get_vertex_value(i), self.get_vertex_value(j)))
#                 self.add_edge(j, i, weight_function(self.get_vertex_value(j), self.get_vertex_value(i)))
#
#     def out_edges(self, i):
#         """Returns a list of directed edges outgoing from vertex i."""
#         return [(i, j, self.get_edge_weight(i,j)) for j in range(self._num_vertices) if self.has_edge(i, j)]
#
#     def add_edge(self, i, j):
#
#     def has_edge(self,i,j):
#         return not i == j
#
#     def in_edges(self, j):
#         """Returns a list of directed edges incoming to vertex j."""
#         return [(i, j, self.get_edge_weight(i, j)) for i in range(self._num_vertices) if self.has_edge(i, j)]
#
#     def get_edge_weight(self,i,j):
#         return self.weights[i][j]
#
#     def num_edges(self):
#         return self.num_vertices() ** 2 - self.num_vertices()
#
#     def __str__(self):
#         return "WeightedGraph with %d vertices and %d edge(s):\n%s" % (self.num_vertices(),
#                                                                        self.num_edges(),
#                                                                        self._edges)
#
#     def edges(self):
#         """Returns an iterator over the edges of the graph."""
#         for i in range(self._num_vertices):
#             for j in range(i+1,self._num_vertices):
#                 yield (i,j,self.get_edge_weight(i,j))
#
#
#
#
#
#
#     def __repr__(self):
#         pass

class FullyConnectedWeightedGraph(DirectedGraph):

    def __init__(self, list_of_vertices, weight_function, sort = False):
        # set vertex values
        self.vertex_LUT = dict()
        if sort:
            list.sort(list_of_vertices)
        self._vertices = list_of_vertices
        self._num_vertices = len(self._vertices)
        for i, vertex in enumerate(list_of_vertices):
            self.vertex_LUT[vertex] = i
        #set weights
        g = [None]*self.num_vertices()
        for i in range(self.num_vertices()):
            g[i] = [0]*self.num_vertices()
        self.weights = g

        self.set_weights(weight_function)

    def add_edge(self, i, j):
        self.weights[i][j] = self.weight_function(i,j)

    def set_weights(self, weight_function):
        def _set_weights(self):
            for i in range(self.num_vertices()):
                for j in range(i + 1, self.num_vertices()):
                    self.add_edge(i, j)
                    self.add_edge(j, i)
        def vertex_index_weight_function(i,j):
            return weight_function(self.get_vertex_value(i), self.get_vertex_value(j))
        self.weight_function = vertex_index_weight_function
        _set_weights(self)

    def num_vertices(self):
        return self._num_vertices

    def has_vertex(self, vertex):
        return vertex in self._vertices

    def get_vertex_value(self, index):
        return self._vertices[index]

    def get_vertex_index(self, vertex_value):
        return self.vertex_LUT[vertex_value]

    def has_edge(self,i,j):
        if self.weights[i][j] == None:
            return False
        else:
            return True

    def out_edges(self, i):
        """Returns a list of directed edges outgoing from vertex i."""
        return [(self.get_vertex_value(i), self.get_vertex_value(j), self.get_edge_weight(i,j)) for j in range(self._num_vertices) if self.has_edge(i, j)]

    def in_edges(self, j):
        """Returns a list of directed edges incoming to vertex j."""
        return [(self.get_vertex_value(i), self.get_vertex_value(j), self.get_edge_weight(i, j)) for i in range(self._num_vertices) if self.has_edge(i, j)]

    def get_edge_weight(self,i,j):
        return self.weights[i][j]

    def edges(self):
        """Returns an iterator over the edges of the graph."""
        for i in range(self._num_vertices):
            for j in range(self._num_vertices):
                if self.has_edge(i,j):
                    yield (self.get_vertex_value(i),self.get_vertex_value(j),self.get_edge_weight(i,j))
                else:
                    pass

    def highest_weight_path(self, tie_function):
        untraversed_vertices = [i for i in range(self.num_vertices())]
        path = []
        def max_weight_edges():
            max_weight = 0
            max_edges = []
            for i in untraversed_vertices:
                for j in untraversed_vertices:
                    if self.has_edge(i,j):
                        edge_weight = self.get_edge_weight(i,j)
                        if max_weight < edge_weight:
                            max_weight = edge_weight
                            max_edges = [(i,j)]
                        elif max_weight == edge_weight:
                            max_edges.append((i,j))
            return max_edges

        def get_next_vertex(start_vertex):
            max_weight = 0
            next_vertex = None
            for j in untraversed_vertices:
                if self.has_edge(start_vertex, j):
                    if max_weight < self.get_edge_weight(start_vertex, j):
                        next_vertex = j
                    elif max_weight == self.get_edge_weight(start_vertex, j):
                        if not next_vertex: next_vertex = j
                        else:
                            choose_j = tie_function(next_vertex, j)
                            if choose_j:
                                next_vertex = j
            return next_vertex
        next_vertex = max_weight_edges()[0][0]
        path.append(next_vertex)
        untraversed_vertices.remove(next_vertex)
        while untraversed_vertices:
            next_vertex = get_next_vertex(next_vertex)
            path.append(next_vertex)
            untraversed_vertices.remove(next_vertex)
        return [self.get_vertex_value(i) for i in path]





if __name__ == '__main__':
    print("Test!")
    func = lambda x, y: x+y
    print(func(1,2))
    g = FullyConnectedWeightedGraph([1,2,3], func)
    print(g)



