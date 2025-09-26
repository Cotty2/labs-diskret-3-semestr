import heapq

def input_graph():
    graph = {}
    reverse_graph = {}
    n = int(input("Введите количество рёбер: "))
    print("Введите ребра в формате: начальная вершина, конечная вершина, вес")
    for _ in range(n):
        u, v, w = input().split()
        w = float(w)
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w
        if v not in graph:
            graph[v] = {}
        if v not in reverse_graph:
            reverse_graph[v] = {}
        reverse_graph[v][u] = w
        if u not in reverse_graph:
            reverse_graph[u] = {}
    return graph, reverse_graph

def dijkstra(graph, start, end):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        (cost, v, path) = heapq.heappop(queue)
        if v == end:
            return (path, cost)
        if v in visited:
            continue
        visited.add(v)
        for neighbor, weight in graph[v].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return ([], float('inf'))

def all_paths(graph, start, end, path=None, total_cost=0):
    if path is None:
        path = [start]
    if start == end:
        return [(path, total_cost)]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = all_paths(graph, node, end, path + [node], total_cost + graph[start][node])
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def main():
    graph, reverse_graph = input_graph()

    start = 'A'
    end = 'D'

    print("\nВсе маршруты от A до D:")
    paths = all_paths(graph, start, end)
    for path, cost in paths:
        print(f"Маршрут: {' -> '.join(path)}, значение: {cost} y.e.")

    min_path, min_cost = dijkstra(graph, start, end)
    print(f"\nМинимальный маршрут от A до D: {' -> '.join(min_path)}, значение: {min_cost} y.e.")

    rev_min_path, rev_min_cost = dijkstra(reverse_graph, end, start)
    print(f"Минимальный маршрут от D до A: {' -> '.join(rev_min_path)}, значение: {rev_min_cost} y.e.")

    print("\nВсе маршруты от D до A:")
    rev_paths = all_paths(reverse_graph, end, start)
    for path, cost in rev_paths:
        print(f"Маршрут: {' -> '.join(path)}, значение: {cost} y.e.")

if __name__ == "__main__":
    main()
