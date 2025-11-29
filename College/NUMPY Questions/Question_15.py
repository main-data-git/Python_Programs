# Create a 3X3 matrix and compute :
# 1. Transpose
# 2. Determinant

import numpy as np

mat_3X3 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

mat_trans = mat_3X3.T

mat_det = np.linalg.det(mat_3X3)


print(f"The transpose o fthe given 3X3 matrix is {mat_trans}")

print(f"The determinant of the given 3X3 matrix is {mat_det}")

