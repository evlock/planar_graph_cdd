import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, V):
        self.V = V  # Number of vertices
        self.adj_list = [[] for _ in range(V)]  # Adjacency list

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_planar(self):
        if self.V < 4:
            return True  # All graphs with 3 or fewer vertices are planar

        if self.V > 2 * self.V - 4:
            return False  # Kuratowski's theorem

        return self.can_add_edges()

    def can_add_edges(self):
        # Initialize visited array for DFS traversal
        visited = [False] * self.V

        for v in range(self.V):
            # Skip vertices that have already been visited
            if visited[v]:
                continue

            # Perform DFS from vertex v
            if not self.dfs(v, visited):
                return False

        return True

    def dfs(self, v, visited):
        visited[v] = True
        num_edges = len(self.adj_list[v])
        edges_added = 0

        for u in self.adj_list[v]:
            if not visited[u]:
                # Add edge (u, v)
                edges_added += 1
                visited[u] = True

                # Check if adding edge causes a crossing
                if edges_added >= 2:
                    return False

                # Recur for adjacent vertices
                if not self.dfs(u, visited):
                    return False

        return True


# Example usage
if __name__ == "__main__":
    n = 8
    non_graph = Graph(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            non_graph.add_edge(i, j) 
            print(f"{i}" ", " f"{j}")

    # Check if the graph is planar
    if non_graph.is_planar():
        print("The graph is planar.")
    else:
        print("The graph is not planar.")

    G = nx.Graph()
    for v in range(non_graph.V):
        for u in non_graph.adj_list[v]:
            G.add_edge(v, u)

    # Draw the graph
    pos = nx.spring_layout(G)  # Positioning algorithm
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()


class Graph2:
    def __init__(self, V):
        self.V = V  # Number of vertices
        self.adj_list = [[] for _ in range(V)]  # Adjacency list

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_planar(self):
        if self.V < 3:
            return True  # All graphs with 2 or fewer vertices are planar

        if self.V > 2 * self.V - 4:
            return False  # Kuratowski's theorem

        return self.kuratowski_planarity_check()

    def kuratowski_planarity_check(self):
        # Planarity check based on Kuratowski's theorem (simplified)
        # For simplicity, we'll assume all edges are distinct

        # Check for presence of K5 (complete graph on 5 vertices)
        for v in range(self.V):
            if len(self.adj_list[v]) >= 5:
                return False

        # Check for presence of K3,3 (bipartite complete graph on 3+3 vertices)
        for v in range(self.V):
            if len(self.adj_list[v]) >= 3:
                count_neighbors = 0
                for u in self.adj_list[v]:
                    if len(self.adj_list[u]) >= 3:
                        count_neighbors += 1
                if count_neighbors >= 3:
                    return False

        return True
    