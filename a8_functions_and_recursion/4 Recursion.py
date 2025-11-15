'''Recurson is a function that calles itself 
because the logic of the function is connected with that function'''
'''You can write a factorial formula simpely by using factorial in function'''

def factorial(n):
  if(n==1 or n==0):
    return 1
  return n*factorial(n-1)  #here the function call itself but not a string or anyother value

n=int(input("enter the numbe you want factorual of: "))
print(f"factorial of the number {n} is: {factorial(n)}")