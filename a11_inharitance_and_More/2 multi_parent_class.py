class parent1():
  name="Shikhar Dutta"
  print(f"Name: {name}")

class parent2():
  age="19"
  print(f"Age: {age}")

class parent3():
  language="python"
  print(f"Language good at: {language}")

class parent4():
  job="AI/ML developer"
  print(f"Work he do: {job}")

class parent5():
  education="Btech - Computer science"
  print(f"His education: {education}")

class child(parent1, parent2, parent3, parent4, parent5):
  @staticmethod
  def __init__():
    print("Thank you!!!")

details=child()
