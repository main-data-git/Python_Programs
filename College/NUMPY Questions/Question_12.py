# Create a 3X3 array and find : Row wise and column wise sum.

import numpy as np 

arr_3X3 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
count_sum = 0

a,b = arr_3X3.shape


for i in range(a):
  print(f"The sum of row {i+1} is => {arr_3X3[i,:].sum()}")
  print(f"The sum of column {i+1} is => {arr_3X3[:,i].sum()}")
  


  
