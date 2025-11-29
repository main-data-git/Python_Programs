# Create two numpy Array an dperform : Addition , Substraction , Multiplication , and Divivsion (element-wise)

import numpy as np 

arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([6,7,8,9,10])

add_arr = arr_1 + arr_2
sub_arr = arr_1 - arr_2
mul_arr = arr_1 * arr_2
div_arr = arr_1 / arr_2

print(f"The addition of the given two array is => {add_arr}")
print(f"The substraction of the given two array is => {sub_arr}")
print(f"The multiplication of the given two array is => {mul_arr}")
print(f"The division of the given two array is => {div_arr}")