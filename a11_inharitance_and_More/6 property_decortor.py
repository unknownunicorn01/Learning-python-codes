# class employee():
#   @property
#   def name(self):
#     return f"{self.fname} {self.lname}" 
#   @name.setter
#   def name(self, value):
#     self.fname= value.split(" ")[0]
#     self.lname= value.split(" ")[1]


# # name=input("enter you full name: ")
# s=employee()
# s.name="Shikhar Dutta"
# # print(f"your first name: {s.fname}")
# # print(f"your last name: {s.lname}")
# print(f"{s.name}")





class employee:
  a=1
  @property
  def namesplit(self):
    return f"{self.fname} {self.lname}"
  @namesplit.setter
  def namesplit(self,value):
    self.fname=value.split(" ")[0]
    self.lname=value.split(" ")[1]

o=employee()
o.namesplit="shikhar dutta"
print(o.namesplit)
