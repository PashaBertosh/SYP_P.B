def divide_numbers(a, b):
    try:
        result = a / b
        print("Результат деления:", result)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    finally:
        print("Блок finally: выполнение завершено.")

# Пример вызова функции
try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    divide_numbers(a, b)
except ValueError:
    print("Ошибка: некорректный ввод числа.")
