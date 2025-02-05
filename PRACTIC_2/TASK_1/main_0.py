a = str(input())
res_a = ""
for i in a:
    i_count = str(a.count(i))
    if not(i + i_count) in res_a:
        res_a += i
        if i_count != "1":
            res_a += i_count
print(res_a)