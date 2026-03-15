#Joining & Split NumPy Arrays Using
import numpy as np

var = np.array([1,2,3,4])
var_1 = np.array([6,7,8,9])
var_3 = np.array([[1,2,3],[4,5,6]])
var_4 = np.array([[7,8,9],[7,6,5]])

# for 1D joining array
join = np.concatenate((var,var_1))
print(join)

# for 1D joining array
join = np.concatenate((var_3,var_4),axis=1)

print(join)
