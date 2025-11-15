'''write a python program to convert calcius to faranite and faranite to celcies
(C*9/5) + 32 = F '''
def fun(temp,type):
  if(type=="fara"):
    print(f"tamprature in celsious is: {round((temp-32)*(5/9),2)} celsious")
  elif(type=="cels"):
    print(f"tamprature in Fahrenite is: {round((temp*9/5)+32)} Fahrenite")
  else:
    print("invald scale according to code")
  return "done"  #will return done after the code otherwise will return None(because we are taking input from the user)

temp=int(input("enter temprature you want to convert: "))
type=input("which type of scale your temprature is (fara / cels): ")
print(f"{fun(temp,type)}")  #we write round(ele,number) to get round off value like jus tto print the value to that decimal place after point
