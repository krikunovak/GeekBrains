# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
i = ""
j = 0
number_of_words = 0

with open("dz_5_2.txt", "a+", encoding="utf-8") as dz52:
    dz52.write("Мы живем в городе Н\n")
    dz52.write("Привет, меня зовут Алиса\n")
    dz52.write("1234567\n")
    dz52.seek(0)  # курсор на начало
    for i in dz52:
        j += 1
        number_of_words = len(i.split())
        print(f"В {j} строке слов {number_of_words} шт: {i}",end="")
        #print("",i, end="")

dz52.close()

print("Количество строк в файле ", str(j))
