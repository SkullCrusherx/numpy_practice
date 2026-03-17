# Search ,Sort , Search Sorted , Filter
import numpy as np

var = np.array([1,2,3,4,5,6])
finding_from_arr = np.where(var%2 == 1)
print(finding_from_arr)


insert_element_sort = np.searchsorted(var,100,side='right')
print(insert_element_sort)