# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
my_list = []
avg_list = []


def Average(lst):
    return sum(lst) / len(lst)


print("-------------------")
print("Содержимое файла:")
with open("dz_5_3.txt", "r", encoding="utf-8") as dz53:
    for i in dz53:
        print("", i, end="")
print("\n-------------------")
print("У следующих сотрудников оклад меньше 20 тыс.:")
with open("dz_5_3.txt", "r", encoding="utf-8") as dz53:
    my_list = [i.split()[0] for i in dz53 if float(i.split()[1]) < 20000]
    print(my_list)

print("\n-------------------")

with open("dz_5_3.txt", "r", encoding="utf-8") as dz53:
    avg_list = [float(i.split()[1]) for i in dz53]

print("Оклады всех сотрудников:", avg_list)
print(f"Среднее значение дохода сотрудников: {Average(avg_list)}")
