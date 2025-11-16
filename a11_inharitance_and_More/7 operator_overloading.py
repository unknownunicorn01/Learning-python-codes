# class number:
#   def __init__(self,a):
#     self.a=a
#   def __add__(self,num):  #__add__ is a dunder methord you can not write another word
#     # or it will consider it as function 

#     return self.a + num.a  #we are passing num so we have to write it to give the input
  
# a = number(12)
# b = number(23)
# print(a+b)  #we cant directly add two classes we have to use fucntion __add__ to add
# #which is also a dunder methord


'''
we also have other function (dunder methords) like:
1 __add__  #for addition
2 __sub__  #for subtraction
3 __mul__  #for multiplication
4 __truediv__  #for division
5 __floordiv__  #also used for divide

6 __str__ #for converting in string  can be called by str(obj)

7 __len__  #for getting lenght of the string by  called.__len__ or len(obj)
'''



class calc:
  def __init__(self,a):
    self.a=a
  def __add__(self,num):
    return self.a + num.a
  def __sub__(self,num):
    return self.a - num.a
  def __mul__(self,num):
    return self.a * num.a
  def __truediv__(self,num):
    return self.a / num.a
  
n1=int(input("enter the number1: "))
n2=int(input("enter the number2: "))
a=calc(n1)
b=calc(n2)
opr=input("enter the operator + - / * : ")

if(opr=="+"):
  print(f"{n1} {opr} {n2} = {a+b}")
elif(opr=="-"):
  print(f"{n1} {opr} {n2} = {a-b}")
elif(opr=="*"):
  print(f"{n1} {opr} {n2} = {a*b}")
elif(opr=="/"):
  print(f"{n1} {opr} {n2} = {a/b}")
else:
  print("invalid operator!!")