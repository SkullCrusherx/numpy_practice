#Copy and View
import numpy as np

var = np.array([1,2,3,4,5,6])
var_copy = var.copy()

var[0]=19

print(var_copy)




var_view = var.view()
print(var_view)