# 7
import json
key = ''
value = 0
dic_ = {}
k = 0
avg = 0
avg_f = 0

with open("dz_5_7.txt", "r", encoding="utf-8") as dz55:
    for i in dz55:
        key = i.split()[0]
        value = float(i.split()[3]) - float(i.split()[2])
        dic_[key] = value
        if value > 0:
            k += 1
            avg += value

avg_f = avg / k
dic_f = {"average_profit": avg_f}
my_list = [dic_, dic_f]
#print(my_list)

with open("my_file.json", "w") as write_f:
    json.dump(my_list, write_f)


with open("my_file.json") as read_f:
    data = json.load(read_f)
print(data)