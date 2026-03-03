# session 4
import numpy as np
from numpy import dtype

var  = np.array([1,2,3,4])
print(var.dtype) #check the datatype int64

var_f  = np.array([1.0,2.0,3.9,4.0])
print(var_f.dtype) #check the datatype float64

var_s  = np.array(["A","B","C","D"])
print(var_s.dtype) #check the datatype <u1 for string

var_u  = np.array(["A","B","C","D",1 ,2, 3, 4])
print(var_u.dtype) #check the datatype <u21 for string

#change datatype
var  = np.array([1,2,3,4],dtype = np.int8)
print(var.dtype) #check the datatype int64 now its goes for int8

#alternative we can use altertive datatype shorcut number or format like this
var_ch = np.array([1,2,3,4],dtype = "f")
print(var_ch)
print(var_ch.dtype)

new_dtype = np.array([1,2,3,4])
f = np.float32(new_dtype)
print(f.dtype)
print(f)
