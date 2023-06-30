# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Breadth-First Search (BFS)
def bfs(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Depth-First Search (DFS) - Preorder
def dfs_preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)

# Depth-First Search (DFS) - Inorder
def dfs_inorder(root):
    if root is None:
        return

    dfs_inorder(root.left)
    print(root.data, end=" ")
    dfs_inorder(root.right)

# Depth-First Search (DFS) - Postorder
def dfs_postorder(root):
    if root is None:
        return

    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data, end=" ")

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Perform BFS
print("BFS:")
bfs(root)
print()

# Perform DFS - Preorder
print("DFS - Preorder:")
dfs_preorder(root)
print()

# Perform DFS - Inorder
print("DFS - Inorder:")
dfs_inorder(root)
print()

# Perform DFS - Postorder
print("DFS - Postorder:")
dfs_postorder(root)
print()
