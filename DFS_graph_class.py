class Graph:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.visited = set()

    def add_edge(self,v,u):
        self.graph[v].append(u)

    def dfs(self,root):
        if root not in self.visited:
            print(root)
            self.visited.add(root)
            for neighbor in self.graph[root]:
                self.dfs(self, neighbor)

G = Graph(4)
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(1,3)

dfs(visited.graph, "A")

        