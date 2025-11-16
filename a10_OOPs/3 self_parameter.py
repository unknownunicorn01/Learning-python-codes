'''self we use in function we declear in the class'''

class employ(): 
  language="python"
  salery=1200000  #this is a class attribute
  def getInfo(self):  #we can write anything as name but usely write self
    print(f"{self.name} is the name of the employ\nSalery of employ is: {self.language}\nand the language he work in is: {self.language}")
  def greet(self):  #we also have to give the input self even if the print statement nothing to call
    print("thank you")

shikhar=employ()  #this is an object
shikhar.name="Shikhar Dutta"  #we input out name here which is instence class
shikhar.getInfo()  #we can also write employ.getInfo(shikhar) which will work same and call function
employ.greet(shikhar)