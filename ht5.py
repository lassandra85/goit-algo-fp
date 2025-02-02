import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#00008B"):  # Початковий колір - темно-синій
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає вузли та зв’язки у граф"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes=[]):
    """Візуалізує дерево з підсвіченими відвіданими вузлами"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = []
    labels = {}
    
    for node in tree.nodes(data=True):
        node_id = node[0]
        if node_id in visited_nodes:
            step = visited_nodes.index(node_id) / max(len(visited_nodes), 1)
            color = (0.1 + 0.8 * step, 0.3 + 0.6 * step, 1.0)  # Градієнт від темного до світлого
            colors.append(color)
        else:
            colors.append("#00008B")  # Початковий колір вузлів

        labels[node_id] = node[1]['label']

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs(root):
    """Обхід у ширину (BFS) з візуалізацією"""
    queue = deque([root])
    visited_nodes = []
    
    while queue:
        node = queue.popleft()
        if node:
            visited_nodes.append(node.id)
            draw_tree(root, visited_nodes)
            queue.append(node.left)
            queue.append(node.right)

def dfs(root):
    """Обхід у глибину (DFS) з візуалізацією"""
    stack = [root]
    visited_nodes = []
    
    while stack:
        node = stack.pop()
        if node:
            visited_nodes.append(node.id)
            draw_tree(root, visited_nodes)
            stack.append(node.right)  # Спочатку правий вузол
            stack.append(node.left)   # Потім лівий вузол

# Створення дерева
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

# Виконання обходу
print("Обхід у ширину (BFS):")
bfs(root)

print("Обхід у глибину (DFS):")
dfs(root)
