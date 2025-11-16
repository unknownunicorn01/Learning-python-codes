'''write a class vactor representing a vector of n dimention. Overload the + and  * operator
which calculate the sum and the dot(.) product of them'''

class complex:
  def __init__(self,i,j,k):
    self.i=i
    self.j=j
    self.k=k

  def __add__(self, other):
    return complex(self.i + other.i, self.j + other.j, self.k + other.k)

  def __mul__(self, other):
    return complex(self.i * other.i + self.j * other.j + self.k * other.k)
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  
i=int(input("enter the  i of 1st quadrant: "))
j=int(input("enter the  j of 1st quadrant: "))
k=int(input("enter the  k of 1st quadrant: "))

a=complex(i,j,k)

i2=int(input("enter the i of 2nd quadrant: "))
j2=int(input("enter the j of 2nd quadrant: "))
k2=int(input("enter the k of 2nd quadrant: "))

b=complex(i2,j2,k2)

opr=input("enter the operator + or *: ")

if opr=="+":
  print(f"your quardants are: {a+b}")
elif opr=="*":
  print(f"your dot product is: : {a*b}")
else: 
  print("invalid operator!!")