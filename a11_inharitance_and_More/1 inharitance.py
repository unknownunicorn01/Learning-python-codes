class parent():  #this is parent class also known as base class
  language="python"  #parent class attribute
  def show(self):
    self.name= "Shikhar"
    self.salery= 1200000
    print(f"Name: {self.name}\nSalery:{self.salery}")

class child(parent):  #this is a chile class also known as derive class
    #a child class can contain more then one parent class
  language="java"  #we can also change te attribute in child class
  def showinfo(self):
    print(f"name : {self.name}\nSalery:{self.salery}")  #this function is only in child class
a=parent()
b=child()
print(a.language,b.show())  #if i write a function which is not in child class but in parent class
  # the function will be in child class and if you want you can add more info what you like

