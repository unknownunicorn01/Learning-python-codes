'''add a static methord in 6.2 practice.py and write it here'''
# with open("6.2 practice.py","r") as f:
#   data = f.read()
#   print(data)

# with open("6.4 practice.py","w")  as f:  #6.4 practice.py the the name of this file only, just to see
#    #if i can copy past the code in this file using file input output concept
#    f.write(data)


import math
class number():
  def __init__(self, num):
    self.num = num
    print(f"square of number {num}: {num**2}\nCube of number {num}: {num**3}\nSquare root of number {num} is: {round(math.sqrt(num),4)}")
  @staticmethod
  def greet():
    print("thanks for exicution, code run succesfully")

n=int(input("enter the number:"))
shikhar=number(n)
shikhar.greet()

