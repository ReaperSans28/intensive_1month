# cup_with_ball: int = 5
# max_count_cup: int = 5
# user_answer: int = input("Введите число: ")

# if type(user_answer) is int and user_answer == cup_with_ball:
#     print("Верно, вы победили!")

# elif user_answer > 5:
#     print("Такого количества стаканов у нас нет!")
# elif user_answer < cup_with_ball or user_answer > cup_with_ball:
#     print("Неверно")
# elif user_answer <= 0:
#     print("Это невозможно")

# else:
#     print("Вы ввели некорректное значение!")

# >, <, >=, <=, ==, !=
# not, and, or


# Написать программу-анкету, которая запрашивает имя, возраст и хобби пользователя, а затем выводит отформатированную информацию о нем.
# 1) Если пользователь введет возраст текстом, а не числом, выйдет ValueError
# 2) Возраст можно ввести как отрицательное значение, так и до конца значений инта большое. Также оно может быть просто пустым.
# 3) McDonald, Жанна д'Арк,
name: str
age: int
hobby: str


def get_username():
    while True:
        user_name_answer = input("Введите имя: ")
        if type(user_name_answer) is not str or user_name_answer.isdigit() is True:
            print(f"{user_name_answer} не того типа")
        elif len(user_name_answer) <= 0 or len(user_name_answer) > 1500:
            print("Имя не может быть такой длины")
        elif user_name_answer[0].islower() and "'" not in user_name_answer:
            print("Имя не может начинатся со строчной буквы")
        elif (
            not user_name_answer[0].isalpha()
            and not user_name_answer[-1].isalpha()
            and user_name_answer[-1].isupper()
        ):
            print("Имя может заканчиваться только строчной буквой")

        else:
            name = str(user_name_answer)

        break
    return "Имя провалидировано"
