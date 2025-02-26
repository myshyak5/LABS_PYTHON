mas = [int(i) for i in input().split()]
res = [mas[i] for i in range(1, len(mas)) if (mas[i] > mas[i - 1])]
print(res)