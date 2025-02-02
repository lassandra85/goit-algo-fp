import heapq

def dijkstra(graph, start):
    """Знаходить найкоротші шляхи з вершини start до всіх інших вершин"""
    
    # Ініціалізація відстаней: ∞ для всіх вершин, крім стартової
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    # Мін-купа для зберігання (відстань, вершина)
    heap = [(0, start)]  # Починаємо з вершини start
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)  # Вибираємо найближчу вершину
        
        if current_distance > shortest_paths[current_node]:
            continue  # Якщо знайшли кращий шлях раніше, пропускаємо
        
        # Оновлення сусідніх вершин
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < shortest_paths[neighbor]:  # Якщо знайшли коротший шлях
                shortest_paths[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))  # Додаємо в купу

    return shortest_paths

# Приклад графа (словник суміжності)
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

# Виконання алгоритму Дейкстри
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Вивід результату
print(f"Найкоротші шляхи з вершини {start_node}:")
for node, distance in shortest_paths.items():
    print(f"{node}: {distance}")
