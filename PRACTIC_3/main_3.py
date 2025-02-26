mas_dict = {}
mas = [i for i in input().split()]
for elem in mas:
    if elem not in mas_dict:
        mas_dict[elem] = 1
    else:
        mas_dict[elem] += 1
print(*mas_dict.values())