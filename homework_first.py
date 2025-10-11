def cheker(var):
    k = 0
    for j in var:
        if j in "0123456789":
            k += 1
    if len(var) <= 1 or k > 0:
        return False
    else:
        return True


while True:
    name = input("Введите имя: ").capitalize()
    if not cheker(name):
        print("Вы ввели не имя или же в написание есть цифры!")
    else:
        break


while True:
    try:
        age = int(input("Введите возраст: "))
        if age < 0:
            print("Возраст не может быть отрицательным!")
        else:
            break
    except ValueError:
        print("Вы ввели не число!")


while True:
    profession = input("Введите профессию: ").title()
    if not cheker(profession):
        print("Некорректное написание профессии")
    else:
        break


def questionnaire(name: str, age: int, profession: str) -> str:
    return (
        f"Анкета: \n 1. Имя: {name} \n 2. Возраст: {age} \n 3. Профессия: {profession}"
    )


print(questionnaire(name, age, profession))
