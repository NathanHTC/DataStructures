#the implementation of graph in python
#representation of graph in matrix
class Graph_matrix:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start, end):
        #undirected graph
        self.adj_matrix[start][end] = 1
        self.adj_matrix[end][start] = 1
    
    def remove_edge(self, start, end):
        self.adj_matrix[start][end] = 0
        self.adj_matrix[end][start] = 0

    def display_matrix(self):
        for row in self.adj_matrix:
            print(row)

g = Graph_matrix(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.display_matrix()

