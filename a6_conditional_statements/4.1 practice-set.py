#enter the greatest of the four number entered by the user
a=int(input("enter the 1st number you want: "))
b=int(input("enter the 2nd number you want: "))
c=int(input("enter the 3rd number you want: "))
d=int(input("enter the 4th number you want: "))

if(a>=b and a>=c and a>=d):
  print(f"{a} is the greates number")
elif(b>=a and b>=d and b>=c):
  print(f"{b} is the greatest number")
elif(c>=a and c>=b and c>=d):
  print(f"{c} is the greatest number")
elif(d>=a and d>=b and d>=c):
  print(f"{d} is the greatest number")

print("end of the program")


