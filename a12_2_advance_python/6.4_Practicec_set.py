'''filter teh number which are devisible by 5 in the list:'''
l=[23,34,11,191,10,100,15,35,2,3,55,3545]

def fun(x):
  if(x%5==0):
    return True
  return False
filt= filter(fun,l)
print(list(filt))