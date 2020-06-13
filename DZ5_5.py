# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.
summ = 0
k = 0
try:
    with open("dz_5_1.txt", "w", encoding="utf-8") as dz55:
        f = input("Введите строку через пробел: ")
        print(f, file=dz55)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    dz55.close()

try:
    with open("dz_5_1.txt", "r", encoding="utf-8") as dz55:
        for i in dz55:
            for k in range(0, len(i.split())):
                if i.split()[k].isdigit() == True:
                    summ += float(i.split()[k])
    print(f"Сумма чисел = {summ}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    dz55.close()
