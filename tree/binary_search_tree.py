# A node has a value, a left property which is a Node object and similarly a right property
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ----------- binary search tree ------------

class BinarySearchTree:
    def __init__(self):
        # initializing an empty tree
        # root is an object of type Node
        self.root = None

# ------------ insert ------------

    # function to insert a node in the binary search tree
    def insert(self ,value):
        new_node = Node(value)

        # empty tree
        if self.root == None:
            self.root = new_node
            return True
        
        current_node = self.root

        while (True):
            # same node value already in the tree
            if new_node.value == current_node.value:
                return False
            
            # left
            if new_node.value < current_node.value:
                # check if left is empty
                if current_node.left == None:
                    current_node.left = new_node
                    return True
                
                # move current_node to the left_node for further investigation
                current_node = current_node.left

            # right
            else:
                # check if right is empty
                if current_node.right == None:
                    current_node.right = new_node
                    return True
                
                # move current_node to the right_node for further investigation
                current_node = current_node.right

# ----------- contains ---------------

    # function to check if the tree contains a value
    def contains(self, value):
        current_node = self.root

        # check till current_node is not None
        while current_node is not None:

            # left
            if value < current_node.value:
                # move node to left
                current_node = current_node.left

            # right
            elif value > current_node.value:
                # move node to right
                current_node = current_node.right

            else:
                # current node is the one we are looking for
                return True
            
        return False

# ------------- breadth first search --------------
    
    def bfs(self):
        current_node = self.root
        # a list to store all the elements
        visited_nodes = []

        queue = []
        queue.append(current_node)

        while queue:
            current_node = queue.pop(0)
            visited_nodes.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)
            
        return visited_nodes

# ------------- depth first search (pre-order) --------------
# In pre-order traversal, we store the nodes as we traverse along the tree
    
    # recursive approach
    def dfs_pre_order(self):
        # a list to store all the visited nodes
        visited_nodes = []

        def traverse(current_node):
            visited_nodes.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return visited_nodes
    
# ------------- depth first search (post-order) --------------
# In post-order traversal, we store the node only when we have visited it's left and right value
    
    # recursive approach
    def dfs_post_order(self):
        # a list to store all the visited_nodes
        visited_nodes = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)

            visited_nodes.append(current_node.value)

        traverse(self.root)
        return visited_nodes

# ------------- depth first search (in-order) --------------
# In in-order traversal, we store the node after we have visited the left value of that node
    
    # recursive approach
    def dfs_in_order(self):
        visited_nodes = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)

            visited_nodes.append(current_node.value)

            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return visited_nodes

# ------------- main logic ---------------
    
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(76)
my_tree.insert(52)
my_tree.insert(82)

#             47
#     21              76
# 18      27      52      82

print(my_tree.root.value)           # 47
print(my_tree.root.left.value)      # 21
print(my_tree.root.right.value)     # 76

print(my_tree.contains(52))         # True         
print(my_tree.contains(9))          # False

print(my_tree.bfs())                # [47, 21, 76, 18, 27, 52, 82]
print(my_tree.dfs_pre_order())      # [47, 21, 18, 27, 76, 52, 82]
print(my_tree.dfs_post_order())     # [18, 27, 21, 52, 82, 76, 47]
print(my_tree.dfs_in_order())       # [18, 21, 27, 47, 52, 76, 82]