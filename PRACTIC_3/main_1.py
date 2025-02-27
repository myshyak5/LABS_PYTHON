mas = [int(i) for i in input().split()]
max_mas = max(mas)
min_mas = min(mas)
for i in range(len(mas)):
    if (mas[i] == max_mas):
        mas[i] = min_mas
    elif (mas[i] == min_mas):
        mas[i] = max_mas
print(mas)
