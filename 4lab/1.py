import heapq

def dijkstra(graph, start, end):
    if start not in graph or end not in graph:
        return float('inf')
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_node in visited:
            continue
        visited.add(curr_node)

        if curr_node == end:
            break

        for neighbor, weight in graph.get(curr_node, []):
            if neighbor not in visited:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

    return distances[end]

def build_graph_from_edges(edge_list):
    graph = {}
    for u, v, w in edge_list:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))
        if v not in graph:
            graph[v] = []
    return graph

def find_shortest_paths_for_pairs(graph, pairs):
    results = {}
    for pair in pairs:
        if len(pair) != 2:
            results[pair] = float('inf')
            continue
        start, end = pair[0], pair[1]
        dist = dijkstra(graph, start, end)
        results[pair] = dist
    return results

print("Введите количество рёбер:")
n_edges = int(input().strip())

edges = []
print("Введите рёбра в формате: <откуда> <куда> <вес> (например: a b 3)")
for _ in range(n_edges):
    parts = input().split()
    u = parts[0]
    v = parts[1]
    w = int(parts[2])
    edges.append((u, v, w))

print("Введите пары вершин для поиска кратчайших путей (через пробел, например: ac ad bc):")
pairs_input = input().split()
pairs = pairs_input
graph = build_graph_from_edges(edges)
results = find_shortest_paths_for_pairs(graph, pairs)

print("\nРезультаты:")
for pair, dist in results.items():
    if dist == float('inf'):
        print(f"{pair}: недостижимо")
    else:
        print(f"{pair}: {dist}")