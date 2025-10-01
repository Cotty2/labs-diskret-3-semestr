import math
def count_distinct_cycles():
    n = int(input("количество вершин цикла "))

    if n < 0:
        print("Количество вершин не может быть отрицательным")
        return

    if n <= 1:
        num_distinct_graphs = 0
    elif n == 2:
        num_distinct_graphs = 1
    else:
        num_distinct_graphs = math.factorial(n - 1) // 2

    print("количество различных конечных графов, которые можно получить")
    print(f"перенумерацией вершин {num_distinct_graphs}")

count_distinct_cycles()