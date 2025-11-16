class person():
  def body(self):
    self.height= f"{5.8} ft"
    self.weight= f"{70} Kg"
    print(f"Height: {self.height}\nWeight: {self.weight}")

class interest():
  def hobby(self):
    self.playIn="chess"
    self.playOut="Cricket"
    self.like="reading"
    print(f"Person's hobby are:\n{self.playIn}\n{self.playOut}\n{self.like}")

class persnalInfo(person,interest):
  def allPer(self):
    self.body()
    self.hobby()

    print("\nabove are the person's persnal information,\nHope you like it\n\n")

class info():
  def perInfo(self):
    self.num= 10000001
    self.id= 12345
    self.gmail="example@gmail.com"
    print(f"Persnol number: {self.num}\nPersons ID number: {self.id}\nPerson's gmail: {self.gmail}")

class work():
  def workInfo(self):
    self.name="Shikhar Dutta"
    self.language="python"
    self.salery=4000000
    print(f"Person's name: {self.name}\nLanguage person work with: {self.language}\nPerson's salery: {self.salery}")

class profInfo(info,work):
  def allPro(self):
    self.perInfo()
    self.workInfo()

    print("\nabove are the person's profeshnal information,\nThanks for readig!!!")



class allInfo(persnalInfo, profInfo):
  print("following are the information for employ:\n")

shikhar=allInfo()
shikhar.allPro()
shikhar.allPer()
