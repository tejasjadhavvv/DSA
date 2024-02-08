# here we have to do the pip command in the terminal pip install collection
from collections import deque

# Here the deque is the double ended queue and apply the FIFO METHOD 

class Graph:
    # This is the actually the intialization of the graph with the  empty dictionary
    def __init__(self):
        self.graph = {}
    # This is the actually the edge of the graph
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
        
        
    # This is the actually the recursive algo with the starting varible and the and the actually the implementation of depth first search787
    def dfs_recursive(self, start):
        visited = set()
        #This is actually the method for adding the unvisited vertex to the visited
        self._dfs_recursive_helper(start, visited)

    def _dfs_recursive_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive_helper(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("DFS traversal (recursive):")
g.dfs_recursive(0)
print()

print("BFS traversal:")
g.bfs(0)
print()
