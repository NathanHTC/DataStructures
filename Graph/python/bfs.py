#breath first search for graph represented in ajd list
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        #defaultdict initialize dict with a default function, a list, in this case; not need to check if index exists
        #when graph is represented in dict, keys are vertex, keys are unique
        self.adjList = defaultdict(list)
    
    def addEdge(self, u, v):
        self.adjList[u].append(v)
    
    def bfs(self, startNode):
        queue = deque()
        visited = {} #use a dictionary 

        #init
        visited[startNode] = True
        queue.append(startNode)

        #loop
        while queue:
            #vertex stored in queue are numbers; we use it as index to access the corresponding neighbors in self.adjList
            curNode = queue.popleft()
            print(curNode, end=" ")
            
            for neighbor in self.adjList[curNode]:
                #check for its unvisited neighbors
                if neighbor not in visited: #benefit of checking if visited in O(1) time
                    queue.append(neighbor)
                    visited[neighbor] = True
    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 4)

g.bfs(0)

#Time O(V+E)
#Space O(V)
    
