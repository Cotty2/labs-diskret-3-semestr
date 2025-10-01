def is_graphic_sequence():
    seq_str = input("Последовательность ")
    degree_sequence = [int(x.strip()) for x in seq_str.split(',')]

    n = len(degree_sequence)
    print(f"1)количество вершин {n}")

    if n == 0:
        print("2)сумма степеней 0")
        print("3) степенная/нестепенная последовательность-  степенная последовательность")
        return

    degree_sequence.sort(reverse=True)

    sum_degrees = sum(degree_sequence)
    print(f"2)сумма степеней {sum_degrees}")

    if sum_degrees % 2 != 0:
        print("3) степенная/нестепенная последовательность-  нестепенная последовательность")
        return

    is_graphic = True
    for k in range(1, n + 1):
        left_sum = sum(degree_sequence[:k])
        right_sum_inner = []
        for i in range(k + 1, n + 1):
            right_sum_inner.append(min(degree_sequence[i - 1], k))
        right_sum = k * (k - 1) + sum(right_sum_inner)

        if left_sum > right_sum:
            is_graphic = False
            break

    if is_graphic:
        print("3) степенная/нестепенная последовательность-  степенная последовательность")
    else:
        print("3) степенная/нестепенная последовательность-  нестепенная последовательность")

is_graphic_sequence()