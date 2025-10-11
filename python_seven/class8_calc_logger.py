def log_operation(operation: str, a: int, b: int, result: int | str | float) -> None:
    """Функция логирует операции калькулятора в файл calc_logs.txt"""
    with open("calc_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{a} {operation} {b} = {result}\n")

def calculator(operation: str, a: int, b: int) -> int | str | float:
    """Функция принимает 1 строчную переменную и 2 числовые переменные, производит операцию и возвращает исход операции"""

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    elif operation == '**':
        result = a ** b
    else:
        return 'Аргументы введены не верно!'
    
    log_operation(operation, a, b, result)
    return result


import os

if not os.path.exists("data/calc_logs.txt"):
    # create file if not exists
    with open("calc_logs.txt", "w", encoding="utf-8") as f:
        f.write("История операций калькулятора:\n")


# example usage
if __name__ == "__main__":
    a = 8
    b = 7
    calculator('+', a, b)

