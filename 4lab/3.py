import heapq

def dijkstra_with_path(graph, start):
    # Инициализация
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    
    # Очередь с приоритетом
    heap = [(0, start)]
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        
        if current_dist > distances[current]:
            continue
            
        for neighbor, weight in graph[current].items():
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distances, previous

def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(str(current))
        current = previous[current]
    path.reverse()
    return " -> ".join(path)

# Граф из вашего изображения (неориентированный)
graph = {
    1: {2: 7, 3: 9, 6: 14},
    2: {1: 7, 3: 10, 4: 15},
    3: {1: 9, 2: 10, 4: 11, 6: 2},
    4: {2: 15, 3: 11, 5: 6},
    5: {4: 6, 6: 9},
    6: {1: 14, 3: 2, 5: 9}
}

start_node = 1

# Запускаем алгоритм
distances, previous = dijkstra_with_path(graph, start_node)

# Вывод для всех вершин
print(f"Вершина {start_node}: расстояние = 0, путь = {start_node}")
for node in sorted(graph.keys()):
    if node != start_node:
        dist = distances[node]
        path = reconstruct_path(previous, start_node, node)
        print(f"Вершина {node}: расстояние = {dist}, путь = {path}")

print()

# Вывод для указанных пар (1->6, 1->5, 1->4)
pairs = [(1, 6), (1, 5), (1, 4)]
print("Кратчайшие пути для указанных пар вершин:")
for src, dst in pairs:
    dist = distances[dst]
    path = reconstruct_path(previous, src, dst)
    print(f"{src} -> {dst}: расстояние = {dist}, путь = {path}")