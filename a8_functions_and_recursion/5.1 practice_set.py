'''write a program to find the reatest of the 3 number using function'''
def fun(a,b,c):
  if(a>=b and a>=c):
    print(f"{a} is the greatest number")
  elif(b>=a and b>=c):
    print(f"{b} is the greatest number")
  elif(c>=b and c>=a):
    print(f"{c} is the greatest number")

a=int(input("enter the 1st number: "))
b=int(input("enter the 1st number: "))
c=int(input("enter the 1st number: "))
fun(a,b,c)