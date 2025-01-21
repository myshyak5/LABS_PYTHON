n = int(input())
mas = []

for i in range(n):
    mas1 = [1] * (i + 1)
    for j in range(1, i):
        mas1[j] = mas[j - 1] + mas[j]
    mas = mas1
    print(*mas1)