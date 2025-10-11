def text_analyzer(text, case_sensitive=True, remove_punctuation=False):
    """
    Анализирует текст и возвращает статистику.

    Args:
        text (str): Текст для анализа
        case_sensitive (bool): Учитывать регистр (по умолчанию True)
        remove_punctuation (bool): Удалять знаки препинания (по умолчанию False)

    Returns:
        tuple: (количество_слов, количество_символов_без_пробелов,
                самое_частое_слово, самое_длинное_слово)
    """

    marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~«»—"
    for i in marks:
        text = text.replace(i, "")

    words = list(text.split())  # Создаем список и считаем количество слов
    count = 0
    for i in words:
        count += 1

    symbols = 0  # Считаем количество символов в строке (без пробелов)
    for i in text:
        if i == " ":
            continue
        symbols += 1

    word_count = {}  # Создаем словврь для подсчета слов

    # Считаем слова
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # # Находим самое частое
    max_count = 0
    most_common = None

    for k, v in word_count.items():
        if v > max_count:
            max_count = v
            most_common = k

    longest_word = max(words, key=len)  # Находим сомое длинное слово

    return count, symbols, longest_word, k


print(text_analyzer(text="Привет, мир! Это тестовый текст. Мир Мир Мир."))
