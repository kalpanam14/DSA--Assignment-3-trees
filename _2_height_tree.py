# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to calculate the height of a binary tree
def calculate_height(node):
    if node is None:
        return 0

    # Recursively calculate the height of the left and right subtrees
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)

    # Return the maximum of the left and right subtree heights, plus 1 for the current node
    return max(left_height, right_height) + 1

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate the height of the binary tree
height = calculate_height(root)

print("Height of the binary tree:", height)