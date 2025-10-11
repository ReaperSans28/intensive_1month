# Описание: Напишите программу, которая принимает строку и выводит ее в обратном порядке.
word: str = str(input())
reversed_text: str = ""
index = len(word) - 1

for i in range(len(word) - 1, -1, -1):
    reversed_text += word[i]

while index >= 0:
    reversed_text += word[index]
    index -= 1

print(reversed_text)

# name: str = "Дракула"
# vegetables: list = ["potatoe", "carrot", "cabbage"]
# abc: map = {"a": 1, "b": 2, "c": 3}
# teacher_data: tuple = ("Bogdan", "Leontev", "23")

# for char in name:
#     print(char, end=" ")

# for vegetable in vegetables:
#     print(f"Овощь присутствует: {vegetable}")

# for x in abc:
#     print(f"По ключу {x} у нас значение {abc[x]}")

# for data in teacher_data:
#     print(data)
# for index, vegetable in enumerate(vegetables):
#     print(f"index {index}: {vegetable}")
