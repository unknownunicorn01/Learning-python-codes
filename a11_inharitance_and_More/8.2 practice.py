'''create a class pet from the class animal, then create a class dog with class pet
and write a method bark in dog class'''

class animal:
  def __init__(self):
    print("every animal is an animal")

class pet(animal):
  def __init__(self):
    super().__init__()  #we used super keyword so it will print that init statement of the last class too.
    print("not every animal is an pet")

class dog(pet):
  def __init__(self):
    super().__init__()  #we used super keyword so it will print that init statement of the last class too.
    print("not every pet is dog")
  @staticmethod
  def bark():
    print("every dog bark")

a=dog()
a.bark()