import string
from collections import Counter


def text_analyzer(
    text: str, case_sensitive: bool = True, remove_punctuation: bool = False
) -> tuple:
    """
    Функция принимает текст и два необязательных параметра.
    Возвращает кортеж из:
    - количества слов
    - количества символов (без пробелов)
    - самого частого слова
    - самого длинного слова
    :param text: str
    :param case_sensitive: bool
    :param remove_punctuation: bool
    :return: tuple(words_count, letters_count, most_used_word, most_length_word)
    """
    words_count: int
    letters_count: int
    most_used_word: str
    most_length_word: str

    signs = string.punctuation
    text_without_signs = "".join(letter for letter in text if letter not in signs).split()
    words_count: int = len(text_without_signs)
    letters_count: int = len(text) - words_count + 1

    word_counter = Counter(text_without_signs)
    most_used_word = word_counter.most_common(1)[0][0]

    most_length_word = ""
    for _ in text.split():
        if len(_) > len(most_length_word):
            most_length_word = _

    return words_count, letters_count, most_used_word, most_length_word


# Пример использования:
result = text_analyzer("Привет, мир мир! Это.", case_sensitive=False)
print(result)

# - количества слов
# - количества символов (без пробелов)
# - самого частого слова
# - самого длинного слова

# Требования:
# - Параметр case_sensitive определяет, учитывать ли регистр (по умолчанию True)
# - Параметр remove_punctuation определяет, удалять ли знаки препинания (по умолчанию False)
# - Используйте именованные аргументы для необязательных параметров
# - Функция должна возвращать ровно 4 значения
