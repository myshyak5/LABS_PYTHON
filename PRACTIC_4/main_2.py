ex_dict = {}

mas = set([i for i in input("Ключи: ").split()])
for elem in mas:
    val = input(f"Значение по ключу {elem}: ")
    ex_dict[elem] = val
res_value = input("Вывести ключ по значению ")
for key, value in ex_dict.items():
    if (value == res_value):
        print(key)