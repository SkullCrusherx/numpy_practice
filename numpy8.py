import numpy as np

var = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#checking the shape
f = var.shape
print(f"shape of var : \n",f)

#2D shape making
var_2d = var.reshape(3,4)
var_2d = var.reshape(6,2)
var_2d = var.reshape(4,3)

#2D shape print
print(f"shape of var_2d : \n",var_2d)

#3D shape making
var_3d = var.reshape(2,3,2)
var_3d = var.reshape(1,12,1)
var_3d = var.reshape(3,2,2)
var_3d = var.reshape(6,2,1)
var_3d = var.reshape(1,6,2)

#print 3D
print(f"3D making 1# : \n",var_3d)

#1D Remake the shape like this
i = var_3d.reshape(-1)
j = var_3d.ravel()
k = var_3d.flatten()

#print 3D
print(f"1D remake : \n",i)