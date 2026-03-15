#Joining & Split NumPy Arrays Using
import numpy as np

var = np.array([1,2,3,4])
var_1 = np.array([6,7,8,9])
var_3 = np.array([[1,2,3],[4,5,6]])
var_4 = np.array([[7,8,9],[7,6,5]])

# for 1D joining array
join = np.concatenate((var,var_1))
print(join)

# for 2D joining array
join_2D_row = np.concatenate((var_3,var_4),axis=1)
join_2D_col = np.concatenate((var_3,var_4),axis=0)
print(join_2D_row)
print(join_2D_col)
