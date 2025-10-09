import sys
import math

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        Этот метод обеспечивает симметричность графика. Другими словами, если существует путь от узла A к B со значением V, должен быть путь от узла B к узлу A со значением V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    """
    Реализация алгоритма Дейкстры
    Возвращает:
    - shortest_path: словарь {узел: минимальное расстояние}
    - previous_nodes: словарь для восстановления пути
    """
    unvisited_nodes = list(graph.get_nodes())
    
    # Инициализация всех расстояний как бесконечность
    shortest_path = {node: float('inf') for node in unvisited_nodes}
    shortest_path[start_node] = 0
    
    # Для восстановления пути
    previous_nodes = {node: None for node in unvisited_nodes}
    
    while unvisited_nodes:
        # Находим узел с минимальным расстоянием
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # Получаем соседей текущего узла
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        
        # Удаляем текущий узел из непосещённых
        unvisited_nodes.remove(current_min_node)
    
    return shortest_path, previous_nodes


def get_shortest_path(previous_nodes, start_node, target_node):
    """Восстанавливает путь от start до target"""
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    
    path.append(start_node)
    path.reverse()
    return path


# === ЗАДАНИЕ: ПУТЬ ИЗ РЕЙКЬЯВИКА В БЕЛГРАД ===

# Определяем города (узлы)
nodes = [
    "Рейкьявик", "Копенгаген", "Берлин", "Вена", "Белград",
    "Осло", "Стокгольм", "Прага", "Мюнхен", "Загреб"
]

# Определяем начальный граф (условные расстояния в "условных единицах" — например, сотни км)
init_graph = {
    "Рейкьявик": {"Копенгаген": 15, "Осло": 12},
    "Копенгаген": {"Берлин": 8, "Стокгольм": 6},
    "Осло": {"Стокгольм": 4},
    "Стокгольм": {"Берлин": 10},
    "Берлин": {"Прага": 5, "Мюнхен": 7},
    "Прага": {"Вена": 6},
    "Мюнхен": {"Вена": 4},
    "Вена": {"Загреб": 3, "Белград": 9},
    "Загреб": {"Белград": 5}
}

# Создаём экземпляр графа
graph = Graph(nodes, init_graph)

# Запускаем алгоритм Дейкстры от Рейкьявика
shortest_path, previous_nodes = dijkstra_algorithm(graph, "Рейкьявик")

# Находим путь до Белграда
target = "Белград"
path = get_shortest_path(previous_nodes, "Рейкьявик", target)
distance = shortest_path[target]

print("=== РЕЗУЛЬТАТЫ ===")
print(f"2.1 Путь (ценность) маршрута из Рейкьявика в Белград:")
print(" → ".join(path))
print(f"Общая стоимость (условная длина): {distance}")

print(f"\n2.2 Наиболее короткий маршрут из Рейкьявика в Белград:")
print(" → ".join(path))

# === 2.3 Пересчёт в км по координатам ===

# Координаты городов (широта, долгота)
city_coords = {
    "Рейкьявик": (64.1265, -21.8174),
    "Копенгаген": (55.6761, 12.5683),
    "Берлин": (52.5200, 13.4050),
    "Вена": (48.2082, 16.3738),
    "Белград": (44.8040, 20.4651),
    "Осло": (59.9139, 10.7522),
    "Стокгольм": (59.3293, 18.0686),
    "Прага": (50.0755, 14.4378),
    "Мюнхен": (48.1351, 11.5820),
    "Загреб": (45.8150, 15.9667)
}

def haversine(lat1, lon1, lat2, lon2):
    """Вычисляет расстояние в километрах между двумя точками по широте и долготе"""
    R = 6371  # радиус Земли в км
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

# Вычисляем реальное расстояние по координатам для найденного пути
total_km = 0
print(f"\n2.3 Пересчёт маршрута в км (по координатам):")
for i in range(len(path) - 1):
    city1 = path[i]
    city2 = path[i + 1]
    lat1, lon1 = city_coords[city1]
    lat2, lon2 = city_coords[city2]
    dist_km = haversine(lat1, lon1, lat2, lon2)
    total_km += dist_km
    print(f"  {city1} → {city2}: {dist_km:.2f} км")

print(f"\nОбщая длина маршрута (по координатам): {total_km:.2f} км")