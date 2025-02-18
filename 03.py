import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Додає ребро у граф"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Для неорієнтованого графа

    def dijkstra(self, start):
        """Алгоритм Дейкстри для знаходження найкоротших шляхів"""
        # 1. Ініціалізуємо відстані як нескінченність
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0

        # 2. Використовуємо мін-купу для вибору найкоротшої відстані
        min_heap = [(0, start)]  # (відстань, вершина)

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            # Пропускаємо обробку, якщо знайшли кращий шлях раніше
            if current_distance > dist[current_node]:
                continue

            # 3. Оновлюємо сусідів
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # Якщо знайшли коротший шлях, оновлюємо
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return dist

# Тестування
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('D', 'E', 8)
graph.add_edge('E', 'A', 7)

start_node = 'A'
shortest_paths = graph.dijkstra(start_node)

print(f"Найкоротші шляхи від {start_node}:")
for node, distance in shortest_paths.items():
    print(f"До {node}: {distance}")
