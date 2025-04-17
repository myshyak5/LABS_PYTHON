import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')
species = iris[:, -1]
unique, counts = np.unique(species, return_counts = True)
for i in range(len(counts)):
    print(f"{unique[i].decode('utf-8')}: {counts[i]}")