class Laba4:
    def __init__(self, number: int) -> None:
        self.set_number(number)

    def set_number(self, number: int):
        if number > 999:
            raise ValueError("Число не должно быть больше 999.")
        self.number = number

    def get_str_ending(self) -> str:
        if 11 <= self.number % 100 <= 19: return "рублей"
        elif self.number % 10 == 1: return "рубль"
        elif self.number % 10 in (2, 3, 4): return "рубля"
        else: return "рублей"

    def add_time(self) -> str:
        ending = self.get_str_ending()
        return f'Ваше число: {self.number} {ending}.'  # Возвращает строку с окончанием


try:
    number_test = Laba4(123)
    print(number_test.add_time())  
except Exception as e: print(e)

try: number_test = Laba4(1000)  
except Exception as e: print(e)  

try:
    number_test = Laba4(1)
    print(number_test.add_time())  
except Exception as e: print(e)

try:
    number_test = Laba4(22)
    print(number_test.add_time())  
except Exception as e: print(e)

try:
    number_test = Laba4(11)
    print(number_test.add_time())  
except Exception as e: print(e)
