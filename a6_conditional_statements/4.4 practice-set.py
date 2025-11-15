"""check wether the user name have characters less then 10"""

usrname=input("enter you name: ")
if(len(usrname)<10):    # space between elemets also count as a character
  print("character in your name is less then 10")
else:
  print("your name have more then 10 characters")

"""check wether the name is already present in the list or not"""
list_of_name=["shikhar","rohan","aditiya","ayush","parth"]
urname=input("enter the name you want to check in the list: ")
if((urname in list_of_name)==True):
  print("name is in the list")
else:
  print("name is NOT present in the list")


