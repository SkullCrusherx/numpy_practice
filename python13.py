# Search ,Sort , Search Sorted , Filter
import numpy as np
var = np.array([1,2,3,4,5,6,5,8,6,9])
alphabet = np.array(['A','B','C','H','G','J','T'])

#for checking condition or number index number
finding_from_arr = np.where(var%2 == 1)

#Checking the number index and condition where given input send and
#Checking side left to right & return the index number
#from left to right
insert_element_sort = np.searchsorted(var,100)
insert_element_sort_r = np.searchsorted(var,100,side = 'right') #from right to left

#sorting alphabet and also number
sorting = np.sort(var)

#alpabet sorting
alphabet_sorting = np.sort(alphabet)

#reverse sorting number
Reverse_sorting = np.sort(var)[::-1] #For 1D

#reverse alphabet sorting
Reverse_alphabet_sorting = np.sort(alphabet)[::-1] #For 1D

print("search index number of array according to condition : ",finding_from_arr)
print("index check from right to left : ",insert_element_sort_r)
print("index check from left to right : ",insert_element_sort)
print("sorting : ",sorting)
print("alphabet sorting : ",alphabet_sorting)
print("reverse sorting : ",Reverse_sorting)
print("reverse alphabet sorting : ", Reverse_alphabet_sorting)