# # create a 1D array of 12 elemnets and reshape it into 
# => 3X4
# => 2X6
# Display both array 

import numpy as np

arr_1d = np.arange(12)
print(arr_1d)

new_3X4_array = arr_1d.reshape(3,4)
print(new_3X4_array)

new_2X6_array = arr_1d.reshape(2,6)
print(new_2X6_array)