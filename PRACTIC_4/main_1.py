ex_dict = {}

mas = set([i for i in input("Ключи: ").split()])
for elem in mas:
    val = input(f"Значение по ключу {elem}: ")
    ex_dict[elem] = val
res_key = input("Вывести значение по ключу ")
print(ex_dict[res_key])