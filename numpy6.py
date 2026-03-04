#arthemetic funtion using

import numpy as np

var = np.array([1,2,3,4,5,2,3,45,8,9])
#smalll number of array
print(np.min(var))
#large number of array
print(np.max(var))
# minimum index number
print(np.argmin(var))
# maximum index number
print(np.argmax(var))

#for 2d array min
var_1 = np.array([[2,1,4],[9,5,6]])

#coloumn regarding axis 0 show
print(np.min(var_1,axis=0))

#coloumn regarding axis 1 show
print(np.max(var_1,axis=1))

#square root if come from 1D & 2D array
print(np.sqrt(var))
print(np.sqrt(var_1))

print("------------------")

#sin cos value
var_sin = np.array([1,2,3])
print(np.sin(var_sin))
print(np.cos(var_sin))
