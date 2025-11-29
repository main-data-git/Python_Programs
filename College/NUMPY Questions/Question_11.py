# Given array [1,2,3,4,5] , find : SUM , Mean , Standard Deviation and Variance.

import numpy as np 

given_arr = np.array([1,2,3,4,5])
sum = 0
sd_sum = 0 

for i in given_arr:
  sum = sum + i

mean = sum/len(given_arr)

for num in given_arr:
  sd_sum = sd_sum + (num - mean)**2
  
sd = sd_sum/len(given_arr) 

var = sd**0.5


print(f"The sum of the array is => {sum}")
print(f"The mean is => {mean}")
print(f"The Standard Deviation is => {sd}")
print(f"The Variance is => {var}")

