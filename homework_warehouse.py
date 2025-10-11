array = {}
id = 0

while True:
    print(
        """\nКаталог команд:
    1. Добавить товар
    2. Удалить товар
    3. Зафиксировать продажу товара
    4. Зафиксировать поставку товара
    5. Найти ID товара
    6. Найти товар по ID
    7. Общая стоимость всех товаров
    8. Список товаров    
    9. Завершить программу
Для управления терминалом введите номер команды.
          """
    )
    try:
        user_answer = int(input())
    except ValueError:
        print("Введите номер команды!")
        continue
    match user_answer:
        case 1:
            try:
                a1 = input("Введите товар: ").lower()
                a2 = int(input("Введите кол-во товара, которое хотите добавить: "))
                a3 = int(input("Введите цену (в рублях) 1шт.: "))
            except ValueError:
                print("Аргументы введены не верно!")
                continue
            try:
                int(a1)
                print(f"Товаров с именем {a1} не существует")
                continue
            except ValueError:
                new_list = [a1, a2, a3]
                id += 1
                array.update({id: new_list})
                print(
                    f"Товар {a1} успешно добавлен. ID: {id}. Исходная цена товаров: {a2 * a3} руб."
                )

        case 2:
            try:
                item = int(input("Введите индекс элемента который вы хотите удалить: "))
                try:
                    del array[item]
                    print(f"Товар успешно удален")
                except KeyError:
                    print("Товар отсутствует")

            except ValueError:
                print("Введен не индекс")
                continue

        case 3:
            try:
                b1 = int(input("Введите ID товара: "))
                b2 = int(input("Введите количество продаж: "))
            except ValueError:
                print("Аргументы введены неверно!")
                continue

            record = array.get(b1)
            if not record:
                print("Нет такого ID")
                continue

            name, qty, price = record

            if b2 <= 0:
                print("Количество продаж должно быть положительным.")
                continue

            if qty < b2:
                print("Ошибка. Продаж больше, чем остаток!")
                continue
            qty -= b2
            array[b1][1] = qty
            revenue = b2 * price
            total_left = qty * price
            print(
                f"""Продажа зафиксирована.
Итоговый остаток ({name}) — {qty} шт.
Общая стоимость остатка: {total_left} руб.
Выручка: {revenue} руб."""
            )
        case 4:
            try:
                s1 = int(input("Введите ID товара: "))
                s2 = int(input("Введите количество поставки: "))
            except ValueError:
                print("Аргументы введены неверно!")
                continue

            record = array.get(s1)
            if not record:
                print("Нет такого ID")
                continue

            if s2 <= 0:
                print("Количество поставки должно быть положительным.")
                continue

            name, qty, price = record
            qty += s2
            array[s1][1] = qty

            print(
                f"""Поставка зафиксирована.
        Итоговое количество товара ({name}) — {qty} шт. на складе.
        Текущая цена за шт.: {price} руб.
        Общая стоимость остатка: {qty * price} руб."""
            )

        case 5:
            try:
                item = str(input("Введите название товара: ").lower())
            except ValueError:
                print("Название товара введено неверно!")
                continue
            if not array:
                print("Склад пуст")
            else:
                gen = [k for k, v in array.items() if v[0] == item]
                if len(gen) > 0:

                    print(f"ID товара: {gen}")
                else:
                    print(f"Товара с названием {item}, нет на складе")

        case 6:
            try:
                id_5 = int(input("Введите ID искомого товара: "))
            except ValueError:
                print("Введено не ID")
                continue
            try:
                name_5, *another = array[id_5]
                print(f"Искомый товар: {name_5}")
            except KeyError:
                print("Товара с таким ID на складе нет")

        case 7:
            total_price = 0
            for v in array.values():
                total_price += v[1] * v[2]
            print(f"Стоимость товаров на складе: {total_price} руб.")

        case 8:
            if not array:
                print("Склад пуст")
            else:
                print("Товары:")
                for item_id in sorted(array):
                    name, qty, price = array[item_id]
                    print(
                        f"""#{item_id}(ID)
Название: {name}
Количество: {qty} шт.
Цена: {price} руб.
            """
                    )
        case 9:
            print("Программа завершена!")
            break
        case _:
            print("Некорректный номер команды")
