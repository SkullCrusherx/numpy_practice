#Joining & Split NumPy Arrays Using
import numpy as np

var = np.array([1,2,3,4])
var_1 = np.array([6,7,8,9])

var_3 = np.array([[1,2,3],[4,5,6]])
var_4 = np.array([[7,8,9],[7,6,5]])

var_5 = np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])
var_6 = np.array([[[7,8,9]],[[2,3,4]],[[7,6,5]]])

# for 1D joining array
join = np.concatenate((var,var_1))
print(join)
#using stack 1D
join_stk = np.stack((var,var_1),axis=1)
print(join_stk)

"""# for 2D joining array
join_2D_row = np.concatenate((var_3,var_4),axis=1)
join_2D_col = np.concatenate((var_3,var_4),axis=0)
print(join_2D_row)
print(join_2D_col)

# for 3D joining array
join_3D_row = np.concatenate((var_5,var_6),axis=1)
join_3D_col = np.concatenate((var_5,var_6),axis=0)
print(join_3D_row)
print(join_3D_col)
"""