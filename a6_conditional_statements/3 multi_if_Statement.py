age=int(input("enter your age: "))
if(age%2==0):
  print("age is even")# if statement can be witen alone but not else statement
  #if this condition is not matched this code will not run because there is no other conditions
  #end of first if statement

#start of another if statement
if(age>=18):
  print("is an adult")
elif(age<18 and age > 0):
  print("not an adult")
elif(age==0):
  print("you entered 0 which is not an valid age")
else:
  print("not an valid age")  #end or second if statement

#just like this you can have as many if statement as you want