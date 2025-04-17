import numpy as np

array = np.array([0,1,2,0,0,4,0,6,9])
nonzero_ind = array.nonzero()[0]
print(*nonzero_ind)