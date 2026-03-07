#numpy Shape Reshape
import numpy as np

var = np.array([[1,2],[3,4]])
print(var.shape)
var_1 = np.array([[1,2,3],[3,4,5]])
#show the shape

print(var_1.shape)
#for multi dimension regarding

var_multi = np.array([1,2,3,4],ndmin=5)
print(var_multi)

#for dimension check
print(var_multi.ndim)

#for shape check
print(var_multi.shape)

#Reshape convert 1d to 2d 3d or multi
var_shape = np.array([1,2,3,4,5,6])
print(var_shape)
print(var_shape.shape)
#For 2d dimension making
var_reshape = var_shape.reshape(6,2)
print(var_reshape)
var_reshape = var_shape.reshape(3,4)
print(var_reshape)

