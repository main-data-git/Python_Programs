# Generate a random array of 10 integers between 1 and 100. Find maximun , minimum and their indices 

import numpy as np 

rand_arr = np.random.randint(1,100,size=10)
print(rand_arr)

max_val = max(rand_arr)
min_val = min(rand_arr)

max_idx = np.where(rand_arr == max_val)
min_idx = np.where(rand_arr == min_val)

print(f"The maximum value is => {max_val} and at Index {max_idx[0]}")

print(f"The minimum value is => {min_val} and at Index {min_idx[0]}")



