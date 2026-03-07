import numpy as np

var = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#checking the shape
f = var.shape
print(f"shape of var : \n",f)


#3d shape making
var_reshape = var.reshape(2,3,2)
print(f"3D making 1# : \n",var_reshape)