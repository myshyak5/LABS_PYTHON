n = int(input())
spc = 0

for i in range(n, 0, -1):
    res = "1"
    for j in range(2, i + 1):
        res = str(j) + res + str(j)
    res = " " * spc + res + " " * spc
    spc += len(str(i))
    print(res)