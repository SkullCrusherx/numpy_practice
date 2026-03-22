#Last series of WS cube Tutorial
#MATRIX and matrix operations

import numpy as np
var_22 = np.matrix([[1,2],[4,5]])
var = np.matrix([[1,2,3],[3,4,5]])
var_2d = np.matrix([[4,5,6],[7,8,9]])

np.add(var,var_2d)

print(var)
print("===========")
print(var.transpose())
print("===========")
print(var_22.transpose())
print("===========")
print(var_22.T)