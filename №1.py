def are_anagrams(word1, word2):
    # Удаляем пробелы и приводим все символы к нижнему регистру
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Проверка на равное количество символов
    if len(word1) != len(word2):
        return False

    # Проверка на наличие всех букв из первого слова во втором
    for char in word1:
        if char not in word2:
            return False

    return True


# Получаем два слова от пользователя
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

# Проверяем являются ли они анаграммами
if are_anagrams(word1, word2):
    print("Эти слова являются анаграммами.")
else:
    print("Эти слова не являются анаграммами.")
