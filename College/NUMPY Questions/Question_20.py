# Demostrate broadcasting using an example.

#When performing element-wise operations (like +, -, *, /), NumPy compares array shapes from right to left and tries to match them using these rules:

#✅ Broadcasting Rules

#1. If the dimensions are equal → OK


#2. If one of the dimensions is 1 → it can be stretched


#3. If they are different and none is 1 → error

import numpy as np

a = np.array([1, 2, 3])    # shape (3,)
b = 5                      # shape ()

print(a + b)
#print(a.shape)


#[6 7 8]
