mas_1 = [int(i) for i in input().split()]
mas_2 = [int(i) for i in input().split()]
res = set(mas_1) & set(mas_2)
print(len(res))