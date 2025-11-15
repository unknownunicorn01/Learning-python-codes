'''group of code to perform a specific task are klnown as functions'''
"""lets say if you want to calculate the avrage for the given numbe doing it everytime
will take much time and you will have to right mroe line of code"""

def avg():  #here we define a function (can also say finction defination)
  l=[]
  sum=0
  num=int(input("enter how many time you want to take avrage:"))
  for i in range(0,num):
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=int(input("enter the number:"))
    print("avrage:",(a+b+c)/3)
avg() #Function call
 
'''when a program gets big and complex it get hard for a programer to understand
 what happening where so for decreasing the complixity and efficiency we declear function
 so we can also call it anytime our code need it'''