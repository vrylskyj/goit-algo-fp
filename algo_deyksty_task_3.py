import heapq

def dijkstra(graph, start):
    # Ініціалізуємо словники для відстаней та попередників
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph}
    
    # Ініціалізуємо чергу пріоритетів з кортежами (відстань, вершина)
    queue = [(0, start)]
    
    while queue:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(queue)
        
        # Якщо поточна відстань більша, ніж збережена відстань, пропускаємо
        if current_distance > distances[current_vertex]:
            continue
        
        # Переглядаємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Оновлюємо відстань, якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                # Додаємо вершину у чергу пріоритетів
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, predecessors

# Приклад графу
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances, predecessors = dijkstra(graph, start_vertex)

print("Shortest distances from vertex", start_vertex)
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")

print("\nPredecessors:", predecessors)
