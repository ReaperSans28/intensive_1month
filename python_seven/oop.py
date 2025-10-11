from abc import ABC, abstractmethod


class AbstractProgrammer(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_salary(self, salary):
        pass


class JuniorProgrammer(AbstractProgrammer):
    def __init__(self, name, ages_of_work):
        self.name = name
        self.ages_of_work = ages_of_work
        self.grade = "Junior"
        self.bonus = 1

    def get_salary(self, salary):
        return salary * self.bonus

    def get_info(self):
        return f"Junior Programmer: {self.name}, ages_of_work: {self.ages_of_work}"


class MiddleProgrammer(JuniorProgrammer):
    def __init__(self, name, work_ages, is_free=True):
        super().__init__(name, work_ages)
        self.grade = "Middle"
        self.bonus = 1.05
        self.is_free = is_free

    def get_info(self):
        return f"Middle Programmer: {self.name}, ages_of_work: {self.ages_of_work}"

    def get_is_free(self):
        return f"Свободен для проектов" if self.is_free == True else f"Занят"


class SeniorProgrammer(MiddleProgrammer):
    def __init__(self, name, ages_of_work, is_free=True, mentis_count=0):
        super().__init__(name, ages_of_work, is_free)
        self.grade = "Senior"
        self.bonus = 1.2
        self.mentis_count = mentis_count

    def get_info(self):
        return f"Senior Programmer: {self.name}, ages_of_work: {self.ages_of_work}"

    def add_menti(self):
        self.mentis_count += 1


class FrontendProgrammer(AbstractProgrammer):
    def __init__(self, name, ages_of_work):
        self.name = name
        self.ages_of_work = ages_of_work
        self.grade = "Frontend"
        self.bonus = 1

    def get_salary(self, salary):
        return salary * self.bonus * 1.05

    def get_info(self):
        return f"Junior Programmer: {self.name}, ages_of_work: {self.ages_of_work}"


class FullStackProgrammer(SeniorProgrammer, FrontendProgrammer):
    def __init__(self, name, ages_of_work, is_free=True, mentis_count=0):
        super().__init__(name, ages_of_work, is_free)
        SeniorProgrammer.__init__(
            self, name, ages_of_work, is_free=True, mentis_count=0
        )


# jun_programmer = JuniorProgrammer("Bob", 1)
# mid_programmer = MiddleProgrammer("Ruben", 2, False)
# sen_programmer = SeniorProgrammer("Ignatiy", 5, True, 2)
# print(jun_programmer.get_info())
# print(mid_programmer.get_info())
# print(sen_programmer.get_info())


class BancAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self.__pin = "1234"

    @property
    def balance(self):
        """Публичный метод, чтобы узнать баланс. Это тоже часть интерфейса."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Публичный метод для пополнения счёта. Это часть интерфейса."""
        if amount > 0:
            self._balance = (
                amount  # к защищённому атрибуту обращаемся ТОЛЬКО внутри методов
            )
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount, pin):
        """Публичный метод для снятия денег. Это часть интерфейса."""
        if pin == self.__pin:  # проверяем пин-код, который спрятан глубоко внутри
            if amount <= self._balance:
                self._balance -= amount
            else:
                print("Недостаточно средств")
        else:
            print("Неверный пин-код")

    def __str__(self):
        return f"Класс BancAccount с методом withdraw и геттером + сеттером balance."

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"

    def __add__(self, other):
        new_owner = f"{self.owner}+{other.owner}"
        new_balance = self.balance + other.balance
        return BancAccount(new_owner, new_balance)


account = BancAccount("Komasan", 4)
account_2 = BancAccount("Cocoa", 8)

print(account)
print(repr(account))

account_3 = account_2 + account
print(account_3.owner)

account.balance = 1
print(account.balance)
