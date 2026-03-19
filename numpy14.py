# Shuffle() # Unique() # Resize() # Flatten() # Ravel()
import numpy as np

var_31 = np.array([1,2,3,4])
var = np.array([1,2,3,4,5,6,4,6,7,8,2,9])
var_2d = np.array([[1,2,3],[7,8,9]])
#--------------------------------------------------------
#----------------Shuffle---------------------------------
np.random.shuffle(var) #no need to store it return Value
np.random.shuffle(var_2d) #no need to store it return Value

#--------------------------------------------------------
#----------------""Unique""------------------------------

unqe = np.unique(var)
unqe_2d = np.unique(var_2d)
print(unqe)
print(unqe_2d)
#--------------------------------------------------------
#----------------""Resize""------------------------------
rsize = np.resize(var,(5,4))
print(rsize)
#--------------------------------------------------------
#----------------""Flatten""-----------------------------
one_D_make = var_2d.flatten()
one_D_make = var_2d.flatten(order='F') #here order wise F for row wise C for col wise
print("Output :", one_D_make)

#--------------------------------------------------------
#----------------""Ravel""-------------------------------
one_D_make_ravel = var_2d.ravel()
print("Output :", one_D_make_ravel)

#--------------------------------------------------------
#--------------------------------------------------------