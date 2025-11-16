'''
take name, marks and phone number as an input of the usse and show it in follow formate
using formate function

"The name of the student is Harry, his marks are 72 and phone number is 9999888"
'''

info= lambda name=str,marks=int,number=int:"The name of the student is {0}, his marks are {1} and phone number is {2}".format(name,marks,number)

name=input("enter the name: ")
marks=int(input("enter you marks: "))
number=int(input("enter you phone number: "))

print(info(name,marks,number))