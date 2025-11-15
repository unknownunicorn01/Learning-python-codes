a=(1,2,3,"shikhar","shivam",True,32,3.14)
print(a)  # this is our tuple

# we cant directly change tuples but we can make changes by makeing another tuple 

#slice Mthod
aSlice=a[0:4]
print(aSlice)  # will return the value of tuple from index 0 to 3

aIdx1=a[0]  # will retuen the value from the perticular index
print(aIdx1)

#length Method
aLen=len(a)
print(aLen)  # it will return the number of elements(or length of tuple) in the tuple

aIdx=a.index("shikhar")
print(aIdx)  # it will return the index of shikhar string

#member in tuples
print(1 in a)   #output will be true
print('shikhar' in a)  # output will be true

#for repetation of tuples
aRepeat=a*3  # because we multuply with 3 so tuple will be repeted 3 times
print(aRepeat)

aCount=a.count(1)
print(aCount)  # will return the number of time this element come in the list

my_tup=(1,2,3,4)
x, y, z, t = my_tup  # you can store you tuple in variable is number of varuable are equle to number of elements in the tuple
print(x, y, z, t)

for item in my_tup:  # for applying look in tuples
  print(item)       

# convert tuple into list or list into tuples
aList=list(a)
print(aList[0:6])
aList.pop(1)
print(aList)  # now because it is list, it will work like list 

