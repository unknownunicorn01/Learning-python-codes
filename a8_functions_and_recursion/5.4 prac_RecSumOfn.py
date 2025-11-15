# def fun(n):
#   if(n<0):
#     return "Done"
#   sum=0
#   for i in range(1,n+1):
#     sum+=i
#   return sum

# n=int(input("enter hte number:"))
# print(f"sum of n natural number is: {fun(n)}")


def su(n):
  if(n==1):
    return 1
  return su(n-1) + n

num=int(input("enter the number you want to print: "))
print(su(num))