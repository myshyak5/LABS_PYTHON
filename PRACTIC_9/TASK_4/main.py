import numpy as np

values = list(map(int, input().split()))
x = np.array(values)

values0 = []

for i, value in enumerate(x[1:], 1):
    if x[i - 1] == 0:
        values0.append(value)

values0 = np.array(values0)
print(np.max(values0))
