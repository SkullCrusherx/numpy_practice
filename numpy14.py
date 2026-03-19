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
ff = var.flatten()
print("Output : ", ff)