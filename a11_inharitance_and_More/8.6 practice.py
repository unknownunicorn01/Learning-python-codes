'''wrtie __str__ method to print the vactor present bellow:
7i + 8j + 10k

assuming vector of dimention 3 for this problem'''

class complex():
  def __init__(self,i,j,k):
    self.i=i
    self.j=j
    self.k=k
  def __str__(self):
    return f"{self.i}i + {self.j}j +{self.k}k"
  

a=complex(7,8,10)
print(a)
