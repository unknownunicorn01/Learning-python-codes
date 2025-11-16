'''this python code will works as a module for 9.1 main.py
because we will import the function of this file in that file '''

def myFun():
  print("hellow world")
'''
myFun()  #because we run this function in this file, so it will also run in 9.1 main.py
print(__name__)  #if we run this it will print main, but from other file it will print file name
'''
print("hwllow world")

'''in case you dont want other code in this file run but not some part you can do the following'''
if __name__ == "__main__":
  myFun()  
  print(__name__)  
  #not this part of code will not run in other file even if this file if imported