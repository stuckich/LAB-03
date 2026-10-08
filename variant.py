def check_signal_level(value):
    """Определяет уровень сигнала по таблице или выводит ошибку диапазона."""
    # Все интервалы включают границы (доверительные концы)
    if not (0 <= value <= 100):
        return "Ошибка диапазона"
    elif 0 <= value <= 34:
        return "Слабый"
    elif 35 <= value <= 74:
        return "Средний"
    else:  # 75 <= value <= 100
        return "Сильный"


def find_minimum(a, b, c):
    """Возвращает минимальное из трех чисел."""
    return min(a, b, c)


def calculator(num1, op, num2):
    """Простой калькулятор для базовых операций."""
    if op == '+':
        return f"{num1 + num2:.2f}"
    elif op == '-':
        return f"{num1 - num2:.2f}"
    elif op == '*':
        return f"{num1 * num2:.2f}"
    elif op == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return f"{num1 / num2:.2f}"
    else:
        return "Ошибка: неизвестная операция"


def check_point_position(x, y):
    """
    Проверяет положение точки относительно прямоугольной области.
    Для примера взяты границы: X от 0 до 5, Y от 0 до 3.
    """
    # Границы подобраны под тестовые примеры: (5, 3) на границе, (5.1, 3) снаружи
    if (x == 5 and 0 <= y <= 3) or (y == 3 and 0 <= x <= 5) or (x == 0 and 0 <= y <= 3) or (y == 0 and 0 <= x <= 5):
        return "на границе"
    elif 0 < x < 5 and 0 < y < 3:
        return "внутри"
    else:
        return "снаружи"


# ==============================================================================
# БЛОК ПРОВЕРОК (ТЕСТИРОВАНИЕ)
# ==============================================================================
if __name__ == "__main__":
    print("--- 1. ПРОВЕРКА УРОВНЯ СИГНАЛА (Вариант с пороговыми значениями) ---")
    # Проверяем -1, 0, 100, 101 и значения вокруг порогов (34/35 и 74/75)
    test_points = [-2, -1, 0, 1, 33, 34, 35, 36, 73, 74, 75, 76, 99, 100, 101, 102]
    for val in test_points:
        print(f"Значение {val}: {check_signal_level(val)}")

    print("\n--- 2. ПРОВЕРКА МИНИМУМА ---")
    print(f"(2, 10, 3) → {find_minimum(2, 10, 3)}")
    print(f"(5, 5, 5) → {find_minimum(5, 5, 5)}")
    print(f"(-4, 0, -2) → {find_minimum(-4, 0, -2)}")
    print(f"(10, 5, 2) [минимум на последней позиции] → {find_minimum(10, 5, 2)}")

    print("\n--- 3. ПРОВЕРКА КАЛЬКУЛЯТОРА ---")
    print(f"7 / 2 → {calculator(7, '/', 2)}")
    print(f"5 / 0 → {calculator(5, '/', 0)}")
    print(f"5 ? 2 → {calculator(5, '?', 2)}")
    # Проверка остальных трех операций
    print(f"5 + 3 → {calculator(5, '+', 3)}")
    print(f"10 - 4.5 → {calculator(10, '-', 4.5)}")
    print(f"4 * 2.5 → {calculator(4, '*', 2.5)}")

    print("\n--- 4. ПРОВЕРКА ТОЧКИ ---")
    print(f"(2, 2) → {check_point_position(2, 2)}")
    print(f"(5, 3) → {check_point_position(5, 3)}")
    print(f"(5.1, 3) → {check_point_position(5.1, 3)}")
