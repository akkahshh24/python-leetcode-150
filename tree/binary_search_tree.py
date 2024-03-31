class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # initializing an empty tree
        self.root = None

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

# ------------- main logic ---------------
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)