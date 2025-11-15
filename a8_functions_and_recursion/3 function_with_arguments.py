def fun(name,end):  #we give an variable to take input
  print("good day, "+ name)
  print(end)  #argument given by the user will be printed in the place of name and end
  return "ok"

fun("Shikhar Dutta","Thank you!")  #here you can pass teh argument

#but if you want to take input from the use you can do this
name=input("enter the name: ")
great=input("what you want to write in the end: ")  #this way you can even take input from the user
fun(name, great)  #We give stating and ending string


# a = fun("Aditiya","Hey!")  #You cant just save it in any variable because it is
#                            #defined as a function and you can only call a function function name
# print(a)  #this will return nothing 


a = fun("Aditiya","Hey!")  #now we gave a return value so it can even store in a variable
print(a)  #and also return the value in the return statement
#now the value is stored inside the variable a
'''this is used is that value is to be used in a function so you 
can just store teh value in a variable'''


#anoteher inpotring thing
def fun2(name2,ending="Thank You!"):  #this bassicaly tells the code if the value
  #of the ending is entered then its ok but if not get Thank you automaticly.
  print(f"Good Day, {name2}")
  print(ending)

fun2("shubham")
print("nice to meet you!")  #you can also add string after the function call ( your choice )
fun2("Rahul","its a good day!")  #here we entered the value of the ending so it will return this value


