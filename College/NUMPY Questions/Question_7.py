# # Create a 3X3 array
# => Access the element in 2nd row 3rd column
# => Extract first two rows 
# => Extract last column

import numpy as np

arrr_3d = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(arrr_3d)

print(arrr_3d[1,2])

for i in range(2):
  print(arrr_3d[i])
  
print(arrr_3d[:,2])


