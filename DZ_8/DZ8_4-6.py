"""4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

class SkladOrg:
    """Класс, описывающий склад оргтехники"""


class BasOrg:
    """Базовый класс оргтехники"""
    org_count = 0
    table_count = 0
    all_staff = {}

    def __init__(self, producer, color, year, cost):
        self.producer = producer
        self.color = color
        self.year = year
        self.cost = cost

    def what_is_it(self):
        print(f' !Это {self.producer} цвета {self.color} buy in {self.year} cost {self.cost}')


class Printer(BasOrg):
    """Класс принтер"""
    BasOrg.org_count += 1


    def __init__(self, producer, color, year, cost, pr_type):
        super().__init__(producer, color, year, cost)
        self.pr_type = pr_type
        if cost.isdigit() == False:
            print("!!!Ошибка: введено не корректное значение цены")
            return
        cost = float(cost)
        if year.isdigit() == False:
            print("!!!Ошибка: введено не корректное значение года")
            return
        year =int(year)

    def __str__(self):
        return f'Это принтер {self.producer}, цвет {self.color}, сделанный в {self.year}, стоит {self.cost} usd, тип {self.pr_type}'

    @staticmethod
    def org_name():
        print("<<Принтер>>", end=' ')

    def type_printer(self):
        return self.pr_type


    def where_use_it(self):
        if self.year.isdigit() == False:
            print("!!!Ошибка: введено не корректное значение года")
            return ""
        #self.year = int(self.year)
        if int(self.year) > 2020:
            return 'Ошибка в дате, нужно подключать сотрудников поддержки'
        elif 2020 > int(self.year) > 2001:
            return 'Будет работать в офисе!'
        else:
            return 'Очень старый,нужно списать'

    def get_to_storehouse(self):
        BasOrg.all_staff['printer'] = self.producer

class Scanner(BasOrg):
    """Класс сканер"""
    BasOrg.org_count += 1
    def __init__(self, producer, color, year, cost, sc_cod):
        super().__init__(producer, color, year, cost)
        self.sc_cod = sc_cod

    def __str__(self):
        return f'Это сканер {self.producer}, цвет {self.color}, сделанный в {self.year}, стоит {self.cost} usd, код {self.sc_cod}'

    @staticmethod
    def org_name():
        print("<<Сканер>>", end='  ')

    def sc_cod_(self):
        return self.sc_cod

    def get_to_storehouse(self):
        BasOrg.all_staff['scaner'] = self.producer

class Xerox(BasOrg):
    """Класс ксерокс"""
    BasOrg.org_count += 1
    def __init__(self, producer, color, year, cost, xer_email):
        super().__init__(producer, color, year, cost)
        self.xer_email = xer_email

    def __str__(self):
        return f'Это ксерокс {self.producer}, цвет {self.color}, сделанный в {self.year}, стоит {self.cost} usd, оправка на email: {self.xer_email}'

    @staticmethod
    def org_name():
        print("<<Ксерокс>>", end=' ')

    def xer_email_send(self):
        return self.xer_email

    def get_to_storehouse(self):
        BasOrg.all_staff['XSEROX'] = self.producer

class Table(BasOrg):
    BasOrg.table_count +=1
    tabels_by_m2 = []
    def __str__(self):
        return f'Таблица {self.producer}, цвет {self.color}, куплен в {self.year}, цена {self.cost} usd'
    def square(self,width,lenth):
        Table.tabels_by_m2.append(width*lenth/1000)
        return width * lenth / 1000
    def get_to_storehouse(self):
        BasOrg.all_staff['table'] = self.producer

print("-----------------")
p = Printer('HP  ', 'red  ',input("введите год:"),input("введите стоимость:"), 'лазерный')
s = Scanner('Canon', 'yello',2000,123, 'rtf_55643')
x = Xerox('Hp   ', 'green',2015,123, 'есть')
b = Table('Simple',"Ikea 90*60",2019,400)
print(p)
print(p.where_use_it())
print(s)
print(x)
print("-----------------")

print("принтер",p.where_use_it())
print("количество единиц",p.org_count)
print("-----------------")
b.square(90,60)
p.get_to_storehouse()
s.get_to_storehouse()
x.get_to_storehouse()
b.get_to_storehouse()
print("-----------------")
print(b)
print(b.tabels_by_m2)
print(b.table_count)
print(BasOrg.all_staff)



