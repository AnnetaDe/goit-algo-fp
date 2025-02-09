import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


class BinaryHeapVisualizer:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def generate_gradient_color(self, step, max_step):
        r = 255
        g = int(0 + (255 - 0) * (1 - step / max_step))
        b = 255
        return f"#{r:02X}{g:02X}{b:02X}"

    def visualize(self):
        G = nx.DiGraph()
        for i, value in enumerate(self.heap):
            G.add_node(value, subset=i.bit_length())
            parent_index = (i - 1) // 2
            if parent_index >= 0:
                G.add_edge(self.heap[parent_index], value)

        pos = nx.multipartite_layout(G, subset_key="subset")
        plt.figure(figsize=(8, 6))
        plt.title("Binary Heap Visualization")
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="fuchsia",
            edge_color="gray",
            node_size=2000,
            font_size=10,
            edgecolors="black",
            linewidths=1.5,
        )
        plt.show()

    def bfs_visualize(self):
        if not self.heap:
            return
        queue = deque([0])
        visited = set()
        G = nx.DiGraph()
        max_step = len(self.heap)

        for i, value in enumerate(self.heap):
            G.add_node(value, subset=i.bit_length(), color="#000000")
            parent_index = (i - 1) // 2
            if parent_index >= 0:
                G.add_edge(self.heap[parent_index], value)

        step = 0
        while queue:
            node_index = queue.popleft()
            if node_index in visited:
                continue
            visited.add(node_index)
            color = self.generate_gradient_color(step, max_step)
            print(color)
            G.nodes[self.heap[node_index]]["color"] = color

            left_child = 2 * node_index + 1
            right_child = 2 * node_index + 2
            if left_child < len(self.heap):
                queue.append(left_child)
            if right_child < len(self.heap):
                queue.append(right_child)
            step += 1

        pos = nx.multipartite_layout(G, subset_key="subset")
        node_colors = [G.nodes[n]["color"] for n in G.nodes]
        plt.figure(figsize=(8, 6))
        plt.title("BFS Traversal of Binary Heap")
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color=node_colors,
            edge_color="gray",
            node_size=2000,
            font_size=10,
            edgecolors="fuchsia",
            linewidths=1.5,
        )
        plt.show()

    def dfs_visualize(self):
        if not self.heap:
            return
        stack = [0]
        visited = set()
        G = nx.DiGraph()
        max_step = len(self.heap)

        for i, value in enumerate(self.heap):
            G.add_node(value, subset=i.bit_length(), color="#000000")
            parent_index = (i - 1) // 2
            if parent_index >= 0:
                G.add_edge(self.heap[parent_index], value)

        step = 0
        while stack:
            node_index = stack.pop()
            if node_index in visited:
                continue
            visited.add(node_index)
            color = self.generate_gradient_color(step, max_step)
            print(color)
            G.nodes[self.heap[node_index]]["color"] = color

            right_child = 2 * node_index + 2
            left_child = 2 * node_index + 1
            if right_child < len(self.heap):
                stack.append(right_child)
            if left_child < len(self.heap):
                stack.append(left_child)
            step += 1

        pos = nx.multipartite_layout(G, subset_key="subset")
        node_colors = [G.nodes[n]["color"] for n in G.nodes]
        plt.figure(figsize=(8, 6))
        plt.title("DFS Traversal of Binary Heap")
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color=node_colors,
            edge_color="gray",
            node_size=2000,
            font_size=10,
            edgecolors="fuchsia",
            linewidths=1.5,
        )
        plt.show()


heap_visualizer = BinaryHeapVisualizer()
heap_visualizer.insert(10)
heap_visualizer.insert(20)
heap_visualizer.insert(5)
heap_visualizer.insert(30)
heap_visualizer.insert(15)
heap_visualizer.insert(25)
heap_visualizer.insert(8)

heap_visualizer.visualize()
heap_visualizer.bfs_visualize()
heap_visualizer.dfs_visualize()
