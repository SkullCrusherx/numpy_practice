#numpy Shape Reshape
import numpy as np

var = np.array([[1,2],[3,4]])
print(var.shape)

var_1 = np.array([[1,2,3],[3,4,5]])

print(var_1.shape) #show the shape
#for multi dimension regarding

var_multi = np.array([1,2,3,4],ndmin=5)
print(var_multi)
print(var_multi.shape)


