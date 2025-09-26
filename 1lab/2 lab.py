def convert_element(element):
    try:
        return int(element)
    except ValueError:
        try:
            return float(element)
        except ValueError:
            return element

def input_set(name):
    print(f"\nВведите элементы множества {name} (через пробел):")
    elements = input().split()
    return {convert_element(elem) for elem in elements}

def custom_sorted(s):

    numbers = [x for x in s if isinstance(x, (int, float))]
    strings = [x for x in s if isinstance(x, str)]
    return sorted(numbers) + sorted(strings)


print("Можно вводить числа и буквы:")
A = input_set("A")
B = input_set("B")

# Вывод результатов
print(f"\nМножество A: {custom_sorted(A)}")
print(f"Множество B: {custom_sorted(B)}")
print(f"A ∪ B: {custom_sorted(A | B)}")
print(f"A ∩ B: {custom_sorted(A & B)}")