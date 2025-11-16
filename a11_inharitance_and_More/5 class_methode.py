class name:
  a=4
  @classmethod  #because we use @classmethod now only the class attribute will get prefrence
  def fun(cls):  #after the class method we write here cls insted of self because is will
      # only take value of the class and not the insente attribute
    print(f"value of a is: {cls.a}")
  
s=name()
s.a=23  #we we dont use classmethod this value of a(insent attribute) will get prefrence 
s.fun()