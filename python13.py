import numpy as np

var = np.array([[1,2,3,4,5]])
var_1 = np.array([[5,6,7,8,9]])



new_nor = np.dstack((var,var_1))
print(f"new normal :\n",new_nor)