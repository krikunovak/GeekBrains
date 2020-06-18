'''
Реализовать проект расчета суммарного расхода ткани на
производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на
практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике
работу декоратора @property.
'''


class Textil:
    def __init__(self, number):
        self.number = number



class Coat(Textil):
    def __init__(self, number):
        self.V = number

    @property
    def get_square(self):
        return round(self.V / 6.5 + 0.5,2)

    def __str__(self):
        return f'Площадь на пальто {self.get_square} (V/6.5+0.5, V={self.V})'


class Jacket(Textil):
    def __init__(self, number):
        self.H = number

    @property
    def get_square(self):
        return round(self.H * 2 + 0.3,2)

    def __str__(self):
        return f'Площадь на костюм {self.get_square} (H*2+0.3, H={self.H})'


coat = Coat(12)
jacket = Jacket(2)
print("-----")
print(coat)
print(jacket)
print("-----")
print("Общий расчет ткани", round(coat.get_square+jacket.get_square,2))
print("-----")


