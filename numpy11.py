import numpy as np

a = np.array([1,2,3], dtype=np.int16)
b = np.array([10,20,30], dtype=np.int64)

it = np.nditer([a,b], flags=['common_dtype'])

for x,y in it:
    print(type(x), type(y))