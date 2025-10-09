import heapq


def dijkstra_with_path(graph, start, end):
    # Инициализация
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    # Очередь с приоритетом
    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        # Если дошли до конечной вершины, можно остановиться
        if current == end:
            break

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
    if previous[end] is None and end != start:
        return None  # Путь не существует

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path


# Граф (неориентированный)
graph = {
    1: {2: 7, 3: 9, 6: 14},
    2: {1: 7, 3: 10, 4: 15},
    3: {1: 9, 2: 10, 4: 11, 6: 2},
    4: {2: 15, 3: 11, 5: 6},
    5: {4: 6, 6: 9},
    6: {1: 14, 3: 2, 5: 9}
}


def main():
    print("=" * 50)
    print("ПОИСК КРАТЧАЙШЕГО ПУТИ В ГРАФЕ")
    print("=" * 50)

    # Показываем доступные вершины
    available_nodes = sorted(graph.keys())
    print(f"Доступные вершины: {available_nodes}")
    print("-" * 50)

    # Ввод начальной вершины
    while True:
        try:
            start_node = int(input("Введите начальную вершину: ").strip())
            if start_node in available_nodes:
                break
            else:
                print(f"Ошибка: вершина {start_node} не существует. Доступные вершины: {available_nodes}")
        except ValueError:
            print("Ошибка: введите число")

    # Ввод конечной вершины
    while True:
        try:
            end_node = int(input("Введите конечную вершину: ").strip())
            if end_node in available_nodes:
                break
            else:
                print(f"Ошибка: вершина {end_node} не существует. Доступные вершины: {available_nodes}")
        except ValueError:
            print("Ошибка: введите число")

    print("-" * 50)

    # Запускаем алгоритм Дейкстры
    distances, previous = dijkstra_with_path(graph, start_node, end_node)

    # Восстанавливаем путь
    path = reconstruct_path(previous, start_node, end_node)

    # Выводим результат
    if path:
        distance = distances[end_node]
        print(f"Маршрут: {' → '.join(map(str, path))}")
        print(f"Расстояние: {distance}")

        # Детализация пути по сегментам
        print("\nДетализация пути:")
        total_distance = 0
        for i in range(len(path) - 1):
            segment_distance = graph[path[i]][path[i + 1]]
            total_distance += segment_distance
            print(f"  {path[i]} → {path[i + 1]}: {segment_distance} (всего: {total_distance})")
    else:
        print(f"✗ Путь из вершины {start_node} в вершину {end_node} не существует")


# Запуск программы
if __name__ == "__main__":
    main()