class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]  

    #Find the root of a node
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    # Union two sets
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x  # Attach one root to another

    # Check if two elements are connected
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # Show the parent list
    def display(self):
        print("Parent array:", self.parent)
