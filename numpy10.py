# Iterration of numpy array
import numpy as np

var = np.array([[1,2,3,4,5,6],[11,12,13,14,15,16]])

#for 1D one for loop for 2D two for loop for 3D three for loop for 4D for four loop
for x in var:
    for item in x:
        print(item)

#funtion nditer() using here
for x in np.nditer(var):
    print(x)


