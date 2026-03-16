# Search ,Sort , Search Sorted , Filter
import numpy as np

var = np.array([1,2,3,4,5,6])
f = np.where(var%2 == 1)
print(f)
g = np.searchsorted(var,100,side='right')
print(g)