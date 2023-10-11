def find_max_index(matrix):
    max_value = float('-inf')
    max_row, max_col = -1, -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row, max_col = i, j

    return max_row, max_col

# Запрос у пользователя для ввода матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

print("Введите элементы матрицы:")

# Инициализация матрицы с введенными значениями
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Введите элемент [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

# Вывод матрицы
print("Матрица:")
for row in matrix:
    print(row)

# Находим индексы первого вхождения максимального элемента
max_row, max_col = find_max_index(matrix)

# Выводим результат
print("Индексы первого вхождения максимального элемента:")
print("Номер строки:", max_row)
print("Номер столбца:", max_col)
