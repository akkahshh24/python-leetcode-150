class Graph:
    # constructor
    def __init__(self):
        self.adj_list = {}

    # method to add vertex
    def add_vertex(self, vertex):
        # check if vertex exists in the map
        if vertex in self.adj_list.keys():
            return False
        
        self.adj_list[vertex] = []
        return True
    
    # method to remove vertex
    def remove_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            return False
        
        # first remove the edges of that vertex, and then we can remove that vertex
        for other_vertex in self.adj_list[vertex]:
            self.adj_list[other_vertex].remove(vertex)
        del self.adj_list[vertex]
        return True

    # method to add edge
    def add_edge(self, vertex1, vertex2):
        # check if vertices exist in the map
        if vertex1 not in self.adj_list.keys() and vertex2 not in self.adj_list.keys():
            return False
        
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        return True

    # method remove edge 
    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list.keys() and vertex2 not in self.adj_list.keys():
            return False
        
        try:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
        # this is required as we might get list.remove(x) x not in list error when edge is absent
        except ValueError:
            pass

        return True

    # method to print the adjacency list
    def print(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

# -------------- main logic -----------------

# Create a graph
my_graph = Graph()

# Add vertices
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.print()

# Add edges
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')
my_graph.print()

# Remove edge
my_graph.remove_edge('B', 'C')
my_graph.print()

# Remove vertices
my_graph.remove_vertex('D')
my_graph.print()