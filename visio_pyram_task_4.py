import networkx as nx
import matplotlib.pyplot as plt
import math
import uuid  

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap_array):
    # Створюємо порожнє бінарне дерево
    root = None

    # Додаємо кожен елемент масиву в бінарне дерево
    for key in heap_array:
        if root is None:
            root = HeapNode(key)
        else:
            add_to_heap(root, key)
    
    return root

def add_to_heap(node, key):
    if key < node.val:
        if node.left is None:
            node.left = HeapNode(key)
        else:
            add_to_heap(node.left, key)
    else:
        if node.right is None:
            node.right = HeapNode(key)
        else:
            add_to_heap(node.right, key)

# Припустимо, що у нас є бінарна купа у вигляді масиву
heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
# Побудова дерева з купи
heap_tree_root = build_heap_tree(heap_array)
# Відображення бінарної купи у вигляді дерева
draw_heap(heap_tree_root)
