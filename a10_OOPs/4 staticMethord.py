'''we use self in every function we defing inside the class and then call it
even if we dont have to pass any value for that we use @staticmethod which is
also an dacurator, which tell that which function fo neet to take input'''

class employ():
  name="shikhar"
  age=19
  def info(self):  # we take the self here because we will take input
    print(f"Name = {self.name}\nAge = {self.age}")
  @staticmethod  #we take static methor here because we have to tell the code that we are not passing any value in it
  #and static method is also a dacurator
  def greet():  #now we dont have to write the input
    print("thank you")

shikhar=employ()
shikhar.info()
shikhar.greet()