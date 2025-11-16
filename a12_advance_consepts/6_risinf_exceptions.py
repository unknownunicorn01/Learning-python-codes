"""we need this so our code still run even if it have a small mistake

in sinple words we return error in our code by ourself
we do it because if sometime we crease a module we dont want it to be wrong or do somthing 
that is not ment to be so it perform it's take perfectly

rethat than that some examples are given bellow: 
"""

a=int(input("enter the number: "))
b=int(input("enter the number to divide: "))
if(b==0):
  raise ZeroDivisionError("can't divide by zero")  #we can also write the statement we want in case of error

else:
  print(a/b)