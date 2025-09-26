def factorial(x):
    """Вычисление факториала числа"""
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def main():
    # Ввод данных
    n = int(input("Введите число n: "))
    m = int(input("Введите число m: "))
    
    # Проверка корректности ввода
    if m > n:
        print("Ошибка: m не может быть больше n!")
        return
    
    if n < 0 or m < 0:
        print("Ошибка: числа должны быть неотрицательными!")
        return
    
    # Вычисления
    P = factorial(n)  # Перестановки
    A = factorial(n) // factorial(n - m)  # Размещения
    C = factorial(n) // (factorial(m) * factorial(n - m))  # Сочетания
    
    # Вывод результатов
    print(f"Перестановки P({n}) = {P}")
    print(f"Размещения A({n},{m}) = {A}")
    print(f"Сочетания C({n},{m}) = {C}")

# Запуск программы
if __name__ == "__main__":
    main()