import functools

def processing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try: return func(*args, **kwargs)
        except Exception as e: print(f'Ошибка вида: {e}.....')  # Общая обработка ошибок
    return wrapper

class Laba4:
    def __init__(self, number: int) -> None:
        self.set_number(number)

    def set_number(self, number: int):
        if number > 999:
            raise ValueError("Число не должно быть больше 999.")
        self.number = number

    @processing
    def add_time(self):
        return self.number  # Возвращает число, а не строку
    
# Тестирование
try:
    number_test = Laba4(123)
    print(number_test.add_time())  # Должно вернуть 123
except Exception as e: print(e)

try: number_test = Laba4(1000)  # Это должно вызвать ошибку
except Exception as e: print(e)  # Выведет сообщение об ошибке
