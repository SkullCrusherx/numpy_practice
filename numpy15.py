# insert element and Delete element from Array
import numpy as np

var = np.array([1,2,3,4,5])
var_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
var_3D = np.array([[[1,2,3]],[[5,4,7]],[[4,5,6]]])

#======================================================================================
#==================np.insert(array,index number ,element or list)======================
#======================================================================================
insrt = np.insert(var,5,[7,8,9]) #for 1D usage insert by index number

var_2d_0 = np.insert(var_2D,0,[7,8,9],axis=0)
var_2d_1 = np.insert(var_2D,0,[7,8,9],axis=1)

var_3d_0 = np.insert(var_3D,0,[7,8,9],axis=0)
var_3d_1 = np.insert(var_3D,0,[7,8,9],axis=1)
#var_3d_2 = np.insert(var_3D,0,[7,8,9],axis=2)

print("for 2D output :",var_2d_0)#For axis 0 row wise
print("for 2D output :",var_2d_1)#For axis 1 coloumn wise

print("for 3D output :",var_3d_0)#For axis 0 row wise
print("for 3D output :",var_3d_1)#For axis 1 coloumn wise
#print("for 3D output :",var_3d_2)##For axis 2 edge wise

#**************************************************************************************
#==================np.append(array,element or list)====================================
#======================================================================================

appnd = np.append(var,4) # number
appnd = np.append(var,[3,4,5]) # list pass
print("append : ",appnd)