# Create atwo 2X2 matrices and perform : 
# 1. Matrix addition 
# 2. Matrix multiplication using both * and np.dot()


import numpy as np

arr_1 = np.array([[1,2],
                  [3,4]])
arr_2 = np.array([[5,6],
                  [7,8]])

mat_add = arr_1 + arr_2

mat_mul1 = arr_1 * arr_2

mat_mul2 = np.dot(arr_1,arr_2)

print(f"The addition of both the matrix is {mat_add}")
print(f"The multiplication of both matrix is {mat_mul1}")
print(f"The matrix multiplication by np.dot() is {mat_mul2}")



