import numpy as np
"""var = np.array([1,2,3,4])
print(var.shape)
var_1 = np.ones((2,4,3))
print(var_1)"""



# Create a 3D array with ones along the second axis
arr = np.ones((2, 3, 4), dtype=int)
arr[:, 1, :] = 2
print(arr)