import numpy as np

x = np.array([2, 2, 2, 3, 3, 3, 5])
values = []
counts = []

value = x[0]
count = 1
for elem in x[1:]:
    if elem == value:
        count += 1
    else:
        values.append(value)
        counts.append(count)
        value = elem
        count = 1
values.append(value)
counts.append(count)

print((np.array(values), np.array(counts)))