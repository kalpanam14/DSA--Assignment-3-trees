# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to find the maximum level sum in a binary tree
def max_level_sum(root):
    if root is None:
        return 0

    # Initialize variables for maximum level sum and current level sum
    max_sum = float('-inf')
    current_sum = 0

    # Create a queue for the BFS traversal
    queue = [root]

    # Perform BFS to calculate the sum at each level
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)

        # Calculate the sum of nodes at the current level
        for _ in range(level_size):
            node = queue.pop(0)
            current_sum += node.data

            # Enqueue the left and right child nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Update the maximum level sum if necessary
        max_sum = max(max_sum, current_sum)

        # Reset the current level sum
        current_sum = 0

    return max_sum

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)

# Find the maximum level sum in the binary tree
max_sum = max_level_sum(root)

print("Maximum level sum:", max_sum)