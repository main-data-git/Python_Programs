# Create a array and replace all the odd numbers with -1

import numpy as np

my_arr = np.array([1,2,3,4,5,6,7,8,9,10])

for idx,ele in enumerate(my_arr):
  if ele % 2 != 0:
    my_arr[idx] = -1
    
print(my_arr)