import numpy as np

var = np.array([1,2,3,4,5])
var_1 = np.array([5,6,7,8,9])
var_2 = np.array([10,11,12,13,14])
var_3 = np.array([16,17,18,19,20])

new_nor = np.stack((var,var_1,var_2,var_3),axis=0)
print(f"new normal :\n",new_nor)

new_ver= np.stack((var,var_1,var_2,var_3),axis=1)
print(f"new normal :\n",new_ver)