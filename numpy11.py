import numpy as np

a = np.array([1,2,3], dtype=np.int32)
b = np.array([1.5,2.5,3.5], dtype=np.float64)

it = np.nditer([a,b], flags=['common_dtype'])

for x, y in it:
    print(x, y, type(x), type(y))