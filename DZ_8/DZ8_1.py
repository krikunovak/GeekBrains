"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
 на реальных данных.
 """

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def metod_1(cls, day_month_year):
        day, month, year = map(int, day_month_year.split('-'))
        return day, month, year

    @staticmethod
    def metod_2(day_month_year):
        day, month, year = map(int, day_month_year.split('-'))
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Данные введены корркетно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'
    def __str__(self):
        return f"Текущая дата {Data.metod_1(self.day_month_year)}"


d_1 = '11-11-2004'
d_0 = '22-22-2020'
data_1 = Data(d_1)
print("-------")
print(data_1)
print("-------")
print("Метод_1 возвращает:",Data.metod_1(d_1))
print("Метод_2 возвращает:",Data.metod_2(d_1))
print("-------")
print("Метод_1 возвращает:",data_1.metod_1(d_0))
print("Метод_2 возвращает:",data_1.metod_2(d_0))
print("-------")
