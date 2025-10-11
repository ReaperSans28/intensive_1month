text = input("Введите слово: ")
answers = {"greeting" : ["Привет", "hi", "hello", "прив", "привет"],
           "goodbue" : ["пока", "Пока", "bue"],
           }

while True:

    if text == answers.get('greeting'):
        print("Привет")
        continue
    elif text.startswith("Как"):
        print("Как дела?")
    elif text == answers.get('goodbue'):
        print("Пока")
        continue
    else:
        print("Ошибка ввода. Введите приветствие")
        break