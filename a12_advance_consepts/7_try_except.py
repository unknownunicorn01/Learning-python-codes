try:
  a=int(input("enter the number: "))
  print(a)

except Exception as e:
  print(e,"\nplease write int only!!")

else:
  print("we are in else")  #this else condition will only work when the try dondition run sucessfully
  #otherwise it will show error
  