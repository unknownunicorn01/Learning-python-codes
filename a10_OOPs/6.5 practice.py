'''create a form from indian railway in whihch user will fill his info like number of seat
he want his name, age, gender, and give the fare information of train runing under the
indian railway'''
class railway():
  def __init__(self, name, age, gender, seat):
    self.name=name
    self.age=age
    self.gender=gender
    self.seat=seat
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Number of seat: {seat}")
  @staticmethod
  def greet():
    print("Thanks for shareing your information to us, we will update you soon!")

def welcom():
  print("Welcom to Indian Railways!!!")
  print("provide the following information for your registration.")
welcom()
name=input(f"Enter your name: ")
age=input(f"Enter your age: ")
gender=input(f"Enter your gender: ")
seat=input(f"Enter the number of seat you want: ")
person=railway(name, age, gender, seat)
person.greet()