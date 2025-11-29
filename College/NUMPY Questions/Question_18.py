#Use np.where() to find indices of element greater than a user given value. 

import numpy as np


stu_data = np.array([[61,62,63],
                     [62,63,64],
                     [63,64,65],
                     [64,65,66],
                     [65,66,67]])

#user_value = int(input("Enter the number => "))
user_value = 65

a,b = np.where(stu_data > user_value)
print("The indices are => ")
for i in range(len(a)):
  print(f"The index {i+1} is {int(a[i]),int(b[i])}")

