from collections import deque

# Graph class with BFS and DFS
class Graph:
    def __init__(self):
        self.adj_list = {}  # Dictionary for neighbors

    # Add a node
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    # Add a directed edge
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)

    # BFS traversal from a start node
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue.extend(self.adj_list[node])
        return result

    # DFS traversal from a start node
    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(node):
            if node not in visited:
                result.append(node)
                visited.add(node)
                for neighbor in self.adj_list[node]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    # Show graph
    def display(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
