import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_vertices):
        self.time = 0
        self.num_vertices = num_vertices # number of vertices
        self.graph = [[] for _ in range(num_vertices)] # list of neighbor lists
        self.traversal_array = [] # DFS traversal array result
        self.node_positions = None
        
    def add_edge(self, v, u):
        # add neighbers to neighber list
        self.graph[v].append(u)
        self.graph[u].append(v)
        print(f"{v}: {self.graph[v]}")


    def visualize_graph(self, visited_nodes, current_node):
        G = nx.Graph()
        for v in range(self.num_vertices):
            G.add_node(v)
            for u in self.graph[v]:
                G.add_edge(v, u)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        if self.node_positions is None:
            self.node_positions = nx.spring_layout(G)

        nodes_colors = ['orange' if node in visited_nodes else 'lightblue' for node in range(self.num_vertices)]
        
        if current_node is not None:
            nodes_colors[current_node] = 'red'

        nx.draw(G, pos=self.node_positions, with_labels=True, node_size=500, node_color=nodes_colors, font_weight='bold')

        plt.title('Graph Visualization with DFS Traversal')
        plt.show()

    def dfs(self, node, visited_nodes):
        self.visited[node] = True
        visited_nodes.append(node)
        self.visualize_graph(visited_nodes, node)
        
        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, visited_nodes)

        self.visualize_graph(visited_nodes, None)  # Revert color after exploring neighbors

    def dfs_with_visualization(self):
        self.visited = [False] * self.num_vertices
        plt.ion()
        
        for node in range(self.num_vertices):
            if not self.visited[node]:
                visited_nodes = []
                self.dfs(node, visited_nodes)

        plt.ioff()
        plt.show()

# Create the graph and perform DFS with visualization
G = Graph(10)  # Considering 10 nodes in the graph

# Adding 30 edges to the graph
edges = [
    (0, 1), (0, 2), (0, 3), (1, 4), (1, 5),
    (2, 6), (2, 7), (3, 8), (3, 9), (4, 5),
    (4, 6), (5, 7), (6, 8), (7, 9), (8, 9),
    (0, 4), (1, 6), (2, 8), (3, 7), (4, 9),
    (5, 8), (6, 9), (7, 5), (0, 8), (1, 7),
    (2, 9), (3, 6), (4, 8), (5, 9)
]

for edge in edges:
    G.add_edge(edge[0], edge[1])

G.dfs_with_visualization()
