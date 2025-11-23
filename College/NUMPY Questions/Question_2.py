#Create a 2D array (3X3 matrix) with elements 1 to 9 using np.arange() and reshape().

import numpy as np

arr_1d = np.arange(1,10)
print(arr_1d)

matrix_1 = arr_1d.reshape((3,3))
print(matrix_1)