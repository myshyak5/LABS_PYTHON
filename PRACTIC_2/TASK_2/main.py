a = str(input())
set_a = list(set(a))
if " " in set_a:
    set_a.remove(" ")
k = [a.count(i) for i in set_a]
for i in range(len(k) - 1):
    for j in range(i, len(k)):
        if k[i] < k[j]:
            k[i], k[j] = k[j], k[i]
            set_a[i], set_a[j] = set_a[j], set_a[i]
for i in range(3):
    print(set_a[i], k[i])