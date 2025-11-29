# Store marks of 5 students in 3 subjects using Numpy array. Compute average marks per student and per subject.

import numpy as np

stu_data = np.array([[61,62,63],
                     [62,63,64],
                     [63,64,65],
                     [64,65,66],
                     [65,66,67]])

num_r , num_c = stu_data.shape

for i,e in enumerate(stu_data):
  sum_r = 0
  for j in e:
    sum_r += j
  mean = sum_r/num_c
  print(f"The average marks of student {i+1} is => {mean}")
  
for i in range(num_c):
  avg = sum(stu_data[:,i])/num_r
  print(f"The average of subject {i+1} of all the students is {avg}")
  

  
  

  