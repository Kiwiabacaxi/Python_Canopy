# Undirected Graphs - Adjacency Matrix Representation
# Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph.

# class for an undirected graph
from dataclasses import dataclass


@dataclass
class GraphStatic:
    """ base class for an undirected graph
    """
    # type hinting
    vertices: int
    matrix: list[list[int]]
    
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    def add_edge(self, u: int, v: int):
        """ add edge to the graph
        """
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
        
    def remove_edge(self, u: int, v: int):
        """ remove edge from the graph
        """
        if self.matrix[u][v] == 0:
            return
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0
        
    def print_graph(self):
        """ print the graph
        """
        for row in self.matrix:
            print(row) # print each row of the matrix
            
        
# Test
# create the graph
graph = GraphStatic(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

# print the graph
graph.print_graph()

# remove edge
graph.remove_edge(1, 2)
print()

# print the graph
graph.print_graph()

# output:
# [0, 1, 1, 0]
# [1, 0, 1, 0]
# [1, 1, 0, 1]
# [0, 0, 1, 0]

# [0, 1, 0, 0]
# [1, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 0, 1, 0]
    