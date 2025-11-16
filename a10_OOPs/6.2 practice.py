import math
class number():
  def __init__(self, num):
    self.num = num
    print(f"square of number {num}: {num**2}\nCube of number {num}: {num**3}\nSquare root of number {num} is: {round(math.sqrt(num),4)}")

n=int(input("enter the number:"))
shikhar=number(n)

