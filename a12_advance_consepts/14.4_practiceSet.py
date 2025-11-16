'''perform division take a and b as input and if b is 0 print infinite with ZeroDivisionError'''

try:
  a=int(input("enter a:"))
  b=int(input("enter b:"))
  print(f"{a} divide by {b} is : {a/b}")

except ZeroDivisionError as e:
  print(e,"infinite")