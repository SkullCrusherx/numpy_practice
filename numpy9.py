# Indexing and Slicing
import numpy as np

#1D slicing
var = np.array([1,2,3,4,5,6,7,8,9,10])

# : use for after or before here number like [x:] x index number to  all show
print(var[1:])

# [:Y] y index number before all number
print(var[:4])

# [x:y] x to y all index numbers mention that means [start : end ]
print(var[1:4])

# If we need to step like 2 add [1 3 5 7] like these need to step like these [start : end : step]
print(var[0:10:2]) # here step 2

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#2D slicing process
