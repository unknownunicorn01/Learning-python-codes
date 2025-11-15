'''in this we iwll learn about the break, contineu and pass statement'''
#Break statement
for i in range(100):  #it telles compiler to run till 99 from 0
  if(i==34):  #tells the loop that it stop the counting after 33
    break   #stope the loop right now
  print(i)





#continue statement
"""just like break statement we have continew statement
but in break staetment we see code stop exicuteing after the condition
but in continue statement code will skip the value continue statement passes in 
"""

for i in range(100):
  if(i==2):
    continue  #will skip the iteration
  print(i)

'''pass is a null statement
it instructs to do nothing'''
for i in range(100):   #not writeing whole program right now
                       #or want to finish it later
  pass  # it will you to skip this for look, and will not include it in the program and run rest of the program


i=0
while(i<=5):
  print("hellow python")
  i+=1