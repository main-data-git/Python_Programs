# Create a 5X5 matrix with random integers (0-100) and Find: Mean of each row and Mean of each column

import numpy as np 

mat_5X5 = np.random.randint(0,100,size=(5,5))
print(mat_5X5)



for i in range(5):
  sum = 0
  for j in mat_5X5[i,:]:
    sum = sum + j
  mean = sum/5
  print(f"The mean of row {i+1} is => {mean}")
    
  
  

for i in range(5):
  sum = 0
  for j in mat_5X5[:,i]:
    sum = sum + j
  mean = sum/5
  print(f"The mean of column {i+1} is => {mean}")
