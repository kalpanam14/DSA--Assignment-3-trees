# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print the binary tree
def print_binary_tree(node, level=0):
    if node is not None:
        print("  " * level + str(node.data))
        print_binary_tree(node.left, level + 1)
        print_binary_tree(node.right, level + 1)

print("Binary Tree:")
print_binary_tree(root)