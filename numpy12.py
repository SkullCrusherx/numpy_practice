#Joining & Split NumPy Arrays Using
import numpy as np

var = np.array([1,2,3,4])
var_1 = np.array([6,7,8,9])

# for 1D joining array
join = np.concatenate(var,var_1)
print(join)
