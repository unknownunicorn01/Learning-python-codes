class employee:
  def __init__(self):
    print("this is an employee")
  a=1

class programer(employee):
  b=2
  def __init__(self):
    super().__init__()  #now it will run the constructor from the class employee in it
    print("this is an programer")

class manager(programer):
  c=3
  def __init__(self):
    super().__init__()  #now is will run the code from the init of class programer
    print("this is an manager")

o=manager()
print(o.a, o.b , o.c)