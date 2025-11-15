#calculate the factorial of the given number take input from the user
num=int(input("enter the number you want factorial of: "))
fact=1
for i in range(1,num+1):
  fact=i*fact
print(f"factorial of the number {num}: {fact}")
