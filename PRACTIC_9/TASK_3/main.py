import numpy as np

array = np.random.normal(size = (10, 4))
rows_1_5 = array[:5]

min_values = np.min(array)
max_values = np.max(array)
mean_values = np.mean(array)
std_devs = np.std(array)
for row in rows_1_5:
    print(row)
print(min_values)
print(max_values)
print(mean_values)
print(std_devs)