# Search ,Sort , Search Sorted , Filter
import numpy as np

var = np.array([1,2,3,4,5,6])
#for checking condition or number index number
finding_from_arr = np.where(var%2 == 1)

#Checking the number index and condition where given input send and checking side left to right & retun the index number
insert_element_sort = np.searchsorted(var,100) #from left to right
insert_element_sort_r = np.searchsorted(var,100,side = 'right') #from right to left

print("search : ",finding_from_arr)
print("cheking sorting index left to right : ",insert_element_sort)
print("cheking sorting index right to left :",insert_element_sort_r)
