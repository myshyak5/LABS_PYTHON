a = str(input())
res_a = ""
i = len(a) - 1
while i >= 0:
    if a[i].isdigit():
        res_a = a[i - 1] * int(a[i]) + res_a
        i -= 1
    else:
        res_a = a[i] + res_a
    i -= 1
print(res_a)