fruits: list = [
    "apple",
    "banana",
    "orange",
    "apple",
    "apple",
    "apple",
    "apple",
    "apple",
    "apple",
]
vegetables: list = ["potatoe", "carrot", "cabage"]
catalog = [fruits, vegetables]
print(catalog)

PERSON: tuple = ("Tima", "Padusev", "artist")
COLORS: tuple = ("red", "green", "blue", "red")

something: list = ["Ананас"]
something_tuple = ("Ананас",)

print(fruits)

# Добавить
fruits.append("Апельсин")
fruits.insert(2, "Киви")
fruits.extend(vegetables)
print(fruits)

# Удалить
fruits.remove("apple")
del fruits[0]
removed = fruits.pop(-1)

# Изменить
fruits[0] = "Манго"

# Дополнительные методы списка
index_apple = fruits.index("red")
count_of_apples = COLORS.count("red")
exists = "9" in COLORS
print(index_apple)


sorted_fruits = sorted(fruits)

fruits.reverse()

print(exists)
print(sorted_fruits)

# Индексация
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first = data[0]
second = data[1]

last = data[-1]

# Срезы
subset = data[2:5]
every_third = data[::-1]

print(every_third)
