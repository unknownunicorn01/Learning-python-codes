# class vector2D:  #we create a class for 2d vector
#   def __init__(self,i,j):  #we declear class attribute for this class 
#     self.i=i
#     self.j=j
#   def show(self):
#     print(f"2d cordinates are: {self.i}i, {self.j}j")
# class vector3D(vector2D):  #we create another class vectore3D and inharit vector2D class in it
#   def __init__(self,i,j,k):  #we define a fucntion which contain out previous vectors
#     super().__init__(i,j)  #we use super keyword to write i and j value in this function
#     self.k=k 
#   def show(self):
#     print(f"cordinates are: {self.i}i, {self.j}j, {self.k}k")

# b=vector2D(1,2)
# b.show()
# b=vector3D(1,2,3)
# b.show()


'''write python code for 2d vectors than create a 3d vector class with 2d vectors'''

class vector2d():
  def __init__(self,i,j):
    self.i=i
    self.j=j
  def show(self):
    print(f"2D cordinates are: {self.i}i, {self.j}j")

class vector3d(vector2d):
  def __init__(self,i,j,k):
    super().__init__(i,j)
    self.k=k
  def show(self):
    print(f"2D cordinates are: {self.i}i, {self.j}j, {self.k}k")

a=vector2d(1,2)
b=vector3d(3,4,5)
a.show()
b.show()
