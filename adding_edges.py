class Adding_Edges:

    def __init__(self, V):
        self.V = V  # Number of vertices
        self.adj_list = [[] for _ in range(V)]  # Adjacency list
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def is_planar(self):
        if self.V < 5 or self.adj_list < 9:
            return True 

        if self.V >=3 * self.V - 6:
            return False  # Kuratowski's theorem
        

        return self.can_add_edges()
    
    def can_add_edges(self):
        visited = [[] for _ in range(self.V)]
        