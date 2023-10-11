def process_argument(input_arg):
    if isinstance(input_arg, tuple):
        return len(input_arg)
    elif isinstance(input_arg, list):
        sum_until_zero = 0
        for item in input_arg:
            if item == 0:
                break
            sum_until_zero += item
        return sum_until_zero
    elif isinstance(input_arg, int):
        return int(str(input_arg)[::-1])
    elif isinstance(input_arg, str):
        words_count = len(input_arg.split())
        char_frequencies = {}
        for char in input_arg:
            if char != ' ':
                char_frequencies[char] = char_frequencies.get(char, 0) + 1
        most_common_char = max(char_frequencies, key=char_frequencies.get)
        return words_count, most_common_char

# Запрос ввода данных с клавиатуры
user_input = input("Введите данные (кортеж, список, число или строку): ")

# Обработка введенных данных
try:
    # Пытаемся преобразовать в кортеж
    processed_result = process_argument(eval(user_input))
    print("Результат обработки:", processed_result)
except (NameError, SyntaxError):
    print("Ошибка: Некорректный формат данных. Пожалуйста, введите кортеж, список, число или строку.")
