# Indexing and Slicing
import numpy as np

#1D slicing
print("-----------------1D---------------")
var_1d = np.array([1,2,3,4,5,6,7,8,9,10])

# : use for after or before here number like [x:] x index number to  all show
print(var_1d[1:])

# [:Y] y index number before all number
print(var_1d[:4])

# [x:y] x to y all index numbers mention that means [start : end ]
print(var_1d[1:4])

# If we need to step like 2 add [1 3 5 7] like these need to step like these [start : end : step]
print(var_1d[0:10:2]) # here step 2

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#2D slicing process
print("-----------------2D---------------")
var_2d = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here I can use like this [x][x1:]
print(var_2d[0][1:])
print(var_2d[0,1:])
#Both same

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here I can use like this [x][:x1]
print(var_2d[0][:1])
print(var_2d[0,:1])
#Both same

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here I can use like this [x][x1(start):x1(end)]
# [x:y] x to y all index numbers mention that means [start : end ]
print(var_2d[0][1:2])
print(var_2d[0,1:2])
#Both same

# If we need to step like 2 add [1 3 5 7] like these need to step like these [start : end : step]
print(var_2d[0][1:2:2])  # here step 2
print(var_2d[0,1:2:2])
#Both same


#------------------------------------------------------------------------
#------------------------------------------------------------------------
#3D slicing process
print("-----------------3D---------------")

var_3d = np.array([[[1,2,3,4,5,6,7,8,9,10]],[[11,12,13,14,15,16,17,18,19,20]],[[21,22,23,24,25,26,27,28,29,30]]])
print(var_3d.shape)
# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here I can use like this [x(which block)][x1(which row)][y1:(which coloumn)]
print(var_3d[0][0][1:])
print(var_3d[0,0,1:])
#Both same

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here I can use like this [x][:x1]
print(var_3d[0][0][:4])
print(var_3d[0,0,:4])
#Both same

# : use for after or before here number like [x][x1] x is index number of which block x1 belong to block's index number
#here I can use like this [x][x1(start):x1(end)]
# [x:y] x to y all index numbers mention that means [start : end ]
print(var_3d[0][0][0:4])
print(var_3d[0,0,0:4])
#Both same

# If we need to step like 2 add [1 3 5 7] like these need to step like these [start : end : step]
print(var_3d[0][1][0:7:2])
print(var_3d[0,1,0:7:2])
#Both same