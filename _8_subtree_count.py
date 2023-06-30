# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count the number of subtrees that sum up to a given value
def count_subtrees_with_sum(root, target_sum):
    count = 0

    def helper(node):
        nonlocal count

        if node is None:
            return 0

        # Calculate the sum of the current subtree
        subtree_sum = node.data + helper(node.left) + helper(node.right)

        # If the sum equals the target sum, increment the count
        if subtree_sum == target_sum:
            count += 1

        # Return the sum of the current subtree
        return subtree_sum

    helper(root)
    return count

# Create the binary tree
root = Node(5)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(6)

# Define the target sum
target_sum = 6

# Count the number of subtrees that sum up to the target sum
subtree_count = count_subtrees_with_sum(root, target_sum)

print("Number of subtrees with sum", target_sum, ":", subtree_count)