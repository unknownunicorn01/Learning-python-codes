class nam:
  def name1(self):
    self.name="Shikhar Dutta"
    print(f"name={self.name}")

class greet:
  def greet1(self):
    print("following is the information about shikhat dutta")

class ini:
  def __init__(self):  #it will also print in the strart because it is init function
    print("thank you")
  def __helo__(self):
    print("Good Morning!")

class all(nam,greet,ini):
  def fun(self):
    super().__helo__()
    super().greet1()
    self.name1()
    super().__init__()
    

shikhar=all()
shikhar.fun()