# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также
# покажите результат

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f' поехала'

    def stop(self):
        return f' остановилась'

    def turn(self, direction="никуда"):
        if direction == "right":
            return f' повернула направо'
        if direction == "left":
            return f' повернула направо'
        else:
            return "никуда не поворачивала"

    def show_speed(self):
        return f'Текущая скорость машины {self.name} равна {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 60:
            return f'Скорость машины {self.name} равна {self.speed} км/ч, она прервышает допустимые 60 км/ч'
        else:
            return f'Текущая скорость машины {self.name} равна {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 40:
            return f'Скорость машины {self.name} равна {self.speed} км/ч, она прервышает допустимые 40 км/ч'
        else:
            return f'Текущая скорость машины {self.name} равна {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f' является полицейской'
        else:
            return f' не является полицейской'


a1 = SportCar(200, 'Red', 'Mazda', False)
a2 = TownCar(100, 'Black', 'Ford', False)
a3 = WorkCar(77, 'Green', 'Nessan', False)
a4 = PoliceCar(333, 'Blue', 'Infinity', True)
print("-------------")
print(f'Машина {a1.name} {a1.turn("left")}, затем {a1.go()}, а затем {a1.turn("right")}')
print(f'Машина {a2.name} {a2.turn("right")}, {a2.stop()}')
print(f'Машина {a3.name} {a3.turn()}, {a3.stop()} ')
print(f'Машина {a4.name} {a4.turn()}, {a4.stop()} ')
print("-------------")
print(f'Машина {a1.name} {a1.go()} со скоростью {a1.speed} км/ч')
print(f'Машина {a2.name} {a2.go()} со скоростью {a2.speed} км/ч')
print(f'Машина {a3.name} {a3.go()} со скоростью {a3.speed} км/ч')
print(f'Машина {a4.name} {a4.go()} со скоростью {a4.speed} км/ч')
print("-------------")
print(f'{a1.show_speed()}, она SportCar')
print(f'{a2.show_speed()}, она TownCar')
print(f'{a3.show_speed()}, она WorkCar')
print(f'{a4.show_speed()}, она PoliceCar')
print("-------------")
print(f'{a1.name} -  {a1.color}')
print(f'{a2.name} -  {a2.color}')
print(f'{a3.name} -  {a3.color}')
print(f'{a4.name} -  {a4.color}')
print("-------------")
print(f'{a1.name}  полицейская (да/нет)? : {a1.is_police}')
print(f'{a2.name}  полицейская (да/нет)? : {a2.is_police}')
print(f'{a3.name}  полицейская (да/нет)? : {a3.is_police}')
print(f'{a4.name}  полицейская (да/нет)? : {a4.is_police}')
print("-------------")
