import networkx as nx

import matplotlib.pyplot as plt
import heapq


class BinaryHeapVisualizer:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def visualize(self):
        G = nx.DiGraph()
        for i, value in enumerate(self.heap):
            G.add_node(value, layer=(i.bit_length()))
            parent_index = (i - 1) // 2
            if parent_index >= 0:
                G.add_edge(self.heap[parent_index], value)

        pos = nx.multipartite_layout(G, subset_key="layer")
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="gray",
            node_size=2000,
            font_size=10,
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
