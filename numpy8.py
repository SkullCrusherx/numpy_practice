#BroadCasting
import numpy as np

# 1) check dimension and element if both equal its goes work
# 2) check always shape is shape from right side compare if same like Var_1 coloumn is 1 or n and
# var_2 is 1 or n if both same or one of them 1 its work

var_1 = np.array([1,2,3,4,5])
var_2 = np.array([1,2,3,4,5])
#both same possible done dimension check using ndim and shape check using shape
print(var_1.ndim)
print(var_1.shape)
print(var_2.ndim)
print(var_2.shape)
#arethemetic operation done here

#if dimension same shape is different like these
var_1 = np.array([1,2,3,4,5])
var_2 = np.array([1,2,3,4])
#****print(var_1+var_2)
#arthemetic operation error show broadcast error shape error

#if dimension are different check shape
var_1 = np.array([1,2,3])
var_2 = np.array([[1,2,3],[4,5,6]])
#check shape from right side or shape is both compare
# check right axis1 (coloumn) one of them 1 or both same like n==n
# then compare 2nd axis (row)
#same formula here if one of them 1 or same shape var_1.shape (Axis 1) == var_2.shape (Axis 2)
#or if dimension one is 2d another is 3d 4d or nD then no extra shape then means in numpy its goes for ok
print(var_1+var_2)

