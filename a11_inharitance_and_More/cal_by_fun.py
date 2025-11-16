def add(a,b):
  print(a+b)

def sub(a,b):
  print(a-b)

def mul(a,b):
  print(a*b)

def div(a,b):
  print(a/b)

def mod(a,b):
  print(a%b)

def pow(a,b):
  print(a**b)

a=int(input("enter the value 1: "))
b=int(input("enter the value 2: "))

opr=input("enter a operator (+, -, *, /, %, ^):")
if(opr=="+"):
  print(f"sum of a and b: {add(a,b)}")
if(opr=="-"):
  print(f"subtraction of a and b: {sub(a,b)}")
if(opr=="*"):
  print(f"multiplication of a and b: {mul(a,b)}")
if(opr=="/"):
  print(f"division of a from b: {div(a,b)}")
if(opr=="%"):
  print(f"remender of a devide by b: {mod(a,b)}")
if(opr=="^"):
  print(f"a^b: {pow(a,b)}")