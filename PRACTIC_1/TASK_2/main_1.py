n = int(input())

for i in range(n, 0, -1):
    res = ""
    for j in range(i):
        res += str(j + 1)
    print(res)