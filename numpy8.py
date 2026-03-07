import numpy as np

var = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#checking the shape
f = var.shape
print(f"shape of var : \n",f)

#2D shape making
var_2d = var.reshape(3,4)
var_2d = var.reshape(6,2)
var_2d = var.reshape(4,3)
print(f"shape of var_2d : \n",var_2d)


#3d shape making
var_3d = var.reshape(2,3,2)
print(f"3D making 1# : \n",var_3d)