import uuid
import networkx as nx
import matplotlib.pyplot as plt
import time
from collections import deque


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_tree(arr):
    """Будує бінарне дерево з масиву"""
    if not arr:
        return None

    nodes = [Node(val) for val in arr]
    for i in range(len(arr)):
        left_index, right_index = 2 * i + 1, 2 * i + 2
        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]
    return nodes[0]  # Корінь дерева


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає вузли та ребра у граф"""
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)
    return graph


def draw_tree(tree_root):
    """Візуалізує бінарне дерево"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def hex_color_gradient(start_color, end_color, steps):
    """Генерує градієнт кольорів між двома HEX"""
    def hex_to_rgb(hex_color):
        return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

    def rgb_to_hex(rgb):
        return f'#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}'

    start_rgb, end_rgb = hex_to_rgb(start_color), hex_to_rgb(end_color)

    return [
        rgb_to_hex((
            int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (steps - 1)),
            int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (steps - 1)),
            int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (steps - 1))
        )) for i in range(steps)
    ]


def dfs_preorder_stack(root):
    """Обхід у глибину (DFS) з використанням стека"""
    if not root:
        return []

    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node)
        if node.right:
            stack.append(node.right)  # Додаємо правий, щоб лівий вийшов першим
        if node.left:
            stack.append(node.left)
    return result


def bfs_queue(root):
    """Обхід у ширину (BFS) з використанням черги"""
    if not root:
        return []

    queue, result = deque([root]), []
    while queue:
        node = queue.popleft()
        result.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def visualize_traversal(root, traversal_func, start_color="#0000FF", end_color="#ADD8E6"):
    """Анімована візуалізація обходу дерева"""
    nodes = traversal_func(root)
    colors = hex_color_gradient(start_color, end_color, len(nodes))

    for i, node in enumerate(nodes):
        node.color = colors[i]
        draw_tree(root)
        time.sleep(1)  # Затримка для анімації


# 🔹 Створення дерева та запуск візуалізації
values = [10, 5, 15, 3, 7, 12, 18]
tree_root = build_tree(values)

print("🔹 Візуалізація DFS (обхід у глибину)")
visualize_traversal(tree_root, dfs_preorder_stack, "#FF0000", "#FFA07A")

print("🔹 Візуалізація BFS (обхід у ширину)")
visualize_traversal(tree_root, bfs_queue, "#0000FF", "#87CEFA")
