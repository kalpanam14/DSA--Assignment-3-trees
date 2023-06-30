# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal: root -> left -> right
def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# In-order traversal: left -> root -> right
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

# Post-order traversal: left -> right -> root
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform pre-order traversal
print("Pre-order traversal:")
preorder_traversal(root)
print()

# Perform in-order traversal
print("In-order traversal:")
inorder_traversal(root)
print()

# Perform post-order traversal
print("Post-order traversal:")
postorder_traversal(root)
print()