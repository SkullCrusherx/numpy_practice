#Last series of WS cube Tutorial
#MATRIX and matrix operations
import numpy as np

var = np.matrix([[1,2,3],[3,4,5]])
var2 = np.matrix([[4,5,6],[7,8,9]])

add = np.add(var,var2)
sub = np.subtract(var,var2)
mul = np.multiply(var,var2)
dev = np.divide(var,var2)

print("addition : \n",add)
print("Subtract : \n",sub)
print("Multiply : \n",mul)
print("Devide : \n",dev)