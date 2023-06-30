# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to print all the leaves in a binary tree
def print_leaves(root):
    if root is None:
        return

    # Perform DFS
    def dfs(node):
        if node is None:
            return

        # If it's a leaf node, print its data
        if node.left is None and node.right is None:
            print(node.data)

        # Recursive calls for left and right subtrees
        dfs(node.left)
        dfs(node.right)

    # Start DFS from the root node
    dfs(root)

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Print all the leaves in the binary tree
print("Leaves in the binary tree:")
print_leaves(root)