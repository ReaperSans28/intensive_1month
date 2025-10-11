from datetime import datetime


def logger(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        params = (args, kwargs)
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"Функция: {func.__name__} начала работу в {start_time} и завершила в {end_time}, принимая аргументы: {params}, с результатом {result}")
        return result
    return wrapper
