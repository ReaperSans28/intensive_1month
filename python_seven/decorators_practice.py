def add(num_1: int, num_2: int)->int:
    """
    Плюсует из числа 1 число 2.
    :param num_1:
    :param num_2:
    :return:
    """
    return num_1 + num_2

def substract(num_1: int, num_2: int)->int:
    """
    Минусует из числа 1 число 2.
    :param num_1:
    :param num_2:
    :return:
    """
    return num_1 - num_2

def multiply(num_1: int, num_2: int)->int:
    """
    Умножает число 1 на число 2.
    :param num_1:
    :param num_2:
    :return:
    """
    return num_1 * num_2

def divide(num_1: int, num_2: int)->int:
    """
    Делит число 1 на число 2.
    :param num_1:
    :param num_2:
    :return:
    """
    return num_1 / num_2

def square(num_1: int, num_2: int)->int:
    """
    Возводит число 1 в степень числа 2.
    :param num_1:
    :param num_2:
    :return:
    """
    return num_1 ** num_2

def calculator(operation, num_1, num_2):
    """
    Калькулятор.
    Принимает оперцию и 2 числа.
    :param operation:
    :param num_1:
    :param num_2:
    :return:
    """
    result = 0
    if operation == '+':
        result = add(num_1,num_2)
        print(result)
    elif operation == '-':
        result = substract(num_1, num_2)
        print(result)
    elif operation == '*':
        result = multiply(num_1, num_2)
        print(result)
    elif operation == '/':
        result = divide(num_1, num_2)
        print(result)
    elif operation == '**':
        result = square(num_1, num_2)
        print(result)

# try:
#     with open("logs/logging_calc.txt", "a", encoding="utf-8") as file:
#         file.write(f"{num_1} {operation} {num_2} = {result}\n")
# except FileNotFoundError:
#     print("NO FILE")

operation = input()
num_1 = int(input())
num_2 = int(input())

calculator(operation, num_1, num_2)
