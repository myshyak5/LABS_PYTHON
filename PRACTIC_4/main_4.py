ex_dict = {}
res_dict = {}

arr = input().split()
for elem in arr:
    int_elem = int(elem)
    if int_elem not in ex_dict:
        ex_dict[int_elem] = 1
    else:
        ex_dict[int_elem] += 1
sorted_list = sorted(ex_dict.items(), key = lambda item: item[1], reverse = True)[:3]
sorted_dict = dict(sorted_list)
print(sorted_dict)