# Write a class 'complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies times.
class complex:
   def __init__(self, real, imag):
       self.real = real
       self.imag = imag 

   def __add__(self, other):
       return complex(self.real + other.real, self.imag + other.imag)

   def __str__(self):
       return f"{self.real} + {self.imag}i"
   
   def __mul__(self, other):
       return complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

c1 = complex(1, 2)
c2 = complex(2, 3)
print(c1 + c2)
print(c1 * c2)