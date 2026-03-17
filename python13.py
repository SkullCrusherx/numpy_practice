# Search ,Sort , Search Sorted , Filter
import numpy as np

#for checking condition or number index number
var = np.array([1,2,3,4,5,6])
finding_from_arr = np.where(var%2 == 1)
print(finding_from_arr)

#Checking the number index and condition where given input send and checking side left to right & retun the index number
#from left to right
insert_element_sort = np.searchsorted(var,100)
insert_element_sort_r = np.searchsorted(var,100,side = 'right') #from right to left

print(insert_element_sort_r)
print(insert_element_sort)