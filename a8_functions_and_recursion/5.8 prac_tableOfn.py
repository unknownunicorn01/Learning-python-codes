'''print table of the givem number by using function in python'''
def fun(num):
  for i in range(1,11):
    print(f"{num} x {i} = {i*num}")
  return "Done"
num=int(input("enter the number you want table of:"))
fun(num)