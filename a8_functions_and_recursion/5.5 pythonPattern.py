'''print the following line in python function to print the following pattern
***
**
*
for n=3
'''

# def funPattern(n):
#   for i in range(0,n):
#     print(f"{"*"*(n-i)}")
#   return "Done"
# n=int(input("enter the number of line you want to print: "))
# funPattern(n)

def fun(n):
  if(n==0):
    return
  print("*"*n)
  fun(n-1)

fun(5)