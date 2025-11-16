'''finally statement work as normal print statement if not in function but if it is in function 
will work even after the return statement '''
def fun():
  try: 
    a=int(input("enter the number: "))
    return a
  finally:
    print("we are in finally even after the return statement\nSurely i have some aura😈") 
    #return statemnet will work after the finally staement


print(fun())