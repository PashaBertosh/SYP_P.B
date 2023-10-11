C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)

def calculate_sum(tuple):
    return sum(tuple)

def find_min_max_indices(tuple):
    min_index = tuple.index(min(tuple))
    max_index = tuple.index(max(tuple))
    return min_index, max_index

# Вычисляем суммы элементов кортежей
sum_C1 = calculate_sum(C_1)
sum_C2 = calculate_sum(C_2)

# Определяем, сумма какого кортежа больше, и выводим соответствующее сообщение
if sum_C1 > sum_C2:
    print(f"Сумма больше в кортеже C_1: {sum_C1}")
elif sum_C1 < sum_C2:
    print(f"Сумма больше в кортеже C_2: {sum_C2}")
else:
    print("Суммы в кортежах равны.")

# Находим порядковые номера минимальных и максимальных элементов кортежей
min_index_C1, max_index_C1 = find_min_max_indices(C_1)
min_index_C2, max_index_C2 = find_min_max_indices(C_2)

# Выводим порядковые номера минимальных и максимальных элементов для каждого кортежа
print("Порядковые номера минимальных и максимальных элементов кортежа C_1:")
print("Минимальный элемент: ", min_index_C1 + 1)  # Добавляем 1, так как индексы начинаются с 0
print("Максимальный элемент: ", max_index_C1 + 1)
print("Порядковые номера минимальных и максимальных элементов кортежа C_2:")
print("Минимальный элемент: ", min_index_C2 + 1)
print("Максимальный элемент: ", max_index_C2 + 1)
