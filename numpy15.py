# insert element and Delete element from Array
import numpy as np

var = np.array([1,2,3,4,5])
var_2d = np.array([[1,2,3],[4,5,6]])

#np.insert(array,index number ,element or list)
insrt = np.insert(var,5,[7,8,9]) #for 1D usage insert by index number

appnd = np.append(var,[10,11,12])
dd = np.append(var,[13,14,15])
