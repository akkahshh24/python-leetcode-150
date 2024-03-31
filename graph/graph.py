class Graph:
    # constructor
    def __init__(self):
        self.adj_list = {}

    # method to add vertex
    def add_vertex(self, vertex):
        # check if vertex exists in the map
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    # method to delete vertex
    
    # method to add edge
    def add_edge(self, vertex1, vertex2):
        # check if vertices exist in the map
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    # method delete edge 
    
    # method to print the adjacency list
    def print(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

# Create a graph
my_graph = Graph()

# Add vertices
my_graph.add_vertex("A")
my_graph.add_vertex("B")

# Add edges
my_graph.add_edge("A", "B")

# Print graph
my_graph.print()