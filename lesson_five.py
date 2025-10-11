person: dict = {
    "name": "Alice",
    "age": 25,
    "city": "Moscow",
    "professions": ["Teacher", "Programmer"],
}

numbers: set = {1, 2, 3, 4, 5}

# Получение данных
name = person["name"]
age = person["age"]
get_age = person.get("age")

# Изменение данных по ключу
person["name"] = "Bob"

# Добавление данных в словарь
person.update({"height": 180, "country": "Russia"})

# Удаление данных
# del PERSON["name"]
# age = PERSON.pop("age")
# PERSON.clear()

if "name" in person:
    print("Существует")

# Методы класса
keys = person.keys()
values = person.values()
items = person.items()

# Итерация
for key, value in person.items():
    print(f"{key}, {value}")

print()

answers = {"greetings": []}
