from datetime import datetime

from python_seven.decorators import logger

@logger
def calculate_avg(numbers: list[int]) -> float:
    """
    Функция для вычислеия среднего значения.
    :param numbers:
    :return:
    """

    # Валидируем данные
    if not numbers:
        return 0

    # Создаем промежуточные переменные
    sum_of_numbers: int = 0

    # Основная логика функции
    for number in numbers:
        sum_of_numbers += number

    return sum_of_numbers / len(numbers)


squares: list[int] = [x**2 for x in range(10)]

print(calculate_avg(squares))