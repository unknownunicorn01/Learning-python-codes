'''there are 2 type of approach to code one is functional and another is by makeing object 
making object is where we can use out code many times

OPPs concept focus on reusable code (DRY{do not repeat yourself} principel)
DRY Principel
  this concept mean you should avoide repeating your code manytime in a code using reusable code
  
CLASSES
  Classes are the blue print to your object'''

class employ:  #here we create the class which the name employ
  language="python"   #this all are attribute of the class
  salery=1200000   
  '''in case we want to hire someone which python language and salery 1200000 
  we dont write name because we can take it later'''

shikhar=employ()  #here we assign class to an object
shikhar.name="Shikahr Dutta"  #here name is an instence attribute
print(shikhar.name,shikhar.language)  