# Search ,Sort , Search Sorted , Filter
import numpy as np
var = np.array([1,2,3,4,5,6,5,8,6,9])
var_2d = np.array([[1,2,3],[4,5,6],[8,6,9]])

alphabet = np.array(['A','B','C','H','G','J','T'])
alphabet_2d = np.array([['A','B','C'],['H','G','J']])

#For checking condition or number index number
finding_from_arr = np.where(var%2 == 1)

#Checking the number index and condition where given input send and
#Checking side left to right & return the index number
#from left to right
insert_element_sort = np.searchsorted(var,100)
insert_element_sort_r = np.searchsorted(var,100,side = 'right') #from right to left

#Sorting alphabet and also number
sorting = np.sort(var)

#Alpabet sorting
alphabet_sorting = np.sort(alphabet)

#Reverse sorting number
Reverse_sorting = np.sort(var)[::-1] #For 1D
Reverse_sorting_2d = np.sort(var_2d)[::-1]

#Reverse alphabet sorting
Reverse_alphabet_sorting = np.sort(alphabet)[::-1] #For 1D
Reverse_alphabet_sorting_2d = np.sort(alphabet_2d)[::-1]

print("*"*100)
print("search index number of array according to condition : ",finding_from_arr)
print("index check from right to left : ",insert_element_sort_r)
print("index check from left to right : ",insert_element_sort)
print("*"*100)
print("sorting 1D: ",sorting)
print("alphabet sorting 1D: ",alphabet_sorting)
print("reverse sorting 1D: ",Reverse_sorting)
print("reverse alphabet sorting 1D: ", Reverse_alphabet_sorting)
print("reverse number sorting 2D: ", Reverse_sorting_2d)
print("reverse alphabet sorting 2D: ", Reverse_alphabet_sorting_2d)