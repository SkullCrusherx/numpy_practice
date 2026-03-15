# Iterration of numpy array
import numpy as np

var = np.array([1,2,3,4,5,6])
var_2d = np.array([[1,2,3,4,5,6],[9,8,7,6,5,4]])
var_3d = np.array([[[1,2,3,4,5,6]],[[3,4,5,6,7,8]],[[4,5,6,7,8,9]]])

#for 1D one for loop for 2D two for loop for 3D three for loop for 4D for four loop
for x in var_2d:
    for item in x:
        print(item)

#funtion nditer() using here
for x in np.nditer(var):
    print(x)

#funtion nditer() change data type using here
#using flags for extra space from memory
# using OP_dtype for byte string "S"
# If only need int or other than using casting to change it like these Casting=["unsafe"]
for x in np.nditer(var_3d,flags=["buffered"],op_dtypes=['U'],casting="unsafe"):
    print(x)

# If we need index number also then we need to use this function and also like these
for index,x in np.ndenumerate(var_3d): #here index contains the index number of that
    print(index,x)

