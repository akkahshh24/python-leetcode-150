# a list to store all the nodes/vertices
nodes = []
node_count = 0

# a list to store the adjacency matrix
adj_matrix = []

# function to add a node to the graph
def add_node(n):
    if n in nodes:
        return False
    
    # add to nodes list
    nodes.append(n)
    node_count = len(nodes)

    # add a column in adj_matrix
    # n is a row, every element of n is a column
    for n in adj_matrix:
        n.append(0)

    # add a row in adj_matrix
    new_row = [0 for i in range(node_count)]
    adj_matrix.append(new_row)
    return True

# function to add an edge to the graph
# for weighted graph, just store cost instead of 1
def add_edge(n1, n2):
    if n1 not in nodes and n2 not in nodes:
        return False
    
    # get the indices of n1 and n2
    index_n1 = nodes.index(n1)
    index_n2 = nodes.index(n2)

    adj_matrix[index_n1][index_n2] = 1
    adj_matrix[index_n2][index_n1] = 1
    return True

# function to print the adjacency matrix
def print_matrix():
    print(nodes)
    for row in adj_matrix:
        print(row)

# main code
print_matrix()

add_node('x')
add_node('y')
print_matrix()

add_edge('x', 'y')
print_matrix()
