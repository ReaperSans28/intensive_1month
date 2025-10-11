import os

# r - чтение. Файл обязан существовать. Прочитать файл можно всего 1 раз.
def read_my_file():
    content: str
    with open("../data/test_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print(content)


# a - добавление в конец. Либо записывается, либо создается новый
with open("../data/test_file.txt", "a", encoding="utf-8") as file:
    file.write("\nАга")


with open("../data/test_file.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())

with open("../data/test_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# w - перезапись. Либо перезаписывается, либо создается новый
with open("../data/test_file.txt", "w", encoding="utf-8") as file:
    file.write("Да так и не\n")
    file.write("Выловировали\n")

lines = ["Первый\n", "Второй\n", "Третий"]
with open("../data/test_file.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

if os.path.exists("operations.txt"):
    with open("operations.txt", "r", encoding="utf-8") as source, open("logging_calc.txt", "a", encoding="utf-8") as file:
        content = source.read()
        file.write(content)


# # x - эксклюзивное создание. Ошибка, если файл существует
# # b - бинарный режим. Используется в комбинациях, rb и wb
# # + - расщирение выбранного параметра. r+ читать и записывать

# Exceptions
# try:
#     with open("../data/test_file111.txt", "r", encoding="utf-8") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Файла нет")
# except PermissionError:
#     print("Нет прав")
# except IOError:
#     print("Ошибка вывода")
# except Exception as e:
#     print("Неожиданная ошибка")
