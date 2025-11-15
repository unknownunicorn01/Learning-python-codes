# print the sum of first n natural number take input from the user using while loop
num=int(input("enter the numebr: "))
i=1
sum=0
while(i<=num):
  sum=i+sum
  i+=1
print(f"Sum of number till {num}: {sum}")