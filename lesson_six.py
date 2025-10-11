def add(a: int, b: int) -> int:
    """Функция принимает 2 числовые переменные и возваращает их сумму"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Функция принимает 2 числовые переменные и возваращает их разность"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Функция принимает 2 числовые переменные и возваращает их произведение"""
    return a * b


def divide(a: int, b: int) -> float:
    """Функция принимает 2 числовые переменные и возваращает их частное"""
    return a / b


def square(a: int, b: int) -> int:
    """Функция принимает 2 числовые переменные и возваращает возведенное в степень число"""
    return a**b


def calculator(operation: str, a: int, b: int) -> int | str | float:
    """Функция принимает 1 строчную переменную и 2 числовые переменные, производит операцию и возвращает исход операции"""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "**":
        return a**b
    else:
        return "Аргументы введены не верно!"
