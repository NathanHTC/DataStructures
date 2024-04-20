#adjacency list for undirected graph 
class Graph:
    def __init__(self):
        #dictionary, key is unique, value is adjacency list
        self.adjList = {}
    #each index is a vertex e.g i = 0  i is adjacent to [x, y, z] vertex 
    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = set() #using set instead of list
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjList[u].add(v)
        self.adjList[v].add(u)

    def display(self):
        for vertex in self.adjList:
            print(self.adjList[vertex])


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 1)
g.add_edge(1, 2)

g.display()