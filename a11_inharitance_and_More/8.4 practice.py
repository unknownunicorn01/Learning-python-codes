'''create a class complex to represent the complex numbers, along  with overloaded operator 
"+" and "*" which adds and mubliplies them'''

class complex():
  def __init__(self,n, i ):
    self.n=n
    self.i=i
  def __add__(self, num):
    return complex(self.n + num.n, self.i + num.i)
  def __mul__(self, num):
    return complex(self.n * num.n - self.i * num.i,
                   self.n * num.i + self.i * num.n)
  def __str__(self):
    return f"{self.n} + {self.i}i"
  
a=complex(1,-2)
b=complex(2,4)
print(a+b)
print(a*b)