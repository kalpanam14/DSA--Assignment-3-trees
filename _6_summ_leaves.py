# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to calculate the sum of all left leaves in a binary tree
def sum_left_leaves(root, is_left=False):
    if root is None:
        return 0

    # Check if the current node is a left leaf
    if root.left is None and root.right is None and is_left:
        return root.data

    # Recursively calculate the sum of left leaves in the left and right subtrees
    left_sum = sum_left_leaves(root.left, True)
    right_sum = sum_left_leaves(root.right, False)

    # Return the sum of left leaves in the current node's subtrees
    return left_sum + right_sum

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.right.left = Node(9)
root.left.right.right = Node(10)

# Calculate the sum of all left leaves in the binary tree
sum_of_left_leaves = sum_left_leaves(root)

print("Sum of left leaves:", sum_of_left_leaves)