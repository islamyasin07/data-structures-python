class Graph:
    def __init__(self):
        self.adj_list = {}  #dictionary to hold neighbors

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    #Add an edge from one node to another
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        self.adj_list[u].append(v)  

    #Show the graph
    def display(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
