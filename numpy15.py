# insert element and Delete element from Array
import numpy as np

var = np.array([1,2,3,4,5])
var_2d = np.array([[1,2,3],[4,5,6]])

#np.insert(array,index number ,element or list)
insrt = np.insert(var,5,[7,8,9]) #for 1D usage insert by index number
#np.insert(array, element or list)
appnd = np.append(var,[10,11,12]) #for 1d insert data or append at the last side of array

var_2d = np.insert(var_2d,0,[7,8,9])
print(var_2d)
