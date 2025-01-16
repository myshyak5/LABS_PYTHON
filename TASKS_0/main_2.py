n = int(input())

for i in range(n):
    res = ""
    for j in range(i+1):
        res += str(j+1)
    print(res)