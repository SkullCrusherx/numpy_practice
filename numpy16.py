#Last series of WS cube Tutorial
#MATRIX and matrix operations
import numpy as np

var = np.matrix([[1,2],[3,4]])
var2 = np.matrix([[5,6],[7,8]])

add = np.add(var,var2)
sub = np.subtract(var,var2)
mul = np.multiply(var,var2)
dev = np.divide(var,var2)
dot = np.dot(var,var2)

print("addition : \n", add)
print("Subtract : \n", sub)
print("Multiply : \n", mul)
print("Devide : \n", dev)
print("Print : \n", dot)

print(np.dot(var,var))
print("-"*10)
print(np.linalg.matrix_power(var,2))
print("-"*10)
print(np.linalg.matrix_power(var,0)) #for identity matrix
print("-"*10)
print(np.linalg.matrix_power(var,-1)) # for inverse power
# model are ready