#creating numpy array using numpy function
# 0's arra fill special Character
import numpy as np
ar = np.zeros(4)
print(ar) #single Dimension
arm = np.zeros((3,4))
print(arm) # multi Dimension
# 1 's dimension same like zero
#empty also like this using np.empty() its shows prevous element may be show
# range using like for loop
m = np.arange(1,10,2)
print(m)

# Diagonal fill with ones like
arr_Dig = np.eye(7)
print(arr_Dig)

arr_Dig = np.eye((3,3))
print(arr_Dig)


