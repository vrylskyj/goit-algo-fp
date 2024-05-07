import networkx as nx
import matplotlib.pyplot as plt
import uuid
import math

class TreeNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_traversal(root, level=0):
    if root:
        color = "#{:02x}{:02x}{:02x}".format(0, 100 + level * 10, 240 - level * 10)
        root.color = color
        print(root.val, end=" -> ")
        dfs_traversal(root.left, level + 1)
        dfs_traversal(root.right, level + 1)

def bfs_traversal(root):
    if not root:
        return

    queue = [root]
    level = 0

    while queue:
        next_level = []
        for node in queue:
            color = "#{:02x}{:02x}{:02x}".format(0, 100 + level * 10, 240 - level * 10)
            node.color = color
            print(node.val, end=" -> ")
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level += 1
        queue = next_level

# Створення дерева
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Обхід дерева у глибину
print("DFS Traversal:")
dfs_traversal(root)
print()

# Обхід дерева у ширину
print("BFS Traversal:")
bfs_traversal(root)

# Відображення дерева
draw_tree(root)
