#session 2nd

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

#diagonal multi Dmensional purpose
arr_Digg = np.eye(3,5)
print(arr_Digg)

# linspace use how much reqired from client
arr_spc = np.linspace(0,10,6)
print(arr_spc)


