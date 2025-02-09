import heapq
from collections import deque
import uuid


class Node:
    def __init__(self, value, color="black"):
        self.value = value
        self.edges = []
        self.color = color
        self.id = str(uuid.uuid4())

    def add_edge(self, neighbor, directed_both=False):
        self.edges.append(neighbor)
        if directed_both:
            neighbor.edges.append(self)


class Graph:
    def __init__(self):
        self.graph = {}
        self.levels = {}

    def add_vertex(self, vertex, color="black"):
        if vertex not in self.graph:
            self.graph[vertex] = Node(vertex, color)
            self.levels[vertex] = None

    def add_edge(self, u, v, directed_both=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].add_edge(self.graph[v], directed_both)

    def add_level(self, level):
        if level not in self.levels:
            return "no level"
        queue = deque([level])
        self.levels[level] = 0
        while queue:
            current = queue.popleft()
            for vertex in self.graph[current].edges:
                if self.levels[vertex.value] is None:
                    self.levels[vertex.value] = self.levels[current] + 1
                    queue.append(vertex.value)

    def dfs(self, start, target, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()
        path.append(start)
        visited.add(start)

        if start == target:
            print(f"DFS-Path to {target}: {path}")
            print(f"Visited: {visited}")
            print("*" * 50)
            return path
        for vertex in self.graph[start].edges:
            if vertex.value not in visited:
                return self.dfs(vertex.value, target, path, visited)

        return None

    def bfs(self, start, target):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            if node == target:
                print(f"BFS-Path from {start} to {target}: {path}")
                print(f"Visited: {visited}")
                print(f"Queue: {queue}")
                print("*" * 50)
                return path

            visited.add(node)
            for neighbor in self.graph[node].edges:
                if neighbor.value not in visited:
                    queue.append((neighbor.value, path + [neighbor.value]))
                    visited.add(neighbor.value)

        return None

    def show(self):
        for vertex, node in self.graph.items():
            print(
                f"Vertex: {vertex}: Level:{self.levels[vertex]}---> {[n.value for n in node.edges]}"
            )

    def dijkstra(self, start):
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.graph[current_node].edges:
                weight = 1  # Якщо є ваги, змініть цю частину
                distance = current_distance + weight

                if distance < distances[neighbor.value]:
                    distances[neighbor.value] = distance
                    heapq.heappush(priority_queue, (distance, neighbor.value))

        return distances


hand_made_graph = Graph()
hand_made_graph.add_edge("A", "B", True)
hand_made_graph.add_edge("A", "C", True)
hand_made_graph.add_edge("B", "D", True)
hand_made_graph.add_edge("C", "D", True)
hand_made_graph.add_edge("D", "E", True)
hand_made_graph.add_edge("E", "F", True)
hand_made_graph.show()
print("Dijkstra shortest paths from A:")

print(hand_made_graph.dijkstra("A"))
