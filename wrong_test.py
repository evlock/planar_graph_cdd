class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        
    def is_planar_util(self, u, parent, visited):
        visited[u] = True
        for v in self.adj_list[u]:
            if not visited[v]:
                if self.is_planar_util(v, u, visited):
                    return True
            elif v != parent:
                return True
        return False
    
    def is_planar(self):
        visited = [False] * self.num_vertices
        for v in range(self.num_vertices):
            if not visited[v]:
                if self.is_planar_util(v, -1, visited):
                    return False
        return True


# Example usage:
G = Graph(7)
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 6)

f = [[_] for _ in range(2)]
if G.is_planar():
    print("The graph is planar.")
else:
    print("The graph is not planar.")
print(f"vertices{G.adj_list}")
print(f"{f}")