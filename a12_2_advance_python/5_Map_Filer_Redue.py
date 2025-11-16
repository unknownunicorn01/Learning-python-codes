from functools import reduce
'''use of map function is if we have to use a function of every element in the list we can use
without using the loop'''
l=[1,2,3,4,5]
sq= lambda x:x**2
newList=map(sq,l)
print(list(newList)) #you have to give list input otherwise it will show the memory location

'''filter method fuction can filter the list'''
def fun(x):
  if(x%2==0):
    return True
  return False

filterList=filter(fun,l)  #this will call function without () bracket and filter accordind to the function
print(list(filterList))

'''recude function, for using this we have to import it from functools'''

sum= lambda a,b:a+b  #first value will take the input and second will return output
print(reduce(sum,l))

'''
how reduce fuction works given bellow:
1,2,3,4,5
1+2,3,4,5
3+3,4,5
6+4,5
10+5
15 the result after reduce method work
'''