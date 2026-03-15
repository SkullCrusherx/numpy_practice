#Copy and View
import numpy as np

#copy function direct copy original function andif changes doesnt represent it
var = np.array([1,2,3,4,5,6])
var_copy = var.copy() #original copy

var[0]=19
print(var_copy)

var_view = var.view()
print(var_view)