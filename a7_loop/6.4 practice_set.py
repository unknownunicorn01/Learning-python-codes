#check wether the given number is prime of not
l=[]
num=int(input("enter the number you want to check: "))
for i in range(2,num):
  l.append(num%i)
if(0 in l):
  print(f"{num} is not a prime number")
else:
  print(f"{num} is a prime number")