#arthemetic funtion using

import numpy as np

var = np.array([1,2,3,4,5,2,3,45,8])
#smalll number of array
print(np.min(var))
#large number of array
print(np.max(var))
# minimum index number
print(np.argmin(var))
# maximum index number
print(np.argmax(var))

#for 2d array min

var_1 = np.array([[2,1,3],[9,5,6]])
print(np.min(var_1,axis=0))
