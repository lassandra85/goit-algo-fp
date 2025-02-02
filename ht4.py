import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Додає елемент у купу та підтримує властивість мін-купу"""
        heapq.heappush(self.heap, value)

    def build_heap(self, values):
        """Будує купу з масиву"""
        self.heap = values[:]
        heapq.heapify(self.heap)

    def get_heap(self):
        """Повертає список елементів купи"""
        return self.heap

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор

def build_tree_from_heap(heap):
    """Створює бінарне дерево з купи"""
    if not heap:
        return None

    nodes = [Node(value) for value in heap]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]  # Корінь дерева

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає ребра у граф та розташовує вузли"""
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

def draw_heap(heap):
    """Будує та візуалізує бінарну купу"""
    root = build_tree_from_heap(heap)

    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    graph = add_edges(graph, root, pos)

    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення купи та візуалізація
heap = BinaryHeap()
values = [10, 20, 15, 30, 40, 50, 25]
heap.build_heap(values)

draw_heap(heap.get_heap())
