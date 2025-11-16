from functools import reduce

'''return the greatest number from the list'''
l=[2323,433,2233,2324,5435,7585,2345]
def greatest(a,b):
  if b>a:
    return b
  return a
print(reduce(greatest,l))
