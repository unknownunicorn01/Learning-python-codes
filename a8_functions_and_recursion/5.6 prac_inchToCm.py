def funIntoCm(n,type):
  if type=="cm":
    return n/2.54
  elif type=="inch":
    return n*2.54
  else:
    return "invalid mesurment"

n=int(input("enter the value you want to convert: "))
type=input("enter the type of mesurment that you will pass (cm or inch): ").lower()
if(type=="inch"):
  print(f"{n} {type} = {funIntoCm(n,type)} cm")
elif(type=="cm"):
  print(f"{n} {type} = {funIntoCm(n,type)} inch")