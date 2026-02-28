#session 1D
#Array Creating

import numpy as np # import library
x = [1,2,3,4,5,6] #list
y = np.array(x) #make list into array
print(y) #show output

lst = [] #empty list
for i in range(6):
    user = int(input(" enter new input : "))
    lst.append(user)

print(np.array(lst))


# 1D Dimension []
# 2D Dimension [[]]
# 3D Dimension [[[]]]
# Higher Dimension Array [[[[[]]]]]


print(y.ndim) # check dimension
