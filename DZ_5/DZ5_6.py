# Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести словарь на экран.
l = 0
p = 0
la = 0
key = ''
value = 0
dic_ = {}

with open("dz_5_6.txt", "r", encoding="utf-8") as dz55:
    for i in dz55:
        # print(i)
        key = i.split()[0]
        # print(i.split()[3])
        if i.split()[1] == "-":
            l = 0
        else:
            l = float(i.split()[1].replace("(л)", ""))

        if i.split()[2] == "-":
            p = 0
        else:
            p = float(i.split()[2].replace("(пр)", ""))

        if i.split()[3] == "-":
            la = 0
        else:
            la = float(i.split()[3].replace("(лаб)", ""))
        value = l + p + la
        dic_[key] = value

print(dic_)
