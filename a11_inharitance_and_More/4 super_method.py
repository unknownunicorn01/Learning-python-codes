class val:
  def __init__(self):
    print("constructor of a: ")
  a=1

class val2(val):  #this class contain the properties of class val1 along with its own properties
  def __init__(self):
    print("cunstructor of b: ")
  b=2

class val3(val2): #val2 contain properties of val1 so it have all the properties of val1 and val2
  def __init__(self):
    super().__init__()  #we can call any function here from which class we want and it will run along with this code
      #we write __init__ because this was tthe function we wanted to call
    print("cunstructor of c: ")
  c=3

shi=val()
print(shi.a)
# shi=val2()
# print(shi.a,shi.b)
shi=val3()
print(shi.a,shi.b,shi.c)