# Define a class for a tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

# Function to print the nodes at odd levels of a tree
def print_odd_level_nodes(root):
    if root is None:
        return

    # Create a queue for level-order traversal
    queue = [root]
    level = 1

    # Perform level-order traversal
    while queue:
        level_size = len(queue)

        # Traverse nodes at the current level
        for _ in range(level_size):
            node = queue.pop(0)

            # Print the node data if the level is odd
            if level % 2 != 0:
                print(node.data)

            # Enqueue children for the next level
            for child in node.children:
                queue.append(child)

        # Increment the level
        level += 1

# Create the tree
root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7), Node(8)]

# Print the nodes at odd levels of the tree
print("Nodes at odd levels:")
print_odd_level_nodes(root)