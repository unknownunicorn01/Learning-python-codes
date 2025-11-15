#write a code to print multiplication table of the given number using loop
num=int(input("enter the number you want to print table of: "))
for i in range(1,11):
  print(f"{num} X {i} = {num*i}")