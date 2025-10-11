# dev = "1"


# def examplee(number: int, string="Один", list_of_bl=None):
#     """
#     Эта функция принимает число и строку
#     Возвращает строку с полученой строкой и числом.
#     :param list_of_bl:
#     :param number:
#     :param string:
#     :return:
#     """
#     global dev
#     if list_of_bl is None:
#         list_of_bl = ["1"]

#     dev = f"{string}: {number}"

#     dev += "1"
#     return dev, list_of_bl

# examplee(1)
# print(dev)


# def modify_list(lst):
#     lst.append(4)  # изменит оригинальный список


# def modify_number(x):
#     x += 10  # не изменит оригинальную переменную


# my_list = [1, 2, 3]
# modify_list(my_list)  # my_list станет [1, 2, 3, 4]

# num = 5
# modify_number(num)  # num останется 5

# print(my_list)
# print(num)


# def for_spaces(*args: int, **kwargs):
#     print(f"Позициональные аргументы: {args}")
#     print(f"Именованные аргументы: {kwargs}")


# for_spaces(1, 2, 3, 4, number=1, numda_two=2)


# your_list = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, your_list))
# print(list(map(lambda x: x**2, [1, 2, 3, 4])))


# guv: int = 1

# def give_guv(guv):
#     guv: int = 0
#     guv += 2
#     return guv

# give_guv(guv)

# print(guv)

students = [
    {"name": "Анна", "grade": 85},
    {"name": "Петр", "grade": 92},
    {"name": "Мария", "grade": 78},
    {"name": "Иван", "grade": 95},
]

sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)
for student in sorted_by_grade:
    print(f"{student['name']}, grade: {student["grade"]}")
