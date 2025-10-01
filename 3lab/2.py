def get_graph_type():
    n = int(input("количество вершин графа "))
    edges_input = input("перечислить ребра ")
    edges = edges_input.split(', ')

    violated_conditions = set()

    for edge_str in edges:
        if len(edge_str) != 2:
            violated_conditions.add(3)
            continue

        try:
            v1 = int(edge_str[0])
            v2 = int(edge_str[1])
        except ValueError:
            violated_conditions.add(3)
            continue

        if not (1 <= v1 <= n) or not (1 <= v2 <= n):
            violated_conditions.add(3)
            continue

        if v1 == v2:
            violated_conditions.add(3)
            continue

    unique_edges = set()
    for edge_str in edges:
        if len(edge_str) != 2:
            continue

        try:
            v1 = int(edge_str[0])
            v2 = int(edge_str[1])
            if not (1 <= v1 <= n) or not (1 <= v2 <= n):
                continue
            if v1 == v2:
                continue
        except ValueError:
            continue

        normalized_edge = tuple(sorted((v1, v2)))

        if normalized_edge in unique_edges:
            violated_conditions.add(2)
        else:
            unique_edges.add(normalized_edge)

    if violated_conditions:
        for num in sorted(violated_conditions):
            print(f"Нарушено условие №{num}")

    if 2 in violated_conditions or 3 in violated_conditions:
        graph_type = "Псевдограф"
    else:
        graph_type = "Простой граф"

    print(graph_type)

get_graph_type()