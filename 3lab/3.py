import math


def combinations(n, k):
    """Вычисление числа сочетаний C(n, k)"""
    if k < 0 or k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def main():
    print("=== Число мультиграфов полного графа ===")

    # Ввод данных
    n = int(input("количество вершин графа "))
    m = int(input("количество ребер "))

    # Общее количество ребер в полном графе
    total_edges = n * (n - 1) // 2

    # Количество мультиграфов с m ребрами
    # Это число сочетаний с повторениями: C(total_edges + m - 1, m)
    num_multigraphs = combinations(total_edges + m - 1, m)

    # Вывод результатов
    print(f"\nОбщее количество ребер {total_edges}")
    print(f"Количество мультиграфов C({total_edges + m - 1},{m}) = {num_multigraphs}")

    # Дополнительный вывод в формате как в тесте
    print(f"\nФормула: C_{{{total_edges + m - 1}}}^{{{m}}} = {total_edges + m - 1}!/({m}!×{total_edges - 1}!)")


if __name__ == "__main__":
    main()