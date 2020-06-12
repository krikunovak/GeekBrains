# 4. Создать (не программно) текстовый файл со следующим содержимым:
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_k = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

strr = ''
with open("dz_5_4.txt", "r", encoding="utf-8") as dz54:
    for i in dz54:
        for k, v in dict_k.items():
            if i.split()[0] == k:
                strr = i.replace(k, v)
                print(strr, end="")
                with open("dz_5_44.txt", "a+", encoding="utf-8") as dz544:
                    print(strr, end="", file=dz544)
                dz544.close()
dz54.close()
