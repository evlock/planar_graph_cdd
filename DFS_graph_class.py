class Graph:
    def __init__(self, num_vertices):
        self.time = 0
        self.num_vertices = num_vertices # number of vertices
        self.graph = [[] for _ in range(num_vertices)] # list of neighbor lists
        self.traversal_array = [] # DFS traversal array result

    def add_edge(self, v, u):
        # add neighbers to neighber list
        self.graph[v].append(u)
        self.graph[u].append(v)
        print(f"{v}: {self.graph[v]}")

    def dfs(self):
        # boolean list keep track of each v visited or not
        self.visited = [False] * self.num_vertices
        """
        Each v has 2 time marks:
        start_time = when v is visited
        end_time = when all v's neighbors and neighbors' neighbors
                    (basically all descendents) are visited
        """
        self.start_time = [0] * self.num_vertices
        self.end_time = [0] * self.num_vertices

        for node in range(self.num_vertices):
            # this node not visited
            if self.visited[node] == False: 
                self.visiting_vertex(node)
        # now visited all, exit loop
        print()
        print("DFS Traversal: ", self.traversal_array)
        print()
                
    def visiting_vertex(self, node):   
        # for each v ("node"):
        self.visited[node] = True # mark v visited!
        self.traversal_array.append(node) # add v to path result

        self.start_time[node] = self.time # add starting time for v
        self.time += 1 # increment time by 1
        
        neighbors = self.graph[node] # all neighbors of current vertex

        for neighbor in neighbors:
            # if neighbor never visited, neighbor is not ancestor
            if not self.visited[neighbor]:
                print('Tree Edge: ', str(node) + "-->" + str(neighbor))
                self.visiting_vertex(neighbor)

            # if neighbor visited...
            else:
                # neighbor is ancestor
                if self.start_time[node] > self.start_time[neighbor] \
                    and self.end_time[node] < self.end_time[neighbor]:
                    print('Back Edge: ', str(node) + "-->" + str(neighbor))
                # neighbor is descendant not part of the tree
                elif self.start_time[node] < self.start_time[neighbor] \
                    and self.end_time[node] > self.end_time[neighbor]:
                    print('Forward: ', str(node) + "-->" + str(neighbor))
                # neighbor is not descendant nor ancestor 
                elif self.start_time[node] > self.start_time[neighbor] \
                    and self.end_time[node] > self.end_time[neighbor]:
                    print('Cross Edge: ', str(node) + "-->" + str(neighbor))

            self.end_time[node] = self.time
            self.time += 1


G = Graph(5)
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)
G.add_edge(4, 1)
print(f"1: {G.graph[1]}")

G.dfs()


        