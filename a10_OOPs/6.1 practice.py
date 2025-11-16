'''create a program to write the information of the employes in microsoft'''

class employ():
  def __init__(self, name, language, salery, age):
    self.name= name
    self.language= language
    self.salery= salery
    self.age= age
    print("information of the following employee")
  def info(self):
    print(f"Name: {self.name}\nLanguage: {self.language}\nSalery: {self.salery}\nAge: {self.age}")
  
emp1=employ("Shikhar Dutta","Python",1200000,19)
emp1.info()
emp2=employ("Aditiya","Rust",1200000,19)
emp2.info()
emp3=employ("Rahul","JavaScript",1000000,20)
emp3.info()
emp4=employ("Shubham","Java",1100000,21)
emp4.info()