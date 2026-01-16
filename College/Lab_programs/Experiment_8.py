class complex:
  
  def __init__(self,real,imag):
    self.real = real
    self.imag = imag 
    pass
  
  def display(self):
    print(f"The complex number is {self.real} + {self.imag}i")
    
  def add_complex(self,c1,c2):
    real_sum = c1.real + c2.real
    imag_sum = c1.imag + c2.imag
    return complex(real_sum,imag_sum)

n = int(input("How many complex number you want to add => "))
complex_num_list = []    
for i in range(n):
  print(f"Enter the complex number {i+1}")
  real_part = int(input("Enter the real part => "))
  imag_part = int(input("Enter the imag part => "))
  complex_num_list.append(complex(real_part,imag_part))
  
result = complex_num_list[0]

for i in range(1,n):
  result = result.add_complex(result,complex_num_list[i])
  
  
print(f"The sum of all the complex number is => {result.real} + {result.imag}i")

    