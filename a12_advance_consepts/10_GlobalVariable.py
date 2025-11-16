a=23
def fun():
  global a
  a=3
  print(a)
fun()  #a will work as a global variable if you declear it and call the function before printing
    # the value of a and all other a will be not condider becore this a in function whic is global

print(a)
print(a+2)