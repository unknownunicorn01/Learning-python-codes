'''Override teh __len__() method on verctor of problem 5 to display the dimentions 
of the vector'''

#len is a method that print the length of the list
class shikhar():
  def __init__(self, l ):
    self.l=l
  def __len__(self):
    return len(self.l)
  
a=shikhar([1,2,3,4])
print(len(a)) #we have to write len method to print the lenght
#directly writing a will not print the value because the value is stored in memory location
#and for accessing that value we have to use string overloading function



'''code given bellow is just for fun'''
# with open("8.7 practice.py","r") as f:
#   data=f.read()
#   print(f"number for elemtnt in this file are: {len(data)}")