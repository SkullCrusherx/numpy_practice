#Joining & Split NumPy Arrays Using
import numpy as np

var = np.array([1,2,3,4])
var_1 = np.array([6,7,8,9])

"""var_3 = np.array([[1,2,3],[4,5,6]])
var_4 = np.array([[7,8,9],[7,6,5]])

var_5 = np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])
var_6 = np.array([[[7,8,9]],[[2,3,4]],[[7,6,5]]])
#--------------------------------------------------------------------
# For 1D joining array
#--------------------------------------------------------------------
join = np.concatenate((var,var_1))
print(join)
#using stack 1D row wise
join_stk_col = np.stack((var,var_1),axis=0)
join_stk_row = np.stack((var,var_1),axis=1)
print(join_stk_col)
print(join_stk_row)
#--------------------------------------------------------------------
# For 2D joining array
#--------------------------------------------------------------------
join_2D_row = np.concatenate((var_3,var_4),axis=1)
join_2D_col = np.concatenate((var_3,var_4),axis=0)
print(join_2D_row)
print(join_2D_col)

#--------------------------------------------------------------------
#----------------------Using Stack 2D-------------------------------
#--------------------------------------------------------------------
join_stk_col = np.vstack((var,var_1)) #Vertical stack making 1D + 1D
join_stk_row = np.hstack((var,var_1)) #Making 1D array
join_stk_height = np.dstack((var,var_1)) #Acording to Height col depend on how many array add

print(join_stk_col)
print(join_stk_row)
print(join_stk_height)
#--------------------------------------------------------------------
#---------------------For 3D joining array---------------------------
#--------------------------------------------------------------------
join_3D_row = np.concatenate((var_5,var_6),axis=1)
join_3D_col = np.concatenate((var_5,var_6),axis=0)
print(join_3D_row)
print(join_3D_col)
#--------------------------------------------------------------------
#------------------------Using Stack 3D------------------------------
#--------------------------------------------------------------------
join_stk_col_3d = np.vstack((var,var_1)) #Vertical stack making 3D
join_stk_row_3d = np.hstack((var,var_1)) #Making 3D array
join_stk_height_3d = np.dstack((var,var_1)) #Acording to Height col depend on how many array add
#--------------------------------------------------------------------
#---------------------2D makes 3D------------------------------------
#---------------------3D makes 4D------------------------------------
#---------------------4D makes 5D------------------------------------
print(join_stk_col_3d)
print(join_stk_row_3d)
print(join_stk_height_3d)
"""
#=============================Split===============================
split = np.array_split(var,3) #3 number how much splice actually i need
print(split)