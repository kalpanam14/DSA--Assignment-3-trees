# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to calculate the sum of all nodes in a perfect binary tree
def sum_of_nodes(root):
    if root is None:
        return 0

    # Calculate the sum of nodes in the left and right subtrees
    left_sum = sum_of_nodes(root.left)
    right_sum = sum_of_nodes(root.right)

    # Return the sum of nodes in the current tree rooted at 'root'
    return root.data + left_sum + right_sum

# Create the perfect binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Calculate the sum of all nodes in the perfect binary tree
sum_of_all_nodes = sum_of_nodes(root)

print("Sum of all nodes:", sum_of_all_nodes)