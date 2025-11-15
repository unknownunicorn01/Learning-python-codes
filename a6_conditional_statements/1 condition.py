'''
conditional statements are those who tell you if you want to do one thing
or you want to do another, that depend on the condition you give, in short 
the task will be perform if the condition will be matched
eg: 
  if there is rain today
   you will take umbrella
  if not 
   you will not take umbrella
'''
 
#another examplay by code
day="rainy"
if(day=="rainy"):
  print("take umbrella")  #also the space which come after clicking the enter is called indentation
                          #indentation is importent in python and consider the mart of syntex
else:
  print("no need to take umberlla")

age=int(input("enter your age:"))
if(age>=18):
  print("an adult")
else:
  print("not an adult")

print("end of program")