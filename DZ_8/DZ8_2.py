"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
 Проверьте его работу на данных, вводимых пользователем.
 При вводе пользователем нуля в качестве делителя программа должна корректно обработать
 эту ситуацию и не завершиться с ошибкой.

"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DelByNull:
    def __init__(self, d_1, d_2):
        self.d_1 = d_1
        self.d_2 = d_2

    @staticmethod
    def divide_by_null(d_1, d_2):
        try:
            if d_2 == 0:
                raise OwnError(f"!!!Ошибка: Деление на ноль недопустимо")
                #return f"Результат деления {d_1} на {d_2} "
            else:
                return f"Результат деления {d_1} на {d_2} равен: {d_1 / d_2}"

        except OwnError as err:
            print(err)

        finally:
            if d_2 == 0:
                return f"Результат деления {d_1} на {d_2} нельзя получить"


print("-----------------------")
print(DelByNull.divide_by_null(10, 0))
print("-----------------------")
print(DelByNull.divide_by_null(10, 2))
print("-----------------------")
print(DelByNull.divide_by_null(10, 0.1))
print("-----------------------")

