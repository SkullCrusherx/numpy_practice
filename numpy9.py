# Indexing and Slicing
import numpy as np

#1D slicing
"""var_1d = np.array([1,2,3,4,5,6,7,8,9,10])

# : use for after or before here number like [x:] x index number to  all show
print(var_1d[1:])

# [:Y] y index number before all number
print(var_1d[:4])

# [x:y] x to y all index numbers mention that means [start : end ]
print(var_1d[1:4])

# If we need to step like 2 add [1 3 5 7] like these need to step like these [start : end : step]
print(var_1d[0:10:2]) # here step 2"""

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#2D slicing process

var_2d = np.array([[1,2,3],[4,5,6]])

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here i can use like this [x][x1:]
print(var_2d[0][1])
print(var_2d[0][1])

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here i can use like this [x][:x1]
print(var_2d[:4])

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here i can use like this [x][x1(start):x1(end)]
# [x:y] x to y all index numbers mention that means [start : end ]
print(var_2d[1:4])

# If we need to step like 2 add [1 3 5 7] like these need to step like these [start : end : step]
print(var_2d[0:10:2]) # here step 2"""


#------------------------------------------------------------------------
#------------------------------------------------------------------------
#3D slicing process