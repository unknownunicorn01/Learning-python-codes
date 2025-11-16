'''create a class employee and add salery and increment property to it'''
class employ():
  def __init__(self, salary, incr):
    self.salary=salary
    self.incr=incr
    print(f"your current salary: {salary}")
  def increment(self):
    print(f"incremented salary {self.incr}% increment: {self.salary+((self.salary*self.incr)/100)}")

a=employ(120000,12)
a.increment()