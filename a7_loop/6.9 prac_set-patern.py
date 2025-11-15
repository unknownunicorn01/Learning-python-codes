'''draw the following patern using loop in python
***
* *
***'''
h=int(input("enter how long box you want: "))
i=0

while(i<h):     #here is another way to continue the next print statement in first 
                          #we can do it you using ,end="" ant the end outside the string
  if(i==0 or i==h-1):
    print(f"{"* "*h}")
  else:
    print(f"{"* "}",end="")
    print(f"{"  "*(h-2)}",end="")
    print(f"{"*"}")
  i+=1

