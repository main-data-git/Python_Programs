# Create a 1D array of 10 zeros , another of 10 ones , and concatenate them together.


import numpy as np 

arr_zero = np.zeros((10,))
print(arr_zero)

arr_ones = np.ones((10,))
print(arr_ones)

sum_arr = np.concatenate((arr_zero,arr_ones))
print(sum_arr)

