#Copy and View
import numpy as np

#copy function direct copy original function andif changes doesnt represent it
var = np.array([1,2,3,4,5,6])
var_copy = var.copy() #original copy

var[0]=19 #changes the var elemnt index number of 0
print(var_copy)

#view function direct copy original function and if changes show as it is
var_view = var.view()
print(var_view)