'''we use cunstructor by two undersocore __init__()
it runs in code when the class is called even if you dont call the function 
it can be use to write the input or take input of you desire
this is also known the dundor function __init__() '''

class employ():  #this is a class
  name="shikhar" #class attribute
  age=19
  def __init__(self, name, age, language):  #this is a dundor function
    #you can even take input from this constructor
    self.name=name
    self.age = age
    self.language=language  #here we define tha attribute now we can take th e input

    print("this code will run ")  #this code will run ever time the class is called
  def info(self):
    print(f"Name: {self.name},\nAge: {self.age}\nLanguage: {self.language}")

shikhar=employ("Shikhar Dutta", 19, "Javascript")  #remember to give input in the order the variables are define

shikhar.info()